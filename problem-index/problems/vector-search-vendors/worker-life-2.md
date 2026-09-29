# SRE on the Index Rebuild

**Industry:** [[vector-search-vendors|Vector Search Vendors]]
**Type:** Worker Life Changing
**One-liner:** Site reliability engineers schedule and babysit index rebuilds that consume double the memory and hours of wall clock, without any measurement telling them whether the rebuild was needed.
**Tags:** #time-series-forecasting #change-point-detection #confidence-intervals #evaluation-metrics #optimization-fundamentals #hypothesis-testing #workflow-orchestration #worker-facing

## The Problem
Vector indexes need periodic rebuilding. Tombstones accumulate, graph connectivity degrades, and at some point the index should be rebuilt from the live vectors.

For a large corpus this is a serious operation. It requires memory for both the old and new index simultaneously, takes hours, saturates CPU, and must be coordinated so that queries continue to be served — typically by building a shadow index and swapping.

The SRE owns it. They schedule it in a low-traffic window, monitor it, handle the failures — a node that runs out of memory partway through, a build that takes longer than the window, a swap that causes a latency spike — and roll back if something goes wrong.

The schedule is a guess. Weekly, monthly, or when someone complains about quality. There is no measurement of index health driving it, so rebuilds happen too often, consuming resources unnecessarily, or too rarely, leaving degraded recall in place for weeks.

Multi-tenant deployments compound this: rebuilding one large tenant's index affects the memory headroom and latency of every tenant on the node.

## Why It Matters to the Worker
Rebuilds are scheduled in maintenance windows, which means nights and weekends, for an operation that produces no visible improvement when it goes well and an incident when it does not.

The uncertainty is the specific frustration. The SRE cannot say whether this rebuild was necessary and cannot say when the next one will be, so capacity planning is guesswork and every rebuild is a risk taken for an unquantified benefit.

Memory headroom is a permanent tax on the same reasoning. Clusters are provisioned with enough spare capacity to build a shadow index, which is a substantial fraction of the fleet sitting idle for an operation that runs occasionally.

And the failures are unpleasant. A rebuild that fails at hour four leaves the SRE deciding whether to retry within the window or abandon it for another month, with degraded recall continuing either way.

## What a Solution Looks Like
Index health as a continuously measured metric. Sample a few hundred queries, compare against an exact scan, and report actual recall — cheap, direct, and the number that should drive every rebuild decision. Rebuilds become a response to measured degradation rather than a calendar entry.

Degradation forecasting. Recall decays as a function of churn rate and deletion pattern, both observable, so the time until a rebuild becomes necessary is predictable and can be planned against rather than discovered.

Incremental compaction rather than full rebuilds where the structure permits, so the operation becomes continuous background work instead of an event requiring a window.

Rebuild duration and resource prediction from corpus size, dimensionality and index parameters, so the SRE knows whether it fits the window before starting.

Multi-tenant scheduling that accounts for the aggregate effect across tenants on a node rather than treating each rebuild in isolation.

## Impact If Solved
Index rebuilds are a recurring out-of-hours operation performed on a guessed schedule with unmeasured benefit and a permanent memory tax attached. Measuring recall continuously makes the decision evidence-based, and forecasting degradation converts an emergency into a plan.
