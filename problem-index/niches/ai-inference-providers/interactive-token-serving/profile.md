# Interactive Token Serving

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to hold time-to-first-token and inter-token latency steady while concurrency climbs — and whoever does that takes the account, because a product whose cursor stalls loses its users regardless of what the model can do.

## Profile
**Market Size:** ~$1.15B US
**Share of Parent Industry:** ~19% of category revenue
**Digital Adoption:** High
**Target Buyer:** Product engineering teams shipping user-facing applications
**Automation Potential:** High — batching and admission decisions are optimisable

## What Makes This a Distinct Niche
A user is watching a cursor. Time-to-first-token determines whether the product feels responsive; inter-token latency determines whether the stream feels natural; and both degrade as concurrency rises, because continuous batching trades individual latency for aggregate throughput. The provider's job is to hold both under load, which means reserving headroom, composing batches carefully, and refusing work it cannot serve well. The customer's alternative is a frontier model API with its own latency characteristics, which sets the bar. Nothing about this contest resembles the batch workload, and the operating decisions that win it — smaller batches, reserved capacity, admission control — are precisely the ones that make batch inference expensive.

## Current Tools & Gaps
Continuous batching, paged attention, prefix caching, speculative decoding and autoscaling endpoints. The gaps: batch composition is not optimised against latency objectives, only against throughput; requests are admitted regardless of whether their objective can be met, so degradation is silent; prefix cache hit rates are not surfaced to the customer despite dominating time-to-first-token for chat workloads; and no provider exposes a latency objective as a parameter the caller can set.

## Problems
- [[niches/ai-inference-providers/interactive-token-serving/build|🔨 Build: Latency That Degrades as Concurrency Climbs]]
- [[niches/ai-inference-providers/interactive-token-serving/buy|🛒 Buy: Tail Latency Engineering]]
- [[niches/ai-inference-providers/interactive-token-serving/fix|🔧 Fix: Admitted Anyway and Degraded Silently]]
