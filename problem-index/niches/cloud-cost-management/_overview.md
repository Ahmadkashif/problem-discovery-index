# Niche Analysis — Cloud Cost Management

**Parent Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Cost Attribution & Ownership | 🔵 High Market Share | $720M | Low — the mapping depends on tags nobody maintains | Platform engineering and FinOps |
| 2 | Cloud Financial Platforms | 🔵 High Market Share | $1.2B | High and converged | Finance and engineering, separately |
| 3 | Kubernetes & Shared Infrastructure | 🟠 Low Digitized | $460M | Low — shared capacity defeats resource-level billing | Platform teams running shared clusters |
| 4 | Hybrid & Non-Hyperscaler Estates | 🟠 Low Digitized | $380M | Very Low — the tooling stops at the cloud bill | Enterprises with on-premise, colocation and licence spend |
| 5 | The FinOps Practitioner | 🟣 Underserved Audience | $190M | Low — the week is spent chasing tags | FinOps leadership; the beneficiary is the practitioner |
| 6 | The Engineer Told to Cut | 🟣 Underserved Audience | $160M | None — the engineer sees no cost until asked to reduce it | Engineering teams; nominally platform leadership |
| 7 | Commitment Purchasing | ⚡ Highly Automatable | $540M | Medium — recommendations exist and look backwards | Finance and cloud economics functions |
| 8 | Cross-Organisation Benchmarking | ⚡ Highly Automatable | $290M | None — the corpus is unused | The vendors themselves |

## Why These Niches

The category's defining failure is stated in its own profile: the tools tell finance what was spent and cannot tell engineering what to do. That gap is attribution — the bill arrives organised by resource and the decisions are organised by team, product, customer and feature — and bridging it depends on tagging discipline that does not exist anywhere. Inferring ownership rather than demanding it is the largest contested surface in the category.

Cloud financial platforms **failed the filter as one niche**. The finance-facing contest is allocation, chargeback, forecasting and variance explanation, bought by a finance function that needs the numbers to reconcile. The engineering-facing contest is credible, safe, specific recommendations that an engineer will act on, bought by platform engineering and lost permanently after two bad suggestions. The category has converged because it has been selling one product to both and satisfying the first. Decomposed below.

The two underdigitised areas are shared infrastructure and everything that is not a hyperscaler bill. Kubernetes attribution is a genuinely hard problem where resource-level billing breaks down entirely. And the on-premise, colocation, licence and software spend that sits alongside the cloud bill is outside every tool, which means nobody can answer what a workload costs in total.

The two underserved constituencies are the FinOps practitioner, whose week is spent chasing tags and explaining variances they cannot investigate, and the engineer who experiences cost as an intermittent instruction to cut something with no way to know what is safe.

The automation niches are the category's two standing omissions: commitment purchasing, which is a multi-year bet recommended from the recent past, and the cross-organisational corpus, which is the one thing these vendors hold that no customer can assemble.

## Niches
- [[niches/cloud-cost-management/cost-attribution-and-ownership/profile|🔵 Cost Attribution & Ownership]]
- [[niches/cloud-cost-management/cloud-financial-platforms/profile|🔵 Cloud Financial Platforms]]
  - [[niches/cloud-cost-management/finance-facing-chargeback/profile|🎯 Finance-Facing Allocation & Chargeback]]
  - [[niches/cloud-cost-management/engineering-facing-optimisation/profile|🎯 Engineering-Facing Optimisation]]
- [[niches/cloud-cost-management/kubernetes-shared-infrastructure/profile|🟠 Kubernetes & Shared Infrastructure]]
- [[niches/cloud-cost-management/hybrid-and-non-hyperscaler/profile|🟠 Hybrid & Non-Hyperscaler Estates]]
- [[niches/cloud-cost-management/the-finops-practitioner/profile|🟣 The FinOps Practitioner]]
- [[niches/cloud-cost-management/the-engineer-told-to-cut/profile|🟣 The Engineer Told to Cut]]
- [[niches/cloud-cost-management/commitment-purchasing/profile|⚡ Commitment Purchasing]]
- [[niches/cloud-cost-management/cross-organisation-benchmarking/profile|⚡ Cross-Organisation Benchmarking]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Cloud Financial Platforms** is not: it names the product category rather than a contest, and the category's own convergence is the evidence — every product ingests the same billing data and renders it similarly, because they are all satisfying the finance buyer and none has won the engineering one. Finance-facing allocation is won on accuracy, reconcilability and forecast quality, and is bought by a function that needs the numbers to add up. Engineering-facing optimisation is won on whether a recommendation is specific, safe and trusted enough to be acted on, and is lost permanently the second time a tool proposes downsizing a standby that exists to be idle. Different buyers, different failure modes, different definitions of winning. Decomposed into two contested sub-niches.

Two candidates were rejected. *Multi-cloud normalisation* was rejected because it is a feature every vendor has and nobody wins on; the underlying contest is attribution, which is covered. *Sustainability and carbon reporting* was rejected as adjacent rather than contested — it is currently a reporting obligation served by the same allocation machinery rather than a separate capability anyone is competing to build.
