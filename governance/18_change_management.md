# 18 — Change Management

## Changes requiring review

- New policy document or version.
- New topic or business process.
- Guardrail rule change.
- Retrieval-threshold change.
- Logging change.
- Claude or other model integration.
- Real employee data.
- Public or cloud deployment.
- Authentication or HR-system integration.
- New country or user group.

## Change process

1. Create change request.
2. Describe business reason and affected users.
3. Assess privacy, security, AI, legal, and operational impact.
4. Update risk register and control mapping.
5. Implement in a branch.
6. Add or update tests.
7. Run complete suite.
8. Obtain required approvals.
9. Merge and tag release.
10. Monitor after release.

## Versioning

- Application version: semantic versioning.
- Policy version: metadata in each document.
- Guardrail version: application release.
- Future model version: exact provider model identifier in system card.

## Emergency change

Emergency fixes may be expedited, but retrospective review, testing, documentation, and approval are still required.
