# Build: Context That Survives the Pipeline

**Niche:** Enrichment & Integration
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An ingestion layer that preserves provenance, relationships and context through deduplication and normalisation, so the alert carries everything that was known about the indicator.
**Tags:** #graph-theory #graph-neural-networks #evaluation-metrics #bert #data-integration #workflow-orchestration #automation #confidence-intervals
**Contested on:** Whether context arrives attached to the indicator or is assembled by whoever needs it, every time.

## The Problem

An indicator leaves the vendor with substantial context. It came from a specific report about a specific campaign attributed to a specific actor. It is related to other indicators — the domain it resolved to, the malware that contacted it, the certificate it presented. It has a collection method, a first-seen date, a confidence and an intended use.

By the time it reaches the matching engine, most of that is gone. The ingestion pipeline normalised several feeds into a common schema, deduplicated across them, and reduced each indicator to a value, a type and a score. The report it came from is not attached. The related indicators are separate rows. The feed that supplied it may not be recorded at all.

So when the alert fires, the analyst sees that an address matched a threat feed. Everything that would let them assess it in seconds — the campaign, the actor, the report, the related infrastructure — was present at the vendor and discarded in transit.

The loss also blocks everything else. Feed provenance is what makes per-feed measurement possible, and deduplication destroys it. Relationships are what make an alert interpretable as part of a campaign rather than as an isolated hit, and flattening destroys them.

## Why Nobody Has Built This

**Normalisation is the point of the ingestion layer.** Its job is to make heterogeneous feeds uniform, and uniformity is achieved by reducing to the common subset — which is a value and a type.

**Downstream platforms accept little.** SIEM and endpoint matching engines take lists of values. Rich context has nowhere to go in the systems that consume it, so preserving it upstream appears pointless.

**Deduplication is operationally correct and destroys attribution.** Matching an indicator once rather than four times is right. Retaining all four sources as provenance is an extra field nobody added.

**Relationships require a graph and the pipeline is a list.** Preserving the connections between indicators means carrying a graph through a pipeline built for rows.

**Nobody asked.** Analysts adapted to alerts without context by looking things up manually, and the adaptation made the gap invisible.

**Feed richness varies.** Some vendors ship substantial context and others ship lists, so a pipeline preserving context handles both and the common denominator argument wins.

## What to Build

**Retain provenance through deduplication.** Every source that supplied an indicator, kept as a list rather than collapsed to the first or the highest-confidence. This is one extra field and it unlocks every per-feed measurement in [[niches/threat-intelligence-vendors/feed-quality/profile|🔵 Feed Quality Measurement]].

**Carry the context object alongside the match list.** The matching engine gets the flat list it needs; the alerting layer gets a reference to the full context — report, campaign, actor, collection method, intended use. The two are separable and the pipeline currently discards the second because the first is all the matcher wants.

**Preserve relationships as a graph.** Indicators and the connections between them, so an alert can be presented as part of a cluster rather than as an isolated value. An analyst seeing that the matched address is one of six related to a campaign is in a completely different position from one seeing a bare hit.

**Enrich once, at ingestion.** Infrastructure type, reallocation status, sinkhole status, age — computed at the ingestion layer for every indicator, so every downstream alert carries them without a per-alert lookup.

**Resolve conflicts explicitly.** When two feeds disagree about an indicator's confidence or classification, record the disagreement rather than picking one. Feed disagreement is informative and is currently resolved silently.

**Push context into the alert.** The alerting layer should render the retained context with the alert, which is where the whole chain pays off and where every existing pipeline drops it.

**Make it work with lists too.** Vendors shipping bare lists should be enriched at ingestion to the same standard, so the customer's context does not depend on which vendor was most generous.

## Target Customer

Threat intelligence platform vendors — Anomali, ThreatConnect, OpenCTI, MISP — for whom this is the core of their own product and where provenance and context loss is a known and unaddressed weakness.

Security operations teams running their own ingestion, who lose the same context and would recover it with pipeline changes rather than new products.

SIEM vendors, who could accept and render a context object alongside the match list and mostly do not.

## Impact If Built

Retaining feed provenance through deduplication is one field and is the specific technical blocker preventing every organisation from measuring which of its subscriptions is worth anything.

Carrying context to the alert would give analysts the campaign, actor and report at triage time, which is the enrichment that most changes how quickly an alert resolves.

And enriching once at ingestion rather than per alert removes a duplicated lookup that currently happens thousands of times a day in every organisation running intelligence.
