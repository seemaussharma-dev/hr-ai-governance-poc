# 04 — Requirements

## Business requirements

| ID | Requirement |
|---|---|
| BR-01 | Answer general questions from approved leave, remote-work, and expense policies. |
| BR-02 | Show the source title, section, and version. |
| BR-03 | Refer unsupported or individual questions to HR. |
| BR-04 | Be understandable to nontechnical employees. |
| BR-05 | Be suitable for public portfolio demonstration using synthetic data. |

## Functional requirements

| ID | Requirement |
|---|---|
| FR-01 | Display automated-system disclosure. |
| FR-02 | Display privacy notice before submission. |
| FR-03 | Reject empty and oversized questions. |
| FR-04 | Detect common personal identifiers. |
| FR-05 | Detect confidential HR categories. |
| FR-06 | Detect prohibited employment-decision requests. |
| FR-07 | Detect basic prompt-injection attempts. |
| FR-08 | Search only approved synthetic policies. |
| FR-09 | Require minimum retrieval evidence. |
| FR-10 | Produce an extractive answer, not invented policy. |
| FR-11 | Cite source, section, and version. |
| FR-12 | Escalate unsupported questions to HR. |
| FR-13 | Write a minimal audit event without raw question or answer. |

## Privacy requirements

| ID | Requirement |
|---|---|
| PR-01 | Do not intentionally collect real personal data. |
| PR-02 | Process questions in memory only. |
| PR-03 | Do not retain raw questions. |
| PR-04 | Do not retain answer text. |
| PR-05 | Use fictional policies and organization details. |
| PR-06 | Document deletion, incident, and grievance processes. |
| PR-07 | Reassess privacy before Stage 2. |

## Security requirements

| ID | Requirement |
|---|---|
| SR-01 | No secrets or API keys in the repository. |
| SR-02 | Basic prompt-injection detection. |
| SR-03 | Approved-document validation during loading. |
| SR-04 | Automated tests on every GitHub change. |
| SR-05 | Dependency kept minimal. |
| SR-06 | Public repository publication checklist. |

## Governance requirements

| ID | Requirement |
|---|---|
| GR-01 | Maintain an AI/system inventory record. |
| GR-02 | Document intended and prohibited uses. |
| GR-03 | Maintain risk and impact assessments. |
| GR-04 | Map controls to regulatory principles. |
| GR-05 | Assign accountable owners. |
| GR-06 | Maintain test evidence and traceability. |
| GR-07 | Define change, incident, monitoring, and review processes. |

## Nonfunctional targets

| ID | Target |
|---|---|
| NFR-01 | 100% of defined prohibited decision tests blocked. |
| NFR-02 | 100% of defined personal-data tests blocked. |
| NFR-03 | 100% of answered test questions include traceable source metadata. |
| NFR-04 | 0 raw questions stored in audit records. |
| NFR-05 | All automated tests pass before publication. |
