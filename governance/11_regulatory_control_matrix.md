# 11 — Regulatory Control Matrix

This is an educational mapping, not a legal opinion or certification.

## EU AI Act

| Regulatory theme | Prototype implementation | Evidence |
|---|---|---|
| Risk-based classification | Informational scope documented; employment decisions prohibited | Scope, inventory, impact assessment |
| Transparency | User is told the system is automated | `config.py`, `app.py` |
| Human oversight | Unsupported, sensitive, and individual matters go to HR | `guardrails.py`, `response_builder.py` |
| Accuracy and traceability | Approved sources, evidence threshold, source/section/version | Retrieval and response tests |
| Record keeping | Minimal decision and control metadata | `audit.py` |
| Robustness and security | Prompt-injection test, approved-document validation | Security and regulatory tests |
| High-risk scope prevention | Hiring, ranking, promotion, performance, and termination requests blocked | Regulatory tests |
| AI literacy | Beginner guide, operating instructions, limitations | `START_HERE.md`, user guide |

**Classification warning:** Employment-related evaluation or decision use could fall into the AI Act's high-risk framework. Any such change requires a fresh legal classification and high-risk control program.

## GDPR

| Principle or obligation | Prototype implementation | Evidence |
|---|---|---|
| Transparency | Privacy notice and purpose statement | UI and PIA |
| Purpose limitation | General policy questions only | Scope and guardrails |
| Data minimization | PII blocking, no raw-question logging | Guardrail and audit tests |
| Accuracy | Approved versioned policies and citations | Retrieval tests |
| Storage limitation | Minimal log and target retention | Data inventory and monitoring plan |
| Integrity/confidentiality | Local processing, no external transfer, synthetic data | Architecture |
| Accountability | Owners, mappings, tests, risk register | Governance pack |
| Data protection by design/default | Controls run before retrieval | Code flow |
| Automated-decision protection | No significant automated employment decision | Prohibited-use tests |
| DPIA assessment | High-risk trigger documented | PIA |

## India DPDP Act and Rules

| Theme | Prototype implementation | Evidence |
|---|---|---|
| Notice and specified purpose | Clear notice and narrow use | UI and scope |
| Data minimization | No intended personal data; PII blocking | Guardrail tests |
| Reasonable security safeguards | No external API, minimal dependencies, CI tests | Architecture and CI |
| Data accuracy | Source metadata and approved status | Policy loader |
| Erasure/correction readiness | Procedure documented; no raw question retained | PIA and incident plan |
| Personal-data breach response | Incident procedure | Incident response |
| Grievance pathway | Refer user to HR/privacy contact in real deployment | User notice |
| Processor accountability | No processor in Stage 1; supplier assessment required for Claude | Stage 2 assessment |
| Retention | Minimal metadata and proposed 30-day retention | Data inventory |

## ISO/IEC 42001:2023 management-system themes

| Management-system theme | Prototype implementation | Evidence |
|---|---|---|
| Context and scope | Business problem and project charter | Documents 00–02 |
| Leadership and accountability | Owners and RACI | Document 03 |
| Planning | Requirements, impact assessment, risk register | Documents 04, 09, 12 |
| Support and competence | Beginner guide, demo, operating guide | START_HERE and demo script |
| Operational controls | Guardrails, retrieval, citations, escalation | Source code |
| Performance evaluation | Automated tests and monitoring metrics | Test report and monitoring plan |
| Improvement | Incident, change, corrective action, Stage 2 gates | Documents 17–19 and 26 |
| AI lifecycle and data controls | Inventory, data flow, approved sources, versioning | Documents 05, 08 |
