# 09 — AI/System Impact Assessment

## Intended benefit

- Faster access to common policies.
- More consistent responses.
- Reduced repetitive HR workload.
- Better policy traceability.
- Practical governance evidence.

## Affected stakeholders

Employees, managers, HR, privacy, security, legal, and internal audit.

## Potential harms

| Impact area | Potential harm | Stage 1 treatment |
|---|---|---|
| Accuracy | Incorrect or unsupported policy answer | Extractive answer, evidence threshold, citation |
| Employment rights | System influences employment decision | Decision requests blocked; no authority |
| Privacy | User enters personal data | Notice, PII detection, no raw logging |
| Confidentiality | Sensitive HR record disclosed | No HR data source; category blocking |
| Transparency | User believes system is human or authoritative | Automated-system disclosure and limitations |
| Fairness | System treats employees differently | No profiling or personalized decisions |
| Security | Prompt injection changes behavior | Basic injection detection; deterministic logic |
| Accountability | No owner or escalation | Named owners and HR escalation |
| Obsolescence | Old policy used | Version metadata and approval status |
| Overreliance | Employee treats response as final | Human escalation and informational statement |

## Severity and likelihood

Residual risk is considered acceptable for a synthetic, offline portfolio demonstration because no real employee data or employment decisions are processed. It is not acceptable for production without authentication, stronger security, operational controls, legal review, and updated testing.

## Human oversight design

HR handles:

- personal circumstances;
- exceptions;
- disputes;
- legal interpretation;
- medical or accommodation matters;
- employment decisions;
- missing or unclear policy.

## Decision

Proceed with Stage 1 under the documented scope. Reassessment is mandatory for Stage 2.
