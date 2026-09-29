# The Degradation the Provider Saw First

**Niche:** [[niches/edge-cdn-providers/traffic-vantage-intelligence/profile|Traffic Vantage Intelligence]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A transit problem degrades a customer's users in one region, the provider's network observes it immediately, and the customer finds out from their own support queue two hours later.
**Tags:** #change-point-detection #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #data-integration
**Contested on:** Every serious competitor that gets here is fighting to turn a view of a substantial fraction of internet traffic into decisions rather than capacity — and whoever does that holds a vantage point nobody outside the category can obtain.

## The Problem
A network operator's transit arrangement changes and users on that network in one region begin experiencing much higher latency to the provider's nodes. The provider's telemetry shows it within minutes: a clear shift in performance for an identifiable population, visible across many customers simultaneously. Nothing is communicated. Two hours later the customer's support queue fills with complaints from that region, their engineers investigate their own application, find nothing, and eventually open a ticket with the provider — who then confirms what their monitoring showed before the first complaint arrived.

## Why It's Still Broken
Provider network telemetry is operational, watched by a network operations team, and oriented to the provider's own infrastructure rather than to customer impact. Reporting a degradation that originates outside the provider's network is not part of the operational remit, and there is a mild disincentive to volunteer performance information at all. The customer attribution — which customers' users are on the affected network in the affected region — requires a join between network observation and customer traffic that nobody has built. And the status page convention is to report the provider's own incidents, not the internet's.

## What a Fix Looks Like
Tell the customer what you can see. Detect performance shifts by network and region continuously using change-point methods over the provider's own measurements, which is straightforward over data already collected and is the detection half. Attribute to affected customers by joining the affected population to each customer's traffic, which is the piece that turns an operational observation into a notification somebody can act on. Notify proactively with the specific population, the observed magnitude and the provider's assessment of the cause, including when the cause is the provider's own network — because a provider that reports only external causes will be recognised as doing so. Distinguish clearly between a provider problem, an internet problem and a customer problem in the notification, since the customer's next action depends entirely on which it is. Offer the mitigation where one exists, such as steering affected traffic to a different path or provider. And measure the lead time — how long before the first customer complaint the provider knew — which is the metric this whole capability should be judged on and which would currently be embarrassing.

## Who Feels the Pain
Customers investigating their own applications during somebody else's network incident; end users in affected regions; and providers whose customers experience degradations their own monitoring saw first.

## Impact If Fixed
The detection is straightforward over telemetry already collected and the customer attribution is a join, which makes proactive notification an integration rather than a capability. The lead-time metric is the honest measure of the whole thing and is currently unmeasured because it has never been claimed.
