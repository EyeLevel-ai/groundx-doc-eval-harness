# Test Documents

## The library

**About 1,000 pages, spread across documents of no more than 100 pages each** (roughly 15–25 documents) — enough documents that finding the right one is a real task, and no single document dominates.

Documents must be **highly visual and non-standardized**. Templated filings (SEC 10-Ks and the like) are excluded: they follow a common shape and are a popular AI training source, so a large model may have effectively memorized them.

**The library: NTSB accident investigation reports** — wreckage diagrams, flight-path maps, instrument plots, data-recorder charts, and every investigation formatted differently. Selection rule: *the most recent final aviation reports of 20–100 pages, newest first, until ~1,000 total pages.* The rule does the choosing — no hand-picking.

Fallbacks if NTSB sourcing fails a licensing or availability check: municipal budget books, then FDA advisory committee briefing documents (same rule shape).

Questions are written to the mix in `question-taxonomy.md` before any system runs.

**Secondary set:** EyeLevel's published test (1,146 pages of public Deloitte documents, 92 questions — [eyelevel.ai/post/most-accurate-rag](https://www.eyelevel.ai/post/most-accurate-rag)) also runs, for continuity with published results. It is reported separately, never as the headline: GroundX has published results on it before.

## Locking

The document list and all questions are finalized and checksummed before any system runs (see the [locking process](README.md)). NVIDIA — whose RAG blueprint is one of the systems under test — may veto or substitute the library before lock; a replacement goes through the same process.
