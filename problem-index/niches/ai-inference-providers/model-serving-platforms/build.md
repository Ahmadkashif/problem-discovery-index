# One Endpoint, Two Opposite Operating Principles

**Niche:** [[niches/ai-inference-providers/model-serving-platforms/profile|Model Serving Platforms]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same endpoint serves a product team who needs a first token in two hundred milliseconds and a data team who needs a hundred million documents scored by Thursday, and optimising for either harms the other.
**Tags:** #markov-chains #convex-optimization #dynamic-programming #evaluation-metrics #revenue-impact #time-series-forecasting #automation #confidence-intervals
**Contested on:** Not terminal — the contest differs by whether latency is constrained, and the decomposition is recorded in the profile.

## The Problem
A provider runs one fleet and one scheduler. A chat product needs its first token fast and its inter-token gaps even, which argues for small batches and reserved headroom. An embedding job needs a hundred million documents processed at the lowest possible cost, which argues for enormous batches and cheap interruptible hardware. Run them on the same policy and the batch job's large batches lengthen the chat product's tail, while the chat product's headroom reservation raises the batch job's cost. Both customers are unhappy, and the provider is competing badly in two markets with one configuration.

## Why Nobody Has Built This
A single endpoint and a single price list is simpler to build, to document and to sell. The batch workload looks like the same product at a different volume, which conceals that its economics are inverted. Separating them requires the scheduler to understand the guarantee attached to each request, which most serving stacks do not model. And the interruptible capacity that makes batch cheap is exactly what an interactive guarantee forbids, so serving both well requires two hardware strategies rather than one.

## What to Build
Build the shared layer honestly and separate the policies. What genuinely generalises is the request's declared service class — a latency objective, an interruptibility flag, a deadline — carried from admission through scheduling to billing, which almost no stack models and which is the precondition for serving both workloads well. Make admission control aware of that class, so a deadline-bound batch request is admitted into spare capacity and an interactive one is admitted only where its objective can be met, rather than both entering the same queue. Report per-class service levels rather than a fleet-wide latency percentile, since the aggregate conceals exactly the trade being made. Share the model weights, the caches and the optimised kernels across both, because those genuinely are common and duplicating them is pure waste. Bill per class, reflecting the cost of the guarantee rather than the count of tokens. Allow a request to be downgraded explicitly — this can wait, run it cheaply — which many callers would accept and none are offered. Keep the interruptible pool physically distinct where the guarantee requires it, and be explicit with customers about which pool serves them. And publish the per-class trade-offs, since a customer choosing a class knowingly is a far better outcome than one discovering the trade in their tail latency.

## Target Customer
Inference providers, the product and data teams on either side of the split, and the serving engine projects whose schedulers do not model service class.

## Impact If Built
Serving both workloads on one policy competes badly in both markets. Carrying a declared service class from admission through billing is the shared primitive neither side has, and it is what lets the scheduler stop averaging two opposite objectives.
