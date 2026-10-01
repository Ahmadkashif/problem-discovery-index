# The Auction Nobody Grades

**Niche:** [[niches/investment-banking-boutiques/sell-side-ma-advisory/profile|Sell-Side M&A Advisory]]
**Industry:** [[industries/investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every sale process is a designed auction with an observable result, and no boutique measures which of its design choices — buyer count, timetable, round structure — moved the price.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Not terminal as stated — every competitor is fighting to deliver the highest certain price, but a sponsor selling its fifth portfolio company and a founder selling the only company they will ever own buy that outcome on different evidence, from different banks, and the two contests are stated in the sub-niches below.

## The Problem
A banker designing a sale chooses how many buyers to approach, whether to run a broad or targeted process, whether to pre-empt or hold a second round, how long to leave between indications and final bids, and whether to offer stapled financing. Each choice is argued from experience. Each process then produces a result — the number of bids, the spread between first-round indications and final bids, the winning price relative to the banker's own valuation range, and the time to signing — that is recorded and never compared across deals.

## Why Nobody Has Built This
The sample per firm is small and every deal is different, which makes bankers sceptical that anything generalises. The outcomes are recorded in per-deal files with no common schema. And measuring process design invites the uncomfortable finding that some of a firm's habits do not help.

## What to Build
A process outcome ledger across all of the firm's mandates — design choices, buyer funnel counts, indication ranges, final bids, signing price and time — and a causal analysis layer that estimates, with honest intervals, how outcomes vary with design choices after controlling for sector, size, and market conditions. Report it as guidance with uncertainty, not as rules, and update it after every closed deal.

## Target Customer
Heads of M&A and process-management leadership at mid-market boutiques running thirty or more sell-side processes a year.

## Impact If Built
Process design is the part of the outcome the bank controls. Even a coarse, honest estimate of what moves price changes how the next process is run and gives the firm a pitch argument grounded in its own record rather than in league tables.
