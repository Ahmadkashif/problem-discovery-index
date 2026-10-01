# A Standard Trial Harness With a Written Verdict

**Niche:** [[niches/hedge-funds/alt-data-evaluation/profile|Alternative Data Evaluation & Onboarding]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every dataset trial is a bespoke project, so a fund evaluates a small fraction of what it is offered and decides on the rest by reputation.
**Tags:** #linear-regression #regularization #time-series-forecasting #hypothesis-testing #evaluation-metrics #feature-engineering #data-integration
**Contested on:** Every serious competitor in this niche is fighting to prove or disprove, inside the trial window and on the fund's own universe, whether a dataset carries information not already in consensus — and whoever produces a defensible verdict before the trial expires decides which data gets bought.

## The Problem
A data team gets trial access, spends most of the window on mapping and cleaning, runs a rushed test, and presents an opinion. The next trial starts from scratch. Results are not comparable across datasets, so the fund cannot tell whether its portfolio of data subscriptions is earning its cost.

## Why Nobody Has Built This
Each fund regards its evaluation method as proprietary, and vendors have no incentive to build tools that make it easier to reject their data.

## What to Build
A trial harness: ingest, propose entity mappings for review, reconstruct vintages where possible and flag where not, run standard tests (KPI surprise prediction against consensus, coverage of the fund's universe, panel stability, incremental information over existing subscriptions), and generate a verdict memo with the evidence. Store every verdict so subscriptions can be re-evaluated at renewal.

## Target Customer
Heads of data strategy at multi-manager platforms and data-intensive fundamental and quant funds.

## Impact If Built
Several times more datasets evaluated per year, comparable verdicts, and renewals decided on evidence.
