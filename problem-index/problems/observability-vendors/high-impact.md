# Causal Diagnosis During an Incident

**Industry:** [[observability-vendors|Observability Vendors]]
**Type:** High Impact
**One-liner:** The tooling shows an engineer everything and tells them nothing, so the person paging at three in the morning constructs the causal story by hand from dashboards — while the vendor holds the pattern from a thousand comparable incidents at other companies.
**Tags:** #graph-neural-networks #causal-inference #change-point-detection #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #hypothesis-testing

## The Problem
An alert fires. Latency is up on a service, or errors are climbing, or a queue is growing. The on-call engineer opens the dashboards.

What they see is comprehensive and undirected. Dozens of services, each with metrics moving. Traces showing slow requests. Logs at a volume no human can read. Deployment markers. Infrastructure events. All of it correlated with the incident because everything in a distributed system correlates during an incident.

The work is constructing the causal story: which of these moved first, which are consequences, and which is the cause. An experienced engineer does this well through pattern recognition — this shape of latency increase with this error signature after a deployment usually means that — and the recognition comes from having seen it before at this company.

The vendor has seen it thousands of times across thousands of companies. Failure modes repeat far more than any individual engineer can appreciate: connection pool exhaustion, a cache stampede after an eviction, a downstream timeout cascading into thread pool starvation, a deployment that changed a query plan, a certificate expiring, a dependency's rate limit. These have recognisable signatures in telemetry.

The product's response is a dashboard and a query language.

## Why It's Unsolved
The business model rewards collection. Revenue scales with data volume, so the product effort has gone into ingesting more from more sources, and diagnosis has been treated as the customer's job. "Automated root cause analysis" is claimed widely and trusted narrowly, because early attempts produced correlation dressed as causation and engineers stopped believing the feature.

Correlation genuinely is the hard part. In a distributed system under stress, everything moves together, and distinguishing cause from consequence requires the dependency structure and the timing at a resolution most telemetry does not preserve. Service dependency graphs are increasingly available from tracing and are frequently incomplete.

Cross-customer learning is where the leverage is and it is commercially and contractually awkward. Telemetry is customer data, and using patterns from one customer's incidents to help another requires terms most vendors have not sought and customers would scrutinise. Failure signatures can be abstracted from customer specifics, and nobody has done the work to demonstrate that convincingly.

And the bar is unforgiving. A wrong diagnosis during an incident costs time at the most expensive possible moment, so a feature that is right most of the time is worse than no feature unless it is honest about its uncertainty.

## What a Solution Looks Like
Ranked hypotheses rather than an answer. The output should be three candidate explanations with the evidence for each and an explicit confidence, because an engineer can evaluate a hypothesis quickly and cannot evaluate a verdict.

Temporal precedence and dependency structure as the backbone. What moved first, propagated along which edges of the service graph, is the closest thing to causal evidence available, and it requires timing resolution and a dependency graph that tracing can now supply.

Failure signature matching against a corpus of abstracted incident patterns — the shape of the anomaly across metric types, not the customer's service names — which is where cross-customer learning delivers and where it can be made contractually acceptable.

Change correlation done properly. Most incidents follow a change, and the candidate set is enumerable: deployments, configuration changes, feature flags, infrastructure events, dependency releases. Ranking them by temporal and structural plausibility is tractable and is what an engineer does first anyway.

And the resolution loop: what actually fixed it, captured and matched to the signature, so the corpus improves with every incident.

## Impact If Solved
Time to diagnosis is the largest component of incident duration and is currently produced by a tired person reading dashboards. The vendor holds the only cross-organisational corpus of how production software fails, and turning it into ranked hypotheses with honest confidence is the difference between a data store and a product that helps at the moment it was bought for.
