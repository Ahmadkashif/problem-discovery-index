# Stockouts Recorded as Low Demand

**Niche:** [[niches/logistics-consultants/inventory-policy-studies/profile|Inventory Policy & Safety Stock Studies]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Sales history records what shipped, so every week a SKU was out of stock looks like a week nobody wanted it, and the new policy under-stocks exactly the SKUs that ran out.
**Tags:** #expectation-maximization #survival-analysis #probability-distributions #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to release working capital without a service-level miss the client's sales team will blame on the study, and whoever's policies hold their projected fill rate in the first two quarters after go-live takes the account.

## The Problem
A distributor's best seller was out of stock for five weeks last year. The ERP shows five weeks of near-zero sales. Fitted to that history, the demand distribution has lower mean and higher variance than reality, and the policy either under-stocks the SKU or inflates its safety stock for the wrong reason. Backorders and cancelled lines, which would reveal the lost demand, are often purged or kept in a different table.

## Why It's Still Broken
The study receives sales order lines, not demand. Reconstructing demand needs on-hand snapshots to identify stockout periods, which many clients do not retain, and statistical de-censoring the standard formulas omit.

## What a Fix Looks Like
Request on-hand history and backorder or cancellation records in the data request; flag every SKU-week with zero or near-zero available stock; estimate demand in those weeks from pre- and post-stockout rates and similar SKUs; and report which SKUs' policies depend on reconstructed demand.

## Who Feels the Pain
Planners blamed for stockouts in the first quarter; sales teams whose customers are shorted; consultants whose projected fill rate fails.

## Impact If Fixed
A data request change and a de-censoring step remove the most common reason a new policy fails on the SKUs that matter most.
