# Database Engineering Practice

**Niche:** [[niches/vector-search-vendors/vector-index-infrastructure/profile|Vector Index Infrastructure]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Relational databases spent forty years on query planning, cost models, buffer management and crash recovery, and vector systems rebuilt the storage engine without most of it.
**Tags:** #data-integration #graph-theory #evaluation-metrics #convex-optimization #automation #workflow-orchestration #descriptive-statistics #compliance
**Contested on:** Not terminal — the contest differs by whether the buyer is acquiring capacity or avoiding a system, and the decomposition is recorded in the profile.

## The Problem
Cost-based query planning, statistics-driven optimisation, buffer pool management, write-ahead logging, multi-version concurrency, online schema change and point-in-time recovery are the accumulated answers to problems every storage system has. Vector databases are storage systems that arrived recently, and many of them implemented the index brilliantly and the surrounding database poorly — which is why the extension inside a mature relational database is a credible competitor despite a less sophisticated index.

## What Already Exists
Cost-based query optimisers with statistics collection and cardinality estimation; buffer pool and cache management with well-studied replacement policies; write-ahead logging and crash recovery; multi-version concurrency control; online index construction without blocking writes; and backup, point-in-time recovery and replication machinery.

## The Customization Gap
The adaptation is to a query whose cost depends on the data distribution in an unusual way. It requires: (1) a cost model for approximate search, where the work done depends on the query's position relative to the data distribution rather than on a selectivity estimate — which is genuinely novel and is the piece the planning literature does not supply; (2) planning across hybrid queries combining vector similarity with metadata filters, where the ordering decision is consequential and frequently made naively, and where the relational planning tradition applies almost directly; (3) online index construction, since rebuilds currently block or double memory and the database world solved concurrent index build decades ago; (4) recovery semantics for an approximate structure, where the useful guarantee is that recall is restored rather than that bytes match, and stating that clearly is better than implying a stronger guarantee; and (5) statistics on the vector distribution itself, which is what a cost model would need and what nothing currently collects.

## Target Customer
Vector search vendors, platform teams, and the database engineering community whose practice transfers here almost unchanged.

## Impact If Solved
The index was built brilliantly and the database around it was not, which is why a mature relational engine with a weaker index competes. A cost model for approximate search and planning for hybrid filter-plus-vector queries are the two pieces with real leverage.
