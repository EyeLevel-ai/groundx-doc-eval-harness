# The "Just Use a Big Model" Comparison

## Why it's in the test

It answers the natural question: *how well does the best general-purpose model do on the same task with no retrieval system at all?* Same library, same questions, same graders.

## The rules

1. **Which model:** whichever of OpenAI's or Anthropic's current flagship general-purpose models has the more recent release date on the day the test locks — a mechanical rule, not a choice made while looking at anything. The model name, version, and the release dates consulted are recorded in the manifest before any system runs.
2. **It gets the whole library, every question:** the model receives the entire test library with each question, in the most native form the model supports — the same task the retrieval systems face. The preference order is pre-committed: (a) native file/document upload where the provider offers it; (b) otherwise page images plus extracted text with page markers; (c) plain text with page markers only if the provider accepts neither files nor images. On a library preregistered as highly visual, figure and graph content must reach the model as images or files wherever the provider supports it — never as text renderings alone. The harness's frontier adapter (`harness/arms.py`) takes the library through a config-supplied loader, so the config committed at lock fixes the form, and the form used is published with the results. If the library exceeds the model's context window, that is itself a reported finding. No trimming to just the right document — that would turn a find-and-read test into a reading test.
3. **Same grading:** same questions, same two graders, same three repeats as every other system.
4. **Cost is part of the result:** we publish what each question cost in model fees next to the accuracy. Feeding whole documents to a flagship model per question is expensive, and that trade-off is part of the finding.
