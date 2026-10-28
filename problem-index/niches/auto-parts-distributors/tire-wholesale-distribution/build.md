# Size-Level Demand Sensing From Dealer Searches

**Niche:** [[niches/auto-parts-distributors/tire-wholesale-distribution/profile|Replacement Tire Wholesale Distribution]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tire wholesalers forecast from what they shipped; the dealer searches that found no stock, the earliest signal of demand they are missing, are thrown away.
**Tags:** #time-series-forecasting #bayesian-inference #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep independent tire dealers' size-and-brand orders filled from the nearest warehouse, and whoever fills the largest share of a dealer's tire orders as ordered, without substitution, takes the account.

## The Problem
A wholesaler's demand history is censored: it records shipments, so a size that was out of stock for three weeks looks like a size nobody wanted. Dealers search portals and e-catalogs by size and brand all day, and the searches that ended without an order, or with an order from someone else, are the demand the wholesaler failed to fill.

## Why Nobody Has Built This
Portal search logs are kept for web analytics, not joined to the warehouse plan; e-catalog networks don't pass lost searches to the losing seller; and forecasting teams are set up around shipment history and manufacturer allocations.

## What to Build
A demand model at warehouse × size × brand × week that combines shipments with portal searches, quote requests and no-stock events, corrects for censoring, and adds the vehicle parc around each warehouse (tire sizes map to vehicle configurations) and weather-driven seasonal shifts. It outputs replenishment and transfer recommendations with uncertainty bands, and reports as-ordered fill rate by dealer.

## Target Customer
Demand planning and distribution leaders at national and regional tire wholesalers; parts distributors with tire programmes.

## Impact If Built
If as-ordered fill rate on a wholesaler's top 500 sizes rose by ~2–3 points (estimate) at constant inventory, a wholesaler selling ~$500M a year would keep ~$10–15M of orders that now go to rivals or get substituted.
