# Buy: Observability Discipline for the Compliance Pipeline

**Niche:** Evidence Collection & Continuous Monitoring
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data engineering solved pipeline freshness, completeness and lineage with mature tooling, and compliance pipelines — which are data pipelines — run without any of it.
**Tags:** #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation #compliance
**Contested on:** Whether continuous monitoring reports the state of the estate or the state of the integrations.

## The Problem

A compliance platform is, architecturally, a data pipeline. It extracts from many third-party sources on a schedule, transforms the results, applies rules, and produces an output that people make decisions on.

Data engineering has spent the last decade building the discipline for exactly this. Data observability tooling monitors freshness, volume, schema drift and distribution changes, alerting when a pipeline silently degrades. Lineage tracks which source produced which output. Data contracts define expectations between producers and consumers. Quality testing runs assertions on every run. The whole category exists because silent pipeline failure — data that stops arriving while dashboards keep rendering the last value — was recognised as the dominant failure mode.

Compliance pipelines have the same failure mode, higher stakes, and none of the tooling. The output is not a business metric that someone will eventually notice looks odd; it is an assurance artefact presented to auditors, insurers and enterprise customers.

## What Already Exists

Data observability: Monte Carlo, Bigeye, Soda, Metaplane and the open-source equivalents, monitoring freshness, volume, schema and distribution with automated anomaly detection and incident routing.

Pipeline orchestration: Airflow, Dagster and Prefect, with retry semantics, SLA monitoring, dependency-aware scheduling and failure alerting.

Data quality testing: dbt tests, Great Expectations and similar, asserting expectations on every run and failing loudly.

Lineage: OpenLineage and the lineage features in modern catalogues, tracing outputs back to sources.

API reliability: the standard patterns — circuit breakers, retry with backoff, quota management and credential rotation monitoring — from production service engineering.

## The Customization Gap

**Freshness thresholds have to be control-specific and framework-aware.** Data observability lets you set a freshness expectation per table. Here the expectation should derive from what the control is verifying and what the framework implies about continuity, which is a domain mapping no generic tool provides.

**Volume anomalies mean something specific.** A check returning fewer resources than last week is, in data terms, a volume anomaly. In compliance terms it is potential silent scope loss — the most dangerous failure in the category. The detection is generic; the interpretation is not.

**Lineage must reach the audit artefact.** Data lineage traces to a dashboard. Here it needs to trace from a statement in an audit package back to the specific API response, with timestamp and scope, so an auditor can follow the chain. That is a stronger requirement than any lineage tool currently targets and is exactly what an assurance product should offer.

**Sources are third-party and uncooperative.** Data observability assumes some control over upstream systems. Compliance integrations pull from external APIs that change without notice, which puts more weight on schema drift detection and graceful degradation.

**The output is an assurance claim, not a metric.** A wrong business metric is corrected next quarter. A wrong compliance state is presented to an auditor as evidence. The tolerance for silent failure should be far lower here and is in practice far higher.

**Nobody has applied the contract idea.** Data contracts formalise what a consumer expects from a producer. A compliance equivalent — what each control requires from each integration, asserted and monitored — would make verification gaps explicit rather than implicit.

## Target Customer

The compliance platforms themselves, adopting the discipline rather than buying the specific products, since the tooling assumes a data warehouse context that does not quite fit.

Data observability vendors could plausibly extend here, and the more likely path is that platform engineering teams simply apply the patterns they already know from their own data infrastructure.

Auditors and enterprise buyers as the pressure: lineage from an audit statement back to a timestamped API response is an obviously superior artefact and nobody is asking for it yet.

## Impact If Solved

A decade of hard-won discipline about silent pipeline failure reaches a pipeline whose silent failures produce false assurance rather than a wrong chart.

Volume-anomaly detection would catch silent scope loss — a connector still working but seeing less — which is the failure that currently passes completely unnoticed and is the most consequential.

And end-to-end lineage from audit artefact to source observation would make compliance evidence genuinely inspectable, which is what an assurance product ought to offer and none currently does.
