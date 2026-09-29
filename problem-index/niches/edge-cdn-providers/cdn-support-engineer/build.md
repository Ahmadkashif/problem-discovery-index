# It Was Your Own Header

**Niche:** [[niches/edge-cdn-providers/cdn-support-engineer/profile|The CDN Support Engineer]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** CDN support engineers spend every ticket explaining that a cache miss was caused by the customer's own response headers, and the analysis could be delivered before the customer opened the ticket.
**Tags:** #descriptive-statistics #k-means-clustering #logistic-regression #bert #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to tell a customer why their content missed the cache before they open a ticket — and whoever does that takes the support organisation, because that single explanation is most of its volume.

## The Problem
A ticket says the CDN is not caching. The support engineer pulls the logs, sees that the origin is returning a header marking every response private, confirms it in two minutes, and writes an explanation. The customer's framework added that header by default and nobody chose it. The same ticket arrives from a different customer on Thursday with a different framework and the same default. Over a year this pattern is a substantial share of the support organisation's volume, and every instance was visible in the provider's own logs from the day the customer onboarded.

## Why Nobody Has Built This
Support is reactive by design and the provider's product surface is a configuration interface and a dashboard, neither of which is oriented to telling a customer what is wrong. Identifying the cause requires joining the request logs to the response headers and the configuration, which the provider has and has not packaged as a diagnosis. There is also a boundary instinct: the cause is the customer's configuration, which makes it the customer's problem, and the provider's obligation is understood to end at correctly obeying the headers it receives. That is technically right and is why the largest improvement available in the product goes unbuilt.

## What to Build
Diagnose proactively and deliver the answer before the question. Classify every cache miss by cause automatically from the logs — origin directive, key mismatch, expiry, size, purge, error — which is mechanical and produces the distribution that currently requires a support engineer per instance. Detect the patterns that indicate a misconfiguration rather than a choice: a property with a very low hit rate on obviously static content, a cache key whose cardinality is close to the request count, an origin returning inconsistent headers for the same resource — each of which is recognisable and is the subject of most tickets. Alert the customer with the specific cause and the specific remedy, before they notice, which is the whole product and turns a ticket into a notification. Include this in onboarding, since a new customer's configuration is at its worst on day one and is when the explanation is most valuable. Cluster across customers, since a framework default affecting many customers is one finding and is currently diagnosed independently every time. And feed the support corpus back into the product continuously, because the queue is a precise specification of what the product fails to explain.

## Target Customer
Delivery provider support organisations, the solutions engineering teams who currently deliver this analysis to large accounts by hand, and the customers who would rather not open a ticket.

## Impact If Built
A small number of causes account for most of the support volume and each is mechanically detectable in the provider's own logs. Proactive notification eliminates tickets rather than accelerating them, which is the difference between a support improvement and a product one.
