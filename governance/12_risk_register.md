# 12 — Risk Register

Scoring: Likelihood 1–5, Impact 1–5, Inherent score = L × I.

| ID | Risk | L | I | Inherent | Controls | Residual |
|---|---|---:|---:|---:|---|---|
| R-01 | Personal data entered in question | 3 | 4 | 12 | Notice, PII detection, no raw log | Medium |
| R-02 | Confidential HR information requested | 3 | 5 | 15 | No data source, category block, HR referral | Low |
| R-03 | Employment decision requested | 3 | 5 | 15 | Prohibited-use detection and human oversight | Low |
| R-04 | Unsupported answer presented as policy | 3 | 4 | 12 | Evidence threshold, extractive answer, citation | Medium |
| R-05 | Obsolete policy used | 2 | 4 | 8 | Approved status, version metadata, policy owner | Low |
| R-06 | Prompt injection | 3 | 3 | 9 | Basic detection, deterministic Stage 1 logic | Medium |
| R-07 | Logs contain personal data | 2 | 5 | 10 | No raw question/answer fields, audit test | Low |
| R-08 | User overrelies on answer | 3 | 4 | 12 | Disclosure, limitations, HR escalation | Medium |
| R-09 | Public repository contains secret or real data | 2 | 5 | 10 | `.gitignore`, publication checklist, synthetic data | Low |
| R-10 | Regulation mapping misread as certification | 3 | 4 | 12 | Repeated disclaimer and legal-review requirement | Medium |
| R-11 | Guardrails miss an indirect sensitive request | 3 | 4 | 12 | Human review, tests, future classifier | Medium |
| R-12 | Claude Stage 2 introduces external processing | 4 | 4 | 16 | Supplier, transfer, retention, security review gate | Not accepted yet |

## Risk acceptance

Only Stage 1 risks are accepted for a synthetic portfolio demonstration. R-12 is deferred and must be treated before Claude integration.

## Review triggers

- Failed critical test.
- New policy domain.
- Real user data.
- Claude or other model integration.
- Cloud or public deployment.
- Regulatory or legal change.
- Incident or complaint.
