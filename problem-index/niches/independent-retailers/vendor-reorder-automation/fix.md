# Vendor Minimum Order Aggregation and Timing Optimization

**Niche:** [[niches/independent-retailers/vendor-reorder-automation/profile|Vendor Reorder Automation]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Fix (Pain Point)
**One-liner:** Most wholesale vendors require $150-500 minimum orders — the retailer either overstocks to meet minimums (tying up cash) or delays orders until enough items are needed (causing stockouts) — because no tool helps them time and aggregate orders to hit minimums efficiently.
**Tags:** #automation #revenue-impact #worker-facing #quick-win

## The Problem
A retailer buying from 60 vendors, each with a $200-500 minimum order requirement, faces a constant optimization puzzle: Item A from Vendor X is running low, but the reorder quantity ($85) doesn't meet Vendor X's $250 minimum. The owner can: (1) order additional items from Vendor X to reach the minimum (overstocking products that aren't needed yet), (2) wait until more items from Vendor X are needed (risking a stockout on Item A), or (3) skip the reorder and hope Item A sells slowly enough to last until the next planned order (gambling). In practice, owners default to option 1 (overstock to meet minimums), which ties up $5,000-15,000 in excess inventory across their vendor portfolio at any given time.

## Why It's Still Broken
No tool tracks the relationship between individual product reorder needs and vendor minimum order requirements. POS reorder point alerts fire per-product without considering the vendor context. The owner maintains a mental model of which vendors they "owe" an order to and which products can be combined — but this mental model breaks down across 60 vendor relationships with different minimums, lead times, and ordering schedules. The optimization is straightforward: given the reorder needs of all products from Vendor X over the next 4-6 weeks, what's the optimal order timing that hits the minimum without excessive overstock?

## What a Fix Looks Like
A vendor order timing optimizer that: (1) tracks current inventory levels and projected stockout dates for all products per vendor, (2) calculates the earliest date when enough products from a given vendor will need reordering to meet the minimum ("Vendor X: $85 of items need reorder now, $95 will need reorder in 2 weeks, $110 in 4 weeks — wait 2 weeks and order $180+ to exceed the $250 minimum with minimal overstock"), (3) alerts the owner when a vendor order window opens ("Place Vendor X order this week: 6 items totaling $285, meeting the $250 minimum with only $35 of pull-forward overstock"), (4) shows the cash flow impact of order timing ("ordering now vs. waiting 2 weeks: $35 extra inventory now but avoids a $120 stockout loss on Item A"), and (5) generates the purchase order with the optimized item list.

## Who Feels the Pain
Independent retailers who regularly over-order to meet vendor minimums (cash flow pressure) or under-order and experience preventable stockouts (revenue loss), and who spend 2-3 hours per week mentally juggling vendor minimum calculations.

## Impact If Fixed
Reduces minimum-order-driven overstock by 40-60%, freeing $2,000-9,000 in working capital. Reduces minimum-order-driven stockouts by 50-70%, recovering $1,500-5,000 in annual lost sales. Saves 2-3 hours/week of mental effort on vendor order timing calculations.
