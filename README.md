# GroundX Document-QA Evaluation Harness

A **pre-registered, four-arm, reproducible** evaluation harness for document question-answering over visually complex enterprise documents. Built so that anyone — including NVIDIA engineers — can re-run it, substitute their own configurations, or swap in their own corpus with a one-flag change.

## The four arms

| Arm | System | What it answers |
|---|---|---|
| 1 | **GroundX** (self-hosted Helm deployment) | The subject under test |
| 2 | **NVIDIA RAG blueprint v2.6.0** — documented defaults, unmodified | The partnership question |
| 3 | **NVIDIA RAG blueprint** — its own documented tuning recommendations | Removes the "you benchmarked the floor" objection |
| 4 | **Frontier long-context model, no retrieval** — chosen mechanically from a named public leaderboard at freeze date | The durability question |

## Neutrality mechanisms (the point of this repo)

- **Pre-registration:** document-selection rule, question set, question-type quotas, frontier-arm protocol, and the featured-number decision rule are frozen and SHA-256-hashed in [`preregistration/`](preregistration/) **before any arm runs**.
- **Mechanical corpus selection:** documents chosen by a stated rule, not hand-picked.
- **Configs are inputs:** every arm's configuration is a committed, pinned file. Substituting an alternative config (yours) is a first-class path — see `configs/README.md`.
- **Infra errors are not wrong answers:** timeouts and endpoint failures are excluded from scoring, logged, and reported per-arm alongside accuracy.
- **Dual judge:** two independent scoring judges with published prompts and cross-judge agreement stats; ≥10% independent human spot-check.
- **Statistics:** N ≥ 150 questions, ≥3 replicates, bootstrap confidence intervals — never bare point accuracy.
- **Decision rule:** comparative results are featured externally only if the pre-registered criterion is met. Otherwise this repo ships as a transparency artifact, whatever the numbers say.

## Repo layout

```
preregistration/   frozen + hashed: selection rule, QA set, taxonomy, protocols, decision rule
configs/           pinned per-arm configs (substitutable)
harness/           runners, scoring, judges, bootstrap stats
results/           per-question CSVs, replicate variance, per-arm error rates
gallery/           auto-generated side-by-side answer gallery (scripted case selection)
```

## Status

Work in progress — pre-registration phase. Nothing has been run; no numbers exist. That's the point: the rules come first.
