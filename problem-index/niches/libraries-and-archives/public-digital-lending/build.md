# Licence Lifecycle Optimiser

**Niche:** [[niches/libraries-and-archives/public-digital-lending/profile|Public Library Digital Lending]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A library decides how many ebook copies to license, when to add more and whether to renew by holds-ratio rules of thumb, with no forecast of what each licence will return.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #time-series-forecasting #optimization-fundamentals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver the most patron loans per licence dollar under publishers' expiring and pay-per-use terms, and whoever proves cost per loan on the library's own data and helps the selector act on it takes the library's digital content budget.

## The Problem
For each popular title the selector chooses a number of licences, often by a rule such as one copy per four or six holds, buys more as the queue grows, and later decides whether to renew licences that expire after a term or a loan count. Each choice ties up money on a curve the selector cannot see: a breakout title's queue collapses within months, a steady backlist title circulates for years, and a licence bought late in the curve may expire barely used.

## Why Nobody Has Built This
The lending platforms profit from licence sales and offer purchase-suggestion lists rather than spend optimisation. Libraries lack the data science staff, and the pooled demand data that would make forecasts reliable sits with the platform.

## What to Build
A forecaster of each title's holds and loan curve from the library's own and comparable libraries' title-level history, metadata and pre-publication signals, coupled to an optimiser that recommends copies to license now, top-ups by week, licence model where a choice exists, and renew-or-let-lapse decisions at expiry — all under the month's budget, with the selector's overrides recorded and graded.

## Target Customer
Collection development managers at public library systems spending six or seven figures a year on digital content, and consortia managing shared collections.

## Impact If Built
More loans and shorter queues from the same licence budget; at a large system, recovering even 10% of licence spend from poorly timed copies and unneeded renewals is a six-figure sum (estimate).
