# Incident Diagnosis Patterns From Software Observability

**Niche:** [[niches/bi-analytics-platforms/data-engineer-on-call/profile|Data Engineer On-Call]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software observability has spent a decade on incident correlation, dependency-graph diagnosis and alert quality, and data pipelines are treated as a separate world that starts from nothing.
**Tags:** #graph-theory #graph-neural-networks #change-point-detection #causal-inference #evaluation-metrics #confidence-intervals #time-series-forecasting #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to turn a pipeline alert into a diagnosis and a remedy rather than a page — and whoever does that takes the data platform account, because detection is a solved and crowded market and remediation is nobody's product.

## The Problem
Ranking candidate causes of an incident by temporal precedence over a dependency graph, correlating failures with recent changes, and measuring whether alerts are worth firing are all things software observability has worked on for a decade with real results. Data pipeline incidents have the same structure — a dependency graph, a change stream, a time-ordered failure propagation — and data observability products have largely not imported any of it.

## What Already Exists
Dependency-graph-based incident diagnosis, change correlation, alert quality measurement and backtesting, and incident clustering, all developed in the software observability category and documented in its practitioner literature. Orchestrators expose the pipeline dependency graph directly, which is cleaner and more explicit than the service graphs software observability has to infer from tracing. Change-point detection and seasonal modelling for the metric side are standard.

## The Customization Gap
The adaptation is to batch data pipelines, which are easier in some ways and harder in others. It requires: (1) exploiting the explicit dependency graph, since orchestration gives the structure directly rather than requiring inference — this makes causal ordering more reliable here than in the service world and is the main advantage to press; (2) handling batch timing semantics, where lateness rather than failure is the common fault and a job that will eventually succeed but has missed its window is the case that matters, which has no clean analogue in request-serving systems; (3) data-shaped failure signatures — volume, freshness, schema, distribution — rather than latency and error rates, since the failures are about content rather than availability; (4) source-system change correlation, because most upstream causes originate outside the data platform in systems nobody owns, which makes the change stream harder to obtain and more valuable when obtained; and (5) alert quality measurement applied honestly to the data alerts, since the four-class inventory — fired and actioned, fired and ignored, never fired, missed the incident — is as revealing here as in software and nobody has produced it.

## Target Customer
Data observability vendors, orchestration vendors, incident management platforms extending into data, and large data platform teams.

## Impact If Solved
A decade of applicable practice sits one category over and has not been transferred, and the explicit dependency graph makes the diagnosis problem easier here than where the techniques were developed. Batch timing semantics are the genuine adaptation, and the alert quality inventory needs no modelling at all.
