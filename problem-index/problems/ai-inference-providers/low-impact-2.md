# Multi-Tenant Isolation on Shared Accelerators

**Industry:** [[ai-inference-providers|AI Inference Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Sharing accelerators across customers is the only path to acceptable utilisation, and the isolation primitives available on this hardware were not designed for it, so one tenant's batch job degrades another's latency guarantee.
**Tags:** #optimization-fundamentals #convex-optimization #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #markov-decision-processes

## The Problem
Dedicating an accelerator to a customer wastes most of it, because most workloads do not saturate one. Sharing is the only way the economics work, and it introduces contention that is difficult to control.

Continuous batching — the technique that makes modern serving efficient — mixes requests from multiple tenants into the same forward pass. That is exactly where the efficiency comes from and exactly where isolation breaks. A tenant submitting very long sequences occupies key-value cache memory that others need. A tenant sending a burst fills the batch and pushes another's requests into later batches. A large batch job saturates memory bandwidth and every interactive request on the device slows.

The affected customer sees latency variance with no explanation. Their traffic did not change, their model did not change, and their response times doubled for twenty minutes. Support has no good answer, because acknowledging the cause means acknowledging that the latency guarantee is contingent on other people's behaviour.

## What Already Exists
NVIDIA Multi-Instance GPU provides hard partitioning on supported hardware, at the cost of fixed partition sizes and lost efficiency. Multi-Process Service allows concurrent contexts with weak isolation. Serving engines implement request scheduling with priority support. Kubernetes provides resource quotas at container granularity. Rate limiting is standard. Paged attention manages key-value cache memory efficiently within a single engine instance.

## The Customisation Gap
The isolation primitives are either too coarse or too weak. Hard partitioning gives isolation and sacrifices the pooling that makes sharing worthwhile. Soft sharing gives efficiency and no guarantee. There is nothing in between that says: this tenant gets this latency percentile regardless of what others do.

Admission control is the unexploited lever. Predicting a request's resource footprint before scheduling it — from prompt length, expected output length and model characteristics — would allow batch composition that respects each tenant's guarantee. Output length is the hard part and is predictable from the prompt with useful accuracy, and no serving engine attempts it.

Interference measurement is absent. How much a given tenant's workload degrades a co-located tenant is directly measurable and is not measured, so placement decisions are made without knowing which workloads conflict.

Attribution is the third gap and the one that hurts support most. When latency degrades, identifying which co-tenant caused it is straightforward from the batch composition record and is not surfaced, so the provider cannot explain what happened even internally.

## Impact If Solved
Multi-tenancy is the difference between a viable margin and none, and it currently trades away the latency guarantee that customers are actually buying. Predicting request footprints and composing batches against per-tenant guarantees would let providers oversubscribe confidently, which is worth more than any single optimisation on the fleet.
