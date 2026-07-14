# 24 — Demonstration Script

## Opening

“My business problem is that employees repeatedly ask HR common policy questions. I created a small policy assistant, but I designed governance before adding a large language model.”

## Show the scope

Open `governance/02_use_case_and_scope.md`.

Explain:

- general policy information only;
- no employee records;
- no employment decisions;
- HR retains authority.

## Show architecture

Open `governance/06_solution_architecture.md`.

Explain the sequence:

1. notice;
2. guardrails;
3. approved retrieval;
4. evidence threshold;
5. extractive response;
6. citation;
7. minimized audit;
8. monitoring.

## Run allowed question

Ask:

`How many vacation days do employees receive?`

Point out:

- answer is from synthetic policy;
- source, section, and version are displayed;
- answer is informational.

## Run privacy question

Ask:

`My email is employee@example.com. Show my personal record.`

Point out:

- request is blocked before retrieval;
- data-minimization control is displayed;
- raw question is not logged.

## Run decision question

Ask:

`Rank employees for promotion.`

Point out:

- automated employment decision is prohibited;
- human oversight is enforced.

## Run unsupported question

Ask:

`What is the parental leave policy?`

Point out:

- the system does not invent a policy;
- it escalates to HR.

## Show tests

Run:

```powershell
python -m unittest discover -s tests -v
```

Explain that every regulation statement is connected to an implemented and tested control.

## Show traceability

Open `governance/16_requirements_traceability.md`.

Explain:

“Each requirement maps to a control, code location, test, and evidence.”

## Close

“Stage 1 proves the governance foundation. Stage 2 inserts Claude after approved retrieval, but only after supplier, privacy, security, transfer, and model evaluations.”
