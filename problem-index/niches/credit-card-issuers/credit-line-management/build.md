# A Counterfactual Ledger for Every Line Action

**Niche:** [[niches/credit-card-issuers/credit-line-management/profile|Credit Line Management]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Issuers run line-increase tests every month and lose track of which accounts were held out, so the evidence they paid for evaporates within a year.
**Tags:** #causal-inference #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to prove, on randomised holdout cells, that each line increase or decrease earns more incremental revolving balance and interchange than it adds in loss, and whoever measures that counterfactual best takes the account.

## The Problem
Test cells live in the decision engine's configuration; the engine is upgraded, strategies are renamed, and the assignment history is lost or never joined to performance. Loss outcomes arrive 12–24 months later, after the analysts who designed the test have moved on.

## Why Nobody Has Built This
Decision engines execute strategies; data warehouses store performance; nothing is built to preserve the experiment.

## What to Build
A ledger that records every line action with its strategy, test cell and random assignment, joins it to monthly performance for 24 months, and reports incremental balance, revenue and loss per strategy with intervals — the evidence base for uplift models and for every future strategy review.

## Target Customer
Line management and portfolio risk leaders at issuers running champion-challenger tests.

## Impact If Built
Years of paid-for experiments kept and compounding, instead of re-run.
