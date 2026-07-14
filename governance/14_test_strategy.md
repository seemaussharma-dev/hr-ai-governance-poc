# 14 — Test Strategy

## Objective

Prove that the system performs its limited function and that governance controls operate as designed.

## Test layers

| Layer | Purpose |
|---|---|
| Unit | Test each code function |
| Functional | Verify policy answers |
| Privacy | Verify identifier and confidential-data blocking |
| Employment decision | Verify no ranking or decision support |
| Security | Verify injection handling and approved-source validation |
| Groundedness | Verify answer comes from approved text |
| Traceability | Verify title, section, and version |
| Audit | Verify raw question and answer are not stored |
| Human oversight | Verify missing policy escalates |

## Release criteria

- All automated tests pass.
- 100% of defined employment-decision tests blocked.
- 100% of defined privacy tests blocked.
- 100% of answered tests include source metadata.
- No raw question or answer in the audit schema.
- No API keys or real personal data in repository.
- Known limitations documented.

## Test environment

Local Python environment with synthetic policies. No external network or model is required.

## Defect severity

- Critical: personal-data leakage, employment decision allowed, raw question logged.
- High: unsupported answer presented as fact, wrong source.
- Medium: weak retrieval, unclear message.
- Low: formatting or usability issue.

## Failed test process

1. Stop publication or release.
2. Record defect and affected control.
3. Identify root cause.
4. Correct code, policy, or documentation.
5. Add regression test.
6. Rerun complete suite.
7. Obtain approval.
