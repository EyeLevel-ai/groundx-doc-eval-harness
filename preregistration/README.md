# Locked Before Running

Everything in this folder is finalized **before any system answers a single test question**. When it's final, we publish a checksum of every file (in `MANIFEST.sha256`); changing anything afterward would change the checksum and be visible to everyone. Because this repo is under our control, the manifest hash is also anchored outside it at lock time — a signed git tag plus a copy of the hash lodged with NVIDIA and a public timestamping service — and this file will record exactly where. That's the point: the rules can't move after the results exist, and you don't have to take our word for it.

| File | What it locks |
|---|---|
| `corpus-shortlist.md` | Which documents the test library contains, and the rule that chose them |
| `question-taxonomy.md` | The ~150 questions' types and quotas |
| `questions.jsonl` *(added at lock)* | The questions themselves, with answers and source pages |
| `judge-prompts/` | The exact grading instructions given to the two AI graders |
| `frontier-arm-protocol.md` | The rules for the "just paste it into a giant model" comparison |
| `decision-rule.md` | The pre-agreed bar for publicly claiming a win |
| `MANIFEST.sha256` | Checksums of all of the above at lock time |

Anyone — including NVIDIA, whose RAG blueprint is one of the systems under test — may propose or veto the document library **and the question set** before lock. Swapping either re-runs the same locking process on the replacement.
