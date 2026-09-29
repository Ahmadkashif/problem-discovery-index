# Sampling That Keeps the Interesting Requests

**Niche:** [[niches/observability-vendors/application-service-observability/profile|Application & Service Observability]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Survey sampling has a century of theory about keeping the rare and interesting cases, and trace sampling mostly keeps one request in a hundred at random, which is the hundred that explain nothing.
**Tags:** #monte-carlo-methods #descriptive-statistics #gaussian-mixture-models #change-point-detection #evaluation-metrics #confidence-intervals #automation #optimization-fundamentals
**Contested on:** Every serious competitor here is fighting to let an engineer who owns the code understand what their service actually did on a specific request — and whoever does that takes the SRE account, because depth at the level of the code is what distinguishes observability from monitoring.

## The Problem
Tracing every request is prohibitively expensive at scale, so systems sample. The default is head-based uniform sampling: decide at the start of the request, keep one in a hundred, discard the rest. Incidents are made of the unusual requests — the slow ones, the failing ones, the ones with a rare parameter combination — and uniform sampling retains them in proportion to their rarity, which is to say almost never. The engineer investigating an incident routinely finds that the interesting requests were not sampled.

## What Already Exists
Stratified and importance sampling with a long statistical history; tail-based sampling implementations in the open collector ecosystem, which decide after the request completes and can therefore keep the slow and failing ones; reservoir sampling for bounded retention; outlier detection for identifying what is unusual; and exemplar mechanisms that link aggregated metrics back to specific retained traces.

## The Customization Gap
The adaptation is to a streaming, distributed decision under memory constraints. It requires: (1) deciding after completion rather than at the start, which is what makes keeping the interesting requests possible and requires buffering spans across services until the trace completes — the central engineering difficulty and the reason head-based sampling persists; (2) a definition of interesting that goes beyond slow and erroring, including rare path combinations, unusual parameter values, requests from newly deployed versions and requests that touched a degraded dependency; (3) guaranteed coverage of the ordinary as well, since a sample composed entirely of outliers cannot establish what normal looks like and the comparison is half the diagnostic value; (4) statistical correctness of the aggregates computed from a non-uniform sample, which requires carrying the sampling probability and is routinely got wrong, producing metrics that silently misstate; and (5) a budget-aware controller, since the point is to stay within a cost envelope while maximising diagnostic value, which is an optimisation rather than a threshold.

## Target Customer
Observability vendors, the open collector ecosystem, and platform teams operating their own telemetry pipelines under cost pressure.

## Impact If Solved
Uniform sampling discards precisely the requests incidents are made of, which makes this the highest-value change available in the collection layer. Correct aggregate statistics from a non-uniform sample is the part most implementations get wrong and is what makes the approach safe to adopt.
