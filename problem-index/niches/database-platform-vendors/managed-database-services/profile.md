# Managed Database Services

**Parent Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to run a database well enough that the customer never thinks about it — and that contest is fought on latency in one market and on query cost at scale in another, which is why this niche is not terminal and is decomposed below.

## Profile
**Market Size:** ~$11B US managed database services
**Share of Parent Industry:** ~44% of category revenue
**Digital Adoption:** Very High — the default for new workloads
**Target Buyer:** Application platform teams; separately, data platform teams
**Automation Potential:** High — operability is the product and much of it is still manual

## What Makes This a Distinct Niche
Managed services are the category's largest block and its clearest value proposition: the vendor operates the database so the customer does not need the specialist they cannot hire. The proposition is partly delivered — provisioning, patching, backup and failover are genuinely handled — and the operability gap the industry's own profile names remains, because running a database well means tuning, diagnosing and evolving it, and the managed services mostly do the first three of the easier things.

The filter fails here. "Managed database services" names the delivery model rather than a contest, and there are two markets with almost nothing in common beyond it. One serves application traffic and is judged on tail latency, failover behaviour, connection handling and how quickly a developer can get an environment. The other serves analytical workloads and is judged on the cost of a large query, concurrency under many users, and whether the storage format is open enough to leave. Different buyers, different competitors, different failure modes. The two contested sub-niches below carry the terminal statements.

## Current Tools & Gaps
Managed offerings from the hyperscalers and specialist vendors, serverless and branching products that changed provisioning expectations, and analytical platforms with separated storage and compute. The gaps: the managed boundary stops at the infrastructure, so the customer still owns every decision that requires database knowledge; pricing models differ so much between the two halves that comparison is impossible within a single frame; the fleet-wide knowledge these vendors accumulate is used for their own capacity planning rather than for customer operability; and migration in and out is a project in both directions, which is the actual lock-in regardless of what the marketing says.

## Problems
- [[niches/database-platform-vendors/managed-database-services/build|🔨 Build: Managed Infrastructure, Unmanaged Database]]
- [[niches/database-platform-vendors/managed-database-services/buy|🛒 Buy: Autonomous Operation Research Nobody Has Shipped]]
- [[niches/database-platform-vendors/managed-database-services/fix|🔧 Fix: Migration Is a Project in Both Directions]]
