"""Application configuration and user-facing notices."""

APP_NAME = "ABC Horizon Media HR Policy Assistant"
APP_VERSION = "1.0.0-stage1"
SYSTEM_TYPE = "Offline deterministic policy retrieval prototype"

AI_DISCLOSURE = (
    "You are interacting with an automated HR policy assistant. "
    "It provides general information from approved synthetic policies and "
    "does not make employment decisions."
)

PRIVACY_NOTICE = (
    "Do not enter names, email addresses, phone numbers, employee IDs, "
    "salary information, medical information, performance information, "
    "complaints, or disciplinary information. Raw questions are not stored "
    "in the audit log."
)

HUMAN_ESCALATION = (
    "I could not find sufficient approved policy information to answer safely. "
    "Please contact Human Resources through the approved confidential channel."
)
