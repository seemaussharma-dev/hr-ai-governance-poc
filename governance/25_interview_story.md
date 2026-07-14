# 25 — Interview Story

## Problem

A small company wanted to reduce repetitive HR policy questions, but an uncontrolled chatbot could expose employee data, invent policy, or influence employment decisions.

## What I designed

I limited the MVP to three general policy areas and used synthetic data. I created the business case, scope, requirements, architecture, data flow, ownership model, impact assessment, privacy assessment, risk register, regulatory mapping, test strategy, incident plan, monitoring plan, and change process.

## How I implemented it

I built a Python and Streamlit prototype. Guardrails run before retrieval and block personal identifiers, sensitive HR categories, prompt injection, and employment-decision requests. The retrieval engine loads only synthetic documents marked approved. The answer builder uses an evidence threshold and extracts text from the approved policy, with source, section, and version. Unsupported questions go to HR. Audit events store only control metadata, not the raw question or answer.

## How I tested it

I created automated tests for:

- personal data;
- salary and medical data;
- performance and complaints;
- hiring, ranking, promotion, termination, and resignation prediction;
- prompt injection;
- approved-source retrieval;
- groundedness;
- source traceability;
- human escalation;
- minimized logging.

## Governance alignment

I mapped the implemented controls to EU AI Act themes, GDPR principles, India's DPDP obligations, and ISO/IEC 42001 management-system practices.

## Outcome

The Stage 1 POC demonstrates an end-to-end governed implementation that is safe to share publicly. It does not claim production readiness or certification. The next phase adds Claude only after supplier and privacy approval.
