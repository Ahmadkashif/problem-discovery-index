# A Cache Network for Traffic That Cannot Be Cached

**Niche:** [[niches/edge-cdn-providers/dynamic-application-delivery/profile|Dynamic Application Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A growing share of traffic is personalised and uncacheable, which removes the category's original value proposition, and the benefit of routing it through the network is asserted rather than measured.
**Tags:** #descriptive-statistics #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #time-series-forecasting #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to reduce tail latency for content that cannot be cached at all — and whoever does that takes the application platform account, because the bytes are trivial and the milliseconds are the entire product.

## The Problem
An application's traffic is almost entirely authenticated and personalised. It flows through a delivery network whose dashboard reports a cache hit rate near zero, which is correct and expected. The team cannot say whether the network is helping: the connection termination and backbone routing may be saving substantial time, or may be adding a hop for no benefit, and nothing measures it. At renewal the question is asked and answered with a general belief. Meanwhile the semi-cacheable portion — responses that are identical for a minute, or identical for all users in a segment, or safe to serve slightly stale — is treated as uncacheable because the configuration is binary, and it is frequently a substantial share.

## Why Nobody Has Built This
The category's measurement apparatus was built around cache hit rate, which is meaningless for this traffic and is still the headline metric, so the value for dynamic traffic has no metric at all. Establishing the benefit requires comparing against not using the network, which the provider has no reason to measure and the customer cannot easily arrange. And the semi-cacheable middle ground requires understanding which responses are safe to reuse and for how long, which is the cache configuration problem in its hardest form and is left entirely to the customer's headers.

## What to Build
Measure the benefit and expand what counts as cacheable. Measure the network's contribution directly by comparing matched traffic routed through and around it, which is an experiment the edge can run on a fraction of requests and which no provider offers — and which is the only honest answer to the renewal question. Decompose the contribution into its components: connection establishment saved, backbone path improvement, connection reuse to origin, protocol upgrade, so the customer knows which parts are working. Expand the semi-cacheable set deliberately: identify responses that are identical across users, identical within a short window, or acceptable slightly stale, from the traffic rather than from headers — which is the cache configuration analysis applied to the traffic everybody assumes is uncacheable and regularly finds a meaningful share. Configure stale-while-revalidate and request collapsing, which apply to far more traffic than teams assume and are among the most effective available protections against an origin under load. And report the origin load avoided, since that is the financial benefit for this traffic type and is currently invisible.

## Target Customer
Application platform teams whose traffic is mostly uncacheable, and the providers competing for it, for whom demonstrating value on dynamic traffic is the growth question.

## Impact If Built
The category's headline metric is meaningless for a growing share of traffic and nothing has replaced it, which leaves the value asserted. A routed-versus-not experiment answers the renewal question properly, and the semi-cacheable analysis regularly finds cacheable traffic where everybody assumed there was none.
