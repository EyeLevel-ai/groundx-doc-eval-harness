# Question Design

~150 questions, finalized before any system runs. To keep the workload sane, questions are **drafted by an AI assistant reading the documents directly** — independent of every system under test — **and each one is verified by a person** against the source page before lock. The verifier's decision is final. Each question is categorized by **where its answer lives in the document** — following the method of EyeLevel's published accuracy test ([eyelevel.ai/post/most-accurate-rag](https://www.eyelevel.ai/post/most-accurate-rag)).

## Why split by answer source

Enterprise documents carry information three different ways — in figures, in table structure, and in prose — and retrieval systems differ most in how well they read the first two. Splitting the questions evenly across all three sources, plus a set with no answer present, gives broad coverage of how information actually needs to be retrieved from documents.

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
