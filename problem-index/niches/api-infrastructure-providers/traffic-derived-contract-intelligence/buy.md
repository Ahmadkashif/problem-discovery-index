# Schema Inference and Specification Mining

**Niche:** [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/profile|Traffic-Derived Contract Intelligence]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Inferring a schema from a sample of documents is elementary and well implemented, and specification mining from traces is a published research area, and gateways store none of the result.
**Tags:** #bert #descriptive-statistics #k-means-clustering #graph-theory #evaluation-metrics #confidence-intervals #cross-validation #data-integration
**Contested on:** Every serious competitor that gets here is fighting to turn observed traffic into the API's real contract — what is actually used, actually returned and actually relied upon — and whoever does that holds the accurate specification while everyone else holds the intended one.

## The Problem
Deriving a schema from a collection of JSON documents is a solved and trivially available operation. Mining behavioural specifications and invariants from execution traces is a research area with two decades of work behind it. An API gateway processes millions of well-formed documents with known endpoints and consumers, which is about as favourable an input as either technique will ever receive, and computes a latency histogram.

## What Already Exists
Schema inference libraries for JSON and other formats; specification mining and invariant detection research from the program analysis community; data profiling frameworks; sequence mining for usage patterns across endpoints; and specification diffing tools that classify a change as breaking or compatible. Most of it free.

## The Customization Gap
The adaptation is to production traffic at volume under privacy constraints. It requires: (1) incremental inference over a stream rather than batch inference over a corpus, since the schema must be maintained continuously and cannot be recomputed from a year of traffic; (2) stratified sampling that deliberately retains rare shapes, because the interesting divergences are in the tail — the endpoint variant used by one consumer, the conditional field that appears rarely — and uniform sampling loses exactly those; (3) structure-only extraction with no value retention, which is what makes the capability deployable at all and is sufficient for schema, optionality and cardinality, with effective enumerations handled by retaining low-cardinality value sets only where they are clearly not personal data; (4) distinguishing a genuine schema variation from a transient anomaly, since a malformed request from one broken consumer is not a contract variant and a naive inference will treat it as one; and (5) consumer-attributed inference, because the per-consumer view is what makes the result useful for change management rather than merely descriptive.

## Target Customer
Gateway and API management vendors, observability vendors whose pipelines already carry this traffic, and specification and documentation tooling vendors.

## Impact If Solved
The inference is elementary and the input is unusually clean, which leaves sampling design and privacy construction as the real work. Retaining rare shapes is what makes the output useful, since the divergences that matter are in the tail rather than the bulk.
