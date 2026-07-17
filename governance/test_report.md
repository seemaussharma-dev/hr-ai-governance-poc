# Automated Test Report

## Project

HR AI Governance POC — Stage 1

## Execution date

17 July 2026

## Environment

- Python: 3.13.7
- Test framework: Python `unittest`
- External AI model/API: None
- Application type: Deterministic policy-retrieval prototype
- Data: Approved synthetic HR policies only
- Repository visibility during testing: Public
- Deployment: Streamlit Community Cloud

## Approved policy sources tested

- Vacation and Leave Policy
- Remote Work Policy
- Expense Reimbursement Policy
- Equal Employment Opportunity and Non-Discrimination Policy

## Result

- Total tests: 28
- Passed: 28
- Failed: 0
- Errors: 0
- Overall status: PASS

## Command executed

```bash
python -m unittest discover -s tests -p "test_*.py" -v