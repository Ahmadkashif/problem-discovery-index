# Re-Runs Nobody Traces to a Cause

**Niche:** [[niches/auto-parts-distributors/hot-shot-delivery-runs/profile|Hot-Shot Delivery Runs]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** A second trip to the same shop for the same job is the costliest run of the day, and the store records it as just another delivery.
**Tags:** #logistic-regression #feature-engineering #evaluation-metrics #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get each shop order from the nearest stock to the bay, and whoever loses the fewest shop orders to cancellation because the part arrived after the shop's window takes the account.

## The Problem
Re-runs happen because the part was wrong, a part was missed at the pick, the shop changed the order, or the hub item came later. Each cause has a different owner, but the dispatch log shows only another run, so drivers absorb the blame and the cause repeats. A re-run is also the delivery most likely to land after the shop's window, because the clock started with the first order.

## Why It's Still Broken
Dispatch, picking and returns are separate records, and nobody codes why a run went out.

## What a Fix Looks Like
Tag each run as first delivery or re-run, link re-runs to the original order, and capture the cause in one tap (wrong part, missing item, shop change, hub split). A weekly report shows re-runs and the late cancellations they caused, by cause, store and shop, and wrong-part re-runs feed the fitment model.

## Who Feels the Pain
Drivers, store managers paying for the miles, and shops waiting twice.

## Impact If Fixed
If re-runs fell from ~10% to ~6% of runs (estimate) at a store making ~120 runs a day, that is ~5 fewer runs daily, roughly a quarter of a driver's day, and fewer second deliveries arriving after the shop has given up.
