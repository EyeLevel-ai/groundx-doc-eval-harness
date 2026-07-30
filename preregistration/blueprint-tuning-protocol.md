# Tuning the Blueprint Arm

Arm 3 runs NVIDIA's RAG blueprint tuned per its own documentation. That is the arm most exposed to a thumb-on-the-scale objection — *"they tuned their competitor badly"* — so the tuning itself is preregistered:

1. **Who tunes.** The manifest names the person who performed the tuning. NVIDIA may supply or amend the tuned configuration itself any time before lock; whether it did is recorded either way, like the corpus review.
2. **Allowed inputs.** The blueprint's own published documentation and the test document library — never the test questions. Tuning finishes before the question set locks, and the tuner sees no system's test answers or grades.
3. **Budget and stopping rule.** At most 20 evaluated configurations within five working days. Each configuration is evaluated only on a small development question set that is disjoint from the test questions and published with the results, along with the tuning log (configurations tried and their development scores).
4. **Locked like everything else.** The tuned configuration is committed in `configs/` and covered by `MANIFEST.sha256` before any system answers a test question.
