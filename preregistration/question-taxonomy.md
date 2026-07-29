# Question Design

This design follows EyeLevel's published RAG accuracy test ([eyelevel.ai/post/most-accurate-rag](https://www.eyelevel.ai/post/most-accurate-rag)): questions are categorized by **where the answer lives in the document** — text, table, or figure — because that's what separates retrieval systems. This test extends that design in two ways: it weights toward the hardest sources instead of splitting evenly, and it adds a scope dimension (some questions require crossing pages or documents).

## The three information sources, hardest first

1. **Figures and graphs (hardest).** The answer is visual — a trend in a chart, a value read off an axis, a relationship in a diagram — and is *not written anywhere as text*. Systems that only process text score near zero here.
2. **Layout and table structure (second).** The answer isn't stated in any single cell or sentence; it's implied by structure — which column a value sits under, what a row grouping means, what a footnote marker attaches to.
3. **Plain text (easiest).** The answer is written in a sentence; the challenge is only finding the right passage.

## Question mix (~150 questions)

| Answer source | Share | Why this weight |
|---|---|---|
| Figures / graphs | 35% | The hardest problem in document Q&A; the widest gap between systems |
| Layout / table structure | 30% | Second hardest; where table-naive systems quietly fail |
| Plain text | 20% | The baseline every system should handle |
| Not in the library | 15% | Tests refusing to invent an answer — a plausible question whose answer is genuinely absent |

## The scope dimension

Within each of the three source types, questions are split by how far the system must reach:

| Scope | Share within each source type |
|---|---|
| One passage, one document | 50% |
| Across pages of one document | 25% |
| Across two or more documents | 25% |

So, for example, some figure questions require comparing charts in two different documents — the hardest source combined with the hardest scope.

## Recording format

Every question is recorded with: the question, the correct answer, acceptable alternate phrasings, the source type and scope, and the exact document(s) and page(s) holding the answer. Answers are graded on two things separately: **is the answer right** and **does the citation point to the true source page**.
