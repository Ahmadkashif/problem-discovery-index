# The Instance Type Chosen Three Years Ago

**Niche:** [[niches/game-hosting-providers/fleet-cost-optimisation/profile|Fleet Cost Optimisation]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The whole fleet runs on an instance family selected before two hardware generations shipped, and nobody has rerun the comparison.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #revenue-impact #confidence-intervals #automation #optimization-fundamentals #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to serve the same concurrency for less money across regions, instance types and pricing models, on margins thin enough that the difference decides who wins the contract — and whoever optimises it takes the account.

## The Problem
Fleet configuration decisions are sticky. An instance family was benchmarked once, a session density was set conservatively, a commitment was sized against a demand profile that has since changed, and a region mapping was drawn before three regions were added. Each decision was reasonable when made. Together they now cost a meaningful share of a thin margin, and nobody has revisited any of them because the fleet works.

## Why It's Still Broken
There is no review trigger — configuration that works is never re-examined, and cost erosion produces no incident, no alert and no complaint, so the decision simply persists. Benchmarking takes engineering time with no feature output. The price-performance landscape moves quietly. And the saving is invisible until someone looks.

## What a Fix Looks Like
Rerun the comparison you already know how to run. Benchmark the current instance families against the game's real workload, which is the fix and is usually a week that pays for itself many times over. Test a higher session density against measured tick rate and player experience rather than assuming the conservative number, since that is typically the largest single saving available. Recompute the commitment against the current demand distribution, as commitments sized against an old profile are systematically wrong in one direction. Review the region mapping against the current footprint and player distribution. Attribute cost per title and mode so the expensive combinations become visible. Compare price-performance across providers where the architecture allows, which is at minimum a negotiating position. Check for idle and orphaned capacity, which accumulates invisibly in every fleet. Set a calendar review rather than waiting for a cost incident, which is the durable part. Report the saving against a measured baseline so the work keeps being funded. And write down the current configuration's rationale, so the next review starts from reasoning rather than from archaeology.

## Who Feels the Pain
Providers losing contracts on price; finance teams watching margin erode; engineering teams who suspected it and had no time; and studios paying more than they need to.

## Impact If Fixed
Configuration that works is never re-examined, and cost erosion produces no incident, no alert and no complaint, so the decision simply persists. Rerunning the benchmark and the density test is a week against a large share of a thin margin.
