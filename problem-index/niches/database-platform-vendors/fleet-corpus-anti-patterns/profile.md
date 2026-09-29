# Fleet Corpus & Anti-Patterns

**Parent Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor that gets here is fighting to warn a customer about a failure thousands of other customers have already had — and whoever does that holds a corpus of how databases actually fail that no single organisation can assemble.

## Profile
**Market Size:** ~$740M US, largely latent
**Share of Parent Industry:** ~3% of category revenue
**Digital Adoption:** None — the corpus is used for capacity planning
**Target Buyer:** The managed vendors themselves; secondarily platform teams
**Automation Potential:** Very High — the patterns recur constantly and are mechanically recognisable

## What Makes This a Distinct Niche
Managed database vendors observe query workloads, schemas, access patterns and failures across enormous numbers of production systems. The same anti-patterns recur constantly: the query that will not scale past a data volume, the index that stops being selective, the migration that will lock a large table, the connection pattern that exhausts a pool, the schema design that becomes untenable at a particular size. Every customer discovers each of them independently, usually during an outage, and the vendor has watched thousands of customers discover the same one. The corpus that would let a vendor warn before rather than diagnose after exists in the fleet and is used for capacity planning. This is a distinct opportunity because it is the only asset in the category that a customer cannot obtain by any amount of effort on their own system, and because the patterns are structural rather than content-based, which makes the governance story straightforward.

## Current Tools & Gaps
Documentation and best practice guides, support knowledge bases, and community advice of variable quality. The gaps: the accumulated fleet knowledge is expressed as prose documentation rather than as checks that run against a customer's actual schema and workload; the recurrence rate of each pattern is known to the vendor and published by nobody, so customers cannot prioritise; there is no early warning, so the vendor watches a customer approach a failure they have seen a thousand times; and no vendor has articulated a governance position for structural fleet analysis, so the topic is avoided rather than designed.

## Problems
- [[niches/database-platform-vendors/fleet-corpus-anti-patterns/build|🔨 Build: Watching a Customer Walk Into a Known Failure]]
- [[niches/database-platform-vendors/fleet-corpus-anti-patterns/buy|🛒 Buy: Pattern Mining Over Schemas and Workloads]]
- [[niches/database-platform-vendors/fleet-corpus-anti-patterns/fix|🔧 Fix: Best Practice as Prose Rather Than Checks]]
