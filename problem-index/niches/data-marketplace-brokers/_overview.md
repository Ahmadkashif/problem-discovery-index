# Niche Analysis — Data Marketplace Brokers

**Parent Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Pre-Purchase Evaluation | 🔵 High Market Share | $1.3B | None — properties discoverable only after payment | Every buyer in the market |
| 2 | Data Distribution Platforms | 🔵 High Market Share | $1.5B | High | Platform-standardised enterprises; separately, sourcing functions |
| 3 | Provenance & Consent Evidence | 🟠 Low Digitized | $680M | Very Low — a warranty rather than evidence | Legal, compliance and model training buyers |
| 4 | Licence Term Enforcement | 🟠 Low Digitized | $420M | Very Low — prose enforced by nothing | Data governance and legal functions |
| 5 | The Sourcing Analyst | 🟣 Underserved Audience | $310M | None — the same harness rebuilt every quarter | Data sourcing teams |
| 6 | The Provenance Reviewer | 🟣 Underserved Audience | $260M | None — certifying on a self-completed questionnaire | Compliance and vendor risk functions |
| 7 | Schema & Entity Resolution | ⚡ Highly Automatable | $390M | Low — four providers, four bespoke pipelines | Data engineering teams combining sources |
| 8 | Marketplace Outcome Intelligence | ⚡ Highly Automatable | $340M | None — the signal exists and would embarrass suppliers | The marketplaces themselves |

## Why These Niches

This is a market with excellent distribution and no evaluation. A buyer cannot determine whether a dataset covers their population, is fresh, is accurate against a reference, or has the fields they need populated — until they have paid for it and built an integration. That makes the purchase a lottery with a setup cost attached, and it is the largest contested surface in the industry: a broker who can tell a buyer what they are getting before they pay is selling a different product from one who cannot.

Distribution **failed the filter as one niche**. In-ecosystem sharing is won on delivering data without moving it, with governance intact, inside a single cloud data platform; the buyer is an enterprise already standardised on that platform and the competitor is the other platform. Cross-vendor brokerage is won on finding and matching a supplier to a requirement across the whole market, including suppliers with no cloud presence; the buyer is a sourcing function and the competitor is a direct relationship with the provider. One is infrastructure, the other is intermediation and search. Decomposed below.

The two underdigitised areas are both places where prose stands in for machinery. Provenance and consent arrive as a contractual warranty rather than as evidence, which has become a central risk now that buyers need to know whether data may lawfully train a model. And permitted-use terms are written in contract language that nothing in the delivery path can read, so compliance rests on whoever signed remembering what they signed.

The two underserved constituencies are the sourcing analyst rebuilding the same evaluation harness every quarter because the market supplies no basis for comparison, and the provenance reviewer asked to certify a supplier's lawfulness on the strength of a questionnaire the supplier completed about itself.

The automation niches are the entity resolution layer that every multi-provider buyer builds and nobody sells, and the marketplace's own record of what was evaluated, rejected, bought and churned — which is the quality signal the market lacks and which would make some of its suppliers unsaleable.

## Niches
- [[niches/data-marketplace-brokers/pre-purchase-evaluation/profile|🔵 Pre-Purchase Evaluation]]
- [[niches/data-marketplace-brokers/data-distribution-platforms/profile|🔵 Data Distribution Platforms]]
  - [[niches/data-marketplace-brokers/in-ecosystem-data-sharing/profile|🎯 In-Ecosystem Data Sharing]]
  - [[niches/data-marketplace-brokers/cross-vendor-dataset-brokerage/profile|🎯 Cross-Vendor Dataset Brokerage]]
- [[niches/data-marketplace-brokers/provenance-and-consent-evidence/profile|🟠 Provenance & Consent Evidence]]
- [[niches/data-marketplace-brokers/licence-term-enforcement/profile|🟠 Licence Term Enforcement]]
- [[niches/data-marketplace-brokers/the-sourcing-analyst/profile|🟣 The Sourcing Analyst]]
- [[niches/data-marketplace-brokers/the-provenance-reviewer/profile|🟣 The Provenance Reviewer]]
- [[niches/data-marketplace-brokers/schema-and-entity-resolution/profile|⚡ Schema & Entity Resolution]]
- [[niches/data-marketplace-brokers/marketplace-outcome-intelligence/profile|⚡ Marketplace Outcome Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Data Distribution Platforms** is not: it names the delivery function rather than a contest, and the two businesses performing it are unrelated. In-ecosystem sharing is an infrastructure contest — zero-copy delivery, governance, and the gravity of a platform the buyer has already standardised on — and its competitor is another cloud data platform. Cross-vendor brokerage is a search and matching contest — knowing the supply landscape, translating a requirement into candidates, and reaching suppliers with no cloud footprint — and its competitor is the buyer going direct. Different buyers, different economics, different capabilities. Decomposed into two contested sub-niches.

Two candidates were rejected. *Clean rooms and privacy-preserving collaboration* was rejected because its contest is joint computation without transferring data, which belongs to the privacy technology industry covered separately in this vault. *Internal data quality tooling* was rejected because its buyer is a data platform team working on their own data rather than a participant in this market, and it is covered under the data platform integrator and observability industries.
