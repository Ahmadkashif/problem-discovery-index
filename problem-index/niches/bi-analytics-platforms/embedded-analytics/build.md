# Nine Seconds Is a Defect, Not an Inconvenience

**Niche:** [[niches/bi-analytics-platforms/embedded-analytics/profile|Embedded Analytics]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Internal BI tolerates slow queries and customer-facing analytics does not, and every software company embedding analytics rediscovers this and builds its own pre-aggregation layer.
**Tags:** #dynamic-programming #convex-optimization #time-series-forecasting #gradient-boosting #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor in embedded analytics is fighting to serve thousands of a software vendor's customers their own data, fast, inside a product that is not theirs — and whoever holds latency and isolation at that scale takes the deal, because the buyer is an engineering team that will otherwise build it.

## The Problem
A software company embeds an analytics page in its product. In development, with one tenant and a small dataset, it is fast. In production, with four thousand tenants of wildly different sizes, the largest tenant's dashboard takes eleven seconds, the page is the most complained-about part of the product, and the warehouse bill has become a line item somebody asks about. The engineering team responds by building a pre-aggregation layer, a caching strategy and a materialisation schedule — three months of work that every other company embedding analytics has also done, privately, to a similar design.

## Why Nobody Has Built This
BI vendors built for internal use, where a slow dashboard is an irritation and the user count is bounded, and their embedded offerings are the same engine with an authentication layer. The workload is genuinely different: highly repetitive queries across a long tail of tenants of very unequal size, with strict latency requirements and a cost per query that lands on the host's margin. Solving it properly means automatic materialisation — deciding what to pre-compute, for which tenants, at what freshness — which is a real optimisation problem rather than a configuration screen, and the vendors have offered the configuration screen.

## What to Build
Automatic materialisation for multi-tenant analytical workloads. Learn the query pattern per tenant from actual traffic, which is highly repetitive in embedded contexts and therefore unusually predictable. Decide what to materialise as an optimisation over the cost of maintaining an aggregate against the latency and compute it saves, per tenant and per query shape, rather than uniformly — because uniform materialisation over-serves the long tail of small tenants and under-serves the few large ones, which is exactly the mistake hand-built layers make. Schedule refresh against actual access patterns and the host's freshness requirement, which differs by dashboard and is currently set globally. Predict which tenants are approaching a latency problem before they reach it, from their growth in data volume and query rate, so the host learns about it before the customer does. And report the cost per tenant, which the host needs for its own pricing and which no embedded offering exposes, leaving software companies to price a product whose delivery cost they cannot see.

## Target Customer
Product and engineering leadership at software companies embedding analytics, embedded analytics vendors, and the warehouse vendors whose consumption this workload drives.

## Impact If Built
Every software company embedding analytics builds the same pre-aggregation layer badly, and the workload is unusually predictable, which makes automatic materialisation tractable in a way it is not for exploratory internal BI. Per-tenant cost visibility is the second half and is what the host actually needs to run the business.
