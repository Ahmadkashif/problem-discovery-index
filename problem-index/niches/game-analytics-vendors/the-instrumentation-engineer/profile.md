# The Instrumentation Engineer

**Parent Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Category:** 🟣 Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to let one engineer keep data consistent across six live client versions all sending slightly different schemas — and whoever supports that person takes the account.

## Profile
**Market Size:** ~$100M US
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** Low — one person
**Target Buyer:** Data platform leadership
**Automation Potential:** High — version reconciliation and validation

## What Makes This a Distinct Niche
Six client versions are live, each sending a slightly different event schema, and one engineer is responsible for the data being consistent across all of them. They cannot update old clients, cannot force players to upgrade, and must make years of accumulated schema variation produce numbers that agree. When a metric looks wrong, they are the person who finds out why. The role is a single point of failure for the entire analytics stack and is staffed by one person with no tooling.

## Current Tools & Gaps
A pipeline, a transformation layer they maintain, and knowledge of which version does what. The gaps: no version-aware schema mapping; no automated detection of version-specific breakage; no test coverage over transformations; no documentation of the accumulated special cases; and no handover if they leave.

## Problems
- [[niches/game-analytics-vendors/the-instrumentation-engineer/build|🔨 Build: Six Schemas, One Truth]]
- [[niches/game-analytics-vendors/the-instrumentation-engineer/buy|🛒 Buy: Version Compatibility From API Platforms]]
- [[niches/game-analytics-vendors/the-instrumentation-engineer/fix|🔧 Fix: The Special Case Only One Person Knows]]
