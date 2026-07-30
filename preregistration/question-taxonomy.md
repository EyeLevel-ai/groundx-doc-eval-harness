# Question Design

~150 questions, finalized before any system runs. Questions are **drafted by an AI assistant reading the documents directly** — independent of every system under test — **and each one is verified by a person** against the source page before lock. The drafting model is named and pinned in the lock manifest, and is pre-registered to be distinct from both grading models and from the frontier-arm model. The verifier is a named reviewer recorded in the lock manifest; verification happens entirely before lock, so the verifier never sees any system's output. NVIDIA has the same propose/veto right over the question set that it has over the document library ([corpus-shortlist.md](corpus-shortlist.md)): objections to any question before lock remove or replace it, and the replacement re-verifies the same way.

Each question is categorized on two independent dimensions: **where its answer lives** (source type) and **how far the system must look** (reach). The categorization method follows EyeLevel's [published accuracy test](https://www.eyelevel.ai/post/most-accurate-rag).

## Why split by answer source

Documents carry information three ways — in figures, in table structure, and in prose. Splitting evenly across all three, plus a set with no answer present, gives each retrieval mode equal weight instead of letting one dominate the score.

An even split is a choice, not a neutral fact: on a library required to be highly visual, 60% of questions depend on figures or table structure, and any system that reads layout well will benefit. The protection against that being self-serving is procedural, not rhetorical — the mix, the library, and every individual question are published before any system runs, and NVIDIA can strike or replace any of them (recorded in the manifest).

## The mix

| Answer source | Share | What it means |
|---|---|---|
| Figures and graphs | 30% | The answer is visual — a trend, an axis value, a diagram relationship — not written anywhere as text |
| Table and layout structure | 30% | The answer is implied by structure — which column a value sits under, what a row grouping means, what a footnote attaches to — not stated in any one cell or sentence |
| Plain text | 30% | The answer is written in a sentence; the task is finding the right passage |
| Not in the library | 10% | A plausible question whose answer is genuinely absent — the correct response is saying so |

## Reach

Within each of the three answer-source types, questions also vary in how far the system must look:

| Reach | Share within each source type |
|---|---|
| One passage, one document | 50% |
| Across pages of one document | 25% |
| Across two or more documents | 25% |

So the set includes, for example, questions that require comparing charts in two different documents.

## Recording format

Every question is recorded with: the question, the correct answer, acceptable alternate phrasings, its source type and reach, and the exact document(s) and page(s) holding the answer. Answers are graded on two things separately: **is the answer right**, and **does the citation point to the true source page**.
