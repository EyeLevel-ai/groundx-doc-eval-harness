# When We May Claim a Win

**The rule: we publicly claim GroundX outperformed the comparison system only if GroundX's accuracy lead is roughly 8 points or more — a gap too large for luck to explain with ~150 questions. Smaller leads are published as results, with no winner claimed.**

This rule is locked before the test runs, so the call is mechanical — never a judgment made while looking at the numbers.

## How the 8 points is determined

Each system answers every question three times. Two independent graders (two different AI models with published grading instructions, spot-checked by a person) mark each answer right or wrong. Statistics then give each system's accuracy a confidence range — the band its true accuracy almost certainly falls in. A win may be claimed only when **the bottom of GroundX's range is above the top of the other system's range, according to both graders independently.** With ~150 questions, that separation requires roughly an 8-point lead.

## Published either way

- Accuracy and confidence range for every system
- Answer accuracy and citation accuracy, reported separately
- Technical failure counts per system (timeouts and errors don't count as wrong answers, but are shown)
- Every question, answer, and grade in downloadable files, so anyone can re-check any row
