# API Infrastructure Providers

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$4B US API management, gateways and developer platform infrastructure
**Tech Maturity:** High and fragmenting — Kong, Apigee, MuleSoft, AWS API Gateway and a newer generation of developer-first providers handle routing, authentication, rate limiting and analytics competently. The hard problems have moved to the edges: knowing what depends on an API before changing it, and pricing usage in a way that neither party regrets.
**Workforce:** Platform engineers, API product managers, developer experience and documentation teams, integration support engineers, solutions architects

## Key Pain Themes
The central unsolved problem is change. An API is a contract with consumers the provider often cannot enumerate, so every breaking change is a negotiation with unknown counterparties and the safe response is to never break anything — which is how organisations accumulate versions they cannot retire and endpoints nobody can explain. Around that sit two persistent burdens: documentation that drifts from behaviour the moment it is written, since the specification describes intent and the implementation describes reality; and usage-based pricing, where metering is straightforward and choosing the unit, the tier and the overage behaviour is a commercial question every provider guesses at and revisits painfully. Support engineers spend their days determining whether a failure is the provider's or the consumer's, and API product managers deprecate endpoints without knowing who is still calling them.

## Current Tech Landscape
Kong and Apigee lead gateway and management; MuleSoft anchors enterprise integration; the hyperscalers bundle competent gateways with their platforms. OpenAPI is the dominant specification standard and is widely honoured in outline and violated in detail. GraphQL solved over-fetching and introduced its own operational difficulties. Developer portals and interactive documentation are standard. Observability for APIs overlaps heavily with the general observability category. Usage metering and billing has become a distinct product concern as consumption pricing spread.

## Problems
- [[problems/api-infrastructure-providers/high-impact|🔴 High Impact: Knowing What Depends on an API]]
- [[problems/api-infrastructure-providers/low-impact-1|🟡 Low Impact: Documentation Drift from Behaviour]]
- [[problems/api-infrastructure-providers/low-impact-2|🟡 Low Impact: Usage Metering and Pricing Design]]
- [[problems/api-infrastructure-providers/worker-life-1|🟢 Worker Life: Integration Support and the Blame Boundary]]
- [[problems/api-infrastructure-providers/worker-life-2|🟢 Worker Life: API Product Manager Deprecating Blind]]
- [[problems/api-infrastructure-providers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/api-infrastructure-providers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
An API gateway sees every request and response flowing between systems, which is a complete behavioural specification of how software actually integrates — far more accurate than any published document, since it records what consumers do rather than what they were told to do. That traffic answers every question the category struggles with: what fields are actually used, which consumers would break, what the real contract is. Gateways compute rate limits and latency percentiles from it and discard the rest.
