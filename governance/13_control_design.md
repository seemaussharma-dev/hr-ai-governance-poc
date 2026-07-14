# 13 — Control Design

## Preventive controls

| Control | Description | Implementation |
|---|---|---|
| C-01 Disclosure | Tell users the system is automated and limited | `config.py`, `app.py` |
| C-02 Privacy notice | Tell users not to enter personal or sensitive data | `config.py`, `app.py` |
| C-03 Input validation | Reject empty and excessive input | `guardrails.py` |
| C-04 PII detection | Detect email, phone, SSN, employee ID | `guardrails.py` |
| C-05 Confidential category block | Block salary, medical, performance, complaint data | `guardrails.py` |
| C-06 Employment decision block | Block ranking, hiring, promotion, termination, prediction | `guardrails.py` |
| C-07 Injection detection | Detect common instruction-override attempts | `guardrails.py` |
| C-08 Approved source gate | Load only `Approved for POC` and `Internal Synthetic` | `policy_search.py` |
| C-09 Grounded response | Extract from top approved policy section | `response_builder.py` |
| C-10 Minimum evidence | Escalate when retrieval score is insufficient | `response_builder.py` |

## Detective controls

| Control | Description | Implementation |
|---|---|---|
| C-11 Automated tests | Verify expected allow/block/escalate behavior | `tests/` |
| C-12 CI test | Run tests on push and pull request | GitHub Actions |
| C-13 Minimal audit | Record decision, category, control, source | `audit.py` |
| C-14 Monitoring | Track answer, block, escalation, and failure rates | Monitoring plan |

## Corrective controls

| Control | Description | Evidence |
|---|---|---|
| C-15 Human escalation | Send unsupported or sensitive cases to HR | UI response |
| C-16 Incident response | Contain, investigate, delete, correct | Incident plan |
| C-17 Change management | Retest and approve material changes | Change plan |
| C-18 Corrective action | Root-cause and prevent recurrence | Incident record |

## Control limitations

Regex controls are transparent but incomplete. They cannot understand every indirect or multilingual request. Production needs layered controls, authentication, DLP, stronger classifiers, access control, red teaming, and human monitoring.
