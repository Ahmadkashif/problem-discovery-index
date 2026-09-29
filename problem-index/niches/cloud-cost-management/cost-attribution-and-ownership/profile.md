# Cost Attribution & Ownership

**Parent Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to get a cost in front of the person who can change it, without depending on tags nobody maintains — and whoever does that takes the account, because the tagging approach has failed everywhere it has been tried.

## Profile
**Market Size:** ~$720M US attributable to allocation, tagging and ownership resolution
**Share of Parent Industry:** ~24% of category revenue
**Digital Adoption:** Low — every organisation has a tagging policy and none has tagging discipline
**Target Buyer:** Platform engineering and FinOps functions
**Automation Potential:** Very High — ownership is inferable from evidence nobody uses

## What Makes This a Distinct Niche
The bill arrives organised by service and resource. The decisions that would change it are organised by team, product, customer and feature. Bridging the two is the whole problem, and the category's answer has been tagging: define a policy, ask engineering to apply tags, enforce with a checker, report on coverage. This has failed at essentially every organisation that has tried it, for reasons that are structural rather than cultural — resources are created by automation that predates the policy, by managed services that do not support the tags, by people who have left, and by a hundred paths nobody controls. The consequence is that cost reporting reaches finance, where a partially-allocated bill is still usable, and never reaches the engineer who could change it, where it is not. The contest is inferring ownership rather than demanding it, and the evidence to do so — deployment records, code repositories, access patterns, naming conventions, network relationships — exists and is unused.

## Current Tools & Gaps
Tagging policies and enforcement tools, allocation rules, cost categories, and hierarchical account structures. The gaps: unallocated spend is typically a large fraction and is treated as a tagging compliance problem rather than an inference problem; shared and overhead costs are allocated by a proportional rule that nobody believes, so the numbers are disputed; the mapping from resource to product or feature — which is what the business actually wants — is another layer beyond team and is attempted almost nowhere; and ownership goes stale as teams reorganise, with no mechanism to notice.

## Problems
- [[niches/cloud-cost-management/cost-attribution-and-ownership/build|🔨 Build: Tagging Discipline That Does Not Exist]]
- [[niches/cloud-cost-management/cost-attribution-and-ownership/buy|🛒 Buy: Entity Resolution Applied to Infrastructure]]
- [[niches/cloud-cost-management/cost-attribution-and-ownership/fix|🔧 Fix: The Shared Cost Allocation Nobody Believes]]
