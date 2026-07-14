# 21 — System Card

## System

ABC Horizon Media HR Policy Assistant, Stage 1.

## Type

Offline deterministic retrieval and rule-based control prototype. No generative model.

## Purpose

General information from three synthetic policies.

## Not designed for

- individual employee records;
- employment decisions;
- profiling;
- legal advice;
- medical advice;
- real production use.

## Inputs

Short natural-language policy question, maximum 500 characters.

## Outputs

- blocked response;
- extractive policy answer with source metadata;
- human escalation.

## Knowledge

Three approved synthetic policy files.

## Evaluation

Automated tests cover retrieval, privacy, prohibited decisions, injection, groundedness, traceability, audit minimization, and escalation.

## Known limitations

- English-only patterns.
- Regex cannot identify all personal data.
- Small knowledge base.
- No authentication.
- No semantic model.
- No automated retention deletion.
- No accessibility assessment.
- No independent legal review.

## Responsible use

Use only with synthetic data for learning and portfolio demonstration.

## Future model documentation

Stage 2 must identify the Claude model, exact version, provider terms, data handling, retention, region, subprocessors, performance, limitations, evaluation set, and change process.
