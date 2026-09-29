# Completeness Checking Instead of Content Checking

**Niche:** [[niches/contract-lifecycle-platforms/third-party-paper-review/profile|Third-Party Paper Review]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Requirements traceability, checklist completion and coverage analysis are standard in safety engineering and audit, where the question is always what is missing rather than what is wrong.
**Tags:** #graph-theory #large-language-models #bert #word-embeddings #evaluation-metrics #confidence-intervals #compliance #cross-validation
**Contested on:** Every serious competitor here is fighting to find the risk in a counterparty's contract, where the dangerous term is usually the one that is absent — and whoever detects absence takes the review, because checklist review structurally cannot.

## The Problem
Disciplines where omission is the principal failure mode — safety engineering, audit, regulatory submission, clinical protocol review — organise themselves around completeness: a requirements set, traceability from each requirement to where it is satisfied, and an explicit coverage report of what is unaddressed. Contract review, where omission is also the principal failure mode, is organised around inspecting what is present.

## What Already Exists
Requirements traceability tooling and methodology; coverage analysis; audit checklist frameworks with completeness semantics; language models that determine whether a document addresses a stated requirement, which is an entailment question they handle well; and retrieval to locate candidate satisfying text. The techniques are mature in their home disciplines.

## The Customization Gap
The adaptation is to legal requirements that are conditional and implicit. It requires: (1) a conditional requirements model, since what must be present depends on the transaction and a fixed checklist will produce mostly irrelevant findings, which destroys trust faster than missing something; (2) satisfaction judged semantically rather than by presence of a heading, because a limitation of liability can appear inside a general terms section with no title and a heading-based check will report a false absence; (3) partial satisfaction as a distinct outcome, since a clause that addresses a requirement inadequately is different from one that is absent and different again from one that is adequate — three states rather than two; (4) exposure-ranked output, because a complete coverage report on a contract has too many entries and the value is in the two that matter; and (5) requirements elicited from behaviour rather than authored, since asking lawyers to write the complete list produces an incomplete one and their redline history contains the real answer.

## Target Customer
Contract review and CLM vendors, legal operations functions, and the requirements management vendors for whom this is an adjacent domain.

## Impact If Solved
Disciplines built around omission have the right conceptual machinery and it has never been applied to the document type where omission is most expensive. Conditional requirements and semantic satisfaction are the two adaptations, and behaviour-based elicitation is what makes the requirements set obtainable.
