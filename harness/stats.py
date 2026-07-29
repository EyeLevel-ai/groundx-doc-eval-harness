"""Bootstrap confidence intervals, replicate variance, cross-judge agreement.

Pure functions over judged rows; no I/O. Random seed is an explicit argument
(pre-registered in the manifest) so every number is reproducible.
"""

from __future__ import annotations

import random
from collections import defaultdict


def accuracy(rows: list[dict]) -> float:
    scored = [r for r in rows if not r.get("infra_error")]
    if not scored:
        return 0.0
    return sum(1 for r in scored if r["correct"]) / len(scored)


def bootstrap_ci(rows: list[dict], n_boot: int = 10_000, alpha: float = 0.05, seed: int = 0):
    """Percentile bootstrap over QUESTIONS (cluster by qid so replicates move together)."""
    by_q = defaultdict(list)
    for r in rows:
        if not r.get("infra_error"):
            by_q[r["qid"]].append(1 if r["correct"] else 0)
    qids = sorted(by_q)
    if not qids:
        return (0.0, 0.0, 0.0)
    rng = random.Random(seed)
    point = sum(sum(v) / len(v) for v in by_q.values()) / len(qids)
    boots = []
    for _ in range(n_boot):
        sample = [rng.choice(qids) for _ in qids]
        boots.append(sum(sum(by_q[q]) / len(by_q[q]) for q in sample) / len(sample))
    boots.sort()
    lo = boots[int((alpha / 2) * n_boot)]
    hi = boots[int((1 - alpha / 2) * n_boot) - 1]
    return (point, lo, hi)


def replicate_variance(rows: list[dict]) -> dict:
    """Per-replicate accuracy spread — the G1 stability report."""
    by_rep = defaultdict(list)
    for r in rows:
        if not r.get("infra_error"):
            by_rep[r["replicate"]].append(1 if r["correct"] else 0)
    accs = {rep: sum(v) / len(v) for rep, v in sorted(by_rep.items()) if v}
    vals = list(accs.values())
    spread = (max(vals) - min(vals)) if vals else 0.0
    return {"per_replicate": accs, "spread": spread}


def judge_agreement(rows_a: list[dict], rows_b: list[dict]) -> dict:
    """Raw agreement + Cohen's kappa between two judges over shared (qid, arm, replicate)."""
    key = lambda r: (r["qid"], r["arm"], r["replicate"])  # noqa: E731
    a = {key(r): r["correct"] for r in rows_a if not r.get("infra_error")}
    b = {key(r): r["correct"] for r in rows_b if not r.get("infra_error")}
    shared = sorted(set(a) & set(b))
    if not shared:
        return {"n": 0, "agreement": None, "kappa": None}
    n = len(shared)
    agree = sum(1 for k in shared if a[k] == b[k]) / n
    pa = sum(1 for k in shared if a[k]) / n
    pb = sum(1 for k in shared if b[k]) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    kappa = (agree - pe) / (1 - pe) if pe < 1 else 1.0
    return {"n": n, "agreement": agree, "kappa": kappa}


def decision_rule(gx_rows: list[dict], best_blueprint_rows: list[dict], seed: int = 0) -> dict:
    """The pre-registered featured/not-featured decision: GX CI-low > blueprint CI-high."""
    gx = bootstrap_ci(gx_rows, seed=seed)
    bp = bootstrap_ci(best_blueprint_rows, seed=seed)
    return {
        "groundx": {"point": gx[0], "ci_low": gx[1], "ci_high": gx[2]},
        "blueprint_best": {"point": bp[0], "ci_low": bp[1], "ci_high": bp[2]},
        "featured": gx[1] > bp[2],
    }
