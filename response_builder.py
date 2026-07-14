"""Build transparent extractive answers without an LLM."""

from dataclasses import dataclass
import re
from typing import List

from config import HUMAN_ESCALATION
from policy_search import SearchResult, tokenize


MINIMUM_SUPPORTED_SCORE = 0.13


@dataclass(frozen=True)
class AssistantResponse:
    status: str
    answer: str
    source_title: str = ""
    source_section: str = ""
    source_version: str = ""
    confidence_label: str = ""
    applied_controls: tuple[str, ...] = ()


def build_response(question: str, results: List[SearchResult]) -> AssistantResponse:
    if not results or results[0].score < MINIMUM_SUPPORTED_SCORE:
        return AssistantResponse(
            status="escalated",
            answer=HUMAN_ESCALATION,
            confidence_label="insufficient approved evidence",
            applied_controls=(
                "groundedness_threshold",
                "human_escalation",
                "no_unsupported_answer",
            ),
        )

    best = results[0]
    sentences = _sentences(best.chunk.text)
    ranked = _rank_sentences(question, sentences)
    answer_sentences = ranked[:2] if ranked else sentences[:2]
    answer = " ".join(answer_sentences).strip()

    if not answer:
        return AssistantResponse(
            status="escalated",
            answer=HUMAN_ESCALATION,
            confidence_label="insufficient approved evidence",
            applied_controls=("human_escalation",),
        )

    return AssistantResponse(
        status="answered",
        answer=answer,
        source_title=best.chunk.title,
        source_section=best.chunk.section,
        source_version=best.chunk.version,
        confidence_label=_confidence_label(best.score),
        applied_controls=(
            "approved_source_only",
            "source_citation",
            "extractive_response",
            "groundedness_threshold",
        ),
    )


def _sentences(text: str) -> List[str]:
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", text)
        if sentence.strip()
    ]


def _rank_sentences(question: str, sentences: List[str]) -> List[str]:
    query_tokens = set(tokenize(question))
    scored = []
    for index, sentence in enumerate(sentences):
        sentence_tokens = set(tokenize(sentence))
        overlap = len(query_tokens.intersection(sentence_tokens))
        score = overlap / max(1, len(query_tokens))
        scored.append((score, -index, sentence))
    scored.sort(reverse=True)
    return [sentence for score, _, sentence in scored if score > 0]


def _confidence_label(score: float) -> str:
    if score >= 0.55:
        return "strong retrieval match"
    if score >= 0.30:
        return "moderate retrieval match"
    return "limited retrieval match"
