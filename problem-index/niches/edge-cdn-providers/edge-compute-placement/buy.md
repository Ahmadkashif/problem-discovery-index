# Operator Placement From Distributed Query Processing

**Niche:** [[niches/edge-cdn-providers/edge-compute-placement/profile|Edge Compute Placement]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Deciding where to execute an operation relative to the data it needs is the operator placement problem, solved in distributed databases and stream processing, and edge placement is decided by intuition.
**Tags:** #graph-theory #dynamic-programming #optimization-fundamentals #convex-optimization #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to tell a customer whether moving a given piece of logic to the edge would actually improve anything — and whoever answers that takes the edge compute market, because the capability is universal and the reasoning is absent.

## The Problem
Distributed query processing has a well-developed answer to where computation should happen: push the operation to the data when the data is large and the result is small, pull the data to the operation when the reverse holds, and compute the cost of each option explicitly. Stream processing systems solve the same problem for operator placement across a network. Edge compute placement is the identical question — compute here or there, given where the data is and what the network costs — and is answered by architectural intuition.

## What Already Exists
Operator placement algorithms from distributed query processing; predicate pushdown and its cost models; stream processing operator placement research with network-aware formulations; latency and bandwidth modelling; and the general cost-based optimisation framework databases use for exactly this class of decision.

## The Customization Gap
The adaptation is to request-handling logic rather than to data operators. It requires: (1) a dependency model for the logic — which state it reads, which it writes, what consistency it needs — which is an application-level fact the provider does not have and must be supplied or inferred from observed behaviour, and is the piece that determines the whole answer; (2) a latency-dominated cost model rather than a throughput-dominated one, since a single user request's round trips matter and the aggregate data volume usually does not, which inverts the usual weighting; (3) treatment of consistency requirements as constraints, because logic requiring a strongly consistent read cannot be placed away from the authoritative store regardless of latency, and this rules out a large share of candidates immediately; (4) an objective including cost as well as latency, since the pricing models differ substantially between edge and origin and a latency-only optimisation will recommend placements the customer cannot afford; and (5) partial placement, since a piece of logic frequently splits into a cacheable decision that belongs at the edge and a consistent one that does not, and the split is the actual answer more often than the binary.

## Target Customer
Edge providers, application platform and architecture teams, and the framework vendors building edge-first application models.

## Impact If Solved
A mature placement discipline answers exactly this question and has not been applied, leaving a universal capability without any reasoning behind its use. The state dependency model is the required input, and partial placement is more often the right answer than the binary choice the question is usually posed as.
