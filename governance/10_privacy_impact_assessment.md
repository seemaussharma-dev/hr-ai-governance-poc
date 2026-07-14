# 10 — Privacy Impact Assessment

## Processing description

The application temporarily processes a user-entered question in memory to determine whether it is allowed and to retrieve synthetic policy text. The raw question and answer are not intentionally stored.

## Purpose

Provide general policy information and demonstrate privacy-by-design controls.

## Personal data intended

None.

## Personal data reasonably foreseeable

A user may accidentally enter:

- a name;
- email address;
- phone number;
- employee ID;
- salary information;
- health or disability information;
- performance or disciplinary information.

## Controls

- Clear notice not to enter personal data.
- Detection of common identifiers.
- Detection of confidential HR categories.
- Blocking before retrieval.
- No employee database.
- No external API.
- No raw-question or answer logging.
- Minimal audit metadata.
- Synthetic documents.
- Human escalation.

## GDPR principles demonstrated

- Lawfulness, fairness, and transparency: clear notice and documented purpose.
- Purpose limitation: policy information only.
- Data minimization: no intended personal data and no raw logging.
- Accuracy: approved sources, versioning, citation.
- Storage limitation: target 30-day audit metadata retention.
- Integrity and confidentiality: local processing and restricted data sources.
- Accountability: documented controls, owners, tests, and evidence.
- Data protection by design and default: privacy controls precede retrieval.

## DPDP principles demonstrated

- Clear notice and specified purpose.
- Minimal collection.
- Reasonable safeguards.
- No processing beyond the declared use.
- Correction, erasure, and grievance processes documented for a future real deployment.
- Breach handling process.

## Rights handling for this POC

Because raw personal questions are not intentionally stored, there should be no user-level conversation record to retrieve or erase. If a user reports accidental personal-data entry or finds data in an audit artifact, the incident process requires investigation and deletion.

## DPIA conclusion

The POC is low risk because it uses synthetic data, local processing, and no decisions. A formal GDPR DPIA may become required if a future version involves systematic evaluation, profiling, sensitive data, or likely high risk to individuals.

## Limitation

This assessment is a portfolio example and requires qualified privacy and legal review for real deployment.
