# Storage Engine Compaction and Maintenance

**Niche:** [[niches/vector-search-vendors/index-drift-under-mutation/profile|Index Drift Under Mutation]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Log-structured storage engines have spent fifteen years on compaction scheduling, write amplification and background maintenance under live traffic, and vector indexes offer a full rebuild.
**Tags:** #evaluation-metrics #automation #workflow-orchestration #graph-theory #time-series-forecasting #descriptive-statistics #data-integration #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to keep an approximate index's recall stable while the corpus changes underneath it, and to show the operator that it is — and whoever does that takes the account, because the degradation is currently invisible until a user notices.

## The Problem
A structure that degrades under mutation and needs periodic reorganisation without interrupting service is the defining problem of log-structured storage. That community produced compaction strategies with different amplification trade-offs, schedulers that run maintenance under live traffic without destroying tail latency, rate limiting to bound the impact, and metrics that tell an operator exactly how far from optimal the structure currently is. Vector indexes have a rebuild command.

## What Already Exists
Compaction strategies with characterised read, write and space amplification trade-offs; background compaction schedulers with I/O rate limiting and priority; incremental and partial reorganisation; index bloat measurement and reindexing practice from relational databases; and operational metrics exposing structural health continuously.

## The Customization Gap
The adaptation is to a structure whose degradation is a quality loss rather than a performance loss. It requires: (1) a maintenance trigger driven by measured recall rather than by space amplification, since the cost of deferring here is wrong answers rather than slow ones — which is a different objective and the most important difference; (2) partial and localised repair, because graph damage concentrates around deletion-heavy regions and the compaction world's partial strategies map onto this well; (3) maintenance under live traffic with bounded impact, which the storage community solved thoroughly and vector systems handle by taking a maintenance window; (4) a cost model for repair versus rebuild, so an operator can choose knowingly, which is exactly what compaction strategy selection provides in its own domain; and (5) structural health metrics as standard output, since the storage engines expose theirs and vector indexes expose nothing comparable despite the statistics being cheap to compute.

## Target Customer
Vector search vendors, platform operations teams, and the storage engine community whose practice transfers with a change of objective.

## Impact If Solved
Compaction under live traffic is fifteen years mature and vector indexes offer a maintenance window. Driving maintenance from measured recall rather than from space amplification is the objective change that makes the whole practice fit.
