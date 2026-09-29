# Bandit Exploration Practice

**Niche:** [[niches/live-commerce-platforms/cold-start-stream-ranking/profile|Cold-Start Stream Ranking]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Exploration under uncertainty is a mature theory with mature tooling, and it assumes the arm you are exploring will still exist tomorrow.
**Tags:** #bayesian-inference #monte-carlo-methods #confidence-intervals #evaluation-metrics #optimization-fundamentals #hypothesis-testing #gradient-boosting #automation
**Contested on:** Every serious competitor in this niche is fighting to rank a stream that has existed for four minutes against streams with hours of accumulated signal — and whoever gets the first minutes right decides which sellers survive.

## The Problem
Multi-armed bandits and contextual exploration are well-developed, widely deployed and well served by libraries and platform infrastructure. Content platforms use them routinely to decide how much traffic to give an untested item. The whole framework rests on an assumption so basic it is rarely stated: the arm persists, so information bought today pays off tomorrow. A live stream's arm disappears in two hours, which changes the economics of every exploration decision and is not a parameter anyone exposes.

## What Already Exists
Contextual bandit frameworks with Thompson sampling and upper-confidence-bound policies; exploration budgets and traffic allocation infrastructure; off-policy evaluation; warm-start techniques from item features; and experiment platforms with sequential testing.

## The Customization Gap
The adaptation is from persistent arms to expiring ones. It requires: (1) a finite and known arm lifetime entering the allocation decision directly, so exploration value decays to zero at the stream's end — the standard formulations have no term for this and it is the central change; (2) information that survives the arm, since what is learned about a stream is worthless afterwards unless it is attributed to the seller, which makes seller-level posterior updating the actual object of learning; (3) exploration priced against seller retention as well as viewer value, because the two-sided marketplace makes under-exploration a supply cost that no single-sided formulation captures; (4) within-arm non-stationarity, as a stream's quality genuinely changes as the host moves through inventory, violating the stationarity assumption in a way that is real rather than nuisance; and (5) decisions at feed-serving latency, which rules out anything requiring a solve per request.

## Target Customer
Live commerce platforms, recommendation infrastructure teams, and experimentation vendors whose exploration tooling assumes persistent items.

## Impact If Solved
Every exploration framework assumes information bought today pays off tomorrow, and a two-hour arm breaks that quietly. Making the seller rather than the stream the object of posterior updating is what lets any learning survive the arm.
