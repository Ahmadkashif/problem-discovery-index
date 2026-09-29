# Niche Analysis — Internal Developer Platforms

**Parent Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Platform as Product | 🔵 High Market Share | $520M | None — the category error is universal | Platform engineering leadership |
| 2 | Platform Tooling Market | 🔵 High Market Share | $780M | Medium — most platforms are built rather than bought | Platform teams choosing to build or buy |
| 3 | Service Catalogue Accuracy | 🟠 Low Digitized | $340M | Low — populated by asking and stale immediately | Platform and architecture functions |
| 4 | Regulated & Constrained Platforms | 🟠 Low Digitized | $290M | Very Low — the tooling assumes a permissive environment | Platform teams in regulated and air-gapped estates |
| 5 | The Platform Engineer | 🟣 Underserved Audience | $210M | None — the support channel has no metrics | Platform leadership; the beneficiary is the engineer |
| 6 | The Application Developer | 🟣 Underserved Audience | $180M | None — boundaries are discovered by hitting them | Every developer using the platform |
| 7 | Golden Path Drift | ⚡ Highly Automatable | $260M | None — generated once and divergent thereafter | Platform engineering |
| 8 | Platform Usage Telemetry | ⚡ Highly Automatable | $230M | None — the signals are available and uncollected | Platform teams themselves |

## Why These Niches

The category's defining failure is stated plainly in its own analysis: an internal platform team is a product team whose users sit in the same building and whose usage it does not measure. It builds paved paths, developers route around them for reasons the team never learns, adoption stalls at the teams who were consulted, and nobody measures where the abandonment happens — because the team thinks it is building infrastructure. That single category error explains most of the failures in the space.

The tooling market **failed the filter as one niche**. The portal and catalogue contest is about whether an organisation should operate a portal at all and who runs it, fought between the open framework everyone finds expensive to operate and the managed alternatives, and decided by a platform team weighing operational cost. The provisioning and abstraction contest is about hiding infrastructure complexity without leaking, fought against writing the modules yourself, and decided on whether the abstraction holds at the edges. Different decisions, different competitors. Decomposed below.

The two underdigitised areas are the catalogue's accuracy — the foundation everything depends on, populated by asking people to maintain metadata — and the platforms in regulated and air-gapped estates, where the tooling's assumptions do not hold and the need is greatest.

The two underserved constituencies are the platform engineer, answering questions about their own abstractions in a channel with no metrics, and the application developer, who learns what the platform supports by attempting something and failing.

The automation niches are golden path drift, where an improvement never reaches anything that already exists, and the usage telemetry that would have prevented the category's defining failure.

## Niches
- [[niches/internal-developer-platforms/platform-as-product/profile|🔵 Platform as Product]]
- [[niches/internal-developer-platforms/platform-tooling-market/profile|🔵 Platform Tooling Market]]
  - [[niches/internal-developer-platforms/build-vs-buy-portals/profile|🎯 Portals & Catalogues]]
  - [[niches/internal-developer-platforms/provisioning-and-abstraction/profile|🎯 Provisioning & Abstraction]]
- [[niches/internal-developer-platforms/service-catalogue-accuracy/profile|🟠 Service Catalogue Accuracy]]
- [[niches/internal-developer-platforms/regulated-and-constrained-platforms/profile|🟠 Regulated & Constrained Platforms]]
- [[niches/internal-developer-platforms/platform-engineer-support/profile|🟣 The Platform Engineer]]
- [[niches/internal-developer-platforms/the-application-developer/profile|🟣 The Application Developer]]
- [[niches/internal-developer-platforms/golden-path-drift/profile|⚡ Golden Path Drift]]
- [[niches/internal-developer-platforms/platform-usage-telemetry/profile|⚡ Platform Usage Telemetry]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Platform Tooling Market** is not: it names the vendor landscape rather than a contest, and the two decisions inside it are made separately and against different alternatives. The portal and catalogue decision is about whether to operate the widely-adopted open framework, buy a managed equivalent, or build nothing — and is won on operational cost and on whether the catalogue can be kept accurate. The provisioning and abstraction decision is about how much infrastructure complexity to hide and with what — and is won on whether the abstraction holds when a team needs something it does not cover, which is the failure mode that determines adoption. Different alternatives, different competitors, different failure modes. Decomposed into two contested sub-niches.

Two candidates were rejected. *Maturity scorecards* were folded into Platform as Product and Golden Path Drift, since the contest there is whether the scores change anything rather than whether they can be computed — and they are frequently resented, which is itself a product failure rather than a separate market. *Kubernetes abstraction specifically* was folded into Provisioning & Abstraction, since the contest is the abstraction's integrity rather than the particular substrate.
