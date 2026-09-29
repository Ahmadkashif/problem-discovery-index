# Niche Analysis — Web Data Extraction Firms

**Parent Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Extraction Correctness | 🔵 High Market Share | $480M | None — silent wrongness is undetected | Every customer consuming extracted data |
| 2 | Collection Infrastructure | 🔵 High Market Share | $620M | High | Extraction engineers; separately, data teams |
| 3 | Collection Governance Record | 🟠 Low Digitized | $340M | Very Low — reviewed once, never revisited | Legal, compliance and the firms' own leadership |
| 4 | Cross-Source Normalisation | 🟠 Low Digitized | $290M | Low — a thousand sites, a thousand shapes | Data teams consuming multi-source extraction |
| 5 | The Maintenance Engineer | 🟣 Underserved Audience | $220M | None — a queue that never empties | Extraction operations teams |
| 6 | The Compliance Reviewer | 🟣 Underserved Audience | $180M | None — unsettled law, no tooling | Legal and compliance functions |
| 7 | Automated Extraction Repair | ⚡ Highly Automatable | $280M | Low — repair is manual at fleet scale | The firms operating scraper fleets |
| 8 | Request Log Intelligence | ⚡ Highly Automatable | $250M | None — complete records, no reasoning | The firms themselves |

## Why These Niches

A scraper that returns nothing is obvious. A scraper that returns the wrong field with the right shape is invisible, and it feeds a customer's pricing or research pipeline for weeks before anybody notices. Detecting semantic breakage rather than structural failure is the industry's central unsolved technical problem, and it is what separates a delivery service from something a customer can build a business on. That makes correctness the largest contested surface here.

Collection infrastructure **failed the filter as one niche**. Proxy and access infrastructure is fought over reaching a target that does not want to be reached — success rate against anti-bot systems, address pool quality, cost per successful request — bought by extraction engineers whose alternative is another proxy network. Structured extraction is fought over returning correct fields from an arbitrary page, bought by data teams whose alternative is pointing a model at the page themselves, and whose economics are per-page model cost rather than per-gigabyte bandwidth. Different capability, different buyer, different cost structure, different competitor. Decomposed below.

The two underdigitised areas are both records nobody keeps. No firm maintains a continuous, queryable account of what it is collecting, from where, under what permission and for whose stated purpose — the legal review happens at onboarding and is never revisited while sites, laws and use cases all change. And extraction from a thousand sites produces a thousand shapes of the same entity, with reconciliation being the work customers assume they are buying and are not.

The two underserved constituencies are the maintenance engineer with a queue that never empties and no way to know which working extractions are quietly wrong, and the compliance reviewer deciding against a genuinely unsettled legal landscape with no tooling, no precedent library and commercial pressure on one side of every decision.

The automation niches are fleet-scale repair, which model-based extraction has just made tractable, and the complete record of every request these firms make, which reasons about nothing.

## Niches
- [[niches/web-data-extraction-firms/extraction-correctness/profile|🔵 Extraction Correctness]]
- [[niches/web-data-extraction-firms/collection-infrastructure/profile|🔵 Collection Infrastructure]]
  - [[niches/web-data-extraction-firms/proxy-and-access-infrastructure/profile|🎯 Proxy & Access Infrastructure]]
  - [[niches/web-data-extraction-firms/structured-extraction-services/profile|🎯 Structured Extraction Services]]
- [[niches/web-data-extraction-firms/collection-governance-record/profile|🟠 Collection Governance Record]]
- [[niches/web-data-extraction-firms/cross-source-normalisation/profile|🟠 Cross-Source Normalisation]]
- [[niches/web-data-extraction-firms/the-maintenance-engineer/profile|🟣 The Maintenance Engineer]]
- [[niches/web-data-extraction-firms/the-compliance-reviewer/profile|🟣 The Compliance Reviewer]]
- [[niches/web-data-extraction-firms/automated-extraction-repair/profile|⚡ Automated Extraction Repair]]
- [[niches/web-data-extraction-firms/request-log-intelligence/profile|⚡ Request Log Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Collection Infrastructure** is not: it names the delivery stack rather than a contest, and the two halves compete on unrelated axes. Proxy and access infrastructure is an economics and adversarial-engineering contest measured in successful requests per dollar against evolving detection; its buyer is an engineer and its competitor is another network. Structured extraction is a correctness contest measured in fields returned right from an unfamiliar page; its buyer is a data team and its competitor is that team pointing a model at the page themselves. The cost structures — bandwidth and addresses against model tokens per page — have nothing in common. Decomposed into two contested sub-niches.

Two candidates were rejected. *Content licensing and publisher agreements* was rejected because its contest is negotiating rights with rights-holders, which belongs to the digital publishing industries covered separately in this vault. *Anti-bot and bot management* was rejected because it is the other side of this market and its contest — distinguishing automated from human traffic — is already covered as a contested sub-niche under edge and CDN providers.
