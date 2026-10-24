# Demand Hidden by the Empty Shelf

**Niche:** [[niches/grocery-stores/fresh-department-ordering/profile|Fresh Department Ordering]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Fix (Pain Point)
**One-liner:** When a fresh item sells out by noon, the system records noon's sales as the day's demand and orders less next time.
**Tags:** #time-series-forecasting #maximum-likelihood-estimation #gradient-boosting #evaluation-metrics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to set each fresh item's store order before the truck is cut, and whoever cuts the most shrink at an unchanged in-stock rate takes the account.

## The Problem
Sales are only demand when there is product on the shelf. A forecast trained on raw sales learns that the items that sold out were less popular than they were, orders fewer, sells out earlier, and spirals down. Shrink falls and shoppers go elsewhere.

## Why It's Still Broken
Stores rarely record when an item ran out. On-hand counts are unreliable after culls, and shelf cameras cover few stores. The shrink number is visible every month; lost sales are not, so the bias is rewarded.

## What a Fix Looks Like
Estimate stockout time from the sales pattern (the timestamp of the last sale against the item's usual intraday curve), from on-hand when it is reliable, and from shelf scans where cameras or pickers' "not found" events exist. Train the forecast with a censored likelihood, and report estimated lost sales next to shrink on every department scorecard.

## Who Feels the Pain
Department managers whose suggested orders shrink every week; shoppers who find the berries gone by afternoon; and finance teams who see shrink fall while fresh sales slip.

## Impact If Fixed
Correcting censoring on high-velocity fresh items commonly lifts their forecasts by ~5–10% (estimate). For a store selling ~$100,000 of fresh a week, recovering even 1% of lost sales is ~$50,000 a year.
