# The "Just Use a Giant Model" Comparison

## Why this comparison exists

The obvious challenge to any document-retrieval product: *"Why not paste the documents into the biggest general-purpose AI model and skip retrieval entirely?"* Rather than argue, we test it — and we tilt the test **in the big model's favor**, so if GroundX still wins, the result means something.

## The rules

1. **Which model:** whatever model ranks #1 on a named public leaderboard for long-document reading on the day the test locks. Picked by rank, not by us. If a new model takes the #1 spot later, we re-run within a week and publish the new numbers alongside the old.
2. **The handicap in its favor:** the big model is given only the document(s) that actually contain the answer — it never has to find the right document among fifteen, which is half the real problem. This makes its score a *best case*, and we label it that way.
3. **Same grading:** same questions, same two graders, same three repeats as every other system.
4. **Cost is part of the answer:** we publish what each question cost in model fees next to the accuracy. Pasting hundreds of pages into a frontier model per question is expensive; that trade-off is part of the finding.
