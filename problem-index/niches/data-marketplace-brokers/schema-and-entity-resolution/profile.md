# Schema & Entity Resolution

**Parent Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to make four providers covering the same entities into one coherent view without the buyer writing four pipelines and a resolution layer — and whoever does that takes the account, because every multi-source buyer builds this and nobody sells it.

## Profile
**Market Size:** ~$390M US
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** Low — four providers, four bespoke pipelines
**Target Buyer:** Data engineering teams combining multiple sources
**Automation Potential:** Very High — matching and merging are well-studied

## What Makes This a Distinct Niche
Every data integration tool will map one schema to another. What a buyer combining four providers covering the same entities actually needs is different: a canonical entity model, a resolution layer that decides when two records from two providers are the same company or person, and a merge policy deciding which provider's value wins when they disagree — which they constantly do. That layer is built from scratch by every buyer, is the hardest part of every multi-source data programme, and is sold by nobody, because the integration vendors stop at mapping and the providers have no interest in making themselves interchangeable.

## Current Tools & Gaps
Schema mapping tools, transformation pipelines, master data management platforms aimed at internal data, and record linkage libraries. The gaps: no canonical entity model for common domains, so every buyer invents one; identifier fragmentation across providers with no crosswalk; no merge policy framework, so conflict resolution is hard-coded per field; no measurement of which provider is right when they disagree; and no way to tell whether a fifth provider would add anything to the four already integrated.

## Problems
- [[niches/data-marketplace-brokers/schema-and-entity-resolution/build|🔨 Build: Four Pipelines and a Layer Nobody Sells]]
- [[niches/data-marketplace-brokers/schema-and-entity-resolution/buy|🛒 Buy: Record Linkage and Master Data Management]]
- [[niches/data-marketplace-brokers/schema-and-entity-resolution/fix|🔧 Fix: Two Providers Disagree and Somebody Guessed]]
