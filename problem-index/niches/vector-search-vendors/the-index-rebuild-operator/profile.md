# The Index Rebuild Operator

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to make an index rebuild something that happens automatically, online and on evidence, rather than something a person schedules and watches — and whoever does that takes the account, because the rebuild is the category's worst operational experience.

## Profile
**Market Size:** ~$130M US in operations cost and over-provisioned capacity
**Share of Parent Industry:** ~11% of category revenue equivalent
**Digital Adoption:** None — scheduled on a hunch, watched by a person
**Target Buyer:** Site reliability and platform operations teams
**Automation Potential:** Very High — the decision and the execution are both automatable

## What Makes This a Distinct Niche
Rebuilding an index consumes roughly double the memory of the index itself, runs for hours, and is scheduled into a maintenance window by a reliability engineer who then watches it. The reason for the rebuild is usually a hunch — it has been a while, search feels slower, a lot of documents were deleted. There is no measurement telling them whether it was needed, no way to know part-way through whether it will finish, and no partial credit if it fails. The double-memory requirement means the cluster is permanently provisioned for an operation that runs monthly, which is a standing cost nobody has named. This is a distinct operational constituency from the solutions architects and is served by nothing.

## Current Tools & Gaps
Rebuild commands, maintenance windows, replica-swap procedures assembled by the customer, and monitoring that shows the job is running. The gaps: no evidence-based trigger; no progress or completion estimate; no resumability, so a failure at hour four discards four hours; no online rebuild, so capacity must be doubled; and no measurement afterwards showing what the rebuild achieved.

## Problems
- [[niches/vector-search-vendors/the-index-rebuild-operator/build|🔨 Build: Double the Memory and a Maintenance Window]]
- [[niches/vector-search-vendors/the-index-rebuild-operator/buy|🛒 Buy: Online Schema Change and Zero-Downtime Migration]]
- [[niches/vector-search-vendors/the-index-rebuild-operator/fix|🔧 Fix: No Way to Know Whether It Was Needed]]
