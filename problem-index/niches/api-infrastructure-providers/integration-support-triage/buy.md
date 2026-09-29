# Correlation and Replay, Standard Everywhere Else

**Niche:** [[niches/api-infrastructure-providers/integration-support-triage/profile|Integration Support Triage]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Distributed tracing, correlation identifiers and request replay are standard practice inside every engineering organisation, and none of it crosses the boundary to the consumer who is debugging against the API.
**Tags:** #graph-theory #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to answer whose fault a failed integration call was, in seconds rather than in an exchange of messages — and whoever does that takes the support organisation, because fault attribution is where every integration ticket begins and most of them end.

## The Problem
Inside an organisation, a failing request is traced end to end, correlated across services, and replayed in a test environment. All of this stops at the organisational boundary. The consumer, who is the person actually debugging, gets an error code and a status page. The provider, who has the complete trace, uses it internally and shares none of it.

## What Already Exists
Distributed tracing with propagation standards; correlation identifier conventions; structured logging and log search; request replay tooling; error grouping and deduplication from crash reporting; and clustering methods for identifying common failure patterns. All mature, all deployed internally at most providers already.

## The Customization Gap
The adaptation is to sharing across an organisational boundary. It requires: (1) tenant-scoped access to trace and log data, so a consumer sees their own requests and nothing else, which is an access control design rather than a difficulty and is the thing that has not been done; (2) redaction of the provider's internal detail, since a trace contains service names and internal errors the provider will not expose, and the consumer-facing view must be a deliberate projection rather than the raw trace; (3) trace propagation that survives the boundary, so a consumer's own identifier appears in the provider's record and both sides can find the same request — which requires a convention the provider must publish and accept; (4) fault classification as an explicit output rather than an inference the support engineer performs, which means encoding what constitutes a provider fault and what does not, and being willing to say so; and (5) replay that is safe, meaning a consumer can re-execute their failed request against a sandbox with the same payload to see what happens, without side effects.

## Target Customer
API management and gateway vendors, provider support organisations, observability vendors whose tracing already carries this, and developer experience teams.

## Impact If Solved
Every technique is deployed internally at the provider and none of it crosses to the person debugging, which is an access-control and willingness gap rather than a technical one. Tenant-scoped trace access and a propagated correlation identifier are the two changes that would end most of these tickets.
