# Multi-Tenant Query Optimisation as a Product

**Niche:** [[niches/bi-analytics-platforms/embedded-analytics/profile|Embedded Analytics]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Materialised view selection, cache admission and workload-aware physical design have decades of database research behind them, and embedded analytics teams solve them with a cron job and a hunch.
**Tags:** #dynamic-programming #convex-optimization #optimization-fundamentals #k-means-clustering #gradient-boosting #evaluation-metrics #confidence-intervals #automation
**Contested on:** Every serious competitor in embedded analytics is fighting to serve thousands of a software vendor's customers their own data, fast, inside a product that is not theirs — and whoever holds latency and isolation at that scale takes the deal, because the buyer is an engineering team that will otherwise build it.

## The Problem
Choosing which aggregates to maintain given a query workload and a storage budget is the materialised view selection problem, studied in the database literature since the nineties, with known formulations, hardness results and good heuristics. Deciding what to keep in a cache is equally well studied. Embedded analytics teams solve both by materialising whatever was slow last week and refreshing it nightly.

## What Already Exists
Materialised view selection, index selection and automated physical design have a large research literature and appear as advisor features in several commercial databases. Cache admission and eviction policies, including learned ones, are well developed. Query plan cost models are built into every engine. Workload forecasting from historical query traffic is ordinary time-series work. Modern warehouses expose the query history that all of this needs.

## The Customization Gap
The adaptation is to multi-tenant embedded workloads. It requires: (1) per-tenant rather than global optimisation, since tenants differ by orders of magnitude in data volume and query rate and a single global physical design is wrong for nearly all of them — this is the central adaptation and the one hand-built layers get wrong; (2) an objective that includes the host's cost structure, because the host is paying per query and pricing per tenant, so the optimisation is over money and latency jointly rather than latency alone; (3) freshness as a per-dashboard constraint rather than a global setting, since some embedded views must be current to the minute and most are fine at an hour, and treating them uniformly wastes most of the available saving; (4) exploitation of the repetitiveness of embedded traffic, which is far more predictable than exploratory BI and makes forecasting genuinely accurate here; and (5) safe-by-construction tenant isolation in every materialised artefact, because an aggregate that spans tenants is a data leak waiting for a bug, and the optimisation must not be able to produce one.

## Target Customer
Embedded analytics vendors, BI platform vendors with embedded offerings, warehouse vendors, and the larger software companies who have built this in-house and are maintaining it.

## Impact If Solved
A mature research area maps almost directly onto a workload that is unusually well suited to it, and the current practice is manual. Per-tenant optimisation against a cost-and-latency objective is where the gain is, and isolation-by-construction is the non-negotiable constraint.
