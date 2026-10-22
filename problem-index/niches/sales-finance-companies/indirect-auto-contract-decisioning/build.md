# An Override Ledger That Grades Every Manual Decision

**Niche:** [[niches/sales-finance-companies/indirect-auto-contract-decisioning/profile|Indirect Auto Contract Decisioning]]
**Industry:** [[industries/sales-finance-companies|Sales Finance Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lenders report losses by scorecard band and vintage, never by the analyst decisions that moved a deal off the scorecard's answer, so nobody knows whether overrides make or lose money.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #tacit-knowledge-ml #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to give the dealer a workable decision before another lender does," but prime and non-prime paper are won differently — prime by deciding the most applications automatically at a stable loss rate, non-prime by structuring counteroffers the dealer can close and the borrower can pay — with different inputs, staff and winners. Decomposed into contested sub-niches below.

## The Problem
Every indirect lender lets analysts override the engine: approve a deal the score would decline, decline one it would approve, or change the structure. Credit policy caps override rates, and examiners ask about them. But the lender rarely measures whether its overrides are good. An override that performs is invisible; one that fails is a loss attributed to the vintage. Analysts with excellent reads and analysts with expensive habits look the same in the reports.

## Why Nobody Has Built This
Origination systems store the final decision and a reason code, not the engine's original answer beside the analyst's action and the deal as it changed. Outcomes sit in the servicing system months later. Declined deals have no outcome inside the lender at all.

## What to Build
A ledger joining the engine's recommendation, the analyst's action, the change in structure, the cue that motivated it and the outcome — early payment default, 12-month performance, fraud, buyback. Grade overrides by analyst, dealer and cue type with selection-aware statistics, and track declined applicants through bureau data where permitted to estimate what the declines avoided.

## Target Customer
Chief credit officers and credit policy heads at independent and captive indirect lenders with manual review queues.

## Impact If Built
The lender learns which human judgements earn their cost, can widen authority for analysts whose overrides perform, and has a defensible override record for examiners and warehouse banks.
