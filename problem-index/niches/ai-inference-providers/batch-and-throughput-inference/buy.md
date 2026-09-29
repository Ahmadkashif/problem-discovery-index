# Batch Scheduling and Spot Market Practice

**Niche:** [[niches/ai-inference-providers/batch-and-throughput-inference/profile|Batch & Throughput Inference]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** High performance computing and cloud spot markets both solved deadline-aware scheduling on interruptible capacity decades and years ago respectively, and batch inference reimplements neither.
**Tags:** #dynamic-programming #markov-decision-processes #optimization-fundamentals #time-series-forecasting #evaluation-metrics #automation #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver the lowest cost per million tokens by exploiting capacity nobody else can use — and whoever does that takes the account, because the buyer has no latency requirement and therefore no other criterion.

## The Problem
Scheduling deferrable work into whatever capacity is available, surviving interruption, and doing it cheaply is the founding purpose of batch scheduling in high performance computing and of the whole spot instance ecosystem in cloud. Backfilling, checkpoint-restart, deadline scheduling, interruption prediction and bid strategies are all mature. Batch inference runs on an interactive endpoint with a discount code.

## What Already Exists
Batch schedulers with backfilling, deadline scheduling and fair-share allocation; checkpoint-restart infrastructure for long-running jobs; spot instance management with interruption handling and diversification across pools; interruption prediction from historical availability; bid and portfolio strategies for spot capacity; and workflow engines with retry and partial-failure semantics.

## The Customization Gap
The adaptation is to work that is embarrassingly parallel at the item level and expensive to restart at the model level. It requires: (1) checkpointing at item granularity rather than process granularity, which makes interruption almost free and is far easier here than in the scientific computing case the tools were built for — this is the adaptation that unlocks everything; (2) model load time as a scheduling cost, since moving a job to a new accelerator requires loading weights and that cost shapes whether migration is worthwhile, which classical schedulers do not model; (3) deadline scheduling across a heterogeneous accelerator fleet where throughput per device differs by generation; (4) interruption prediction to pre-emptively checkpoint, borrowing directly from spot management practice; and (5) partial results as a first-class deliverable, since a job at ninety percent by the deadline is frequently useful and the scientific batch tradition treats completion as binary.

## Target Customer
Inference providers, data engineering teams, and the high performance computing and cloud cost communities whose tooling transfers directly.

## Impact If Solved
Deadline-aware scheduling on interruptible capacity is mature and unapplied. Item-level checkpointing makes interruption nearly free for this workload, which is a far easier proposition than in the scientific computing setting these tools came from.
