# Pre-registration

Every file in this directory is frozen **before any evaluation arm runs**. The freeze is recorded in `MANIFEST.sha256` (one hash per file) and the manifest's own hash is committed in a tagged git commit. After freeze, changes to these files invalidate the run and require a new pre-registration round, stated publicly in the results.

## Contents (to be authored and frozen — Week 1)

| File | What it locks |
|---|---|
| `document-selection-rule.md` | The mechanical rule that selects corpus documents (no hand-picking, no exclusions) |
| `question-set.jsonl` | All questions + ground-truth answers + page-level citations, authored before any system runs |
| `question-taxonomy.md` | Fixed quotas per question type (table lookup / narrative / cross-page / figure-chart) |
| `frontier-arm-protocol.md` | Leaderboard rule for model choice, context construction, truncation handling, re-run rule, cost reporting |
| `decision-rule.md` | The mechanical criterion for featuring comparative numbers externally |
| `judge-prompts/` | Pinned prompts for both judges |
| `MANIFEST.sha256` | Hash of every file above at freeze |

## Corpus veto

NVIDIA (or any re-runner) may nominate or veto the corpus — including the fallback corpus — via the documented methodology-call process. Swapping corpora is a one-flag change; the pre-registration discipline applies to the replacement equally.
