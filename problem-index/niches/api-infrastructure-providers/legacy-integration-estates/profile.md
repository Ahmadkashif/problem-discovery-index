# Legacy Integration Estates

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to bring visibility and change safety to the file transfers, message queues and SOAP services that still move most enterprise data — and whoever does that takes the integration estate, because nobody can currently see it at all.

## Profile
**Market Size:** ~$890M US attributable to legacy integration estates
**Share of Parent Industry:** ~22% of category revenue
**Digital Adoption:** Very Low — these integrations predate the category and are invisible to it
**Target Buyer:** Enterprise integration and platform teams
**Automation Potential:** High — the transfers are observable and the schemas are discoverable

## What Makes This a Distinct Niche
Modern API infrastructure serves the traffic that speaks its language. A very large share of enterprise data movement does not: nightly file transfers over secure copy, message queues carrying fixed-format records, SOAP services with specifications that are technically complete and practically unreadable, EDI documents flowing to trading partners, and database-to-database replication set up by someone who left in 2014. These integrations carry payroll, settlement, inventory and claims. They have no gateway, no observability, no inventory, no owner in many cases, and they break at three in the morning with a partial file. The category has largely declared them out of scope, which leaves the highest-consequence integrations in most enterprises as the least visible ones. The contest is bringing the basic properties — inventory, monitoring, change safety, schema knowledge — to traffic that will not be rewritten as REST any time soon.

## Current Tools & Gaps
Managed file transfer products, enterprise service buses, EDI translators, message brokers, and integration platforms that support these protocols alongside modern ones. The gaps: inventory is incomplete everywhere, because these integrations were created individually over decades; monitoring is per-tool rather than per-integration, so an end-to-end flow crossing three systems has no single status; schemas are fixed-format specifications in documents rather than machine-readable contracts; failure is usually detected downstream by someone noticing missing data; and nobody can answer what depends on a given file or queue, which is the same breaking-change problem the modern niche has and worse.

## Problems
- [[niches/api-infrastructure-providers/legacy-integration-estates/build|🔨 Build: The Integrations Nobody Can Enumerate]]
- [[niches/api-infrastructure-providers/legacy-integration-estates/buy|🛒 Buy: Schema Inference and Monitoring, Pointed Backwards]]
- [[niches/api-infrastructure-providers/legacy-integration-estates/fix|🔧 Fix: The Partial File Nobody Noticed]]
