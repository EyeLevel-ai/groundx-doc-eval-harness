# The "Just Use a Big Model" Comparison

## Why it's in the test

The obvious challenge to any document-retrieval product: *"Why not paste the documents into the best general-purpose AI model and skip retrieval entirely?"* Rather than argue, we test it — and tilt the test **in the big model's favor**, so the result means something.

## The rules

1. **Which model:** the current flagship model from OpenAI or Anthropic at the time the test locks (model name and date recorded). If a newer flagship ships, we re-run within a week and publish the new numbers alongside the old.
2. **The head start it gets:** the model receives only the document(s) that actually contain the answer — it never has to find the right document in the library, which is half the real problem. Its score is therefore a best case, and is labeled that way.
3. **Same grading:** same questions, same two graders, same three repeats as every other system.
4. **Cost is part of the result:** we publish what each question cost in model fees next to the accuracy. Feeding whole documents to a flagship model per question is expensive, and that trade-off is part of the finding.
