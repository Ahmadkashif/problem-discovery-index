# Covenant Capacity Calls Never Graded Against What Happened

**Niche:** [[niches/investment-banking-boutiques/distressed-credit-intelligence/profile|Distressed & Restructuring Credit Intelligence]]
**Industry:** [[industries/investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vendors publish thousands of judgments about what stressed borrowers can do under their documents and what they will do next, and the archive of what each one actually did is never used to score those calls.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #large-language-models #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious vendor in this pocket is fighting to tell readers first and correctly what a stressed company can do under its documents and what will happen next — and whoever can prove its calls were right keeps the restructuring desks' subscriptions.

## The Problem
An analyst reads a credit agreement and writes that the borrower has capacity to drop assets into an unrestricted subsidiary, or that a priming transaction is likely, or that a filing is imminent. A senior legal analyst's sense of which sponsors use aggressive liability management and which documents will be exploited is tacit and valuable. Every call resolves: the transaction happened, or the company filed, or neither.

## Why Nobody Has Built This
The calls are prose embedded in articles; the outcomes are in later articles and dockets. Grading invites an unflattering record, and journalism culture does not track forecasts.

## What to Build
Extract every forward-looking call from the archive with date and confidence language; link each to subsequent events; report calibration by analyst, document type and sponsor; and train a model on document terms and sponsor history that assigns probabilities to liability-management and filing outcomes, as an analyst aid rather than a published score.

## Target Customer
Heads of research at distressed and leveraged-credit intelligence vendors.

## Impact If Built
A measured forecast record is a differentiator in a crowded subscription market, and the model turns tacit analyst knowledge into a coverage multiplier.
