# Observability Platforms

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to be the place an organisation's telemetry lands and is queried — and that contest is fought twice, for engineering and for security, which is why this niche is not terminal and is decomposed below.

## Profile
**Market Size:** ~$5.4B US observability, monitoring and log analytics platforms
**Share of Parent Industry:** ~45% of category revenue
**Digital Adoption:** Very High — every organisation of size runs at least one
**Target Buyer:** Site reliability and platform engineering; separately, security operations
**Automation Potential:** High, and mostly unexploited in favour of storage and query

## What Makes This a Distinct Niche
This is the category's core market: collect telemetry at extraordinary scale, store it, index it and make it queryable. The engineering is genuinely hard and the products are genuinely good at it. It is also where the category's defining commercial complaint lives, since the bill grows faster than the value and volume-based pricing rewards collection while nobody measures which signals are ever read.

The filter fails here. "Observability platforms" names the product rather than the contest, and the market has long been two markets sharing infrastructure. Engineering observability is bought by SRE and platform teams to understand what their services did, and is won on diagnostic depth and correlation across signals. Security and audit log analytics is bought by a security operations function under compliance-driven retention requirements, and is won on cost at multi-year horizons, detection content and investigation workflow. The vendors that lead each are largely different companies, which is the practical evidence. The two contested sub-niches below carry the terminal statements.

## Current Tools & Gaps
Integrated platforms, open-source stacks, managed metric and log services, and columnar log stores that shifted the cost structure. The gaps: pricing rewards ingestion and nothing measures whether a signal is ever queried, which is the commercial conflict at the heart of the category; the open instrumentation standard decoupled collection from the vendor and the products have not adapted their value proposition to a world where the data is portable; the two buyer types are served by one product with different configurations; and the corpus of how production software fails is the category's unique asset and is used for nothing.

## Problems
- [[niches/observability-vendors/observability-platforms/build|🔨 Build: The Bill Grows Faster Than the Value]]
- [[niches/observability-vendors/observability-platforms/buy|🛒 Buy: Columnar Storage and Open Collection Are Commodity]]
- [[niches/observability-vendors/observability-platforms/fix|🔧 Fix: One Platform, Two Entirely Different Buyers]]
