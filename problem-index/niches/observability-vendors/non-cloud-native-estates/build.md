# The Assumptions Do Not Hold Here

**Niche:** [[niches/observability-vendors/non-cloud-native-estates/profile|Non-Cloud-Native Estates]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Observability tooling assumes ephemeral, connected, instrumentable workloads with cheap telemetry, and the systems running factories, stores and utilities are none of those things.
**Tags:** #time-series-forecasting #change-point-detection #gaussian-mixture-models #hidden-markov-models #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to bring modern observability to systems that are not ephemeral, not containerised and frequently not connected — and whoever does that takes the industrial and enterprise estate, because the current tooling assumes a world these systems do not live in.

## The Problem
A retailer runs point-of-sale systems in nine hundred stores on links that are shared with the store's other traffic and are not generous. Shipping telemetry at cloud-native volumes is not possible, so they ship almost nothing: an up-or-down check and a nightly log upload. When a store's terminals become slow on a Saturday afternoon, the diagnosis is a phone call to the store manager. The systems themselves are stable, run the same software for years, and have extremely regular daily and weekly patterns — which is the best possible setting for detecting that something has changed, and nothing exploits it.

## Why Nobody Has Built This
The category's architecture and its commercial model both assume volume: ship everything to a central store and query it there, priced per gigabyte, which is unworkable over a constrained link and unaffordable across a large fleet. Edge computation was not part of the design. The buyer is also different — operations and engineering functions in retail, manufacturing and utilities rather than a software platform team — and is reached through a different channel. And these estates are unfashionable, which has steered vendor attention toward the cloud-native customer who is easier to sell to and more visible.

## What to Build
Move the analysis to where the data is. Compute at the edge and transmit conclusions rather than raw telemetry: local baselining, local anomaly detection and local aggregation, with full detail retained locally for a window and uploaded only on demand or on an anomaly — which makes constrained links and large fleets viable and is the architectural change the whole niche depends on. Exploit the stability, since these systems repeat daily and weekly patterns with unusual regularity, which makes deviation detection far more reliable here than in a dynamic cloud environment and is an advantage the category has never used. Support intermittent connectivity as a normal condition rather than an error, with store-and-forward, ordering and gap handling built in. Observe from outside where instrumentation is impossible, using network behaviour, power draw, protocol timing and the observable outputs of the system, which is frequently sufficient to detect that something has changed. Compare across the fleet, because nine hundred stores running the same software are nine hundred replicates and an outlier is immediately visible — this is the strongest available signal and it exists in no product. And present it to the people who actually operate these systems, who are not site reliability engineers.

## Target Customer
Retail, manufacturing, utility, logistics and healthcare operations functions; the industrial and device management vendors already present in these estates; and the observability vendors seeking a market beyond the cloud-native one.

## Impact If Built
A large share of the systems that matter most physically are the least observed, because the category's architecture assumes conditions they do not meet. Edge computation with conclusions rather than telemetry is the enabling change, and fleet comparison across identical sites is a signal no current product uses.
