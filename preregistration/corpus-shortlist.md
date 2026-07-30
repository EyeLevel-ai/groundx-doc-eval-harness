# Test Documents

## The library

**About 1,000 pages, spread across documents of no more than 100 pages each** (roughly 15–25 documents) — enough documents that finding the right one is a real task, and no single document dominates.

Documents must be **highly visual and non-standardized**. Templated filings (SEC 10-Ks and the like) are excluded: they follow a common shape and are a popular AI training source, so a large model may have effectively memorized them.

**The library: NTSB accident investigation reports** — wreckage diagrams, flight-path maps, instrument plots, data-recorder charts, and every investigation formatted differently. Selection rule: *the most recent final aviation reports of 20–100 pages, newest first, until ~1,000 total pages.* The rule does the choosing — no hand-picking.

Fallbacks if NTSB sourcing fails a licensing or availability check: municipal budget books, then FDA advisory committee briefing documents (same rule shape).

Questions are written to the mix in `question-taxonomy.md` before any system runs.

## Locking

The document list and all questions are finalized and checksummed before any system runs (see the [locking process](README.md)). NVIDIA — whose RAG blueprint is one of the systems under test — may veto or substitute the library before lock; a replacement goes through the same process.

---

*Footnote: the corpus from EyeLevel's [earlier published test](https://www.eyelevel.ai/post/most-accurate-rag) is also re-run for continuity with that result. It is reported separately and never as the headline — GroundX has published on it before.*
