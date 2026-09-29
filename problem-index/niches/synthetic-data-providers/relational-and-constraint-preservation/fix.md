# Referential Integrity Repaired After the Fact

**Niche:** [[niches/synthetic-data-providers/relational-and-constraint-preservation/profile|Relational & Constraint Preservation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Tables are generated independently and foreign keys are then rewritten to point at something that exists, which produces a database that passes constraint checks over relationships that were invented by the repair step.
**Tags:** #graph-theory #probability-distributions #descriptive-statistics #evaluation-metrics #hypothesis-testing #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make a generated database behave like the real one under the customer's own queries and joins — and whoever does that takes the account, because a dataset that falls apart on a join is worth nothing however well it scored on distributions.

## The Problem
The generator produces an orders table and an order lines table separately. The line rows reference order identifiers that do not exist, so a post-processing step reassigns each line to a randomly chosen valid order. Every foreign key now resolves and the database loads cleanly. But the number of lines per order is now uniform where it was heavily skewed, the correlation between order value and line count is gone, the relationship between a customer's tier and their basket composition is gone, and every analytical query that groups by order returns the wrong shape. The integrity check passes and the data is useless for the reason somebody wanted it.

## Why It's Still Broken
Repair is easy, fast, and produces a database that passes every check anyone runs. Modelling the relationship properly requires generating the child count as a distribution conditional on the parent, which is a real modelling commitment. Nothing in the standard evaluation suite measures cardinality distributions, so the damage is invisible to the vendor's own reporting. And customers discover it only when an aggregate query looks wrong, which is late and is usually blamed on the data being synthetic in general.

## What a Fix Looks Like
Measure the damage and then model the relationship. Report the cardinality distribution per relationship in source and output side by side — mean, variance, and the tail — which takes an afternoon to build, requires no modelling change, and immediately exposes the repair step's cost in a way nobody can argue with. Generate the child count conditional on parent attributes rather than assigning uniformly, since the count is itself a modelled quantity and conditioning is what preserves the correlation structure. Preserve the tail of each relationship, because the parent with four hundred children is frequently the case the analysis exists to study and uniform reassignment erases it entirely. Generate the relationship graph before the rows where the structure carries the signal, which is the correct ordering and the one the repair approach inverts. Report join-result comparisons: run the same aggregate over source and synthetic and show the difference, which is the test the customer will eventually run themselves. And declare when repair was used, so a customer knows which relationships are modelled and which were manufactured.

## Who Feels the Pain
Analytics teams whose aggregates are wrong for a reason nothing reported; application teams whose realistic-looking test database has uniformly shaped relationships; and vendors doing relational modelling properly who lose on benchmarks that do not measure it.

## Impact If Fixed
The repair step destroys the relationship structure while making every integrity check pass. Reporting cardinality distributions side by side costs an afternoon and makes the damage visible before a customer finds it in an aggregate.
