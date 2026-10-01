# Reconstructing Cash Flows From Cumulative Disclosures

**Niche:** [[niches/financial-data-vendors/private-fund-performance-data/profile|Private Fund Performance & LP Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Public pensions disclose cumulative contributions, distributions and NAV at irregular dates, and researchers back out the cash-flow series by hand.
**Tags:** #numerical-methods #bayesian-inference #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to hold accurate, cash-flow-level performance for the most private funds — and whoever has the cleanest cash flows sets the benchmarks LPs and consultants measure managers against.

## The Problem
Different LPs in the same fund report on different dates with different lags; their figures must be reconciled into one fund-level cash-flow series.

## Why Nobody Has Built This
It is treated as clerical work; the reconciliation across LPs is a latent-variable estimation problem nobody frames as one.

## What to Build
Estimate a fund's underlying cash-flow series jointly from multiple LPs' disclosures, with uncertainty, flag LP figures inconsistent with the joint estimate, and route them to researchers.

## Target Customer
Fund performance research leadership.

## Impact If Built
Cleaner cash flows mean more defensible IRRs and benchmarks.
