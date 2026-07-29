# Test Documents — proposal for approval

## What the test must measure

A real deployment answers questions against a **library of many documents** — the system must find the right document(s) first, then the right page. So the test library must support three kinds of questions:

1. Questions whose answer lives in one document the system must locate among many.
2. Questions that require **combining information from two or more documents** (for example: "Which of these companies reported the highest legal reserves, and how did the top two describe the risk?").
3. Questions whose answer is **not in the library at all** — the correct response is "the documents don't contain this."

Single-document question sets, however good, cannot test the first two. That rules out most published document-Q&A benchmarks as the main test.

## Proposed test library (recommended)

**Fifteen recent annual reports (10-K filings), each over 150 pages, from the largest US public companies by market value on the date we lock the test.** Chosen by that rule mechanically — no hand-picking, no exclusions.

Why this works:
- Public documents, no licensing problems, anyone can re-download them.
- Visually hard: dense financial tables, footnotes, multi-hundred-page length.
- Naturally supports cross-document questions (same disclosures across fifteen companies).
- Neither GroundX nor NVIDIA has published accuracy results on this exact set.

**Optional supplement:** a small set from a published single-document benchmark with difficult layouts (candidates: DUDE or MP-DocVQA), used only as an extra stress test on tables and figures — never as the headline number.

## Rules that keep the test honest

- The document list and every question are written **before any system is run**, and their checksums are published so nothing can be quietly changed afterward.
- NVIDIA may veto or substitute the library before the test locks.
- Questions are written by a person, to fixed quotas per question type (see `question-types.md`).

## Approval needed

- [ ] Confirm the fifteen-10-K library (or propose a different mechanical rule)
- [ ] Yes/no on the single-document supplement
- [ ] Name the person who will write and verify the ~150 questions
