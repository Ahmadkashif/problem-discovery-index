# Tabular & Privacy Synthesis

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to generate a multi-table business database whose keys, constraints and conditional structure survive intact while a defensible privacy claim still holds — and whoever does that takes the account, because it is the only version of the problem enterprise customers actually have.

## Profile
**Market Size:** ~$380M US
**Share of Parent Industry:** ~25% of category revenue
**Digital Adoption:** High for single-table synthesis, near zero for relational
**Target Buyer:** Data platform leads with privacy and legal as the approving parties
**Automation Potential:** High

## What Makes This a Distinct Niche
Tabular synthesis is where the privacy claim and the utility claim collide directly, and where the real data is not a table. Enterprise data is a schema: forty tables, foreign keys, cardinality relationships, temporal ordering, business rules that hold in every real record. Single-table synthesis is effectively solved and is not what customers have. The contest is generating the schema — with referential integrity, plausible relationship cardinalities and constraint satisfaction — while the privacy argument survives the fact that a relational release leaks more than the sum of its tables.

## Current Tools & Gaps
Generative adversarial and diffusion models for single tables, copula methods, Bayesian networks, and differential privacy mechanisms for tabular release. The gaps: referential integrity is frequently produced by post-processing rather than modelled, so the relationship structure is fabricated; relationship cardinality distributions are not preserved, so the synthetic database has the wrong shape even when the keys resolve; business rules are not enforced and violation rates go unreported; and the privacy accounting almost never accounts for the multi-table release as a whole.

## Problems
- [[niches/synthetic-data-providers/tabular-privacy-synthesis/build|🔨 Build: Forty Tables With Foreign Keys and Business Rules]]
- [[niches/synthetic-data-providers/tabular-privacy-synthesis/buy|🛒 Buy: Constraint Solving and Statistical Disclosure Control]]
- [[niches/synthetic-data-providers/tabular-privacy-synthesis/fix|🔧 Fix: Privacy Accounted Per Table, Released as a Database]]
