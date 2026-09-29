# Batch & Throughput Inference

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver the lowest cost per million tokens by exploiting capacity nobody else can use — and whoever does that takes the account, because the buyer has no latency requirement and therefore no other criterion.

## Profile
**Market Size:** ~$750M US and growing as offline workloads scale
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Moderate — served as an afterthought on interactive infrastructure
**Target Buyer:** Data engineering and analytics teams running offline jobs
**Automation Potential:** Very High — scheduling against interruptible capacity is fully automatable

## What Makes This a Distinct Niche
Classifying a hundred million support tickets, embedding a document corpus, extracting fields from a decade of contracts, generating summaries overnight — these jobs care about cost and a deadline measured in hours or days, and about nothing else. That makes them the natural consumer of exactly the capacity an interactive guarantee cannot use: spot and preemptible hardware, off-peak troughs, and the gaps between other customers' spikes. A provider who builds for that serves these jobs at a fraction of interactive cost and improves fleet utilisation at the same time. Most providers instead run batch through the interactive path with a discount, which leaves the advantage unclaimed and the workload mispriced.

## Current Tools & Gaps
Batch endpoints with a discount, large batch sizes, and asynchronous job APIs at some providers. The gaps: no deadline-aware scheduling, so a job due Thursday is treated like one due now; no use of interruptible capacity, which is the whole opportunity; no checkpointing, so an interrupted job restarts; no cost-versus-deadline choice offered to the customer; and no visibility into progress or projected completion, which is the thing a data team actually needs.

## Problems
- [[niches/ai-inference-providers/batch-and-throughput-inference/build|🔨 Build: A Deadline in Days, Priced Like a Deadline in Milliseconds]]
- [[niches/ai-inference-providers/batch-and-throughput-inference/buy|🛒 Buy: Batch Scheduling and Spot Market Practice]]
- [[niches/ai-inference-providers/batch-and-throughput-inference/fix|🔧 Fix: The Job That Restarts From Zero]]
