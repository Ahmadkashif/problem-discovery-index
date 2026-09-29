# Cluster Scheduling and Capacity Planning

**Niche:** [[niches/mlops-platforms/the-cluster-arbitrator/profile|The Cluster Arbitrator]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Decades of batch scheduling research and a mature cloud capacity management industry exist, and ML clusters are allocated in a chat channel.
**Tags:** #dynamic-programming #markov-decision-processes #convex-optimization #optimization-fundamentals #time-series-forecasting #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to schedule accelerators on what a job will actually need and be worth rather than on what its author requested — and whoever does that takes the account, because the cluster is the largest line in the budget and it is allocated by negotiation.

## The Problem
Batch scheduling is one of computing's oldest studied problems, with backfilling, gang scheduling, fair-share allocation and preemption all well understood and implemented in production schedulers that have run national computing facilities for decades. Cloud capacity management has mature forecasting, commitment optimisation and spot arbitrage. ML platform teams use a fraction of the first and almost none of the second.

## What Already Exists
High performance computing schedulers with backfilling, fair-share and gang scheduling; container orchestrators with quota, priority and preemption; capacity forecasting and commitment optimisation tooling from the cloud cost management world; spot and preemptible instance management with interruption handling; and queueing theory with well-developed results on scheduling policy under uncertain service times.

## The Customization Gap
The adaptation is to jobs whose duration is unknown, whose value is not stated, and which can frequently checkpoint. It requires: (1) predicted rather than declared duration, since the entire backfilling and fair-share apparatus assumes a declared runtime and ML submitters do not provide one — supplying a prediction makes decades of scheduling machinery immediately applicable, which is the central adaptation; (2) checkpoint-aware preemption, because an ML job that can resume is a fundamentally different scheduling object from one that cannot, and existing preemption policies do not distinguish them; (3) gang scheduling for distributed jobs with accelerator topology awareness, since interconnect placement affects throughput substantially and generic schedulers treat accelerators as interchangeable; (4) value as an input to priority rather than an organisational rank, which is a policy design question the tooling should support and none does; and (5) integrating spot capacity for checkpointable work, which is a large cost reduction available to exactly this workload and is under-exploited because interruption handling and checkpointing are not connected.

## Target Customer
ML infrastructure and platform teams, the finance functions funding capacity, and the scheduler and cloud cost vendors for whom this workload is adjacent and unserved.

## Impact If Solved
The scheduling machinery is decades mature and assumes a declared runtime nobody provides. Supplying a predicted duration unlocks all of it, and connecting checkpointing to spot capacity is a large unclaimed cost reduction for exactly this workload.
