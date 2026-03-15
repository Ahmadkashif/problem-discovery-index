# Dynamic SKU Slotting Optimization

**Industry:** [[warehouse-3pl|Warehouse & 3PL]]
**Type:** High Impact
**One-liner:** Warehouse operations managers who slot SKUs manually based on gut feel and experience — placing fast-moving items near the pick face but without continuously optimizing the slot assignments as velocity and order patterns change — get a slotting optimization model that continuously recommends slot reassignments to minimize total picker travel distance as demand patterns evolve.
**Tags:** #gradient-boosting #regression #tabular-ml #reinforcement-learning #revenue-impact

## The Problem

SKU slotting — assigning each product to a specific warehouse location — is the single highest-leverage warehouse design decision. A poorly slotted warehouse forces pickers to travel far between frequently co-ordered items; a well-slotted warehouse clusters co-ordered items near each other and places high-velocity SKUs closest to the pick path entry and shipping area.

Manual slotting by experienced operations managers works well for stable SKU mixes. It degrades as the product mix changes: seasonal items that were slow movers become fast movers in Q4, new SKUs are added without systematic placement, discontinued items hold premium slots. A 3PL with 10,000 active SKUs might perform a slotting review once per year — by which point slot assignments are significantly misaligned with actual demand patterns.

## Why It's High Impact

Slotting optimization directly affects picker productivity: studies consistently show 15-25% travel time reduction from optimal slotting vs. ad-hoc slotting. For a 3PL with 50 pickers at $18/hour working 8-hour shifts, a 15% productivity improvement reduces labor cost by $108,000 annually — without additional capital investment.

## What a Solution Looks Like

A WMS integration that: (1) analyzes historical order data to identify current SKU velocity (units picked per day) and SKU co-occurrence patterns (which items are ordered together); (2) computes the optimal slot assignment for current demand patterns using a combinatorial optimization algorithm; (3) generates a prioritized slot-swap recommendation list (highest-impact moves first); (4) continuously re-analyzes as order patterns evolve, generating new swap recommendations when the benefit exceeds the labor cost of the slot move. The operations manager approves and schedules moves during off-peak hours.

## Implementation Path

Order history data from the 3PL's WMS provides the velocity and co-occurrence signals. The slotting optimization problem is a well-studied operations research problem — existing algorithms (GRASP, genetic algorithms, simulated annealing) solve it at warehouse scale. The continuous monitoring and incremental swap recommendation system is the product innovation, not the core optimization algorithm. 3-4 month development for a WMS-integrated slotting intelligence tool.
