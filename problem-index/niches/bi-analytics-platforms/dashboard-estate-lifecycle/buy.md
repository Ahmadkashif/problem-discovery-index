# Deprecation Practice From Software Engineering

**Niche:** [[niches/bi-analytics-platforms/dashboard-estate-lifecycle/profile|Dashboard Estate Lifecycle]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering has a well-developed practice for retiring things safely — deprecation notices, usage telemetry, sunset windows, dead code detection — and analytics estates have a clean-up campaign once a year.
**Tags:** #survival-analysis #graph-theory #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor in analytics governance is fighting to make retiring an asset safe enough that an organisation will actually do it — and whoever does that takes the governance account, because every estate grows monotonically and every governance programme has failed to stop it.

## The Problem
Removing a public API, a feature flag or an unused module without breaking consumers is routine software practice with an established playbook: instrument usage, announce deprecation, provide a migration path, wait a defined period, remove, keep a rollback. Dead code detection and dependency analysis are standard tooling. Analytics estates face the identical problem — retire an artefact without breaking an unknown consumer — and have imported none of the practice.

## What Already Exists
Deprecation workflows with sunset windows are standard in every mature engineering organisation. Feature flag lifecycle management products exist. Dead code and unused dependency detection is built into common toolchains. Usage telemetry and its interpretation for removal decisions is well understood. Survival analysis handles the question of how long an asset must be unused before it is safely dead. Every component of the practice is documented and free.

## The Customization Gap
The adaptation is to analytical artefacts with human rather than programmatic consumers. It requires: (1) a consumer model that is people rather than code, which changes everything about notice — a human consumer can be told and can object, which is an advantage software deprecation does not have and the design should exploit it rather than mimicking automated sunsets; (2) periodicity-aware dead detection, since annual and quarterly usage is common and normal here and would be pathological in code, meaning a naive unused-for-ninety-days rule retires the audit extract; (3) dependency analysis that reaches outside the platform to spreadsheets, scheduled deliveries and embedded uses, because the consumers are not all in one system; (4) reversibility as a product capability rather than a backup procedure, since restoring within a click is what makes the notice period acceptable to owners; and (5) an explicit policy the organisation sets once — how long unused, what notice, what audience — because a per-asset judgement is what makes the campaign model collapse.

## Target Customer
BI platform vendors, data catalogue and governance vendors, and internal platform teams who already practise deprecation on their code and have never applied it to their analytics.

## Impact If Solved
A mature engineering practice transfers almost directly and has not been, which is why analytics governance is run as periodic campaigns that fail. Periodicity awareness and human-consumer notice are the two adaptations, and both make the analytics version easier than the software one rather than harder.
