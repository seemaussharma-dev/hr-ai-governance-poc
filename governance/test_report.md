# Automated Test Report

## Project

HR AI Governance POC — Stage 1

## Execution date

15 July 2026

## Environment

- Python: 3.13.7
- Test framework: Python `unittest`
- External AI model/API: None
- Application type: Deterministic policy-retrieval prototype
- Data: Approved synthetic HR policies only
- Repository visibility during testing: Private

## Result

- Total tests: 21
- Passed: 21
- Failed: 0
- Errors: 0
- Overall status: PASS

## Command executed

```bash
python -m unittest discover -s ./tests -p "test_*.py" -v
```

## Control areas tested

- Input validation
- Question-length restriction
- Personal-data minimization
- Email-address detection
- Social Security number detection
- Salary and payroll restriction
- Medical and disability information restriction
- Performance, complaint, and disciplinary information restriction
- Automated employment-decision prohibition
- Prompt-injection detection
- Approved synthetic source validation
- Correct vacation-policy retrieval
- Correct remote-work-policy retrieval
- Correct expense-policy retrieval
- Extractive and grounded responses
- Source title, section, and version traceability
- Human escalation for unsupported questions
- Audit logging without storing raw questions or answers
- Parental-leave unsupported-question regression protection

## Defect identified during manual testing

During manual testing, the following unsupported question was submitted:

> What is the company’s parental leave policy?

The application initially returned an unrelated remote-work-policy response.

### Root cause

Generic terms such as `company`, `employee`, and `policy` were treated as meaningful retrieval evidence. This allowed an unrelated policy section to receive a positive matching score.

### Corrective action

The retrieval stop-word list was updated so generic HR terms do not influence policy matching.

### Retest result

The same parental-leave question now returns:

> I could not find sufficient approved policy information to answer safely. Please contact Human Resources through the approved confidential channel.

### Regression control

A permanent automated regression test was added:

```text
test_company_parental_leave_question_escalates
```

The test verifies that:

- The response status is `escalated`.
- The user is directed to Human Resources.
- No unsupported policy source is returned.

## Final automated test result

```text
Ran 21 tests in 0.025s

OK
```

## Governance interpretation

The test results demonstrate that the documented Stage 1 controls behave as expected for the defined test cases.

The test results do not represent:

- Legal advice
- Regulatory certification
- ISO/IEC 42001 certification
- Proof of complete GDPR, EU AI Act, or DPDP compliance
- Production security approval
- Protection against every possible malicious or unexpected input

## Release decision

Stage 1 is technically suitable for continued private testing and a synthetic portfolio demonstration.

The repository should remain private until:

- Documentation has been reviewed.
- No secrets or confidential information are present.
- Deployment security has been tested.
- The public-release checklist has been completed.