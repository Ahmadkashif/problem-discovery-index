# Operability Practice Borrowed From Software Teams

**Niche:** [[niches/no-code-app-builders/citizen-developer-support-load/profile|Citizen Developer Support Load]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering solved the operability problem with runbooks, error budgets, on-call rotation, structured logging and self-service recovery, and citizen developers have none of it and the same problem.
**Tags:** #large-language-models #bert #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor that takes this seriously is fighting to stop the person who built a useful app becoming its unpaid support desk — and whoever does that takes the builder's loyalty, which is what determines whether the platform spreads inside a company.

## The Problem
Keeping a running system operable without exhausting its author is a solved organisational problem in software: documentation as a deliverable, structured logging, alerting that routes to a rota rather than a person, runbooks for recurring failures, blameless review, and explicit ownership that can be transferred. A citizen developer supporting forty users has the same problem, none of the practice, and none of the vocabulary to ask for it.

## What Already Exists
Site reliability practice with a large published literature; incident management tooling; documentation generation from code and configuration; structured logging and error taxonomy conventions; on-call rotation products; and the whole discipline around ownership and handover. Language models generate readable documentation from structured definitions well. All of it is documented and much of it is free.

## The Customization Gap
The adaptation is to a person with no engineering background and no time. It requires: (1) generated rather than authored artefacts, since a builder will never write a runbook — documentation must be derived from the app and presented for light editing, which inverts the software practice where writing is the expected effort; (2) an error taxonomy in business language, because "a required field was empty" is actionable to a user and a stack trace is not, and the translation is the whole benefit; (3) recovery actions that are safe by construction and exposed to users, since the practice's assumption of a trained operator does not hold and the platform must guarantee that a user cannot make things worse; (4) ownership and handover as platform features rather than as organisational convention, because there is no engineering manager to enforce the convention; and (5) a load measurement that is honest without becoming surveillance of the builder, which means reporting the app's support burden rather than the individual's responsiveness.

## Target Customer
No-code platform vendors, internal developer platform teams supporting citizen builders, and IT functions who inherit these applications.

## Impact If Solved
An entire operability discipline exists and has never been offered to the fastest-growing population of application authors. Generated artefacts and business-language errors are the two adaptations that matter, and safe user-facing recovery is what removes the load rather than redistributing it.
