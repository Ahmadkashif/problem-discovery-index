# Replenish From the Signal, Not the Walk

**Niche:** [[niches/industrial-distributors/vmi-and-industrial-vending/profile|Vendor-Managed Inventory & Industrial Vending]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Replenishment reps visit every bin on a schedule; most visits find nothing urgent, and the stockouts happen between them.
**Tags:** #time-series-forecasting #exponential-smoothing #bayesian-inference #dynamic-programming #optimization-fundamentals #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep the customer's bins, cribs and vending machines in stock at the lowest consigned inventory and the fewest replenishment visits, and whoever replenishes from actual usage signals rather than walk-around counts takes the account.

## The Problem
A territory's onsite programmes are serviced on fixed routes: weekly for one plant, twice a week for another. The rep counts or scans each location, builds a refill order and restocks on the next visit. Visit frequency reflects habit and contract promises, not usage, so labour is spent where it isn't needed and fast movers run dry where it is.

## Why Nobody Has Built This
Dispense logs and sensor readings exist but feed billing and usage reports. Planning sits in the ERP's min/max, which treats each slot as a static rule. The routing and the forecasting have never been joined, and the distributor's field organisation is managed by visits completed.

## What to Build
A replenishment planner that forecasts each slot's demand from dispense and sensor data with the customer's shift calendar, recalculates reorder points against the cost of a stockout at that slot, and builds each rep's route daily from predicted need. Slots whose risk is low are skipped; plants with a looming stockout move up. The planner reports consigned inventory and service level per programme.

## Target Customer
Onsite and inventory-solutions leaders at national and regional distributors running hundreds to thousands of programmes.

## Impact If Built
Fewer visits per programme and fewer stockouts at the same time (estimate ~20–30% visit reduction), which lowers the cost to serve each programme and frees reps to install new ones.
