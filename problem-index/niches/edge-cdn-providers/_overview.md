# Niche Analysis — Edge & CDN Providers

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Cache Configuration | 🔵 High Market Share | $1.6B | Low — rules written once and accumulated | Platform engineering and the CDN configuration owner |
| 2 | Edge Delivery Platforms | 🔵 High Market Share | $3.8B | Very High | Media operations; separately, application platform teams |
| 3 | Edge Compute Placement | 🟠 Low Digitized | $980M | Low — offered by everyone, reasoned about by nobody | Application platform and architecture teams |
| 4 | Constrained Network Delivery | 🟠 Low Digitized | $720M | Very Low — the tooling assumes good connectivity | Companies serving mobile-first and emerging markets |
| 5 | The CDN Support Engineer | 🟣 Underserved Audience | $410M | Low — every ticket begins with the same explanation | Provider support organisations |
| 6 | The Configuration Owner | 🟣 Underserved Audience | $340M | None — nobody can tell whether a change helped | The engineer who owns the rule set |
| 7 | Bot & Abuse Management | ⚡ Highly Automatable | $1.4B | High and perpetually behind | Security and fraud functions |
| 8 | Traffic Vantage Intelligence | ⚡ Highly Automatable | $560M | None — the vantage point is sold as capacity | The providers themselves |

## Why These Niches

Cache configuration is the category's oldest unsolved problem and its most consequential: what to cache, for how long, keyed on what, and when to invalidate determine both performance and origin cost, and they are decided once by hand in rule sets that accumulate for years, while the traffic that would answer them flows past every second.

Edge delivery **failed the filter as one niche**. Large object and media delivery is contested on egress economics, bitrate behaviour and origin offload for media operations teams. Dynamic application delivery is contested on latency for uncacheable content, connection handling and edge-origin behaviour for application platform teams. The economics, the buyers and the failure modes are different. Decomposed below.

The two underdigitised areas are the newest capability and the oldest constraint. Every provider offers edge compute and none can say whether moving a given piece of logic there would improve anything or merely relocate the cost. And delivery to genuinely constrained networks — expensive, intermittent, high-latency — is where the category's value is largest and its tooling assumes conditions that do not hold.

The two underserved constituencies are the support engineer, whose every ticket begins by explaining that the cache miss was caused by the customer's own headers, and the configuration owner, who has no way to know whether any change they made improved anything and therefore dares not remove a line.

The automation niches are bot management, which is an adversarial classification problem run on rules that adversaries adapt to within days, and the traffic vantage point itself, which is unique and is monetised as bandwidth.

## Niches
- [[niches/edge-cdn-providers/cache-configuration/profile|🔵 Cache Configuration]]
- [[niches/edge-cdn-providers/edge-delivery-platforms/profile|🔵 Edge Delivery Platforms]]
  - [[niches/edge-cdn-providers/media-large-object-delivery/profile|🎯 Media & Large Object Delivery]]
  - [[niches/edge-cdn-providers/dynamic-application-delivery/profile|🎯 Dynamic Application Delivery]]
- [[niches/edge-cdn-providers/edge-compute-placement/profile|🟠 Edge Compute Placement]]
- [[niches/edge-cdn-providers/constrained-network-delivery/profile|🟠 Constrained Network Delivery]]
- [[niches/edge-cdn-providers/cdn-support-engineer/profile|🟣 The CDN Support Engineer]]
- [[niches/edge-cdn-providers/the-configuration-owner/profile|🟣 The Configuration Owner]]
- [[niches/edge-cdn-providers/bot-and-abuse-management/profile|⚡ Bot & Abuse Management]]
- [[niches/edge-cdn-providers/traffic-vantage-intelligence/profile|⚡ Traffic Vantage Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Edge Delivery Platforms** is not: it names the product rather than a contest, and the two markets inside it share a network and nothing else. Media and large object delivery is won on cost per delivered byte, origin offload and behaviour under bitrate adaptation, and is bought by media operations teams for whom egress is a dominant cost line. Dynamic application delivery is won on latency for content that cannot be cached, connection and protocol behaviour, and how the edge handles an origin that is slow or failing, and is bought by application platform teams for whom egress is minor and tail latency is everything. Decomposed into two contested sub-niches.

Two candidates were rejected. *Network security and denial-of-service mitigation* was rejected because it has become table stakes across the category — every provider offers it competently and the differentiating contest has moved to bot management, which is covered. *Domain name and certificate management* was rejected as genuinely finished and commoditised.
