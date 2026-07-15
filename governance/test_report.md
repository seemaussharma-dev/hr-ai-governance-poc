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