# Document Question-Answering Evaluation

**Preregistration stage — the rules are public, no results exist yet.** That order is the point: the document library, the questions, and the bar for claiming a win are all committed and checksummed before any system runs, so nothing can move once numbers exist. Results land here whatever they say.

The test itself: a head-to-head accuracy comparison for systems that answer questions from libraries of complex documents — dense tables, charts, diagrams, long filings. It is built to be re-run by anyone, with their own configurations or their own document library.

The pre-committed win bar, in one sentence: a win is claimed only when the bottom of GroundX's accuracy confidence range sits above the top of the comparison system's range, under both graders independently ([decision rule](preregistration/decision-rule.md)).

> **Status**
> - **Runnable today:** the harness code and its self-test (below), plus the rule drafts in [`preregistration/`](preregistration/).
> - **Lands at lock:** the question file, per-system configs, and `MANIFEST.sha256`; per-question results land in `results/` after the run.
> - **NVIDIA's review** of the corpus and question set is an open invitation — open an issue to take it up. It is not a gate: if it hasn't happened by lock, the rules lock without it, and the manifest records who reviewed the corpus and questions and who tuned the blueprint arm — non-engagement is visible, not silent.

## The four systems compared

| # | System | Why it's here |
|---|---|---|
| 1 | GroundX, self-hosted | The system being evaluated |
| 2 | NVIDIA's RAG blueprint, factory settings | The reference stack, untouched |
| 3 | NVIDIA's RAG blueprint, tuned per its own documentation ([tuning protocol](preregistration/blueprint-tuning-protocol.md)) | The reference stack at its best |
| 4 | A frontier model, the whole document library supplied with every question ([protocol](preregistration/frontier-arm-protocol.md)) | The provider-default baseline — no retrieval system of our own |

To stand up the GroundX self-hosted arm, use the deploy scripts in the companion [groundx-nvidia-quickstart](https://github.com/EyeLevel-ai/groundx-nvidia-quickstart) repo (`deploy/` — one GPU machine, ~45 minutes).

Questions are split evenly across the three places answers live in documents — **figures and graphs**, **table and layout structure**, and **plain text** — plus a set whose answers aren't in the library at all, following the method of EyeLevel's [published accuracy test](https://www.eyelevel.ai/post/most-accurate-rag). See [`preregistration/question-taxonomy.md`](preregistration/question-taxonomy.md).

## How the test is designed

- **The rules come first.** Document library, questions, grading instructions, and the bar for claiming a win are finalized and checksummed before any system runs — see [`preregistration/`](preregistration/).
- **Documents are chosen by a stated rule**, not hand-picked.
- **Configurations are inputs.** Each system's settings ship as committed files (added when the test locks); substituting your own is supported.
- **Two independent graders** (different AI models, published instructions, human spot-checks); each question answered three times.
- **Technical failures are separated from wrong answers** — transport errors are retried, then excluded from scoring but counted and published per system; above a 10% failure rate no win is claimed against that comparison.
- **Everything ships**: every question, answer, grade, and confidence range, in downloadable files, whatever the outcome.

## Run the self-test now

The statistics, decision rule, and judge plumbing are runnable today:

```bash
pip install -r requirements.txt
python -m harness.selftest          # synthetic fixtures: stats, decision rule, prompt loading
python -m harness.selftest --live   # adds a 2-item live judge smoke (needs NVIDIA_API_KEY / OPENAI_API_KEY)
```

It verifies, among other things, that the decision rule refuses to claim a win on a small gap.

## How a run executes

The end-to-end runner lands at lock, together with the question file and per-system configs it needs. The flow it drives is already committed: `harness/arms.py` answers each question three times per system, `harness/judge.py` grades every answer with both pinned graders (refusing to run on a manifest mismatch), and `harness/stats.py` computes accuracies, confidence ranges, and the win/no-win call. Per-question output lands in `results/`.

## Repository layout

```
preregistration/   the locked rules: documents, questions, grading, win criteria
configs/           each system's exact settings (substitutable; added at lock)
harness/           the code that runs systems, grades answers, computes statistics
results/           per-question output files (added after the run)
```
