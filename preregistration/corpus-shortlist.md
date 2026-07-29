# Test Documents — proposal for approval

## What the test must measure

A real deployment answers questions against a **library of many documents**. The library and questions must therefore test:

- the three answer sources, hardest first: **figures/graphs**, **table/layout structure**, **plain text** (see `question-taxonomy.md`)
- finding the right document among many, and combining information **across documents**
- recognizing when the answer **isn't in the library at all**

## Two options

### Option A — reuse the published test set

EyeLevel already built and published exactly this kind of test: 1,146 pages of public Deloitte documents with 92 curated questions split across text, table, and figure sources ([eyelevel.ai/post/most-accurate-rag](https://www.eyelevel.ai/post/most-accurate-rag); documents, questions, and code are public).

- **For:** proven design, already public, zero build time.
- **Against:** GroundX has published winning results on this exact set, so a skeptic can argue the system was tuned to it. It also has few cross-document questions and no not-in-library questions.

### Option B — follow that design on fresh documents (recommended)

Build a new library the same way, on documents neither company has published results against, chosen by a stated rule — for example: *fifteen recent annual reports (10-K filings), each over 150 pages, from the largest US public companies by market value on the lock date.* Public, freely redistributable, dense with tables and charts, and naturally supports cross-document questions. New questions get written to the mix in `question-taxonomy.md`.

- **For:** immune to the "tuned to your own benchmark" objection; covers cross-document and not-in-library.
- **Against:** ~150 questions must be written and verified by a person (the main cost).

**Recommendation: Option B for the headline test, with Option A's set run as a secondary check** — it's already public, so reporting results on it costs nothing and adds continuity with the published test.

## Rules that keep the test honest (either option)

- Document list and all questions are finalized **before any system runs**; their checksums are published so nothing can change quietly afterward.
- NVIDIA may veto or substitute the library before the test locks.
- Documents are selected by a stated mechanical rule — no hand-picking.

## Approval needed

- [ ] Option A, Option B, or both
- [ ] If B: confirm the fifteen-10-K rule, or propose another mechanical rule
- [ ] Name the person who writes and verifies the questions
