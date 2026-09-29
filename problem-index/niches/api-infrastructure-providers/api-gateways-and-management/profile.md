# API Gateways & Management

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to be the layer every API call passes through — and that contest is fought twice, for internal traffic and for external consumers, which is why this niche is not terminal and is decomposed below.

## Profile
**Market Size:** ~$1.6B US gateway and API management
**Share of Parent Industry:** ~40% of category revenue
**Digital Adoption:** High — nearly every organisation runs one
**Target Buyer:** Platform engineering internally; API product management externally
**Automation Potential:** High — the position is privileged and mostly used for policy enforcement

## What Makes This a Distinct Niche
The gateway is the most privileged position in the category: every call passes through it, which makes it simultaneously the enforcement point for policy, the source of the only complete record of integration behaviour, and the place any new capability is most cheaply delivered. It is also the most competitive, with the hyperscalers bundling competent gateways into their platforms and a generation of developer-first providers competing on ergonomics.

The filter fails here. "Gateways and management" names the product rather than the contest, and the two contests are different in buyer, competitor and measure. Internal traffic is an operations problem: latency budgets, resilience, observability and how much friction the platform imposes on teams shipping services. External programmes are a product problem: how quickly an outside developer reaches a working integration, how good the documentation and sandbox are, and how the usage is monetised. A vendor strong at one is routinely weak at the other, which is the practical evidence that these are separate markets. The two contested sub-niches below carry the terminal statements.

## Current Tools & Gaps
Gateways from the established management vendors, hyperscaler-bundled offerings, service meshes handling the internal case from a different direction, and developer portal products for the external case. The gaps: the internal and external cases are served by one product with two configurations, which fits neither well; the traffic record is used for policy and percentiles and discarded; policy is expressed per route rather than per contract, so nothing connects a rate limit to what the consumer bought; and the gateway knows more about how the organisation's software actually integrates than any other system and reports almost none of it.

## Problems
- [[niches/api-infrastructure-providers/api-gateways-and-management/build|🔨 Build: The Most Privileged Position and the Least Used]]
- [[niches/api-infrastructure-providers/api-gateways-and-management/buy|🛒 Buy: Proxy Infrastructure Is Commodity and the Layer Above Is Not]]
- [[niches/api-infrastructure-providers/api-gateways-and-management/fix|🔧 Fix: One Product Configured Two Ways]]
