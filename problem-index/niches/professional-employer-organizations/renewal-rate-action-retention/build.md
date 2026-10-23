# Renewal Rates Set Against the Quote the Client Can Actually Get

**Niche:** [[niches/professional-employer-organizations/renewal-rate-action-retention/profile|In-Force Renewal Rate Action]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** PEOs renew each client from its own claims and the plan's trend, without modelling what the client could buy elsewhere, so they overcharge the quiet groups that leave and undercharge the expensive ones that stay.
**Tags:** #bayesian-inference #survival-analysis #logistic-regression #monte-carlo-methods #causal-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each in-force client's health renewal from a year of claims too thin to be credible on its own, and whoever keeps the plan's loss ratio on target while losing the fewest low-claim clients to an ACA small-group or level-funded quote at renewal takes the account.

## The Problem
A low-claim client's renewal arrives with the plan's trend on top. Its broker shops it, an ACA small-group or level-funded quote comes in cheaper, and the client leaves, taking its favourable experience with it. A high-claim client gets a capped increase and stays. Each renewal cycle tilts the pool toward the expensive groups. This is the slow spiral every pooled plan fears.

## Why Nobody Has Built This
The outside price is invisible to the PEO except when an account manager writes it down. Departures are attributed to "price" in exit notes without the counterfactual. And actuaries and sales teams own different halves of the decision.

## What to Build
A renewal engine that estimates, for each client, its credible expected cost (partial pooling by size, industry and region), its likely outside alternatives (ACA community rates for its rating area and size, typical level-funded pricing for its demographics), and its retention probability at each candidate rate, learned from past renewals and departures. It then recommends rate actions that hit the plan's loss-ratio target with the least loss of low-cost membership, and shows the account manager why.

## Target Customer
Chief actuaries and retention leaders at PEOs whose plans renew thousands of clients a year.

## Impact If Built
A few points of retention among low-claim clients compound: the plan's mix improves every cycle instead of deteriorating, and fewer clients need to be replaced through new business, which the deck shows takes about 150 quotes a year for a 3,000-subscriber plan just to grow.
