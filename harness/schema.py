"""Core data shapes for the four-arm eval harness."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict


@dataclass
class QAItem:
    qid: str
    qtype: str  # table | narrative | crosspage | figure | unanswerable
    question: str
    answer: str
    answer_alternates: list[str] = field(default_factory=list)
    evidence: list[dict] = field(default_factory=list)  # [{doc, pages}]


@dataclass
class ArmAnswer:
    qid: str
    arm: str
    replicate: int
    answer_text: str
    citations: list[dict] = field(default_factory=list)  # [{doc, page}]
    latency_s: float | None = None
    tokens_in: int | None = None
    tokens_out: int | None = None
    infra_error: str | None = None  # populated => EXCLUDED from scoring, logged


@dataclass
class JudgedAnswer:
    qid: str
    arm: str
    replicate: int
    judge: str
    correct: bool
    citation_correct: bool | None
    rationale: str

    def row(self) -> dict:
        return asdict(self)
