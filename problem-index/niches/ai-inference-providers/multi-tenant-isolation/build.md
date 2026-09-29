# One Tenant's Batch Job Is Another's Latency Incident

**Niche:** [[niches/ai-inference-providers/multi-tenant-isolation/profile|Multi-Tenant Isolation]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Sharing accelerators across customers is the only path to acceptable utilisation, and the isolation primitives available on this hardware were not designed for it, so one tenant's batch job degrades another's latency guarantee.
**Tags:** #markov-chains #convex-optimization #evaluation-metrics #change-point-detection #descriptive-statistics #confidence-intervals #automation #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to share an accelerator between tenants without one of them being able to affect another's latency — and whoever does that takes the account, because sharing is the only route to acceptable utilisation and the hardware was not built for it.

## The Problem
Two tenants share an accelerator. One serves a chat product with a tight latency requirement; the other starts a large embedding job at nine in the morning. Memory bandwidth saturates, the cache is thrashed, and the chat product's inter-token latency doubles. No quota was exceeded, no limit was violated, and no metric attributes the degradation to its cause. The first customer opens a support ticket about latency; the provider investigates for a day and moves them to a different node, which is the entire remediation available.

## Why Nobody Has Built This
The hardware's isolation features address memory capacity and compute partitioning, not memory bandwidth or cache, which is where most real interference happens — so the gap is genuine rather than neglected. Measuring interference requires observing both tenants, which raises its own questions. Placement heuristics work well enough most of the time, which removes the urgency. And admitting the limits of isolation in customer-facing terms is a commercial decision nobody wants to be first to make.

## What to Build
Measure interference, then schedule against it. Build interference measurement first: characterise each tenant's resource profile — memory bandwidth appetite, cache footprint, batch shape — and attribute observed degradation to co-tenancy rather than guessing, which turns an anecdotal problem into a quantified one and is the precondition for everything else. Place tenants by compatibility, since a bandwidth-heavy workload and a latency-sensitive one are a known bad pairing and profiles make that predictable rather than discovered. Enforce what can be enforced in software: rate limits shaped by resource profile rather than by request count, batch size caps for aggressive tenants, and admission control that accounts for current co-tenant state. Offer explicit isolation tiers — dedicated, isolated-class, best-effort — priced accordingly, so a customer who needs isolation can buy it and one who does not is not paying for it, which is the honest product structure and is missing entirely. Detect and quarantine noisy tenants automatically rather than through a support ticket. Report co-tenancy interference to the affected customer, since telling them their latency moved because of a neighbour is better than letting them hunt for a cause in their own code. And press the hardware vendors for bandwidth and cache partitioning, since the providers are the customers with the standing to ask and the gap is upstream.

## Target Customer
Platform and reliability teams at the providers, the tenants on both sides of an interference event, and the accelerator vendors whose isolation primitives are the constraint.

## Impact If Built
Interference is real, unmeasured and remediated by moving people. Resource profiling makes bad pairings predictable rather than discovered, and explicit isolation tiers are the honest product structure the category has never offered.
