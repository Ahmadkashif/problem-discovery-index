# Instrument Choice per Lot of Cattle

**Niche:** [[niches/commodity-brokers/livestock-hedging-desks/profile|Livestock Hedging Desks]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** For every group of cattle there is a cheapest effective way to protect its price, and nobody computes it.
**Tags:** #monte-carlo-methods #probability-distributions #optimization-fundamentals #bayesian-inference #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to pick, for each pen or barn of animals, the cheapest effective protection among an LRP endorsement, a put option and a futures hedge, and to document why, and whoever protects the most head at the lowest net premium takes the account.

## The Problem
A cattle feeder placing 400 steers can buy LRP at several coverage levels and end dates, buy feeder or live cattle puts, sell futures, or combine them. Each has a different cost after subsidy, a different basis exposure, a different cash-flow profile (premium now, margin calls later, indemnity after sale) and a different fit to the lot size. Brokers and agents usually recommend what their firm sells.

## Why Nobody Has Built This
LRP sits with insurance agents and futures with brokers, and few firms are licensed for both. RMA publishes daily coverage prices and premiums but no comparison against exchange instruments.

## What to Build
A per-lot comparator. Given head, weights, placement and expected sale dates, location basis history and the producer's liquidity limits, it simulates net price outcomes and cash flows for each instrument and combination using daily RMA LRP prices and exchange option prices. It recommends the cheapest protection meeting the producer's floor and records the comparison for compliance.

## Target Customer
Livestock desks at FCMs, livestock-focused IBs, and insurance agencies that also hold futures registrations.

## Impact If Built
Producers protect more animals for less premium, and the broker's recommendation is documented as best for the client rather than for the product.
