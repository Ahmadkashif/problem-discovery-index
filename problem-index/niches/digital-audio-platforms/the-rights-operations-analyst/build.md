# Deriving the Number They Are Asked About

**Niche:** [[niches/digital-audio-platforms/the-rights-operations-analyst/profile|The Rights Operations Analyst]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The person who explains royalty payments to rights holders cannot reconstruct those payments themselves.
**Tags:** #data-integration #workflow-orchestration #worker-facing #automation #evaluation-metrics #confidence-intervals #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to stop analysts matching recordings to owners and reconciling statements across a dozen intermediaries by hand — and whoever equips them ends a month spent explaining a payment they cannot derive.

## The Problem
The analyst receives statements in a dozen formats from platforms, distributors, societies and aggregators, each with its own periods, territories, deductions and identifiers. They match them against a rights database, reconcile the differences, and then answer questions about individual payments they cannot derive from first principles because the inputs are platform-wide aggregates they do not have. They are the accountable human face of a calculation nobody can check.

## Why Nobody Has Built This
The role absorbs the gap between systems, so its existence removes the pressure to connect them — a person who successfully reconciles incompatible sources is the reason nobody builds the integration. Statement formats are set by senders. The derivation is impossible without inputs the platforms do not publish. And the load is invisible until a month-end is missed.

## What to Build
Normalise the inputs and make the derivation available. Normalise every incoming statement format into one internal model, which is the core and removes the largest recurring cost in the role. Match recordings to rights automatically with confidence, routing only the uncertain, connecting to the matching work. Reconcile across sources automatically and surface only the breaks, since reconciliation is currently done in full rather than by exception. Retain lineage from statement line to payment, so a question about a number has an answer. Assemble the answer to a rights holder query before the analyst opens it, because the questions are recurring and the research is repeated. Report what cannot be derived and why, as an honest statement of the limit is better than an improvised explanation. Catalogue the recurring queries, since a handful dominate and each is automatable. Detect statement format changes rather than discovering them through wrong numbers. Track the analyst's workload by task, which nobody measures. And give the analyst a view of the platform-level inputs where disclosure allows, because their inability to see them is the root of the whole problem.

## Target Customer
Operations leadership and analysts, rights holders asking the questions, distributors and societies, and royalty operations vendors.

## Impact If Built
A person who successfully reconciles incompatible sources is the reason nobody builds the integration. Normalising statement formats and retaining lineage converts a month of reconciliation into a month of exceptions.
