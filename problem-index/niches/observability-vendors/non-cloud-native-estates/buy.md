# Edge Analytics and Constrained Telemetry

**Niche:** [[niches/observability-vendors/non-cloud-native-estates/profile|Non-Cloud-Native Estates]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Streaming analytics on constrained devices, sketch-based summarisation and store-and-forward telemetry are all mature, developed for exactly these conditions, and observability products do not use any of them.
**Tags:** #time-series-forecasting #exponential-smoothing #change-point-detection #dimensionality-reduction #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to bring modern observability to systems that are not ephemeral, not containerised and frequently not connected — and whoever does that takes the industrial and enterprise estate, because the current tooling assumes a world these systems do not live in.

## The Problem
Doing useful statistics on a stream without storing it is a well-developed area: sketches for quantiles and cardinality, exponential smoothing for baselines, streaming change detection with bounded memory. Industrial telematics has shipped conclusions over expensive links for decades. Every technique needed to make observability work over a constrained connection exists and was developed for precisely these conditions, and the category's products ship raw telemetry to a central store.

## What Already Exists
Sketch algorithms for approximate quantiles, cardinality and heavy hitters with bounded memory; exponential smoothing and streaming change-point detection; compression and delta encoding for time series; store-and-forward messaging with ordering guarantees; and edge analytics frameworks from the industrial and telematics worlds. All mature and mostly free.

## The Customization Gap
The adaptation is to a fleet of long-lived, similar, poorly-connected systems. It requires: (1) baselines computed and held locally, since the point is to avoid transmitting the data the baseline is computed from, which inverts the usual architecture; (2) fleet-wide comparison despite local computation, which means transmitting compact summaries that remain comparable across sites — a sketch that can be merged centrally is the right primitive and is what makes outlier detection across nine hundred stores possible on a small budget; (3) seasonality modelling tuned to these systems' very strong daily, weekly and annual patterns, which are far more regular than cloud workloads and support much tighter bounds; (4) graceful behaviour across disconnection, so that a site offline for six hours produces a known gap rather than a false anomaly, and the backlog is reconciled rather than discarded; and (5) an upgrade and configuration path that works over the same constrained link, since the operational reality of a large fleet is that changing anything is the hard part.

## Target Customer
Observability vendors moving beyond cloud-native estates, industrial and device management platforms, retail and manufacturing technology functions, and telematics providers.

## Impact If Solved
Every technique was developed for these conditions and the category ignored them because its customers were elsewhere. Mergeable local summaries are the key primitive, since they deliver fleet comparison without fleet-scale transmission.
