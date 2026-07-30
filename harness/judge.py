"""Dual-judge scoring over any OpenAI-compatible endpoint.

Judge prompts are PINNED artifacts (preregistration/judge-prompts/); this module
loads them verbatim and refuses to run if the file hash doesn't match the
manifest. Judge MODEL ids are pinned literals below — no environment
overrides — and are re-pinned in MANIFEST.sha256 at lock; `verify_judges()`
refuses to run on a mismatch, same as `load_prompt()` does for the prompt.
Two judge configs ship: `nemotron` (NVIDIA-hosted; NeMo Evaluator integration
is the committed upgrade path) and `openai`. Temperature 0.
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re

import httpx

from .schema import ArmAnswer, JudgedAnswer, QAItem

PROMPT_DIR = pathlib.Path(__file__).parent.parent / "preregistration" / "judge-prompts"

JUDGES = {
    "nemotron": {
        "base_url": "https://integrate.api.nvidia.com/v1",
        "model": "nvidia/llama-3.3-nemotron-super-49b-v1.5",
        "api_key_env": "NVIDIA_API_KEY",
        "system_extra": "/no_think",
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-2024-11-20",
        "api_key_env": "OPENAI_API_KEY",
        "system_extra": None,
    },
}


def verify_judges(manifest: dict | None = None) -> None:
    """Refuse to run if a judge model id doesn't match the lock manifest.

    The manifest pins each judge's model id under ``judge-model:<name>``; the
    runner calls this alongside load_prompt() before scoring anything.
    """
    if not manifest:
        return
    for name, cfg in JUDGES.items():
        want = manifest.get(f"judge-model:{name}")
        if want and want != cfg["model"]:
            raise RuntimeError(
                f"judge model mismatch for {name!r}: manifest={want} actual={cfg['model']}")


def load_prompt(manifest: dict | None = None) -> str:
    p = PROMPT_DIR / "judge-v1.txt"
    text = p.read_text()
    if manifest is not None:
        want = manifest.get("judge-prompts/judge-v1.txt")
        got = hashlib.sha256(text.encode()).hexdigest()
        if want and want != got:
            raise RuntimeError(f"judge prompt hash mismatch: manifest={want} actual={got}")
    return text


def _parse_verdict(raw: str) -> dict:
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        raise ValueError(f"no JSON verdict in judge output: {raw[:200]!r}")
    v = json.loads(m.group(0))
    if "correct" not in v:
        raise ValueError(f"verdict missing 'correct': {v}")
    return v


def judge_one(item: QAItem, ans: ArmAnswer, judge: str, prompt_template: str) -> JudgedAnswer:
    cfg = JUDGES[judge]
    key = os.environ.get(cfg["api_key_env"])
    if not key:
        raise RuntimeError(f"{cfg['api_key_env']} not set")
    evidence = "; ".join(f"{e['doc']} pages {e['pages']}" for e in item.evidence) or "N/A (unanswerable)"
    user = prompt_template.format(
        question=item.question,
        reference=item.answer,
        alternates="; ".join(item.answer_alternates) or "none",
        evidence=evidence,
        candidate=ans.answer_text,
        citations=json.dumps(ans.citations),
        source_type=item.source_type,
        reach=item.reach,
    )
    messages = []
    if cfg["system_extra"]:
        messages.append({"role": "system", "content": cfg["system_extra"]})
    messages.append({"role": "user", "content": user})
    r = httpx.post(
        f"{cfg['base_url']}/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={"model": cfg["model"], "messages": messages, "temperature": 0, "max_tokens": 600},
        timeout=120,
    )
    r.raise_for_status()
    verdict = _parse_verdict(r.json()["choices"][0]["message"]["content"] or "")
    return JudgedAnswer(
        qid=item.qid,
        arm=ans.arm,
        replicate=ans.replicate,
        judge=judge,
        correct=bool(verdict["correct"]),
        citation_correct=verdict.get("citation_correct"),
        rationale=str(verdict.get("rationale", ""))[:500],
    )
