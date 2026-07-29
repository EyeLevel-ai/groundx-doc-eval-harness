# The "Just Use a Big Model" Comparison

## Why it's in the test

It answers the natural question: *how well does the best general-purpose model do on the same task with no retrieval system at all?* Same library, same questions, same graders.

## The rules

1. **Which model:** the current flagship model from OpenAI or Anthropic at the time the test locks (model name and date recorded).
2. **It gets the whole library, every question:** the model receives the entire test library with each question, in the most native form the model supports (file upload where offered, otherwise full text with page markers) — the same task the retrieval systems face. If the library exceeds the model's context window, that is itself a reported finding. No trimming to just the right document — that would turn a find-and-read test into a reading test.
3. **Same grading:** same questions, same two graders, same three repeats as every other system.
4. **Cost is part of the result:** we publish what each question cost in model fees next to the accuracy. Feeding whole documents to a flagship model per question is expensive, and that trade-off is part of the finding.
