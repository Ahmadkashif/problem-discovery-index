# Traffic-Derived Contract Intelligence

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor that gets here is fighting to turn observed traffic into the API's real contract — what is actually used, actually returned and actually relied upon — and whoever does that holds the accurate specification while everyone else holds the intended one.

## Profile
**Market Size:** ~$430M US, largely latent
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** None — gateways compute percentiles and discard the rest
**Target Buyer:** The infrastructure vendors themselves; secondarily platform and API product teams
**Automation Potential:** Very High — the complete behavioural record passes through the gateway

## What Makes This a Distinct Niche
An API gateway sees every request and response between systems, which constitutes a complete behavioural specification of how software actually integrates — more accurate than any published document, because it records what consumers do rather than what they were told to do. That traffic answers the questions the whole category struggles with: what the real contract is, which fields are genuinely used, what values actually occur, where the specification and the implementation diverge, and what an accurate description of this API would say. Gateways compute rate limits and latency percentiles from it and discard the rest. Writing a specification from traffic rather than from intent is a distinct capability with its own buyer and its own products, and it is the foundation the deprecation, documentation and security niches all depend on.

## Current Tools & Gaps
Specification tooling assuming a hand-authored document, specification linting and diffing, contract testing frameworks, and gateway analytics reporting volumes and latencies. The gaps: specifications are authored and drift immediately, and nothing reconciles them against behaviour; field-level usage is not computed, though every question about change depends on it; value distributions and actual enum ranges are unknown, so a specification says string where the reality is one of six values; undocumented behaviour — parameters that work, fields that appear conditionally — is invisible; and the specification is treated as the source of truth when the implementation is.

## Problems
- [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/build|🔨 Build: The Specification Says Intent and the Traffic Says Reality]]
- [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/buy|🛒 Buy: Schema Inference and Specification Mining]]
- [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/fix|🔧 Fix: The Documented Field Nobody Sends]]
