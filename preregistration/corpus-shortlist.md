# Corpus shortlist — DRAFT for SME sign-off (task 2.2)

Selection rule for the primary corpus: a public, third-party document-QA benchmark with visually complex layouts **that neither GroundX/EyeLevel nor NVIDIA has published results on**. DocBench-family is excluded (GroundX has a published DocBench result). NVIDIA's RAG blueprint publishes accuracy numbers in its `docs/accuracy-benchmarks.md` — whatever datasets appear there are likewise excluded **[action: enumerate and record them here before freeze]**.

## Candidates (in preference order)

| Candidate | Why it fits | Licensing / access | Exclusion risk |
|---|---|---|---|
| **DUDE** (Document Understanding Dataset and Evaluation, ICCV '23) | Multi-domain real documents, multi-page, diverse layouts (forms, tables, diagrams); QA pairs include extractive + abstractive + unanswerable | CC-BY-4.0-ish per-document sourcing; verify redistribution terms | Check both parties' publications before freeze |
| **MP-DocVQA** (multi-page DocVQA) | Multi-page industrial documents; page-level evidence annotations align with our citation-accuracy metric | Registration-gated download; verify redistribution rights for the harness repo | DocVQA family is widely benchmarked — verify NVIDIA blueprint docs don't cite it |
| **TAT-QA** (table-and-text QA over financial reports) | Dense financial tables + narrative — matches the FSI vertical story | MIT-style; hosted on GitHub | Heavily benchmarked in finance-NLP papers; neither-party rule may still hold |
| **Kleister-Charity / Kleister-NDA** | Long real-world documents (charity reports, NDAs); key-information extraction ground truth | CC BY-SA / check per set | Lower benchmark saturation; extraction-shaped rather than QA-shaped (would need question templating) |

## Pre-registered fallback (if all candidates fail licensing or neither-party checks)

Public SEC/government filings with **both layers frozen and hashed before any run**:
1. Mechanical document-selection rule (draft): *the 15 most recent 10-K filings exceeding 150 pages from the largest-by-market-cap constituents of a named index as of the freeze date, no exclusions.*
2. SME-authored question set written before either system runs, against the question-type taxonomy quotas (`question-taxonomy.md`), frozen in the same manifest hash.

## Sign-off checklist (SME)

- [ ] Confirm neither-party publication check per candidate (GroundX blog/bench posts; NVIDIA blueprint `accuracy-benchmarks.md` + NIM model cards)
- [ ] Licensing permits: local evaluation use, quoting excerpts in the gallery, redistribution of document IDs + hashes (not necessarily the documents themselves)
- [ ] Document-class coverage matches target verticals (scanned forms / dense tables / long filings)
- [ ] Pick primary + confirm fallback rule wording
