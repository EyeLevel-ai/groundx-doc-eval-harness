# Test Documents

## The library

**About 1,000 pages, spread across documents of no more than 100 pages each** (roughly 15–25 documents) — enough documents that finding the right one is a real task, and no single document dominates.

Documents must be **highly visual and non-standardized**. Templated filings (SEC 10-Ks and the like) are excluded: they follow a common shape and are a popular AI training source, so a large model may have effectively memorized them.

Sources, in order of preference — public, chart- and diagram-heavy, no two alike:

| Source | Why it's hard | Selection rule |
|---|---|---|
| 1. **NTSB accident investigation reports** | Wreckage diagrams, flight-path maps, instrument plots, data-recorder charts; every investigation formatted differently | Most recent final aviation reports of 20–100 pages, newest first, until ~1,000 total pages |
| 2. **Municipal budget books** | Every city invents its own format; charts, organization diagrams, fund tables | Current adopted budgets of the largest US cities, documents of 20–100 pages, until ~1,000 total pages |
| 3. **FDA advisory committee briefing documents** | Clinical trial figures, dosing charts, statistical plots; sponsor-authored, formats vary widely | Most recent briefing books of 20–100 pages, newest first, until ~1,000 total pages |

The selection rule does the choosing — no hand-picking. Questions are written to the mix in `question-taxonomy.md` before any system runs.

**Secondary set:** EyeLevel's published test (1,146 pages of public Deloitte documents, 92 questions — [eyelevel.ai/post/most-accurate-rag](https://www.eyelevel.ai/post/most-accurate-rag)) also runs, for continuity with published results. It is reported separately, never as the headline: GroundX has published results on it before.

## Keeping it honest

- Document list and all questions are finalized and checksummed **before any system runs**; changes afterward would be visible to everyone.
- NVIDIA may veto or substitute the library before the test locks; a replacement goes through the same locking process.
