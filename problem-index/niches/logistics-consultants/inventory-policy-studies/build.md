# Policies Back-Tested Against Last Year Before Anyone Signs

**Niche:** [[niches/logistics-consultants/inventory-policy-studies/profile|Inventory Policy & Safety Stock Studies]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Inventory studies present a working-capital figure computed from formulas, and nobody simulates how the proposed policy would have performed against the client's actual demand last year.
**Tags:** #monte-carlo-methods #probability-distributions #exponential-smoothing #evaluation-metrics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to release working capital without a service-level miss the client's sales team will blame on the study, and whoever's policies hold their projected fill rate in the first two quarters after go-live takes the account.

## The Problem
The readout says the new policy releases a stated amount of inventory at a 97% fill rate. The figure comes from safety stock formulas applied to fitted distributions. The client's actual demand last year — promotions, lost customers, a supplier that was late for a quarter — is not replayed through the policy, so neither the CFO nor the planners can see where it would have stocked out.

## Why Nobody Has Built This
Planning software simulates forward in production, after implementation. Consultants work in spreadsheets under fixed fees, and a day-by-day replay across thousands of SKUs and locations is a build they cannot justify on one engagement.

## What to Build
A study harness that replays the client's historical demand, receipts and lead times day by day through both the current and proposed policies, reporting fill rate, stockout days, inventory and orders placed per SKU and location, with confidence ranges from resampling. Clients see exactly which SKUs would have failed, and the policy is adjusted before sign-off rather than after the first missed shipment.

## Target Customer
Inventory and planning consultancies, and the CFOs who commission their studies.

## Impact If Built
A working-capital figure with its service risk shown on actual history, which is the evidence sales and finance both accept.
