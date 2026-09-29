# Load Shedding and Graceful Degradation at the Edge

**Niche:** [[niches/edge-cdn-providers/dynamic-application-delivery/profile|Dynamic Application Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Load shedding, admission control and circuit breaking are established resilience patterns, and the edge — which is the ideal place to apply all three — mostly forwards everything and hopes.
**Tags:** #markov-chains #optimization-fundamentals #time-series-forecasting #logistic-regression #confidence-intervals #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to reduce tail latency for content that cannot be cached at all — and whoever does that takes the application platform account, because the bytes are trivial and the milliseconds are the entire product.

## The Problem
When a system is overloaded, serving a subset of requests well beats serving all of them badly — which is admission control, and the resilience literature has established it thoroughly along with load shedding and circuit breaking. The edge sits in front of every request, sees the origin's health directly, and is the natural place to apply all of it. In practice it forwards everything, and the origin fails under a load the edge could have shaped.

## What Already Exists
Admission control and load shedding research; circuit breaker patterns with mature implementations; rate limiting at every edge provider; queueing theory for the capacity reasoning; and the graceful degradation practice from large-scale operations with published descriptions. The edge providers offer the primitives and not the policy.

## The Customization Gap
The adaptation is to a network in front of an origin it does not control. It requires: (1) origin health inference from observable behaviour — response times, error rates, connection acceptance — since the edge cannot see inside the origin and must decide from symptoms, which is the central constraint; (2) shedding by request value rather than uniformly, because dropping a checkout request and a background poll are not equivalent and uniform rate limiting treats them identically — this is the difference between graceful degradation and an outage; (3) a degraded response rather than a rejection where possible, serving stale content, a reduced version or a queued acknowledgement, which is what the customer's users actually need and requires the edge to hold something to serve; (4) coordination across nodes, since each edge location deciding independently can collectively overwhelm an origin that each individually thought it was protecting; and (5) fast and safe recovery, because the classic failure is a circuit that opens under load and closes into a thundering herd.

## Target Customer
Edge and CDN providers, application platform teams, and the resilience and traffic management tooling vendors.

## Impact If Solved
The edge is the ideal place to apply established resilience patterns and mostly forwards everything, which leaves the origin to fail under a load that could have been shaped. Value-based shedding and degraded responses are the two adaptations that turn protection into graceful degradation rather than into a different outage.
