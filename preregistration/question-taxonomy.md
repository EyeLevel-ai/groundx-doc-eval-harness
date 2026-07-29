# Question-type taxonomy and quotas — DRAFT for SME sign-off (task 2.3)

Fixed quotas bound authorship bias on question *mix* (not just document selection). Frozen and hashed with the question set before any arm runs. N ≥ 150 total.

| Type | Quota | Definition | Example shape |
|---|---|---|---|
| **Table lookup** | 30% | Answer is a value or row inside a table; requires reading table structure, not prose | "What is the [column] for [row entity] in [table/section]?" |
| **Narrative extraction** | 25% | Answer is stated in body text; single location | "Under what conditions does [policy/term] apply?" |
| **Cross-page synthesis** | 20% | Answer requires combining evidence from ≥2 pages | "How does the [item] defined on one page apply to the scenario described elsewhere?" |
| **Figure/chart/diagram** | 15% | Answer requires reading a non-text element (chart axis, diagram label, form checkbox) | "What value does the chart show for [category]?" |
| **Unanswerable / not-in-corpus** | 10% | Ground truth is "the documents do not contain this"; scores grounding discipline (hallucination check) | Plausible question whose answer is absent |

## Ground-truth format (per question)

```json
{"qid": "", "type": "table|narrative|crosspage|figure|unanswerable",
 "question": "", "answer": "", "answer_alternates": [],
 "evidence": [{"doc": "", "pages": []}], "author": "", "authored_before_runs": true}
```

Citation accuracy is scored against `evidence.pages` — a correct answer with a wrong citation is scored separately (both metrics reported).

## Sign-off checklist (SME)

- [ ] Quotas reflect the document classes that stall real deals (adjust percentages with rationale, before freeze)
- [ ] Unanswerable set reviewed so none are accidentally answerable
- [ ] Every question authored before any system run; authorship recorded per question
