# Degradation That Is Only Visible at the End

**Industry:** [[database-platform-vendors|Database Platform Vendors]]
**Type:** High Impact
**One-liner:** Databases degrade gradually and fail suddenly — a plan flips, an index stops being selective, growth crosses a threshold — and the engine exposes every diagnostic needed to see it coming and interprets none of them.
**Tags:** #change-point-detection #time-series-forecasting #gradient-boosting #survival-analysis #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics

## The Problem
Database failures are rarely sudden in cause and almost always sudden in appearance. A query that has run in five milliseconds for a year starts taking two seconds because the planner chose a different plan after statistics drifted past a threshold. An index that was selective becomes useless as the data distribution shifts. A table crosses a size where a sequential scan stops fitting in cache. A connection pattern that worked at one concurrency exhausts the pool at another. Transaction identifier consumption approaches a wraparound limit. Bloat accumulates until vacuum cannot keep up.

Each of these is a slow slide with a cliff at the end. And each becomes visible at the cliff, during a traffic peak, when the mitigations available are the worst ones — restart, scale up, shed load.

The engines are not withholding information. They expose extraordinary diagnostic detail: plan statistics, wait events, buffer hit ratios, index usage, bloat estimates, lock waits, replication lag. It is all there, in system catalogues and views, and reading it requires knowing which of hundreds of numbers matters for this workload, in this version, at this scale.

That knowledge belongs to database specialists, and most organisations do not have one. The managed service moved the operational burden and did not move the interpretive burden.

## Why It's Unsolved
Managed services were sold on removing operational work — provisioning, patching, backups, failover — and those are genuinely solved. Interpretation was left with the customer, and the customer no longer has a database administrator, because the managed service was supposed to make one unnecessary.

Prediction is genuinely hard for a specific reason: the relationship between a metric and a failure is workload-dependent and non-linear. Ninety per cent buffer cache hit rate is excellent for one workload and catastrophic for another. Thresholds do not transfer, which is why generic monitoring on database metrics produces noise.

Plan changes are the sharpest case and the hardest. A plan regression is invisible in aggregate latency until it affects a hot query, the planner's decision depends on statistics that update asynchronously, and the same query can flip back and forth. Detecting the flip requires per-query plan tracking that few systems retain.

And the vendor's fleet-wide view — the thing that would make thresholds learnable — has been used for capacity planning rather than for customer warning.

## What a Solution Looks Like
Per-workload baselining rather than global thresholds. What matters is whether this database's behaviour has changed relative to itself, and whether that change resembles trajectories that preceded failures elsewhere in the fleet.

Plan stability monitoring as a first-class capability. Track the plan chosen for each significant query over time, detect flips, and evaluate whether the new plan is worse — which is measurable from execution statistics rather than from cost estimates.

Growth-driven threshold forecasting. Many failures are a data volume crossing a point where an access pattern stops working, and both the growth curve and the threshold are estimable, which converts a cliff into a date.

Fleet-derived pattern matching, which is the vendor's unique advantage. This query shape, at this table size, with this index configuration, has degraded at a predictable point across many customers, and the current customer is approaching it.

And warnings that arrive with the remedy, since telling an organisation without a database specialist that their statistics are stale is only useful if it also says what to run.

## Impact If Solved
Database degradation is the failure mode most likely to take down a production system, it arrives at peak load with the worst mitigation options available, and the managed service era removed the specialists who used to see it coming. The fleet corpus makes the thresholds learnable, which is the only route back to warning rather than diagnosing.
