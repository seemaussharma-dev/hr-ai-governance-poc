# Start Here — HR AI Governance POC

This repository is designed for a beginner who wants to demonstrate **practical AI governance**, not only discuss regulations.

You will show the project in this order:

1. **Business problem** — why the company needs the solution.
2. **Use case and boundaries** — what the assistant may and may not do.
3. **Requirements** — business, privacy, security, and governance requirements.
4. **Architecture and data flow** — how the solution works.
5. **Controls** — where regulatory requirements are implemented in code and process.
6. **Testing and evidence** — how you prove the controls work.
7. **Business outcome and next phase** — what the MVP demonstrates and how Claude can be added later.

## What Stage 1 is

Stage 1 is a public-safe, offline HR policy assistant for a fictional company called **ABC Horizon Media**.

It uses:

- synthetic HR policies;
- a local policy search engine;
- rule-based privacy and employment-decision guardrails;
- extractive responses with citations;
- human escalation;
- privacy-minimized logging;
- automated tests;
- governance documentation.

It does **not** call Claude yet. This is intentional. The free Claude desktop application cannot be called automatically from Python without a separately billed API account. Stage 1 proves that you understand the governance foundation before adding a generative model.

## Suggested learning sequence

Read these files in order:

1. `governance/00_business_problem.md`
2. `governance/01_project_charter.md`
3. `governance/02_use_case_and_scope.md`
4. `governance/03_stakeholders_and_raci.md`
5. `governance/04_requirements.md`
6. `governance/05_data_inventory_and_flow.md`
7. `governance/06_solution_architecture.md`
8. `governance/07_ai_governance_plan.md`
9. `governance/08_ai_system_inventory.md`
10. `governance/09_ai_impact_assessment.md`
11. `governance/10_privacy_impact_assessment.md`
12. `governance/11_regulatory_control_matrix.md`
13. `governance/12_risk_register.md`
14. `governance/13_control_design.md`
15. `governance/14_test_strategy.md`
16. `governance/15_regulatory_test_cases.md`
17. `governance/16_requirements_traceability.md`
18. `governance/17_incident_response.md`
19. `governance/18_change_management.md`
20. `governance/19_monitoring_plan.md`
21. `governance/20_user_notice.md`
22. `governance/21_system_card.md`
23. `governance/22_supplier_assessment_stage2.md`
24. `governance/23_deployment_and_operations.md`
25. `governance/24_demo_script.md`
26. `governance/25_interview_story.md`
27. `governance/26_stage2_claude_roadmap.md`
28. `governance/27_project_closeout.md`

## Run the project

Open a terminal in this folder.

### Run the automated tests

```powershell
python -m unittest discover -s tests -v
```

### Run the console demonstration

```powershell
python demo.py
```

### Run the web application

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

## The main interview message

> I started with the business problem and designed governance into the system before connecting a large language model. I limited the MVP to general policy information, used only synthetic data, blocked personal and confidential HR requests, prohibited automated employment decisions, required approved sources and citations, escalated unsupported questions to a human, minimized audit logs, and created automated tests and governance evidence. The controls are mapped to the EU AI Act, GDPR, India's DPDP framework, and ISO/IEC 42001. Claude can be added in Stage 2 without rebuilding the governance foundation.
