# Cost Accounting and Operations Research

**Niche:** [[niches/ai-inference-providers/inference-cost-corpus/profile|Inference Cost Corpus]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Manufacturing built activity-based costing and capital-intensive industries built asset utilisation analysis, and inference providers allocate cost per token as a flat division.
**Tags:** #revenue-impact #convex-optimization #descriptive-statistics #evaluation-metrics #confidence-intervals #optimization-fundamentals #time-series-forecasting #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to turn request-level history into an empirical account of what inference actually costs — and whoever does that prices, provisions and optimises against evidence while everyone else guesses.

## The Problem
Allocating the cost of expensive shared assets to the activities that consume them is what activity-based costing was built for, and capital-intensive industries — airlines, shipping, semiconductor fabrication — developed sophisticated asset utilisation analysis around the same problem. Inference providers divide total cost by total tokens, which averages across models, hardware generations, concurrency regimes and customers that differ by an order of magnitude in what they actually consume.

## What Already Exists
Activity-based costing with cost driver identification and allocation; contribution margin analysis by product and customer; asset utilisation and overall equipment effectiveness from manufacturing; capacity cost accounting distinguishing used from unused capacity; and operations research for capacity and asset allocation under uncertainty.

## The Customization Gap
The adaptation is to a cost driver that depends on the workload's own composition. It requires: (1) the cost driver defined as accelerator time weighted by memory occupancy, since a request's cost depends on what it was batched with and a token is not a unit of cost — which is the central accounting insight and is entirely absent from current practice; (2) explicit accounting for unused capacity as a separate line rather than spreading it across served requests, which is standard capacity cost accounting and would immediately reveal the insurance component; (3) depreciation on a schedule reflecting accelerator generations rather than a standard asset life, since the useful life is set by the next generation's arrival; (4) customer contribution analysis that accounts for the headroom a latency guarantee reserves, which is a real cost attributable to specific customers and currently attributed to nobody; and (5) continuous recomputation, since the cost structure changes with every hardware generation and every model mix shift.

## Target Customer
Inference providers, their finance functions, their investors, and the cost accounting and operations research professions for whom this is a fresh capital-intensive industry with none of the practice.

## Impact If Solved
A token is not a unit of cost, and the whole industry prices as though it were. Weighting accelerator time by memory occupancy is the correct cost driver, and separating unused capacity as its own line reveals the insurance component immediately.
