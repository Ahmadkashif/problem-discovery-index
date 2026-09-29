# Columnar Storage and Open Collection Are Commodity

**Niche:** [[niches/observability-vendors/observability-platforms/profile|Observability Platforms]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Columnar stores, time-series databases and an open instrumentation standard have commoditised collection and storage, and much of the category still prices and positions as though they were the product.
**Tags:** #dimensionality-reduction #k-means-clustering #time-series-forecasting #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to be the place an organisation's telemetry lands and is queried — and that contest is fought twice, for engineering and for security, which is why this niche is not terminal and is decomposed below.

## The Problem
Storing and querying enormous volumes of timestamped, high-cardinality data is a solved problem with excellent open implementations. Collecting telemetry portably is solved by an open standard with broad adoption. Both were genuinely hard and genuinely differentiating a decade ago. The category's pricing and positioning largely still rest on them, while the customer's actual problem has moved to which data is worth keeping and what it means during an incident.

## What Already Exists
Columnar analytical stores and purpose-built time-series databases, open and mature; object storage with efficient scan; open instrumentation and collection standards with wide language coverage; compression and downsampling techniques; and sketch-based approximate aggregation for high-cardinality summarisation. The floor is high and rising.

## The Customization Gap
The adaptation is from storage to judgement about what to store. It requires: (1) selective retention as a first-class capability rather than a global policy, since the correct answer differs per stream and the products offer per-index rather than per-signal control; (2) intelligent sampling that preserves the unusual rather than the representative, because incidents are made of rare requests and uniform sampling discards precisely the evidence that matters — this is a separable component with outsized value; (3) tiering that is driven by observed access rather than by age, since a two-year-old log queried weekly is worth more than a two-day-old one nobody has opened; (4) summarisation that survives the raw data, so a dropped stream leaves behind aggregates and exemplars rather than nothing, which changes the risk calculus of dropping anything; and (5) collector-layer implementation rather than platform-side, because the decision must be made before ingestion to save anything, which is exactly where the open standard now sits.

## Target Customer
Observability vendors, the open collector ecosystem, cost management vendors, and large platform teams building their own telemetry pipelines.

## Impact If Solved
The storage floor is commodity and the differentiation has moved to selection, which most of the category has not repriced around. Sampling that preserves the unusual and summarisation that survives deletion are the two capabilities that make aggressive cost reduction safe.
