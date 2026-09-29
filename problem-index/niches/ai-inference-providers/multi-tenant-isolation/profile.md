# Multi-Tenant Isolation

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to share an accelerator between tenants without one of them being able to affect another's latency — and whoever does that takes the account, because sharing is the only route to acceptable utilisation and the hardware was not built for it.

## Profile
**Market Size:** ~$380M US
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Very Low — primitives not designed for this
**Target Buyer:** Platform and reliability teams at the providers
**Automation Potential:** Medium — enforcement is buildable, the hardware limits are real

## What Makes This a Distinct Niche
Dedicating an accelerator per tenant guarantees isolation and destroys utilisation, which destroys the business. Sharing is therefore mandatory, and the isolation primitives on this hardware were designed for a single trusted workload: memory partitioning is coarse, scheduling between contexts is limited, caches and memory bandwidth are shared with no enforcement, and one tenant's large batch job can lengthen another tenant's tail without violating any stated limit. Providers manage this with placement heuristics and by keeping the worst offenders apart. The contest is genuine performance isolation on hardware that does not offer it, which is partly a software problem, partly a scheduling one, and partly a matter of being honest with customers about what is actually shared.

## Current Tools & Gaps
Memory partitioning features where the hardware provides them, process and container isolation, placement heuristics, and separating known-noisy tenants. The gaps: no enforcement of memory bandwidth or cache share, which is where most interference occurs; no measurement of interference, so it is diagnosed anecdotally; no attribution of one tenant's degradation to another's behaviour; and no disclosure to customers about what isolation they actually have.

## Problems
- [[niches/ai-inference-providers/multi-tenant-isolation/build|🔨 Build: One Tenant's Batch Job Is Another's Latency Incident]]
- [[niches/ai-inference-providers/multi-tenant-isolation/buy|🛒 Buy: Resource Isolation From Operating Systems and Clouds]]
- [[niches/ai-inference-providers/multi-tenant-isolation/fix|🔧 Fix: Nobody Says What Is Actually Shared]]
