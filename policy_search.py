"""Dependency-free local retrieval from approved synthetic policies."""

from collections import Counter, defaultdict
from dataclasses import dataclass
import math
from pathlib import Path
import re
from typing import Dict, Iterable, List


STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can",
    "company", "companies", "employee", "employees",
    "do", "does", "for", "from", "how", "i", "in", "is", "it",
    "me", "of", "on", "or", "our", "policy", "policies",
    "should", "the", "their", "to", "what", "when", "where",
    "who", "with", "you", "your"
}

SYNONYMS = {
    "holiday": "vacation",
    "holidays": "vacation",
    "pto": "vacation",
    "telework": "remote",
    "hybrid": "remote",
    "reimbursement": "expense",
    "reimburse": "expense",
    "receipt": "expense",
    "receipts": "expense",
}


def tokenize(text: str) -> List[str]:
    tokens = []
    for token in re.findall(r"[a-z0-9]+", text.lower()):
        token = SYNONYMS.get(token, token)
        if len(token) > 1 and token not in STOP_WORDS:
            tokens.append(token)
    return tokens


@dataclass(frozen=True)
class PolicyChunk:
    document_id: str
    title: str
    version: str
    classification: str
    status: str
    section: str
    text: str
    source_file: str


@dataclass(frozen=True)
class SearchResult:
    chunk: PolicyChunk
    score: float
    overlapping_terms: tuple[str, ...]


class PolicySearchEngine:
    def __init__(self, chunks: Iterable[PolicyChunk]):
        self.chunks = list(chunks)
        if not self.chunks:
            raise ValueError("At least one approved policy chunk is required.")

        for chunk in self.chunks:
            if chunk.status.lower() != "approved for poc":
                raise ValueError(f"Unapproved document loaded: {chunk.source_file}")
            if chunk.classification.lower() != "internal synthetic":
                raise ValueError(f"Non-synthetic document loaded: {chunk.source_file}")

        self._counts = [
            Counter(tokenize(f"{chunk.section} {chunk.text}"))
            for chunk in self.chunks
        ]
        df: Dict[str, int] = defaultdict(int)
        for counts in self._counts:
            for token in counts:
                df[token] += 1

        total = len(self.chunks)
        self._idf = {
            token: math.log((1 + total) / (1 + frequency)) + 1
            for token, frequency in df.items()
        }
        self._vectors = [self._weighted_vector(c) for c in self._counts]

    @classmethod
    def from_directory(cls, directory: Path | str) -> "PolicySearchEngine":
        directory = Path(directory)
        chunks: List[PolicyChunk] = []
        for path in sorted(directory.glob("*.txt")):
            chunks.extend(_parse_policy_file(path))
        return cls(chunks)

    def _weighted_vector(self, counts: Counter) -> Dict[str, float]:
        return {
            token: frequency * self._idf.get(token, 1.0)
            for token, frequency in counts.items()
        }

    def search(self, query: str, top_k: int = 3) -> List[SearchResult]:
        query_tokens = tokenize(query)
        query_counts = Counter(query_tokens)
        query_vector = self._weighted_vector(query_counts)

        results = []
        for chunk, chunk_counts, chunk_vector in zip(
            self.chunks, self._counts, self._vectors
        ):
            score = _cosine_similarity(query_vector, chunk_vector)
            overlapping = tuple(sorted(set(query_tokens).intersection(chunk_counts)))

            if score > 0:
                results.append(
                    SearchResult(
                        chunk=chunk,
                        score=round(score, 4),
                        overlapping_terms=overlapping,
                    )
                )

        return sorted(results, key=lambda item: item.score, reverse=True)[:top_k]


def _cosine_similarity(left: Dict[str, float], right: Dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    shared = set(left).intersection(right)
    numerator = sum(left[token] * right[token] for token in shared)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return numerator / (left_norm * right_norm)


def _parse_policy_file(path: Path) -> List[PolicyChunk]:
    lines = path.read_text(encoding="utf-8").splitlines()
    metadata = {
        "document_id": path.stem.upper(),
        "title": path.stem.replace("_", " ").title(),
        "version": "1.0",
        "classification": "",
        "status": "",
    }

    for line in lines:
        for key, prefix in (
            ("document_id", "Document-ID:"),
            ("title", "Title:"),
            ("version", "Version:"),
            ("classification", "Classification:"),
            ("status", "Status:"),
        ):
            if line.startswith(prefix):
                metadata[key] = line.split(":", 1)[1].strip()

    chunks: List[PolicyChunk] = []
    current_section = "General"
    current_lines: List[str] = []

    def flush() -> None:
        nonlocal current_lines
        content = " ".join(line.strip() for line in current_lines if line.strip())
        if content:
            chunks.append(
                PolicyChunk(
                    document_id=metadata["document_id"],
                    title=metadata["title"],
                    version=metadata["version"],
                    classification=metadata["classification"],
                    status=metadata["status"],
                    section=current_section,
                    text=content,
                    source_file=path.name,
                )
            )
        current_lines = []

    metadata_prefixes = (
        "Document-ID:", "Title:", "Version:", "Classification:", "Status:"
    )

    for line in lines:
        if line.startswith("## "):
            flush()
            current_section = line[3:].strip()
        elif not line.startswith(metadata_prefixes):
            current_lines.append(line)
    flush()
    return chunks
