# Three Views and a Copied Identifier

**Niche:** [[niches/observability-vendors/application-service-observability/profile|Application & Service Observability]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engineer moves from the metric that alerted to the trace that might explain it to the log line that names the error, copying identifiers between three views, and the platform could have assembled all three.
**Tags:** #graph-theory #change-point-detection #descriptive-statistics #bert #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to let an engineer who owns the code understand what their service actually did on a specific request — and whoever does that takes the SRE account, because depth at the level of the code is what distinguishes observability from monitoring.

## The Problem
An alert says the ninety-ninth percentile latency on checkout has risen. The engineer opens the latency graph, picks a slow window, switches to traces, filters by service and duration, finds a slow trace, identifies the span that took the time, copies its identifier, switches to logs, searches, finds nothing because the log does not carry the trace identifier, searches instead by timestamp and service, reads forty lines, and finds a connection timeout. Eleven minutes. The three signals describe the same event and the platform stores all three and joins none of them.

## Why Nobody Has Built This
The three signal types were built as three products, frequently by acquisition, and the integration has been presented as navigation between them rather than as a single model of an event. Correlation requires the identifier to be propagated into logs, which is an instrumentation discipline customers adopt partially. And the demonstration for each signal in isolation is compelling, so the product has been sold as three capabilities rather than judged on the time from alert to explanation, which is the only metric that matters to the buyer.

## What to Build
One model of the event rather than three views. Assemble everything about a slow or failing request automatically — the trace, the spans, the logs emitted during each span, the profile samples taken while it ran, the metrics for the services involved, the deployments and configuration in force — and present it as a single object the engineer opens once. Make identifier propagation into logs the default rather than a documented practice, since the correlation depends on it entirely and partial adoption is the commonest reason the join fails. Attach continuous profiling to request context, so that a slow span can be explained by what the code was doing rather than merely timed. Make the comparison available immediately: this request against the normal distribution for the same endpoint, which is what an engineer computes mentally and gets wrong under pressure. Handle the asynchronous case, since a growing share of systems pass work through queues and event streams where the trace currently ends. And measure time from alert to explanation as the product's own metric, because that is what the buyer is actually purchasing and no vendor reports it.

## Target Customer
Site reliability and platform engineering teams, and the observability vendors competing on depth rather than on ingest volume.

## Impact If Built
The signals describe the same events and are stored by the same platform and joined by the engineer manually, which is the largest avoidable cost in the diagnostic path. Time from alert to explanation is the metric the buyer is purchasing and nobody reports it.
