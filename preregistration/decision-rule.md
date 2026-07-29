# Featured-number decision rule — DRAFT (task 2.3)

Frozen and hashed before any arm runs. The go/no-go on featuring comparative numbers externally is **mechanical**, decided by this rule — never a judgment call made while looking at results.

## Rule

Comparative results may be **featured** (headlines, one-pagers, external decks) only if, on the frozen question set with N ≥ 150, 3 replicates per arm, and both judges:

> **GroundX's bootstrap 95% confidence-interval lower bound on answer accuracy exceeds the best blueprint arm's (defaults or tuned, whichever is higher) CI upper bound**, under both judges independently.

Otherwise, the harness and full results still ship as a transparency artifact, and external material leads with integration + deployment (no comparative accuracy claims).

## Reporting requirements regardless of outcome

- Point estimates with bootstrap CIs for all four arms (including the frontier long-context arm, whatever it shows)
- Citation-accuracy reported separately from answer accuracy
- Per-arm infrastructure-error/timeout rates (errors excluded from scoring, logged)
- Per-question CSVs + replicate variance + cross-judge agreement
- Frontier arm: per-question token cost next to accuracy; standing re-run rule on leaderboard change

## Detectable effect note

With N = 150 and typical accuracy variance, the CI-separation criterion roughly requires a true gap of ~8–12 percentage points to trigger **[to compute exactly at freeze with the pilot variance measurement]**. Smaller true gaps will (correctly) fail to feature.
