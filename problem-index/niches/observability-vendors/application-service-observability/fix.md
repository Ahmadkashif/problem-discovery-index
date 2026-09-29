# The Trace That Stops at the Queue

**Niche:** [[niches/observability-vendors/application-service-observability/profile|Application & Service Observability]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A request enters a message queue and the trace ends there, so the half of the system that does the asynchronous work is invisible to the tooling that was supposed to explain it.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #data-integration #automation
**Contested on:** Every serious competitor here is fighting to let an engineer who owns the code understand what their service actually did on a specific request — and whoever does that takes the SRE account, because depth at the level of the code is what distinguishes observability from monitoring.

## The Problem
A user submits an order. The synchronous path is traced beautifully: four services, database calls, a clean waterfall. It ends by publishing a message. Everything after that — the consumer that processes the order, the retry when it failed, the second consumer that reacted to the resulting event, the scheduled job that reconciled it an hour later — is a set of disconnected traces with no relationship to the original request. When a customer asks why their order did not complete, the engineer reconstructs the chain by searching for identifiers in logs, which is precisely the work tracing was meant to eliminate.

## Why It's Still Broken
Context propagation across process boundaries is well specified for synchronous calls and is inconsistent across messaging systems, each of which has its own header or metadata mechanism and some of which have none. Instrumentation libraries cover the synchronous path first because it is easier and more visible. The time gap is also genuinely awkward — a trace spanning an hour breaks the assumptions of tooling built around request latency — so even where context survives, the display does not cope. And the asynchronous path is where the interesting failures live, which means the gap is worst exactly where it costs most.

## What a Fix Looks Like
Propagate context through messaging and display the result honestly. Ensure the trace context travels in message metadata for every broker and streaming system in use, which is a covered case in the open standard and is unevenly implemented — the fix is mostly instrumentation coverage rather than invention. Model the resulting structure as a causal chain rather than a single trace, since a request that fans out to four consumers over an hour is not a waterfall and forcing it into one produces an unreadable display. Handle the time dimension explicitly, so a trace view can span hours without being unusable. Link retries and dead letters to the original message, since a failure that succeeds on the third attempt and a failure that lands in a dead letter queue are the two outcomes an engineer needs to distinguish. Support the query that actually gets asked: given this order identifier, show me everything that happened, in order, across synchronous and asynchronous paths. And report propagation coverage per boundary, so an organisation can see where the context is being dropped rather than discovering it during an incident.

## Who Feels the Pain
Engineers reconstructing asynchronous chains from log searches; support teams answering questions about work that was accepted and never completed; and organisations whose event-driven architecture is the least observable part of their estate.

## Impact If Fixed
The propagation is specified and the gap is implementation coverage, which makes this tractable rather than research. Modelling the asynchronous chain as a causal graph rather than forcing it into a waterfall is what makes the result readable, and coverage reporting turns a silent gap into a known one.
