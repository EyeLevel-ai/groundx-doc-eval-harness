# Frontier long-context arm protocol — DRAFT (task 2.3)

The durability arm: a frontier general-purpose model given the documents directly, no retrieval system. Answers the question any diligence process asks — *does the specialized edge survive frontier progress?*

## Model selection (mechanical)

- Model = the top-ranked model on **[named public long-context leaderboard — select and record at freeze]** as of the freeze date.
- Recorded: leaderboard URL, snapshot date, model ID, provider endpoint.
- **Standing re-run rule:** the arm is a one-flag model swap; re-run within one week of any new #1 on the named leaderboard; results appended, never replacing prior rows.

## Context construction

- **Gold-document-only:** the model receives the document(s) containing the evidence for the question (not the whole corpus). Stated plainly in the methodology doc: this is an *upper bound* for the no-retrieval approach — production systems would not know which document holds the answer.
- Documents provided as extracted text + page markers when the provider supports only text; as native PDF where the provider supports file input **[record per-provider handling at freeze]**.
- Truncation: if the gold document exceeds the model context, truncate tail-first with a recorded flag on that question; report truncated-question count per model.

## Scoring and reporting

- Same judges, same rubric, same replicates as the other arms.
- **Per-question token cost reported next to accuracy** (input + output at provider list prices, recorded at freeze).
- Latency per question recorded.

## Keys

`OPENAI_API_KEY` available; if the leaderboard rule selects a non-OpenAI model at freeze, the additional provider key becomes a named blocker raised immediately (owner: BF).
