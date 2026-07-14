# 17 — Incident Response

## Incident examples

- Personal data appears in a log.
- A prohibited employment decision is answered.
- Confidential policy or real company data is committed.
- A source citation is incorrect.
- A guardrail can be bypassed.
- An API key is exposed in Stage 2.

## Response process

1. **Identify** — receive report or monitoring alert.
2. **Contain** — stop application or remove public access if necessary.
3. **Preserve minimal evidence** — retain technical facts without spreading personal data.
4. **Assess** — identify affected data, users, laws, and severity.
5. **Notify internal owners** — HR, privacy, security, legal, AI governance.
6. **Delete or secure exposed information** where appropriate.
7. **Correct** — fix code, policy, access, or configuration.
8. **Test** — add regression case and rerun full suite.
9. **Communicate** — provide required user or regulator notice after legal review.
10. **Close and improve** — record root cause, action owner, and due date.

## Severity

- Sev 1: real personal data exposure or employment decision harm.
- Sev 2: material control failure without confirmed harm.
- Sev 3: incorrect answer or limited bypass.
- Sev 4: documentation or usability issue.

## POC contact path

Use the repository issue template without posting personal data. For a real system, provide private HR, privacy, and security channels.

## Breach note

Whether an event is a legally reportable personal-data breach depends on the facts and applicable law. Legal and privacy professionals make that determination.
