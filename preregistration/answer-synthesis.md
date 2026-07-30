# The GroundX Arm — Answer Synthesis

## The design: isolate retrieval

The test asks which system finds and reads the right material. So the GroundX arm and the blueprint arms differ **only** in retrieval and ingestion: the GroundX arm retrieves with self-hosted GroundX, then writes its answer with the **same answering-LLM configuration as the blueprint arms** (same model, same endpoint settings, committed in `configs/` at lock). Any accuracy difference is attributable to what each system retrieved, not to a better answer-writing model or prompt on one side.

## The exact synthesis prompt

The GroundX arm's answer is produced by `harness/arms.py` (`_synthesize()`) with this user message, verbatim — `{question}` is the test question and `{context}` is the retrieved passages joined by `---` separators:

```
Answer strictly from the context. If the context lacks the answer, say the documents do not contain it.

QUESTION: {question}

CONTEXT:
{context}
```

No other instructions are added by the GroundX arm. An optional system message comes from the answering-LLM config file — shared with the blueprint arms and committed at lock.

## The abstention instruction and the unanswerable questions

The prompt above tells the model to say when the documents lack the answer. On the unanswerable slice of the question set — where declaring absence *is* the correct answer — that instruction would be an advantage if the blueprint arms lacked an equivalent. Two commitments, made here before lock:

1. Where the blueprint exposes a synthesis prompt, its committed configuration includes an equivalent abstention instruction, recorded in `configs/` at lock.
2. Accuracy on the unanswerable slice is reported separately per system alongside the headline number, so readers can see how much of any gap comes from that slice.

## Locking

This file and the hash of `harness/arms.py` (which contains the prompt) are covered by `MANIFEST.sha256` at lock. Changing the prompt afterward would change both hashes and be visible to everyone.
