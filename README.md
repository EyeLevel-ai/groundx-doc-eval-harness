# Document Question-Answering Evaluation

A head-to-head accuracy test for systems that answer questions from libraries of complex documents — dense tables, charts, diagrams, long filings. Anyone can re-run it, substitute their own configurations, or swap in their own document library.

## The four systems compared

| # | System | Why it's here |
|---|---|---|
| 1 | GroundX, self-hosted | The system being evaluated |
| 2 | NVIDIA's RAG blueprint, factory settings | The reference stack, untouched |
| 3 | NVIDIA's RAG blueprint, tuned per its own documentation | The reference stack at its best |
| 4 | A frontier model, the whole document library supplied with every question | The no-retrieval baseline |

Questions are split evenly across the three places answers live in documents — **figures and graphs**, **table and layout structure**, and **plain text** — plus a set whose answers aren't in the library at all, following the method of EyeLevel's [published accuracy test](https://www.eyelevel.ai/post/most-accurate-rag). See [`preregistration/question-taxonomy.md`](preregistration/question-taxonomy.md).

## How the test is designed

- **The rules come first.** Document library, questions, grading instructions, and the bar for claiming a win are finalized and checksummed before any system runs — see [`preregistration/`](preregistration/).
- **Documents are chosen by a stated rule**, not hand-picked.
- **Configurations are inputs.** Each system's settings ship as committed files (added when the test locks); substituting your own is supported.
- **Two independent graders** (different AI models, published instructions, human spot-checks); each question answered three times.
- **Technical failures are separated from wrong answers** — timeouts and errors are excluded from scoring but counted and published per system.
- **Everything ships**: every question, answer, grade, and confidence range, in downloadable files, whatever the outcome.

## Repository layout

```
preregistration/   the locked rules: documents, questions, grading, win criteria
configs/           each system's exact settings (substitutable; added at lock)
harness/           the code that runs systems, grades answers, computes statistics
results/           per-question output files (added after the run)
```

The test has not yet locked: the question file, configs, and checksum manifest land at lock; results land after the run.
