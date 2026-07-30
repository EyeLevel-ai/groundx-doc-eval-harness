"""Arm adapters: each maps (QAItem, config) -> ArmAnswer.

All four arms return the same shape; infra errors populate `infra_error`
(excluded from scoring, logged, reported per-arm — the failure-rate cap is in
preregistration/decision-rule.md). Configs are pinned files under configs/ —
NVIDIA-submitted configs are first-class substitutes.
"""

from __future__ import annotations

import os
import time

import httpx

from .schema import ArmAnswer, QAItem


def _infra(qid, arm, rep, err):
    return ArmAnswer(qid=qid, arm=arm, replicate=rep, answer_text="", infra_error=str(err)[:300])


def groundx_arm(item: QAItem, cfg: dict, replicate: int) -> ArmAnswer:
    """GroundX search -> answer synthesis via the pinned answering LLM.

    Retrieval from the self-hosted node (cfg['base_url']); answer synthesis uses
    the same answering-LLM config as the blueprint arm so the comparison isolates
    the RETRIEVAL/INGESTION difference. The design and the exact synthesis
    prompt are preregistered in preregistration/answer-synthesis.md.
    """
    t0 = time.time()
    try:
        r = httpx.post(
            f"{cfg['base_url']}/v1/search/{cfg['bucket_id']}",
            headers={"X-API-Key": cfg["api_key"]},
            json={"query": item.question, "n": cfg.get("top_k", 5)},
            timeout=90,
        )
        r.raise_for_status()
        results = r.json()["search"]["results"]
        context, citations = [], []
        for res in results:
            context.append(res.get("suggestedText") or res.get("text") or "")
            page = (res.get("boundingBoxes") or [{}])[0].get("pageNumber")
            citations.append({"doc": res.get("fileName"), "page": page})
        answer = _synthesize(item.question, context, cfg["answer_llm"])
        return ArmAnswer(qid=item.qid, arm=cfg["arm_name"], replicate=replicate,
                         answer_text=answer, citations=citations, latency_s=time.time() - t0)
    except Exception as e:  # noqa: BLE001
        return _infra(item.qid, cfg["arm_name"], replicate, e)


def blueprint_arm(item: QAItem, cfg: dict, replicate: int) -> ArmAnswer:
    """NVIDIA RAG blueprint /v1/generate (non-streaming aggregate of SSE chunks)."""
    t0 = time.time()
    try:
        with httpx.stream(
            "POST",
            f"{cfg['base_url']}/v1/generate",
            json={"messages": [{"role": "user", "content": item.question}],
                  "use_knowledge_base": True,
                  "collection_names": [cfg["collection"]]},
            timeout=180,
        ) as r:
            r.raise_for_status()
            text, cites = [], []
            import json as _json
            for line in r.iter_lines():
                if not line.startswith("data: "):
                    continue
                chunk = _json.loads(line[6:])
                choice = (chunk.get("choices") or [{}])[0]
                delta = (choice.get("delta") or {}).get("content") or ""
                text.append(delta)
                for c in (chunk.get("citations") or {}).get("results", []):
                    cites.append({"doc": c.get("document_name"), "page": c.get("page_number")})
        return ArmAnswer(qid=item.qid, arm=cfg["arm_name"], replicate=replicate,
                         answer_text="".join(text), citations=cites[:10], latency_s=time.time() - t0)
    except Exception as e:  # noqa: BLE001
        return _infra(item.qid, cfg["arm_name"], replicate, e)


def frontier_arm(item: QAItem, cfg: dict, replicate: int) -> ArmAnswer:
    """Frontier model, whole library per request, in the most native form the
    provider supports (preregistration/frontier-arm-protocol.md, rule 2).

    cfg['library_content_loader'] (callable: QAItem -> provider-native message
    content — file/image parts plus the question, so figures reach the model as
    images) is the preferred path; cfg['library_text_loader'] (QAItem -> full
    text with page markers) is the fallback where the provider accepts neither
    files nor images. The config committed at lock selects the form, and the
    form used is recorded with the results. If the library exceeds the context
    window, the resulting error is recorded as the finding — not worked around."""
    t0 = time.time()
    try:
        loader = cfg.get("library_content_loader")
        if loader:
            content = loader(item)
        else:
            doc_text = cfg["library_text_loader"](item)  # callable: QAItem -> str (entire library, page markers)
            content = (f"Answer from the document below. Cite the page like [p. N]. "
                       f"If absent, say so.\n\nQUESTION: {item.question}\n\nDOCUMENT:\n{doc_text}")
        r = httpx.post(
            f"{cfg['base_url']}/chat/completions",
            headers={"Authorization": f"Bearer {os.environ[cfg['api_key_env']]}"},
            json={"model": cfg["model"], "temperature": 0, "max_tokens": 1200,
                  "messages": [{"role": "user", "content": content}]},
            timeout=300,
        )
        r.raise_for_status()
        body = r.json()
        msg = body["choices"][0]["message"]["content"] or ""
        usage = body.get("usage", {})
        return ArmAnswer(qid=item.qid, arm=cfg["arm_name"], replicate=replicate,
                         answer_text=msg, latency_s=time.time() - t0,
                         tokens_in=usage.get("prompt_tokens"), tokens_out=usage.get("completion_tokens"))
    except Exception as e:  # noqa: BLE001
        return _infra(item.qid, cfg["arm_name"], replicate, e)


def _synthesize(question: str, contexts: list[str], llm: dict) -> str:
    messages = []
    if llm.get("system_extra"):
        messages.append({"role": "system", "content": llm["system_extra"]})
    ctx = "\n\n---\n\n".join(contexts)
    messages.append({"role": "user", "content":
        f"Answer strictly from the context. If the context lacks the answer, say the documents do not contain it.\n\nQUESTION: {question}\n\nCONTEXT:\n{ctx}"})
    r = httpx.post(
        f"{llm['base_url']}/chat/completions",
        headers={"Authorization": f"Bearer {os.environ[llm['api_key_env']]}"},
        json={"model": llm["model"], "messages": messages, "temperature": 0,
              "max_tokens": llm.get("max_tokens", 1200)},
        timeout=180,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"] or ""
