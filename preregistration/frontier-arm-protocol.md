# The "Just Use a Big Model" Comparison

## Why it's in the test

The obvious challenge to any document-retrieval product: *"Why not paste the documents into the best general-purpose AI model and skip retrieval entirely?"* Rather than argue, we test it — same library, same questions, same graders.

## The rules

1. **Which model:** the current flagship model from OpenAI or Anthropic at the time the test locks (model name and date recorded). If a newer flagship ships, we re-run within a week and publish the new numbers alongside the old.
2. **It gets the whole library, every question:** the model receives the entire test library with each question, in the most native form the model supports (file upload where offered, otherwise full text with page markers) — the same task the retrieval systems face. If the library doesn't fit in the model's context window, that is itself a reported finding: the do-nothing alternative can't even hold the documents. No trimming to just the right document; that would turn this into a reading test instead of a find-and-read test.
3. **Same grading:** same questions, same two graders, same three repeats as every other system.
4. **Cost is part of the result:** we publish what each question cost in model fees next to the accuracy. Feeding whole documents to a flagship model per question is expensive, and that trade-off is part of the finding.
