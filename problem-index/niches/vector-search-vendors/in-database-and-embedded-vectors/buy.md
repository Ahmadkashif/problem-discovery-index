# Extension and Embedded Database Practice

**Niche:** [[niches/vector-search-vendors/in-database-and-embedded-vectors/profile|In-Database & Embedded Vectors]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Full-text search inside relational databases and embedded database engines both solved the shape of this problem years ago, including the parts vector extensions currently leave to the developer.
**Tags:** #data-integration #evaluation-metrics #automation #workflow-orchestration #graph-theory #compliance #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to be good enough inside the system the developer already runs — and whoever does that takes the market, because the buyer's real alternative is not another vendor, it is not adopting one.

## The Problem
Relational databases have had integrated full-text search for decades: a generated column holding the search representation, maintained by the database on write, indexed with a structure that participates in transactions and recovery, and queryable in the same statement as everything else. That is the exact ergonomic a vector extension should offer. Embedded database engines solved the in-process case with the same care. Vector extensions provide a column type and an index and stop.

## What Already Exists
Integrated full-text search with generated columns, automatic maintenance and transactional index updates; embedded database engines with in-process operation and single-file storage; materialised view machinery with incremental refresh; trigger and change-data-capture infrastructure; and the whole backup, recovery and replication apparatus these engines already provide.

## The Customization Gap
The adaptation is to a derived value produced by an external service. It requires: (1) an asynchronous generated column — a value the database knows it owes, knows is stale, and computes via an external call with retry — which is the precise primitive missing and does not exist in any engine today; (2) index maintenance under a mutation rate that graph indexes handle worse than inverted indexes do, which is where the full-text analogy stops being free; (3) query planning across vector similarity and ordinary predicates, which the planner should do natively and mostly does not; (4) recovery semantics that restore recall rather than exact structure, stated honestly; and (5) keeping the operational surface at zero, since the entire proposition is that the developer adds no new system — an extension that requires its own tuning, its own backup story and its own monitoring has given away its advantage.

## Target Customer
Database and extension vendors, application developers, and the embedded database community.

## Impact If Solved
Integrated full-text search is the exact ergonomic this should have and vector extensions stop at a column type. An asynchronous generated column — a value the database knows it owes — is the missing primitive and would remove the category's most common correctness bug.
