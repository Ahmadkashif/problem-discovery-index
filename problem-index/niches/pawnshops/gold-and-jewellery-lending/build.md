# A Live Loan-to-Melt Ledger for the Jewellery Book

**Niche:** [[niches/pawnshops/gold-and-jewellery-lending/profile|Gold & Jewellery Lending]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A pawnshop's jewellery loans are secured by metal whose price moves every minute, and no system shows the owner which tickets are now worth less than the money lent against them or what premium over melt each kind of piece really fetches.
**Tags:** #gradient-boosting #time-series-forecasting #bayesian-inference #feature-engineering #evaluation-metrics #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to value gold and jewellery collateral against the live spot price — karat, net weight, premium over melt and the risk of a plated or tungsten-filled fake — inside the few minutes a customer will wait, and whoever values it most accurately takes the account.

## The Problem
A store may carry hundreds or thousands of open jewellery tickets. Each was written against the clerk's view of karat, weight and resale premium on the day, with spot at whatever it was. When gold falls ~20% in a few months, as it did between January and October 2026, some of those tickets are now under water — the loan plus fees exceeds what the piece would bring at melt — and those are exactly the tickets customers abandon. Nobody sees this until the forfeits arrive.

## Why Nobody Has Built This
Pawn POS systems store the karat and weight as text fields for the police form, not as a valuation. Chains model exposure at portfolio level, if at all. And the premium over melt — the part of the value that is judgement — has never been recorded separately from the loan amount, so there is nothing to mark.

## What to Build
A ledger that records every gold-backed ticket with net metal weight, karat confidence and the clerk's estimated retail premium; marks the book to live spot daily; flags tickets whose loan-to-melt ratio crosses a threshold; and learns, from the store's own forfeits, the realised premium over melt by style, brand and stone, so that the clerk's premium estimate at intake is checked against history. Feed lending guidance back to the counter: tighter on unstamped pieces, looser where the store's premium history is strong.

## Target Customer
Directors of jewellery operations and lending at chains with hundreds of stores; regional groups with a central jewellery buyer.

## Impact If Built
Exposure to a spot fall becomes visible before the forfeits land, lending tightens on the right tickets rather than all of them, and the store learns what its jewellery is really worth above melt — the single largest judgement in the business.
