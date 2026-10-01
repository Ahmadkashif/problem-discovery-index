# A Mapping Layer Per Analyst Model

**Niche:** [[niches/sell-side-equity-research/model-maintenance/profile|Model Maintenance]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clean extracted data stops at the analyst's model, because each model has its own rows, splits and adjustments.
**Tags:** #transformers #large-language-models #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to get reported numbers into each analyst's own model layout — correct, sourced and with presentation changes flagged — within minutes of the release.

## The Problem
Standardised data does not match custom layouts; associates bridge the gap manually each quarter.

## Why Nobody Has Built This
Vendors sell standardised outputs to many clients; the per-model mapping is bespoke and was too costly to configure by hand.

## What to Build
A learned mapping from source line items to each model's rows, trained on that model's prior fills, proposing values with source links and confidence, and flagging every cell where the company's presentation changed.

## Target Customer
Research departments of all sizes; extraction vendors as a distribution channel.

## Impact If Built
Fill time drops to review time, and published estimates rest on sourced numbers.
