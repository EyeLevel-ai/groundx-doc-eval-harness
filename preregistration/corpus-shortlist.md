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

Build a new library the same way, on documents neither company has published results against. The documents must be **highly visual and non-standardized**. Standardized filings like SEC 10-Ks are ruled out: they follow a template, and they're a popular AI training source — a big general-purpose model may have effectively memorized their shape.

Candidate sources that fit (public, chart- and diagram-heavy, no two alike):

| Source | Why it's hard | Example selection rule |
|---|---|---|
| **NTSB accident investigation reports** | Wreckage diagrams, flight-path maps, instrument plots, data-recorder charts; every investigation formatted differently | The 12 most recent final aviation reports over 60 pages |
| **Municipal budget books** | Every city invents its own format; packed with charts, org diagrams, fund tables | The adopted budgets of the 12 largest US cities for the current fiscal year |
| **FDA advisory committee briefing documents** | Clinical trial figures, dosing charts, statistical plots; sponsor-authored so formats vary widely | The 12 most recent briefing books over 80 pages |

One source (or a stated mix) is picked at approval time; the selection rule does the choosing from there — no hand-picking. New questions get written to the mix in `question-taxonomy.md`.

- **For:** immune to the "tuned to your own benchmark" objection; genuinely visual, non-templated documents; covers cross-document and not-in-library questions.
- **Against:** ~150 questions must be written and verified by a person (the main cost).

**Recommendation: Option B for the headline test, with Option A's set run as a secondary check** — it's already public, so reporting results on it costs nothing and adds continuity with the published test.

## Rules that keep the test honest (either option)

- Document list and all questions are finalized **before any system runs**; their checksums are published so nothing can change quietly afterward.
- NVIDIA may veto or substitute the library before the test locks.
- Documents are selected by a stated mechanical rule — no hand-picking.

## Approval needed

- [ ] Option A, Option B, or both
- [ ] If B: pick the document source (NTSB reports, municipal budgets, FDA briefing books, or a stated mix) and confirm its selection rule
- [ ] Name the person who writes and verifies the questions
