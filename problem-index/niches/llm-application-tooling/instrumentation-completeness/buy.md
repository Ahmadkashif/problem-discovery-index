# Auto-Instrumentation and Context Propagation

**Niche:** [[niches/llm-application-tooling/instrumentation-completeness/profile|Instrumentation Completeness]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Application monitoring solved zero-effort instrumentation and cross-boundary context propagation, and LLM applications instrument by hand and lose the thread at every hop.
**Tags:** #data-integration #automation #workflow-orchestration #graph-theory #evaluation-metrics #descriptive-statistics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make the trace contain the thing you need at the moment you need it — and whoever does that takes the account, because a trace missing the decisive context is indistinguishable from no trace at all.

## The Problem
Instrumenting an application without editing it, and carrying a trace context across process, service and asynchronous boundaries so a distributed operation appears as one trace, are both solved. Runtime agents attach and instrument automatically; context propagation is part of the standard. LLM applications are frequently instrumented by hand, with the context lost whenever work crosses into a queue, a background job or the front end where the user actually reacts.

## What Already Exists
Runtime auto-instrumentation agents; context propagation standards across processes and asynchronous boundaries; automatic instrumentation for common libraries and frameworks; baggage for carrying application-level attributes along a trace; and front-end instrumentation correlating browser events to backend traces.

## The Customization Gap
The adaptation is to a trace whose most valuable span crosses into a human's behaviour. It requires: (1) propagation into the front end and back, so that a user's reaction — an edit, a retry, an abandonment — lands on the same trace as the response that caused it, which is the highest-value missing link and is a standard technique unused here; (2) automatic instrumentation of the application's own retrieval, assembly and post-processing logic, which is where the context lives and which generic agents do not recognise; (3) semantic attribute conventions specific to this domain, which the framework niche develops; (4) propagation across the asynchronous gap between a background generation job and the user who eventually sees it, which is common in this domain and routinely breaks the trace; and (5) sensitivity-aware capture, since automatic instrumentation that helpfully captures every attribute is how payloads end up somewhere nobody assessed.

## Target Customer
Application teams, tracing vendors, and the observability community for whom this domain's asynchronous and human-in-the-loop shape is a new case.

## Impact If Solved
Context propagation is standard and this domain loses the thread at exactly the boundary that matters. Propagating into the front end so the user's reaction lands on the trace that caused it is the highest-value missing link and needs no new technique.
