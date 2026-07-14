# Practical Implementation Walkthrough

## Phase 1 — Define the problem

Start by documenting who has the problem, what happens today, and why the solution may help. Do not start with a model.

Output: `governance/00_business_problem.md`.

## Phase 2 — Limit the use case

Decide what the system may do and what it must never do. For HR, this boundary is essential because a general policy assistant is different from an employee evaluation or recruitment system.

Output: `governance/02_use_case_and_scope.md`.

## Phase 3 — Identify people and accountability

Assign business, technical, privacy, security, legal, and governance owners.

Output: RACI.

## Phase 4 — Write requirements

Turn risk and regulation into system behavior:

- show a notice;
- block identifiers;
- block confidential HR categories;
- prohibit employment decisions;
- retrieve only approved documents;
- cite sources;
- escalate missing answers;
- minimize logs.

Output: requirements catalog.

## Phase 5 — Understand the data

List every data item, where it enters, why it is needed, whether it is stored, and who receives it.

Stage 1 avoids an external processor and stores no raw question.

Output: data inventory and flow.

## Phase 6 — Assess impacts and risks

Ask:

- Who could be harmed?
- What could go wrong?
- How serious would it be?
- Which control reduces the risk?
- What risk remains?

Output: impact assessment, PIA, risk register.

## Phase 7 — Design architecture and controls

The control order matters:

1. notice;
2. validate;
3. privacy and prohibited-use guardrails;
4. approved retrieval;
5. evidence threshold;
6. answer with citation;
7. human escalation;
8. minimized audit.

Output: architecture and control design.

## Phase 8 — Build

The code is separated by responsibility so an interviewer can see where each control lives.

## Phase 9 — Test

A control is not complete just because it is written in a policy. Create a test that attempts to break or violate it.

Output: automated test suite and test report.

## Phase 10 — Create traceability

Map requirement → control → code → test → evidence.

Output: traceability matrix.

## Phase 11 — Prepare operations

Define monitoring, incidents, changes, retention, approvals, and retirement.

Output: operational governance documents.

## Phase 12 — Demonstrate

Show one allowed question, one privacy block, one employment-decision block, and one human escalation. Then show the passing tests and traceability matrix.

## Phase 13 — Add Claude later

Do not treat model integration as the start of governance. Insert Claude only after the Stage 1 controls are working, then assess the provider, data flow, model, prompt, output, cost, and monitoring changes.
