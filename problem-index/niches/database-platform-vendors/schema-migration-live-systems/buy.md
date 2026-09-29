# The Expand-Contract Pattern, Unautomated

**Niche:** [[niches/database-platform-vendors/schema-migration-live-systems/profile|Schema Migration on Live Systems]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Expand-contract is a well-documented pattern for changing a schema without downtime, taught in every continuous delivery text, and it is executed by hand from a runbook every time.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #cross-validation
**Contested on:** Every serious competitor here is fighting to make changing a schema on a live production system routine rather than an event — and whoever does that takes the database team, because every significant migration is currently planned by whoever has done one before.

## The Problem
The safe way to change a schema on a live system is documented and stable: add the new structure, deploy code that writes to both, backfill, deploy code that reads the new, remove the old. It appears in every continuous delivery text and is understood by every team that has done it. It is also a five-stage sequence spanning database changes and application deployments across days, coordinated by hand, tracked in a document, and abandoned halfway more often than anyone admits — leaving schemas with both structures present indefinitely.

## What Already Exists
The expand-contract pattern with extensive documentation; migration frameworks that version and apply database changes; online schema change tools for the mechanical steps; deployment orchestration; static analysis capable of determining which queries touch which columns; and feature flag systems for controlling the read and write paths.

## The Customization Gap
The adaptation is to a sequence spanning two systems with different deployment cadences. It requires: (1) a single orchestrated plan covering database and application steps, since the pattern's failures come from the coordination rather than from any individual step and treating them as two separate processes is the root cause; (2) automated verification of each stage's precondition — is all code writing to both, has the backfill completed and stayed consistent, is any code still reading the old structure — because the stage transitions are currently judged by a human reading a checklist and the dangerous move is advancing early; (3) static analysis of application queries to determine which code paths touch the changing structure, which answers the readiness question mechanically and is the piece nobody has built; (4) enforcement of completion, since the abandoned half-migration is the most common real outcome and produces schemas carrying both structures for years — a tracked plan with an owner and a deadline is what prevents it; and (5) backfill execution with rate control and progress, so the long-running step is monitored rather than watched.

## Target Customer
Database and platform engineering teams, migration framework maintainers, managed database vendors, and the deployment tooling ecosystem.

## Impact If Solved
The pattern is documented and its execution is manual coordination across two systems, which is where it fails. Query-level static analysis makes the stage transitions verifiable, and tracked completion addresses the abandoned migrations that accumulate in every mature schema.
