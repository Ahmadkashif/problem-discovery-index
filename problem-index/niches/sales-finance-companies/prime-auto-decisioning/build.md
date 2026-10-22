# Lost-Deal Inference for the Automated Boundary

**Niche:** [[niches/sales-finance-companies/prime-auto-decisioning/profile|Prime Auto-Decisioning]]
**Industry:** [[industries/sales-finance-companies|Sales Finance Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A lender widening its automated approvals only sees the performance of deals it booked; the deals it declined or lost to faster competitors are the evidence it needs and never has.
**Tags:** #causal-inference #gradient-boosting #logistic-regression #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to auto-decision the largest share of a dealer's prime and near-prime applications in seconds without loss drift, and whoever holds the highest straight-through rate at a stable loss rate takes the account.

## The Problem
Pushing automation outward means approving borrowers the engine used to send to review or decline. The lender's own data cannot say how those borrowers perform, because historically it rarely booked them. Every expansion is either timid or a gamble, and dealers notice which lenders answer the edge cases instantly.

## Why Nobody Has Built This
Reject inference is old statistics with a poor reputation, and the useful outside data — what happened to applicants the lender declined or lost — sits with the bureaus under permissible-purpose rules and with competitors who will not share.

## What to Build
A lost-deal panel: for applications the lender declined or approved but did not book, retrieve (under a permissible purpose and with legal review) whether an auto tradeline opened elsewhere and how it performed, and combine it with controlled expansion tests on randomised dealer traffic. Use the panel to estimate performance beyond the current boundary and to set the next one.

## Target Customer
Credit strategy heads at captives and prime independents competing on automated approval rates.

## Impact If Built
Boundary expansions sized on evidence rather than appetite, with each step's expected loss known before the dealer sees it.
