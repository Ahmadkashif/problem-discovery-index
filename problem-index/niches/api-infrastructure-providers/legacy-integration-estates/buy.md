# Schema Inference and Monitoring, Pointed Backwards

**Niche:** [[niches/api-infrastructure-providers/legacy-integration-estates/profile|Legacy Integration Estates]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Schema inference, data quality monitoring and lineage tracking are mature products built for modern data platforms, and the fixed-width file arriving at two in the morning has none of them.
**Tags:** #bert #descriptive-statistics #change-point-detection #graph-theory #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor here is fighting to bring visibility and change safety to the file transfers, message queues and SOAP services that still move most enterprise data — and whoever does that takes the integration estate, because nobody can currently see it at all.

## The Problem
Data observability is a well-funded category: infer the schema, profile the values, detect drift, track lineage, alert on anomalies. All of it is built for warehouse tables and streaming pipelines. A fixed-width file landing on a transfer server at two in the morning, carrying the day's settlement records, has a schema documented in a Word file from 2011 and no monitoring beyond whether the file arrived.

## What Already Exists
Schema inference from samples; data profiling and quality frameworks with expectation suites; drift and anomaly detection over distributions; lineage tracking tools; and parsers for the major legacy formats including EDI and fixed-width layouts. The data observability category is documented separately in this vault and its techniques transfer directly.

## The Customization Gap
The adaptation is to formats and cadences that predate the tooling. It requires: (1) inference over positional and delimited formats without headers, where field boundaries must be discovered from value patterns across records rather than read from a schema — which is tractable and is the first thing needed; (2) reconciliation against the documentation that does exist, since a 2011 specification is usually mostly right and the differences are the finding; (3) batch-cadence baselines, because these flows are daily, weekly or monthly and a monitoring approach built for streaming has the wrong notion of normal — the relevant anomalies are a file arriving late, a record count outside its usual band for that day of the month, or a total that does not reconcile; (4) content checks that reflect what these flows carry, such as control totals and record count trailers, which are present in most legacy formats and are a stronger integrity signal than anything statistical; and (5) operation without modifying the flow, since these integrations cannot be touched and the monitoring must observe from the side.

## Target Customer
Data observability vendors with an unserved adjacent estate, managed file transfer and integration vendors, and enterprise integration teams.

## Impact If Solved
A well-funded observability category stops exactly where the highest-consequence data movement begins. Headerless schema inference and batch-cadence baselines are the two adaptations, and control-total checking is a strong integrity signal these formats already carry and nobody verifies.
