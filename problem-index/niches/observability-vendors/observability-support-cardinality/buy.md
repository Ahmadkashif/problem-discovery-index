# Cardinality Estimation Is a Solved Sketch Problem

**Niche:** [[niches/observability-vendors/observability-support-cardinality/profile|Observability Support & Cardinality]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Estimating the number of distinct values in a stream with tiny memory is a textbook algorithm, and the category discovers cardinality problems by counting the bill.
**Tags:** #monte-carlo-methods #descriptive-statistics #change-point-detection #gradient-boosting #evaluation-metrics #confidence-intervals #automation #optimization-fundamentals
**Contested on:** Every serious competitor that takes this seriously is fighting to stop cardinality explosions and instrumentation gaps before they reach a support queue — and whoever does that takes the support organisation, because those two topics are most of what its engineers do all day.

## The Problem
Counting distinct values in a stream using a few kilobytes is one of the better-known results in streaming algorithms, implemented in every major database and data processing framework. Detecting that a stream's distinct count is growing without bound is a straightforward extension. The observability category, which is built entirely on high-cardinality time series, applies this at query time for aggregation and not at ingestion time for prevention.

## What Already Exists
Cardinality sketches with bounded memory and known error characteristics; heavy hitter and frequent item algorithms; streaming change detection; and classification of string types from character distributions, which is elementary. All of it is in standard libraries and much of it is already inside these products for other purposes.

## The Customization Gap
The adaptation is to a hot ingestion path with a prediction rather than a measurement. It requires: (1) prediction from the first minutes rather than measurement after the fact, since by the time the cardinality is measurably high the cost has been incurred — which means classifying the value type from its character composition and growth rate rather than waiting for the count; (2) per-label-per-metric tracking rather than global, because the unit of the problem is a specific label on a specific metric and the combinatorics of multiple labels is where the multiplication happens; (3) negligible cost on the ingestion path, which sketches provide and naive approaches do not; (4) projection of the combinatorial effect, since a label with a hundred values on a metric that already has three labels multiplies rather than adds, and the projected total is the number the engineer needs; and (5) attribution back to the source — the service, the code path, ideally the commit — because a warning that does not say who introduced it goes to a platform team who must then hunt for the origin.

## Target Customer
Observability vendors, the open collector ecosystem where prevention can happen before data leaves the customer, and telemetry cost management vendors.

## Impact If Solved
The algorithms are textbook, cheap and already present in these products for other purposes, which makes prevention a matter of where the check is placed rather than whether it is possible. Prediction from the first minutes is the adaptation that turns a measurement into a prevention.
