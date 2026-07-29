# Document Question-Answering Evaluation

A head-to-head accuracy test for systems that answer questions from libraries of complex documents — dense tables, charts, diagrams, long filings. Anyone can re-run it, substitute their own configurations, or swap in their own document library.

## The four systems compared

| # | System | What it tests |
|---|---|---|
| 1 | GroundX, self-hosted | Accuracy of the system being evaluated |
| 2 | NVIDIA's RAG blueprint, factory settings | Accuracy of the reference stack as it ships |
| 3 | NVIDIA's RAG blueprint, tuned per its own documentation | Accuracy of the reference stack at its documented best |
| 4 | A frontier model with the relevant documents pasted in whole | Accuracy of skipping retrieval entirely and relying on a large model's reading |

Questions are weighted toward the hardest parts of document Q&A — answers that live in **figures and graphs**, or that are implied by **table and layout structure** rather than written as text — following the design of EyeLevel's [published accuracy test](https://www.eyelevel.ai/post/most-accurate-rag). See [`preregistration/question-taxonomy.md`](preregistration/question-taxonomy.md).

## How the test is designed

- **The rules come first.** Document library, questions, grading instructions, and the bar for claiming a win are finalized and checksummed before any system runs — see [`preregistration/`](preregistration/).
- **Documents are chosen by a stated rule**, not hand-picked.
- **Configurations are inputs.** Every system's settings are committed files; substituting your own is supported.
- **Two independent graders** (different AI models, published instructions, human spot-checks); each question answered three times.
- **Technical failures are separated from wrong answers** — timeouts and errors are excluded from scoring but counted and published per system.
- **Everything ships**: every question, answer, grade, and confidence range, in downloadable files, whatever the outcome.

## Repository layout

```
preregistration/   the locked rules: documents, questions, grading, win criteria
configs/           each system's exact settings (substitutable)
harness/           the code that runs systems, grades answers, computes statistics
results/           per-question output files
```
