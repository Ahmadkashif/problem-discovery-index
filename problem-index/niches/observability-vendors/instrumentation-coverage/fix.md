# The Boundary Where Trace Context Is Dropped

**Niche:** [[niches/observability-vendors/instrumentation-coverage/profile|Instrumentation Coverage]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** One service strips an unrecognised header and every trace crossing it is truncated, which is experienced as an unrelated tracing problem by the four teams downstream.
**Tags:** #graph-theory #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #data-integration #automation
**Contested on:** Every serious competitor here is fighting to tell an organisation what it cannot see before an incident rather than during one — and whoever does that takes the platform account, because every capability in the category is worthless on a service that emits nothing.

## The Problem
A gateway, a proxy or an older service does not forward the trace context header. Every request passing through it starts a new trace on the other side. Four downstream teams experience this as traces that mysteriously begin in the middle, file separate tickets about their own instrumentation, and each conclude their configuration is wrong. The actual cause is one component, one configuration line, and a fix that takes five minutes once somebody knows where to look — which nobody does, because the symptom appears everywhere except at the cause.

## Why It's Still Broken
Propagation is a distributed property and every tool reports per service, so nothing observes the boundary itself. Truncation is not an error: both traces are valid, they are simply unrelated, and no validation notices. Header stripping happens for legitimate reasons in proxies and gateways configured with allow-lists, so the behaviour is deliberate somewhere upstream and its consequence is unknown to whoever configured it. And the symptom's distance from the cause defeats normal troubleshooting entirely.

## What a Fix Looks Like
Detect the discontinuity and name the boundary. Identify traces that begin at a service which is clearly not an entry point — a service that appears mid-graph in other traces — which is a graph property computable from the trace store and localises the problem immediately. Correlate the truncated traces with the upstream caller by timing and endpoint, producing a specific named boundary rather than a general propagation complaint. Report propagation health per edge in the service graph, so a percentage of traces surviving each hop becomes a monitored property with an owner. Check proxy and gateway configurations for header allow-lists that exclude trace context, which is the commonest single cause and is inspectable. Include this in the coverage report rather than treating it as a tracing curiosity, since its effect on diagnostic capability is as large as a missing agent. And alert on a change, because propagation that was working and stopped is a configuration change somebody made this week.

## Who Feels the Pain
Engineers whose traces begin in the middle of a system; teams filing tickets about their own correctly-configured instrumentation; and organisations whose tracing investment is silently halved by one proxy configuration.

## Impact If Fixed
Detecting mid-graph trace origins is a straightforward graph query over the trace store and localises a cause that normal troubleshooting cannot find. Per-edge propagation health turns an invisible distributed property into a monitored one with an owner.
