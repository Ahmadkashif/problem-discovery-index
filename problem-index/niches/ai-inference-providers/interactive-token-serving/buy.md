# Tail Latency Engineering

**Niche:** [[niches/ai-inference-providers/interactive-token-serving/profile|Interactive Token Serving]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Large-scale interactive serving developed a whole discipline for the tail — hedging, load shedding, adaptive concurrency — and inference stacks report a mean and a maximum batch size.
**Tags:** #markov-chains #probability-distributions #confidence-intervals #evaluation-metrics #descriptive-statistics #automation #convex-optimization #change-point-detection
**Contested on:** Every serious competitor in this sub-niche is fighting to hold time-to-first-token and inter-token latency steady while concurrency climbs — and whoever does that takes the account, because a product whose cursor stalls loses its users regardless of what the model can do.

## The Problem
Keeping the tail short under load is a mature discipline: hedged requests, adaptive concurrency limits that back off before saturation, load shedding that sheds the right requests, queue management that drops rather than lets latency grow unboundedly, and the well-understood relationship between utilisation and queueing delay. Inference serving optimises for average throughput and discovers the tail in customer complaints.

## What Already Exists
Hedged and tied requests for tail reduction; adaptive concurrency limiting that finds the throughput knee automatically; load shedding with priority-aware selection; bounded queues with drop policies; circuit breaking and backpressure; and queueing theory relating utilisation to delay with results that predict exactly the behaviour these systems exhibit.

## The Customization Gap
The adaptation is to a request that streams and whose work is shared with its batch-mates. It requires: (1) a tail defined over the whole stream rather than a single response time, since a request can start fast and stall midway and no conventional latency metric captures that — inter-token gap distribution is the right measure and nobody reports it; (2) adaptive concurrency limits on accelerator memory and batch state rather than on connections, which is where saturation actually occurs; (3) load shedding at admission rather than mid-stream, because abandoning a partially generated response wastes the compute already spent and is worse than never starting; (4) hedging that accounts for a partially completed generation, which is more complex than for an idempotent request and is mostly unexplored; and (5) queueing models with batch-dependent service rates, since the service rate rises with batch size up to a point and then the per-request latency degrades, which is a non-standard and analysable structure.

## Target Customer
Inference providers, serving engine projects, and the reliability engineering community whose practice transfers with a change of unit.

## Impact If Solved
Tail engineering is mature and this category reports means. Inter-token gap distribution is the right tail measure for a streaming response and nobody reports it, and shedding at admission rather than mid-stream avoids paying for work that is then discarded.
