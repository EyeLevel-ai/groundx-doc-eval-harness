# Document Question-Answering Evaluation

A head-to-head accuracy test for systems that answer questions from libraries of complex documents (dense tables, long filings, charts). Built so that anyone — including the vendors being compared — can re-run it, substitute their own configurations, or swap in their own document library.

## The four systems compared

| # | System | Question it answers |
|---|---|---|
| 1 | GroundX, self-hosted | The system under test |
| 2 | NVIDIA's RAG blueprint, factory settings | How does GroundX compare to the reference stack, untouched? |
| 3 | NVIDIA's RAG blueprint, tuned per its own docs | Removes "you tested a badly configured baseline" |
| 4 | A frontier model with the documents pasted in whole | Would skipping retrieval entirely work better? |

## Why the results can be trusted

- **The rules are locked before anything runs.** Document library, questions, grading instructions, and the bar for claiming a win are finalized and checksummed first — see [`preregistration/`](preregistration/).
- **Documents are chosen by a stated rule**, not hand-picked.
- **Configurations are inputs.** Every system's settings are committed files; substituting your own is supported and documented.
- **Two independent graders** (different AI models, published instructions, human spot-checks), each question answered three times.
- **Technical failures aren't wrong answers.** Timeouts and errors are excluded from scoring but counted and published per system.
- **Everything ships**: every question, answer, grade, and confidence range, in downloadable files — whatever the outcome.

## Repository layout

```
preregistration/   the locked rules: documents, questions, grading, win criteria
configs/           each system's exact settings (substitutable)
harness/           the code that runs systems, grades answers, computes statistics
results/           per-question output files (empty until the test runs)
```

## Status

Rules are drafted and under review. No test has been run; no numbers exist yet.
