# Online Schema Change and Zero-Downtime Migration

**Niche:** [[niches/vector-search-vendors/the-index-rebuild-operator/profile|The Index Rebuild Operator]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The database world solved rebuilding a large structure under live traffic with online schema change tools, and vector vendors hand the operator a maintenance window.
**Tags:** #automation #workflow-orchestration #data-integration #evaluation-metrics #compliance #descriptive-statistics #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make an index rebuild something that happens automatically, online and on evidence, rather than something a person schedules and watches — and whoever does that takes the account, because the rebuild is the category's worst operational experience.

## The Problem
Altering a large table without downtime is a solved operational problem with well-known tools: build the new structure alongside, capture changes during the build, apply them, swap atomically, keep the old structure briefly for rollback. It is throttled against live load, resumable, observable, and routine enough to run during business hours. Vector index rebuilds have none of that apparatus, and the operator is handed a blocking command and a warning about memory.

## What Already Exists
Online schema change tools with shadow table construction, change capture and atomic cut-over; concurrent index build in relational engines; blue-green and replica-swap deployment patterns; throttling against replication lag or latency; progress reporting and resumable long-running operations; and rollback procedures with retained old structures.

## The Customization Gap
The adaptation is to a structure whose correctness is statistical and whose build is compute-bound rather than I/O-bound. It requires: (1) cut-over validated on recall rather than on row counts, since the new index is not expected to be identical and the meaningful check is that quality is at least as good — this changes what the cut-over gate tests and is the central adaptation; (2) change capture during a build that may take hours, where insertions must be applied to the new structure as it is constructed, which graph indexes make harder than tables do; (3) throttling against query latency rather than replication lag, since the build competes for CPU and memory rather than for I/O; (4) partial cut-over by shard, which is a natural fit for these deployments and reduces the blast radius of a bad rebuild; and (5) rollback that is genuinely instant, retaining the old index until recall has been verified on live traffic rather than at the moment of swap.

## Target Customer
Vector search vendors, platform operations teams, and the database operations community whose tooling patterns transfer almost directly.

## Impact If Solved
Online rebuild under live traffic is routine one field over and unavailable here. Gating the cut-over on measured recall rather than on structural equality is the adaptation that makes the pattern fit an approximate index.
