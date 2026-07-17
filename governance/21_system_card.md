# 21 — System Card

## System

ssp-dev-hr-aigovern-poc HR Policy Assistant, Stage 1.

## Type

Offline deterministic retrieval and rule-based control prototype. No generative AI model or external AI API is used.

## Purpose

Provide general information from four approved synthetic policies:

- Vacation and Leave Policy
- Remote Work Policy
- Expense Reimbursement Policy
- Equal Employment Opportunity and Non-Discrimination Policy

## Intended users

Employees and managers seeking general policy information for educational and demonstration purposes.

## Approved capabilities

The system may:

- answer general questions from approved synthetic policy sources;
- provide extractive policy answers;
- display the source title, section, and version;
- block confidential or prohibited requests;
- escalate unsupported or case-specific questions to Human Resources.

## Not designed for

The system must not:

- access individual employee or applicant records;
- process real personal or confidential HR data;
- disclose salary, payroll, medical, disability, performance, complaint, investigation, or disciplinary information;
- rank, score, select, reject, promote, discipline, or terminate applicants or employees;
- use protected characteristics to support an employment decision;
- determine whether unlawful discrimination occurred;
- provide legal or medical advice;
- profile or predict employee behavior;
- approve leave, expenses, remote work, or employment actions;
- operate as a production HR system.

## Inputs

A short natural-language HR policy question with a maximum length of 500 characters.

## Outputs

The system produces one of three outcomes:

1. An extractive policy answer with source metadata
2. A blocked response for prohibited or sensitive requests
3. A Human Resources escalation when approved evidence is unavailable or human judgment is required

## Knowledge sources

Four policy files are approved for retrieval.

Each policy must contain:

- a unique document ID;
- a policy title;
- a version;
- `Classification: Internal Synthetic`;
- `Status: Approved for POC`;
- clearly labeled policy sections.

Draft, unapproved, real, or incorrectly classified policy files must not be used as approved knowledge sources.

## EEO safeguards

The EEO policy may be used only for general informational questions.

The system blocks employment-decision requests that combine an employment action with a protected characteristic.

Examples include:

- rejecting an applicant because of age;
- ranking candidates by age;
- making a decision based on pregnancy;
- using disability or another protected characteristic for an employment action.

These requests apply:

- `fairness_and_non_discrimination`;
- `human_oversight`;
- `prohibited_use_enforcement`.

Case-specific questions such as whether unlawful discrimination occurred are escalated before policy retrieval.

These requests apply:

- `human_escalation`;
- `human_oversight`;
- `legal_determination_restriction`.

## Evaluation

Twenty-eight automated tests currently cover:

- input validation;
- question-length restriction;
- personal-data detection;
- confidential HR-data restrictions;
- automated employment-decision prohibition;
- protected-characteristic employment-decision prohibition;
- fairness and non-discrimination;
- human oversight;
- prompt-injection detection;
- approved synthetic source validation;
- policy retrieval;
- grounded extractive responses;
- source traceability;
- unsupported-question escalation;
- case-specific discrimination escalation;
- privacy-minimized audit logging;
- regression protection.

Manual Streamlit testing also validated:

- an approved EEO policy answer;
- blocking of a discriminatory employment-decision request;
- blocking of a confidential complaint request;
- escalation of a case-specific discrimination question.

## Audit approach

The audit event records control outcomes and necessary metadata.

The system is designed not to store:

- the complete raw question;
- the answer text;
- intentionally collected personal information.

## Known limitations

- English-only keyword and regular-expression controls
- Keyword matching may not detect every wording variation
- Regular expressions cannot identify every form of personal information
- Small synthetic policy knowledge base
- No authentication or role-based access
- No semantic retrieval model
- No generative AI model
- No automated retention-deletion process
- No accessibility assessment
- No independent legal or employment-law review
- No production security assessment
- No guarantee against every unexpected or malicious input

## Responsible use

Use only with synthetic information for education, testing, governance demonstration, and portfolio purposes.

The application is not legal advice, regulatory certification, or a production HR system.

## Change-control requirement

A new governance review is required before adding:

- real employee or applicant information;
- real company policies;
- user authentication;
- HR-system integration;
- personalized responses;
- workflow actions;
- candidate or employee evaluation;
- new countries or legal jurisdictions;
- Claude or another external AI model.

## Future model documentation

Stage 2 must document:

- the exact Claude model and version;
- provider and supplier assessment;
- data handling and retention;
- hosting region and subprocessors;
- prompt and context controls;
- output validation;
- model limitations;
- evaluation results;
- monitoring and cost controls;
- incident response;
- model-change management;
- rollback to deterministic Stage 1 operation.