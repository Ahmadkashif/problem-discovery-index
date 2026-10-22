# A Running Forecast of Year-End Indirect Rates

**Niche:** [[niches/contract-research-labs/cost-accounting-indirect-rates/profile|Government Cost Accounting & Indirect Rates]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Small research firms learn their real overhead and G&A rates after the year closes, by which time they have under-billed every cost-type contract for twelve months.
**Tags:** #time-series-forecasting #bayesian-inference #exponential-smoothing #monte-carlo-methods #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a research firm's books through a DCAA accounting-system review and its incurred-cost submission accepted on time, and whoever makes a small firm audit-ready without a full-time government accountant takes the account.

## The Problem
Indirect rates are ratios of pools to bases, and in a small research firm both move sharply with a single award or loss: a new Phase II adds direct labour and lowers overhead; a proposal-heavy quarter loads the G&A pool. Provisional billing rates set at the start of the year drift, and the firm finds out at year end, when the incurred-cost submission is due in six months and the true-up is a cash problem.

## Why Nobody Has Built This
Government-contract ERPs compute actual rates for closed periods; forecasting is left to a controller's spreadsheet, which small firms do not have. The variance that matters depends on the pipeline — which proposals will win — which the accounting system does not know.

## What to Build
A forecast that combines year-to-date pools and bases from the ledger with the firm's pipeline (pending proposals with win probabilities, staffing plans, proposal calendar) and simulates year-end rates as a distribution. It alerts when the provisional billing rates fall outside the likely range, and drafts the request to the contracting officer to adjust them.

## Target Customer
Founders and part-time controllers at SBIR firms with their first several cost-type contracts.

## Impact If Built
Rate surprises shrink from a year-end shock to a mid-year adjustment, avoiding under-billing that can equal several percent of a small firm's annual revenue (estimate), and the firm's submission rests on numbers it has been watching all year.
