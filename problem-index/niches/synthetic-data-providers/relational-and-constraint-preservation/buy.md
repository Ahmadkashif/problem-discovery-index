# Data Profiling and Quality Assertion Frameworks

**Niche:** [[niches/synthetic-data-providers/relational-and-constraint-preservation/profile|Relational & Constraint Preservation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data quality tooling already discovers constraints from real data and asserts them continuously, and generation vendors neither discover the rules nor assert them on their output.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #data-integration #automation #workflow-orchestration #probability-distributions #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make a generated database behave like the real one under the customer's own queries and joins — and whoever does that takes the account, because a dataset that falls apart on a join is worth nothing however well it scored on distributions.

## The Problem
The data quality ecosystem profiles a table and proposes assertions automatically: uniqueness, nullability, value ranges, referential relationships, distributional expectations, functional dependencies. It then runs them on every load and fails the pipeline when they break. This is precisely the machinery a generation vendor needs — profile the source, derive the rule set, assert it on the output — and it is sitting in mature open-source projects the vendors do not use.

## What Already Exists
Assertion-based data quality frameworks with automatic expectation suggestion from a profiled dataset; data profiling engines that recover functional dependencies, candidate keys and inclusion dependencies at scale; schema and contract tooling; anomaly detection on data pipelines; and the orchestration hooks to gate a load on a failed assertion.

## The Customization Gap
The adaptation is pointing the machinery at generation instead of at ingestion. It requires: (1) profiling the source and the synthetic output with the same suite, then reporting the diff, which is a near-mechanical build and immediately produces the violation report the category does not ship; (2) relationship-level assertions rather than column-level, since the interesting failures are cross-table and cross-row and the frameworks are strongest within a column; (3) distributional assertions with appropriate tolerance, because synthetic data is supposed to differ and a framework tuned to detect any drift will flag everything — calibrating what counts as an acceptable difference is the real work; (4) assertions as a generation gate, so a run failing its rule set does not promote; and (5) surfacing discovered constraints to the customer as documentation, since the profiling output is frequently the first written description of rules the business has relied on for a decade, and that has value independent of the synthetic data.

## Target Customer
Generation vendors, enterprise data platform teams, QA and non-production environment owners, and the data quality tooling ecosystem.

## Impact If Solved
Profiling the source and the output with the same assertion suite and reporting the diff is a near-mechanical build that produces the coherence report the category does not ship. The discovered rule set doubles as documentation the business never had.
