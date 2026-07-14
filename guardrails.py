"""Input controls for privacy, purpose limitation, and employment decisions."""

from dataclasses import dataclass, field
import re
from typing import List


@dataclass(frozen=True)
class GuardrailDecision:
    allowed: bool
    reason: str
    categories: List[str] = field(default_factory=list)
    controls: List[str] = field(default_factory=list)
    user_message: str = ""


BLOCK_MESSAGE = (
    "This assistant cannot process personal employee information, confidential "
    "HR records, prompt-injection requests, or employment-decision requests. "
    "Please contact Human Resources through the approved confidential channel."
)

_PATTERNS = {
    "email_address": re.compile(
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE
    ),
    "phone_number": re.compile(
        r"(?<!\d)(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}(?!\d)"
    ),
    "us_ssn": re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)"),
    "employee_id": re.compile(
        r"\b(?:employee|emp|staff)\s*(?:id|number|no\.?)\s*[:#-]?\s*[A-Z0-9-]{3,}\b",
        re.IGNORECASE,
    ),
    "prompt_injection": re.compile(
        r"\b(ignore|bypass|override|disregard|forget)\b.{0,55}"
        r"\b(instruction|rule|policy|guardrail|system prompt|previous)\b",
        re.IGNORECASE,
    ),
}

_SENSITIVE_TERMS = {
    "salary_or_payroll": (
        "salary", "payroll record", "pay rate", "compensation record",
        "bonus amount", "wage record", "how much does"
    ),
    "medical_or_disability": (
        "medical condition", "diagnosis", "disability status",
        "health record", "medical record", "sick note"
    ),
    "performance_or_discipline": (
        "performance review", "performance rating", "disciplinary",
        "written warning", "employee complaint", "investigation record"
    ),
    "individual_employee_record": (
        "my personal record", "my vacation balance", "my leave balance",
        "show my record", "employee file"
    ),
}

_DECISION_TERMS = (
    "rank employees",
    "rank candidates",
    "who should be promoted",
    "recommend promotion",
    "who should be hired",
    "recommend hiring",
    "who should be terminated",
    "recommend termination",
    "fire employee",
    "score employee",
    "predict resignation",
    "likely to resign",
)


def evaluate_question(question: str) -> GuardrailDecision:
    """Evaluate a question before retrieval without persisting it."""
    cleaned = " ".join((question or "").split())
    lowered = cleaned.lower()

    if not cleaned:
        return GuardrailDecision(
            allowed=False,
            reason="empty_question",
            categories=["validation"],
            controls=["input_validation"],
            user_message="Please enter an HR policy question.",
        )

    if len(cleaned) > 500:
        return GuardrailDecision(
            allowed=False,
            reason="question_too_long",
            categories=["validation"],
            controls=["data_minimization"],
            user_message=(
                "Please shorten the question to 500 characters or fewer and "
                "remove unnecessary personal details."
            ),
        )

    categories = []
    controls = []

    for category, pattern in _PATTERNS.items():
        if pattern.search(cleaned):
            categories.append(category)

    for category, terms in _SENSITIVE_TERMS.items():
        if any(term in lowered for term in terms):
            categories.append(category)

    if any(term in lowered for term in _DECISION_TERMS):
        categories.append("automated_employment_decision")

    if categories:
        if any(
            category in categories
            for category in ("email_address", "phone_number", "us_ssn", "employee_id")
        ):
            controls.append("personal_data_minimization")
        if "prompt_injection" in categories:
            controls.append("instruction_integrity")
        if any(
            category in categories
            for category in (
                "salary_or_payroll",
                "medical_or_disability",
                "performance_or_discipline",
                "individual_employee_record",
            )
        ):
            controls.append("confidential_hr_data_restriction")
        if "automated_employment_decision" in categories:
            controls.extend(["human_oversight", "prohibited_use_enforcement"])

        return GuardrailDecision(
            allowed=False,
            reason="prohibited_or_sensitive_request",
            categories=sorted(set(categories)),
            controls=sorted(set(controls)),
            user_message=BLOCK_MESSAGE,
        )

    return GuardrailDecision(
        allowed=True,
        reason="allowed_for_policy_retrieval",
        categories=["general_policy_question"],
        controls=["purpose_limitation", "approved_source_retrieval"],
        user_message="",
    )
