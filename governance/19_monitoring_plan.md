# 19 — Monitoring Plan

## Metrics

| Metric | Purpose |
|---|---|
| Total questions | Usage |
| Answered count and rate | Utility |
| Blocked count and rate | Privacy and misuse signal |
| Escalated count and rate | Knowledge gap |
| Block categories | Risk trend |
| Source-document frequency | Policy demand |
| Retrieval confidence distribution | Quality |
| Test pass rate | Control health |
| Incidents and near misses | Risk |
| Policy age and review date | Obsolescence |

## Privacy rule

Do not store raw questions or raw answers in normal monitoring.

## Review actions

- High blocked rate: improve notice and training.
- High escalation rate: review missing policies.
- Wrong-source report: stop release, investigate retrieval.
- Failed critical test: block deployment.
- Repeated injection attempts: improve security controls.
- Policy nearing expiry: ask owner for review.

## Review cadence

- POC: before every public release.
- Pilot: weekly.
- Production: risk-based, with monthly governance summary and quarterly management review.

## Retention

Target audit-metadata retention is 30 days for the POC design. Actual production retention must be justified and approved.
