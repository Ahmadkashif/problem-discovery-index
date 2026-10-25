# Every Customer's Next-Best Disposal Option

**Niche:** [[niches/landfill-operators/tip-fee-disposal-pricing/profile|Tip Fee & Disposal Contract Pricing]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A landfill raising its gate rate does not know, customer by customer, what it would cost each hauler to go elsewhere, so it finds out which tons were price-sensitive only after they leave.
**Tags:** #logistic-regression #survival-analysis #graph-theory #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to raise the price a landfill realises per ton at the gate and in disposal contracts without losing tonnage to rival landfills and transfer stations, and whoever loses the fewest tons per point of price increase takes the account.

## The Problem
Every hauler's choice of disposal site is a haul-cost calculation: drive time from its routes or transfer station to each landfill, the tipping fee there, line waits and any flow-control or contract obligations. The landfill sees only its own tickets.

## Why Nobody Has Built This
It needs the haulers' origins, which the landfill can infer from ticket times and truck identities but has never modelled, plus rival landfills' rates, which are posted by public sites and guessed for private ones. Consolidators model this for acquisitions, not for routine pricing.

## What to Build
A network model of each customer's disposal alternatives: inferred route origins from arrival patterns and truck IDs, road-network drive times to every competing landfill and transfer station, public gate rates and estimated private rates, and an empirical price-response model fitted to past increases and tonnage moves. The output is each customer's estimated switching threshold and the expected tonnage loss for any proposed rate change.

## Target Customer
Pricing and disposal sales leaders at landfill owners; public solid waste directors preparing rate changes.

## Impact If Built
Setting increases customer by customer instead of across the board could add ~1–2 points of price on ~$20M of a regional landfill's third-party revenue (estimate), ~$200–400K a year, while keeping the tons that would have left.
