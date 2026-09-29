# Golden Path Drift

**Parent Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to make a platform improvement reach the services that already exist — and whoever does that takes the platform, because a golden path that only applies at creation improves nothing after the first month.

## Profile
**Market Size:** ~$260M US attributable to template management and estate conformance
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** None — generation is instantaneous and divergence is permanent
**Target Buyer:** Platform engineering
**Automation Potential:** Very High — divergence is computable and most updates are mechanical

## What Makes This a Distinct Niche
Scaffolding tools generate a service from a template in seconds, and from that moment the service and the template diverge forever, so a platform improvement never reaches anything that already exists. The consequence compounds in a specific way: the platform team improves the template, the improvement applies to services created after that date, and the estate becomes a set of strata — services created in each era, carrying that era's practices, with no mechanism to update. A security fix in the template reaches nothing. A new standard reaches nothing. The platform team's leverage is therefore limited to new services, which is a small fraction of the estate, and the older services accumulate exactly the problems the platform was created to prevent. This is the same one-way generation problem as templates in work management and clause libraries in contract lifecycle, with higher stakes because the divergence includes security posture.

## Current Tools & Gaps
Scaffolding and templating tools, maturity scorecards that measure conformance without fixing it, and occasional migration campaigns. The gaps: there is no update mechanism, so a template change is a fork point; divergence is not measured, so nobody knows how far the estate has drifted; scorecards identify non-conformance and leave the remediation to each team, which is the same asymmetry that makes them resented; automated remediation exists in adjacent tooling and is not applied here; and the strata are invisible, so a platform team cannot see that services from a particular era share a particular deficiency.

## Problems
- [[niches/internal-developer-platforms/golden-path-drift/build|🔨 Build: Generated Once, Divergent Forever]]
- [[niches/internal-developer-platforms/golden-path-drift/buy|🛒 Buy: Automated Migration From Dependency Tooling]]
- [[niches/internal-developer-platforms/golden-path-drift/fix|🔧 Fix: Scorecards That Mark Teams Down and Fix Nothing]]
