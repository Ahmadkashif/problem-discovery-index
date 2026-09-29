# Proxy Infrastructure Is Commodity and the Layer Above Is Not

**Niche:** [[niches/api-infrastructure-providers/api-gateways-and-management/profile|API Gateways & Management]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** High-performance proxies, policy engines and telemetry pipelines are all free and mature, which means nobody should be competing on proxying and most of the category still is.
**Tags:** #graph-theory #descriptive-statistics #time-series-forecasting #evaluation-metrics #confidence-intervals #data-integration #automation #optimization-fundamentals
**Contested on:** Every serious competitor here is fighting to be the layer every API call passes through — and that contest is fought twice, for internal traffic and for external consumers, which is why this niche is not terminal and is decomposed below.

## The Problem
The hard engineering in a gateway — a fast, correct, configurable proxy with connection pooling, retries, circuit breaking and observability — exists as mature open infrastructure that a large share of the commercial products are built on. Policy evaluation is a solved problem with open engines. Telemetry collection is standardised. The remaining differentiation is everything above that layer, and much of the category still positions on throughput benchmarks.

## What Already Exists
Open proxy infrastructure used by the hyperscalers and most commercial gateways; open policy engines with declarative languages; standardised telemetry collection and pipelines; service mesh control planes; and specification tooling for the contract layer. The commodity floor is high and rising.

## The Customization Gap
The adaptation is from plumbing to answers. It requires: (1) treating traffic as data rather than as telemetry, which is a different retention model, a different schema and a different query surface from the metrics pipeline the category currently builds; (2) sampling strategy as a designed property, since full capture is prohibitive and uniform sampling misses the rare requests that carry the most information — stratified sampling that preserves unusual shapes is the right approach and is the same insight the observability niche reaches about traces; (3) identity resolution from credential to owner, which is organisational data the gateway does not hold and must integrate; (4) schema inference over observed payloads, which is ordinary but must be incremental and tolerant of the long tail of valid variation; and (5) privacy by construction — structure and shape rather than values — stated publicly, because a gateway that retains payloads is a liability and one that retains their shape is an asset.

## Target Customer
Gateway and API management vendors, service mesh vendors, observability vendors whose pipelines already carry this data, and large platform teams.

## Impact If Solved
The proxying floor is commodity and the differentiation has moved above it, which most of the category has not acted on. Stratified sampling and privacy-by-construction are the two design decisions that make the traffic usable as data.
