# Edge Delivery Platforms

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to be the network a customer's traffic flows through — and that contest is fought on cost per byte in one market and on latency for uncacheable content in another, which is why this niche is not terminal and is decomposed below.

## Profile
**Market Size:** ~$3.8B US content delivery capacity
**Share of Parent Industry:** ~42% of category revenue
**Digital Adoption:** Very High — delivery is universal
**Target Buyer:** Media operations; separately, application platform teams
**Automation Potential:** Medium-High — routing and offload are optimisable; the economics are structural

## What Makes This a Distinct Niche
Delivery is the category's foundation and its most commoditised layer: several providers operate genuinely excellent global networks and the differences between them, for most traffic, are small. Competition has therefore moved to price, to bundled capabilities, and to the specific characteristics that matter for particular traffic types — which is precisely where the market divides.

The filter fails here. "Edge delivery" names the product rather than a contest, and two markets with different economics sit underneath it. Large object and media delivery is a volume business where cost per delivered byte and origin offload dominate, bought by media operations teams for whom egress is a major cost line, and where the technical contest is about bitrate behaviour, prefetching and peak capacity. Dynamic application delivery is a latency business where most content cannot be cached at all, bought by application platform teams for whom the bytes are trivial and the tail latency is the product, and where the contest is connection handling, protocol behaviour and what the edge does when the origin is slow. Decomposed below.

## Current Tools & Gaps
Global networks with tiered caching and origin shielding, modern transport protocols, real user monitoring, and traffic steering. The gaps: performance is reported as averages across a customer's whole traffic, which conceals the regional and network-specific behaviour that determines the actual experience; real user monitoring exists and is rarely joined to configuration decisions, so nobody can say whether a change helped; the two traffic types are served by one product with different pricing; and multi-provider strategies are common and no tooling manages them coherently.

## Problems
- [[niches/edge-cdn-providers/edge-delivery-platforms/build|🔨 Build: Measured in Averages, Experienced in Tails]]
- [[niches/edge-cdn-providers/edge-delivery-platforms/buy|🛒 Buy: Real User Monitoring, Joined to Configuration]]
- [[niches/edge-cdn-providers/edge-delivery-platforms/fix|🔧 Fix: Multi-Provider Strategies Nobody Manages]]
