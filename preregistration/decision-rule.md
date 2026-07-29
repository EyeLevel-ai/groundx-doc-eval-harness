# When Are We Allowed to Claim a Win?

This rule is written down and locked **before** the test runs, so the decision is mechanical — not a judgment call made while looking at the numbers.

## The rule

Each system answers every question three times. Two independent graders (two different AI models, with published grading instructions and spot-checked by a person) mark each answer right or wrong. From those marks we compute each system's accuracy, plus a statistical confidence range — the band the true accuracy almost certainly falls inside given this many questions.

**We may publicly claim GroundX outperformed the comparison system only if the *bottom* of GroundX's confidence range is higher than the *top* of the other system's range — according to both graders independently.**

In plain terms: the gap has to be big enough that it can't be explained by luck or grader noise. With ~150 questions, that means roughly an 8-point accuracy gap or more. A 74%-versus-72% result does not qualify, and we say so.

## What gets published no matter who wins

- Accuracy and confidence range for every system tested
- Answer accuracy and citation accuracy reported separately
- How often each system failed for technical reasons (timeouts, errors) — those don't count as wrong answers, but they are counted and shown
- Every question, every answer, every grade — in downloadable files, so anyone can re-check any row
