# Real-Time Dispatch From Ride-Hailing

**Niche:** [[niches/game-hosting-providers/matchmaker-objective-design/profile|Matchmaker Objective Design]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Ride-hailing solved batched dispatch under waiting cost at massive scale in real time, and matchmakers still decide greedily.
**Tags:** #optimization-fundamentals #markov-decision-processes #dynamic-programming #convex-optimization #evaluation-metrics #confidence-intervals #time-series-forecasting #numerical-methods
**Contested on:** Every serious competitor in this niche is fighting to turn measured experience costs into a matchmaking policy that runs in milliseconds against a live queue — and whoever builds that policy engine takes the account.

## The Problem
Ride-hailing dispatch is the closest operating analogue: a continuous stream of requests and available supply, a decision about whether to assign now or wait for a better pairing, geographic constraints, and a measured cost of waiting on both sides. The industry moved from greedy nearest-driver assignment to batched optimisation with explicit waiting-cost models, and the improvement was substantial and well documented. Matchmaking has the same structure and largely has not made the same move.

## What Already Exists
Batched dispatch optimisation; waiting cost models on both sides; supply and demand forecasting feeding assignment; geographic and travel-time constraints; and real-time solvers under strict latency budgets.

## The Customization Gap
The adaptation is to matching groups rather than pairs, on quality rather than distance. It requires: (1) assignment of groups of five or ten rather than pairs, which changes the combinatorics fundamentally and is the substantive difference; (2) match quality defined by skill composition rather than by proximity, so the cost function is over a distribution rather than a distance; (3) parties who must be kept together, adding hard constraints with no dispatch analogue; (4) a server region choice alongside the grouping decision, making it a joint assignment and placement problem; and (5) no pricing lever at all — dispatch can use surge to balance supply and matchmaking cannot influence who queues.

## Target Customer
Multiplayer platform vendors, studios with in-house matchmaking, matchmaking providers, and dispatch optimisation vendors.

## Impact If Solved
Ride-hailing moved from greedy assignment to batched optimisation with measured waiting costs and documented the gain. Matching groups on skill composition with no pricing lever is what makes the combinatorics and the balancing different.
