# Forty Tables With Foreign Keys and Business Rules

**Niche:** [[niches/synthetic-data-providers/tabular-privacy-synthesis/profile|Tabular & Privacy Synthesis]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Single-table synthesis is solved and real enterprise data is forty tables joined by foreign keys under business rules, which nothing on the market generates coherently.
**Tags:** #graph-theory #bayesian-inference #gans #diffusion-models #convex-optimization #probability-distributions #evaluation-metrics #data-integration
**Contested on:** Every serious competitor in this sub-niche is fighting to generate a multi-table business database whose keys, constraints and conditional structure survive intact while a defensible privacy claim still holds — and whoever does that takes the account, because it is the only version of the problem enterprise customers actually have.

## The Problem
A team needs a synthetic copy of an order management database for a vendor evaluation. It has customers, accounts, orders, order lines, shipments, returns, payments and adjustments — thirty-odd tables. A synthetic customer must have a plausible number of orders; an order's lines must sum to its total; a shipment cannot precede its order; a return must reference a line that exists and a quantity that does not exceed it. The vendor generates each table well and the database as a whole is incoherent. Every query that joins returns nonsense, which is every query anybody would actually run.

## Why Nobody Has Built This
Relational generation is genuinely hard: the joint distribution spans tables, the dependency graph has cycles in practice, and the cardinality of a parent-child relationship is itself a distribution that must be preserved rather than a constant. The literature is overwhelmingly single-table because that is what benchmarks measure, and the benchmark is what the field optimises. Post-processing keys into validity is fast and demos well, and it silently destroys the relationship structure that was the point. And business rules are customer-specific, undocumented and discovered mostly by being violated.

## What to Build
Generate the schema, not the tables. Model the relational structure explicitly — the dependency graph, the cardinality distribution of each relationship, the conditional structure across the join — rather than generating independently and repairing afterwards, which is the difference between a database and a pile of tables. Mine business rules from the source data automatically: functional dependencies, ordering constraints, sum and balance relationships, categorical co-occurrence, value ranges conditional on other columns. Most are discoverable by inspection and none are documented, which makes automatic discovery the practical route and a standing deliverable in its own right. Enforce discovered constraints during generation rather than filtering afterwards, since filtering distorts the distribution in ways that are hard to characterise. Report a constraint violation rate per rule as a headline number. Handle temporal ordering as a first-class property, because event-shaped business data is mostly sequences and independent row generation destroys them. Preserve the tail of each cardinality distribution, since the customer with four hundred orders is often exactly the case the downstream analysis is about. And evaluate by running the customer's real queries against both databases and comparing results, which is the only test that reflects what the data is for.

## Target Customer
Data platform teams needing non-production copies of production schemas, vendor evaluation and testing functions, and analytics teams blocked on access to production.

## Impact If Built
Real enterprise data is relational and the field generates tables. Automatic business-rule mining plus constraint-aware generation, evaluated by running the customer's own queries, is the shape of the answer and nobody ships it.
