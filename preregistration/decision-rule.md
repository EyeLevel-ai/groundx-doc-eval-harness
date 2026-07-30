# When We May Claim a Win

The operative rule: a win may be claimed only when the bottom of GroundX's accuracy confidence range sits above the top of the comparison system's range, according to both graders independently. With ~150 questions, that separation requires an accuracy lead of roughly **12 points or more** at mid-range scores — less when both systems score high, where the ranges tighten. That figure comes from running the committed bootstrap code on synthetic grades, not from a hand calculation. The confidence-interval separation is the rule; the points are what it means in practice. Smaller leads are published as results, with no winner claimed.

This rule is locked before the test runs, so the call is mechanical — never a judgment made while looking at the numbers. The computation itself is committed code (`harness/stats.py`, `decision_rule()`) — it splits grades by grader and requires the separation under each, with a pre-registered bootstrap seed.

## How grading works

Each system answers every question three times. Two independent graders (two different AI models with published grading instructions) mark each answer right or wrong. Statistics then give each system's accuracy a confidence range — the band its true accuracy almost certainly falls in.

**Human spot-checks, pre-registered:** a person re-grades a uniform random sample of 10% of judged answers (seeded, sampled per system so no system is checked more than another), blind to which system produced each answer. Human/AI disagreements are published as a list; an AI grade is overridden only through that published list, never silently. If spot-check disagreement exceeds 10%, the affected grader's grades are re-audited in full and the audit ships with the results.

**Grader agreement, pre-registered:** cross-grader agreement (Cohen's kappa, computed by `harness/stats.py`) is published. If kappa falls below 0.6, no win is claimed regardless of the score gap, and the disagreement analysis ships with the results.

**Citation accuracy, pre-registered denominator:** for answerable questions, an answer that offers no citation counts as citation-incorrect in the published citation-accuracy number — a system cannot improve its citation score by declining to cite. The count of no-citation answers is also published per system. Mechanically: the graders output `citation_correct: null` when an answer offers no citations, and the harness converts that null to incorrect for answerable questions (`harness/stats.py`, `citation_accuracy()`) — the mapping is committed code, not a post-hoc choice.

**Technical failures, pre-registered:** a failed request is retried up to two times before it is recorded as a technical failure. Only transport-level failures qualify — timeouts, connection errors, server errors. Anything the model actually returns is graded as an answer: a refusal is graded like any answer, and the frontier arm hitting its context-window limit counts as a wrong answer for it and is reported as a finding per the [frontier-arm protocol](frontier-arm-protocol.md). Technical failures are excluded from accuracy but counted and published per system. If either GroundX or the comparison system records technical failures on more than 10% of its requests, no win is claimed against that comparison — exclusions cannot quietly remove a system's hardest questions.

## Published either way

- Accuracy and confidence range for every system
- Answer accuracy and citation accuracy, reported separately
- Technical failure counts per system (timeouts and errors don't count as wrong answers, but are shown)
- Cross-grader agreement and the human spot-check disagreement list
- Every question, answer, and grade in downloadable files, so anyone can re-check any row
