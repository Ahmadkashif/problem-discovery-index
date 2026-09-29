# Relational & Constraint Preservation

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to make a generated database behave like the real one under the customer's own queries and joins — and whoever does that takes the account, because a dataset that falls apart on a join is worth nothing however well it scored on distributions.

## Profile
**Market Size:** ~$210M US
**Share of Parent Industry:** ~14% of category revenue
**Digital Adoption:** Low — coherence is asserted and almost never verified
**Target Buyer:** Enterprise data platform, QA and non-production environment teams
**Automation Potential:** High — verification is fully mechanical

## What Makes This a Distinct Niche
This is the use of synthetic data where privacy is secondary and coherence is everything: development and test environments, vendor evaluations, demo instances, training environments, load testing. The buyer needs a database that behaves like production under real application code and real analytical queries. They do not need a differential privacy guarantee, which is what the certification market is competing on. What they need is that the joins resolve, the aggregates land in the right range, the event sequences make sense, and the application does not crash on a record that cannot exist. That is a verification problem as much as a generation one, and nobody in the category treats verification as a product.

## Current Tools & Gaps
Test data management and subsetting tools from the database tooling world, masking and pseudonymisation products, and generator output that satisfies key constraints by post-processing. The gaps: temporal and event-sequence structure is destroyed by row-wise generation and nothing reports it; referential integrity is repaired rather than modelled, which produces valid keys over fabricated relationships; business rules are undocumented, so violations are found by the application failing; and no vendor offers a verification harness that runs the customer's own queries against both databases and compares.

## Problems
- [[niches/synthetic-data-providers/relational-and-constraint-preservation/build|🔨 Build: Business Data Is Sequences and Generation Produces Rows]]
- [[niches/synthetic-data-providers/relational-and-constraint-preservation/buy|🛒 Buy: Data Profiling and Quality Assertion Frameworks]]
- [[niches/synthetic-data-providers/relational-and-constraint-preservation/fix|🔧 Fix: Referential Integrity Repaired After the Fact]]
