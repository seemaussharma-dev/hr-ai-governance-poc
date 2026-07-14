# 16 — Requirements Traceability Matrix

| Requirement | Control | Code | Test | Evidence |
|---|---|---|---|---|
| FR-01 disclosure | C-01 | `app.py` | Manual | UI screenshot |
| FR-02 privacy notice | C-02 | `app.py` | Manual | UI screenshot |
| FR-04 personal-data detection | C-04 | `guardrails.py` | `test_guardrails.py` | Test report |
| FR-05 confidential HR block | C-05 | `guardrails.py` | `test_regulatory_controls.py` | Test report |
| FR-06 no employment decisions | C-06 | `guardrails.py` | `test_regulatory_controls.py` | Test report |
| FR-07 injection detection | C-07 | `guardrails.py` | `test_guardrails.py` | Test report |
| FR-08 approved sources | C-08 | `policy_search.py` | `test_policy_search.py` | Test report |
| FR-09 evidence threshold | C-10 | `response_builder.py` | `test_response_builder.py` | Test report |
| FR-10 extractive answer | C-09 | `response_builder.py` | `test_response_builder.py` | Test report |
| FR-11 source citation | C-09 | `app.py` | `test_response_builder.py` | Source metadata |
| FR-12 human escalation | C-15 | `response_builder.py` | `test_regulatory_controls.py` | Test report |
| FR-13 minimal audit | C-13 | `audit.py` | `test_audit.py` | Audit schema |
| GR-01 inventory | Governance | N/A | Review | Document 08 |
| GR-03 risk assessment | Governance | N/A | Review | Documents 09–12 |
| GR-06 test evidence | C-11 | `tests/` | CI | Test report |
