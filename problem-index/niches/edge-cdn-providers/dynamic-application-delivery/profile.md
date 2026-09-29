# Dynamic Application Delivery

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to reduce tail latency for content that cannot be cached at all — and whoever does that takes the application platform account, because the bytes are trivial and the milliseconds are the entire product.

## Profile
**Market Size:** ~$1.6B US dynamic and application delivery
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** High and rising as more traffic becomes uncacheable
**Target Buyer:** Application platform engineering
**Automation Potential:** High — routing, connection reuse and origin behaviour are all optimisable

## What Makes This a Distinct Niche
A growing share of traffic is personalised, authenticated or transactional and cannot be cached in any traditional sense, which removes the category's original value proposition entirely. What remains is everything else the network can do: terminate the connection close to the user so the handshake is fast, hold a warm connection to the origin so the request does not pay a new one, choose a path that is better than the public internet's default, absorb the impact of an origin that is slow or failing, and apply the protocol improvements the client and origin have not adopted. The buyer is an application platform team for whom egress is a rounding error and the ninety-ninth percentile response time is what they are judged on, and the contest is entirely about latency and resilience for traffic that will never hit a cache.

## Current Tools & Gaps
Modern transport protocols, connection reuse to origin, private backbone routing, origin shielding, and edge compute for request manipulation. The gaps: the benefit for uncacheable traffic is asserted rather than measured, so customers cannot tell whether the network is helping; origin failure behaviour is configured as timeouts and retries whose interaction under load is nobody's model and which can amplify an origin problem into an outage; stale-while-revalidate and similar semi-caching strategies are available and almost never configured, although they apply to far more traffic than teams assume; and the edge's ability to shed load or degrade gracefully is a capability nobody has packaged as a product.

## Problems
- [[niches/edge-cdn-providers/dynamic-application-delivery/build|🔨 Build: A Cache Network for Traffic That Cannot Be Cached]]
- [[niches/edge-cdn-providers/dynamic-application-delivery/buy|🛒 Buy: Load Shedding and Graceful Degradation at the Edge]]
- [[niches/edge-cdn-providers/dynamic-application-delivery/fix|🔧 Fix: Retries That Amplify an Origin Problem]]
