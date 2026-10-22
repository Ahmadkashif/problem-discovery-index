# Automated Analysis of Change Across Three Accounting Bases

**Niche:** [[niches/life-insurance-carriers/actuarial-valuation-reserving/profile|Actuarial Valuation, Reserving & Quarter Close]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Valuation teams explain reserve movements by re-running models one driver at a time and narrating the result by hand, three times over for three accounting bases.
**Tags:** #monte-carlo-methods #large-language-models #feature-engineering #evaluation-metrics #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to close each quarter's statutory, principle-based and LDTI reserves on the filing calendar with every movement attributed to a driver the auditor accepts, and whoever delivers an attributed close with the fewest overnight reruns takes the account.

## The Problem
Each quarter the reserve change must be split into new business, expected release, experience variance, assumption changes, market movements and model changes, on each basis, and the splits must reconcile. Projection engines run scenarios; they do not organise the attribution or explain it. Teams build step-through runs by hand, so any data or table error late in the close forces a new chain of overnight runs.

## Why Nobody Has Built This
Projection vendors sell the engine and leave the close process to each carrier's own scripts. Close-management vendors know the ledger, not the actuarial model. Each carrier's step order and memo format is different.

## What to Build
An orchestration layer above the engine. It validates inputs against the prior quarter before any run, schedules the attribution steps as a dependency graph so a late fix reruns only what it touches, reconciles statutory, LDTI and offshore movements to a common driver set, and drafts the analysis-of-change memo with each sentence linked to its numbers and to prior quarters' explanations.

## Target Customer
Heads of valuation at life and annuity writers with stochastic PBR or market-risk-benefit reporting.

## Impact If Built
Close compressed by several days (estimate), fewer reruns, and a memo auditors can trace, which frees the valuation actuary's time for assumption and model risk.
