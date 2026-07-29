#!/usr/bin/env python3
"""Harness self-test: synthetic fixtures for stats + decision rule + judge parsing,
plus an optional live dual-judge smoke (2 items) when keys are present.

Run: python -m harness.selftest [--live]
"""

from __future__ import annotations

import os
import sys

from .judge import JUDGES, _parse_verdict, judge_one, load_prompt
from .schema import ArmAnswer, QAItem
from .stats import bootstrap_ci, decision_rule, judge_agreement, replicate_variance

FAIL = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


def synth_rows(n, acc, arm, judge="nemotron", reps=3, seed=1):
    import random

    rng = random.Random(seed)
    rows = []
    for i in range(n):
        truth = rng.random() < acc
        for rep in range(1, reps + 1):
            rows.append({"qid": f"q{i}", "arm": arm, "replicate": rep, "judge": judge,
                         "correct": truth if rng.random() > 0.05 else not truth,
                         "citation_correct": truth, "rationale": ""})
    return rows


# stats
gx = synth_rows(150, 0.85, "groundx", seed=2)
bp = synth_rows(150, 0.70, "blueprint_tuned", seed=3)
p, lo, hi = bootstrap_ci(gx, n_boot=2000, seed=0)
check("bootstrap CI sane", 0.75 < p < 0.95 and lo < p < hi, f"{p:.3f} [{lo:.3f},{hi:.3f}]")
rv = replicate_variance(gx)
check("replicate variance computed", 0 <= rv["spread"] < 0.15, f"spread={rv['spread']:.3f}")
d = decision_rule(gx, bp, seed=0)
check("decision rule separates 85 vs 70", d["featured"] is True, f"gx_low={d['groundx']['ci_low']:.3f} bp_high={d['blueprint_best']['ci_high']:.3f}")
d2 = decision_rule(synth_rows(150, 0.74, "groundx", seed=5), synth_rows(150, 0.72, "blueprint_tuned", seed=6), seed=0)
check("decision rule refuses 74 vs 72 (small gap)", d2["featured"] is False)

# judge agreement
ag = judge_agreement(gx, synth_rows(150, 0.85, "groundx", judge="openai", seed=2))
check("judge agreement computed", ag["n"] > 0 and ag["kappa"] is not None, f"kappa={ag['kappa']:.3f}")

# verdict parsing
v = _parse_verdict('noise {"correct": true, "citation_correct": null, "rationale": "ok"} tail')
check("verdict parser tolerates wrapping", v["correct"] is True)

# prompt loads + placeholders resolve
tpl = load_prompt()
try:
    tpl.format(question="q", reference="r", alternates="a", evidence="e", candidate="c", citations="[]",
               source_type="table", reach="single")
    check("judge prompt placeholders resolve", True)
except KeyError as e:
    check("judge prompt placeholders resolve", False, repr(e))

# optional live smoke
if "--live" in sys.argv:
    item = QAItem(qid="live1", source_type="table", reach="single", question="What is 2+2?", answer="4",
                  evidence=[{"doc": "math.pdf", "pages": [1]}])
    good = ArmAnswer(qid="live1", arm="t", replicate=1, answer_text="The answer is 4.",
                     citations=[{"doc": "math.pdf", "page": 1}])
    bad = ArmAnswer(qid="live1", arm="t", replicate=1, answer_text="The answer is 5.")
    for j in JUDGES:
        if not os.environ.get(JUDGES[j]["api_key_env"]):
            check(f"live judge {j}", False, "key not set — skipped")
            continue
        try:
            g = judge_one(item, good, j, tpl)
            b = judge_one(item, bad, j, tpl)
            check(f"live judge {j}", g.correct is True and b.correct is False,
                  f"good={g.correct} bad={b.correct}")
        except Exception as e:  # noqa: BLE001
            check(f"live judge {j}", False, repr(e)[:160])

sys.exit(1 if FAIL else 0)
