# The CDN Support Engineer

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to tell a customer why their content missed the cache before they open a ticket — and whoever does that takes the support organisation, because that single explanation is most of its volume.

## Profile
**Market Size:** ~$410M US attributable to delivery support operations
**Share of Parent Industry:** ~5% of category revenue
**Digital Adoption:** Low — the same explanation is written by hand, repeatedly
**Target Buyer:** Provider support leadership; the beneficiary is the support engineer and the customer
**Automation Potential:** Very High — the cause of every miss is in the logs

## What Makes This a Distinct Niche
CDN support has an unusually concentrated shape. A very large share of tickets are a customer reporting poor cache performance or origin errors, and a very large share of those are caused by the customer's own configuration: a response header marking content private, a cache key including a varying parameter, an origin returning inconsistent headers, a purge pattern that is too broad. The support engineer establishes this from the logs, writes the explanation, and does it again with a different customer the following day. The analysis is mechanical, the cause is recorded in the request logs the provider already keeps, and the explanation could be delivered before the customer noticed the problem — which would eliminate most of the queue rather than accelerating it.

## Current Tools & Gaps
Log delivery to customers, cache status headers, analytics dashboards, and knowledge base articles. The gaps: the cache status header names the outcome and rarely the reason, so a customer sees a miss and cannot tell why; nothing proactively identifies a customer whose configuration is producing avoidable misses; origin errors are reported as counts rather than diagnosed; the support corpus is never analysed in aggregate, although it is a precise specification of what the product fails to explain; and the customer's own tooling cannot answer the question, which is why they open a ticket.

## Problems
- [[niches/edge-cdn-providers/cdn-support-engineer/build|🔨 Build: It Was Your Own Header]]
- [[niches/edge-cdn-providers/cdn-support-engineer/buy|🛒 Buy: Self-Service Diagnosis From Support Deflection]]
- [[niches/edge-cdn-providers/cdn-support-engineer/fix|🔧 Fix: The Cache Status That Names the Outcome]]
