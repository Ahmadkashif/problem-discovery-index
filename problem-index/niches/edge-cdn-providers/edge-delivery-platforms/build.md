# Measured in Averages, Experienced in Tails

**Niche:** [[niches/edge-cdn-providers/edge-delivery-platforms/profile|Edge Delivery Platforms]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Delivery performance is reported as global averages, and the experience that matters is a user on a congested mobile network in a region where the nearest node is four hundred miles away.
**Tags:** #descriptive-statistics #k-means-clustering #time-series-forecasting #change-point-detection #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to be the network a customer's traffic flows through — and that contest is fought on cost per byte in one market and on latency for uncacheable content in another, which is why this niche is not terminal and is decomposed below.

## The Problem
A provider's dashboard shows median time to first byte at a healthy figure and a high availability number. In one market, users on a particular mobile network experience several times that latency because of a peering arrangement, and the provider's own measurement does not separate them. The customer's support queue contains complaints from that market and nobody has connected the two, because the complaints say the site is slow and the dashboard says the site is fast. Both are accurate descriptions of different populations.

## Why Nobody Has Built This
Delivery metrics were built around the network's own health — node availability, cache hit rate, bandwidth — which are the provider's operational concerns and are aggregated globally because that is how a network is operated. The user's experience depends on the path from the node to them, which the provider does not control and has therefore not reported on. Real user monitoring exists in the category and is sold as an adjacent product rather than joined to the delivery data. And a decomposed view would expose the regions and networks where the provider performs worst, which is not a natural thing to volunteer.

## What to Build
The shared layer both sub-niches need: performance reported as the user experiences it. Join real user measurements to delivery data so that each request's server-side record has a client-side outcome, which is the foundational join and is currently absent even where both datasets exist. Decompose by geography, network, device class and connection type rather than reporting global aggregates, since the variation along those dimensions is far larger than the variation over time and is where every actionable finding is. Report percentiles rather than medians, because the tail is what generates complaints and drives abandonment. Attribute the experience to its components — resolution, connection, first byte, transfer — so a customer can tell whether the problem is the network, the origin or their own page. Detect regional and network-specific degradation as an event, since a peering change affecting one market currently surfaces as a support ticket rather than as an alert. And make the measurement comparable across providers, which is the thing customers most want and no provider offers.

## Target Customer
Media operations and application platform teams, the providers themselves for whom this is a differentiator in a commoditised layer, and the real user monitoring vendors whose data this needs.

## Impact If Built
Delivery is experienced in the tail of a distribution the providers report the middle of, which is why customer complaints and provider dashboards routinely disagree. The real user join is the foundational piece and enables the specific contests in both sub-niches below.
