# Buy: Data Pipeline Practice for Intelligence Ingestion

**Niche:** Enrichment & Integration
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data engineering solved schema evolution, lineage, deduplication with provenance and quality testing, and intelligence ingestion pipelines were built by security teams without any of it.
**Tags:** #evaluation-metrics #change-point-detection #graph-theory #data-integration #workflow-orchestration #automation #confidence-intervals
**Contested on:** Whether context arrives attached to the indicator or is assembled by whoever needs it, every time.

## The Problem

A threat intelligence ingestion pipeline is a data pipeline. It pulls from multiple heterogeneous sources on a schedule, normalises differing schemas, deduplicates, enriches, and loads into downstream systems.

It is almost always built by a security team rather than a data team, which shows. Lineage is not tracked, so nobody can trace an indicator back to the source that supplied it. Schema changes from a vendor break the pipeline silently or corrupt fields. Deduplication collapses records without retaining provenance. There is no quality testing, so a feed that starts returning malformed data is discovered when someone notices odd alerts. And freshness is not monitored, so a feed that stops updating keeps serving its last snapshot.

Every one of those failure modes has a standard solution in data engineering, with mature tooling, and none of it is applied — because the pipeline lives in the security stack where the relevant discipline is a different one.

## What Already Exists

Pipeline orchestration: Airflow, Dagster, Prefect, with dependency management, retries, SLA monitoring and failure alerting.

Data quality: Great Expectations, dbt tests and the data observability platforms, asserting expectations on every run and detecting freshness, volume and schema anomalies.

Lineage: OpenLineage and the lineage features in modern catalogues, tracing outputs to sources.

Schema management: schema registries with compatibility checking, which handle exactly the vendor-changes-their-format problem.

Deduplication with provenance: standard practice in master data management, where retaining all contributing sources is a requirement rather than an afterthought.

Intelligence-specific: STIX and TAXII, MISP and the threat intelligence platforms, with their own ingestion implementations.

## The Customization Gap

**Provenance through deduplication is the specific gap.** Master data management treats source retention as fundamental. Intelligence deduplication collapses to a single record, which destroys the per-feed attribution everything else depends on.

**Schema change handling is absent.** A registry with compatibility checking would catch a vendor format change at ingestion rather than downstream. Feed formats do change and the breakage is routinely silent.

**Freshness monitoring is missing.** A feed that stops updating is a stale-data incident with a well-understood detection pattern, and intelligence pipelines mostly do not detect it.

**Quality assertions are not run.** Expectations on record counts, field population and value distributions would catch a degraded feed immediately, and nobody asserts anything.

**The graph shape is unusual for these tools.** Intelligence data is relational in a graph sense — indicators related to campaigns related to actors — which most data pipeline tooling handles as a foreign concept.

**Latency expectations differ.** Intelligence ingestion runs continuously with minutes-level expectations, where much data tooling assumes batch. This is a real difference and a narrowing one.

## Target Customer

Threat intelligence platform vendors, who are building data pipelines and should be using data pipeline discipline — their customers' most common complaints are pipeline failures described in security vocabulary.

Security engineering teams running their own ingestion, who frequently have a data platform team in the same organisation using all of this tooling for other purposes.

Data observability vendors as potential adapters, though the more likely path is that security teams adopt the patterns from colleagues rather than buying a product.

## Impact If Solved

A discipline developed for exactly this class of problem reaches pipelines built without it, where the failure modes are the textbook ones.

Deduplication with retained provenance is standard practice in master data management and is the single change that would unblock feed-level measurement across the industry.

And freshness and quality monitoring would catch silently degraded feeds — a failure that currently persists until someone notices the alerts look strange, which is the same silent-pipeline-failure problem every data team has already learned to detect.
