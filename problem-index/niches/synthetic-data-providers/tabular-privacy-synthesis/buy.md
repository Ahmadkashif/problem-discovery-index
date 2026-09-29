# Constraint Solving and Statistical Disclosure Control

**Niche:** [[niches/synthetic-data-providers/tabular-privacy-synthesis/profile|Tabular & Privacy Synthesis]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** National statistical offices have released useful microdata under disclosure control for decades and constraint solvers handle exactly the rule enforcement generation needs, and the category uses neither.
**Tags:** #convex-optimization #optimization-fundamentals #dynamic-programming #bayesian-inference #hypothesis-testing #evaluation-metrics #compliance #probability-distributions
**Contested on:** Every serious competitor in this sub-niche is fighting to generate a multi-table business database whose keys, constraints and conditional structure survive intact while a defensible privacy claim still holds — and whoever does that takes the account, because it is the only version of the problem enterprise customers actually have.

## The Problem
Two mature bodies of work sit adjacent to this problem and are largely unused by it. Statistical disclosure control — the discipline by which census bureaus and health agencies release detailed microdata to researchers without exposing individuals — has decades of method, published practice, and hard-won institutional knowledge about the trade-off the category is rediscovering. Constraint programming and integer solvers handle the exact problem of producing records that satisfy a rule set. The category builds from the generative modelling literature alone.

## What Already Exists
Statistical disclosure control methodology including record swapping, micro-aggregation, controlled tabular adjustment, synthetic microdata programmes with published validity studies, and disclosure risk measurement frameworks; constraint programming and mixed-integer solvers; functional dependency and constraint discovery tooling from the data profiling literature; and schema-aware test data generation from the database engineering world.

## The Customization Gap
The adaptation is to modern generative pipelines and enterprise schemas. It requires: (1) disclosure risk measures that operate on a generated dataset rather than a perturbed real one, since the threat model differs and the statistical office measures assume records derive from real ones; (2) constraint solving integrated into sampling rather than applied as a post-filter, because rejection sampling against a dense rule set becomes intractable and distorts what survives; (3) rule discovery at enterprise schema scale, where the profiling literature's methods are sound and the scale and noise tolerance are not what they were designed for; (4) validity studies as a deliverable, which is the practice the statistical world established and the category has not adopted — publishing how well analyses on the synthetic data reproduce analyses on the real; and (5) the institutional lesson those offices learned the hard way, which is that the release decision belongs to a standing committee with published criteria rather than to the party that produced the data.

## Target Customer
Generation vendors, enterprise data platform teams, regulated industry data functions, and the statistical and disclosure control community.

## Impact If Solved
Disclosure control has decades of validated method for exactly this trade-off and the category ignores it. The validity study — published, reproducible, comparing analyses on synthetic against real — is the practice most worth importing.
