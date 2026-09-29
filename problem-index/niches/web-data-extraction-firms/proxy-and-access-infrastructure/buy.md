# Adaptive Routing and Multi-Armed Allocation

**Niche:** [[niches/web-data-extraction-firms/proxy-and-access-infrastructure/profile|Proxy & Access Infrastructure]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Choosing repeatedly among options with uncertain and changing payoffs is the bandit problem, solved thoroughly, and address selection is done with rotation rules written by hand.
**Tags:** #markov-decision-processes #monte-carlo-methods #bayesian-inference #convex-optimization #evaluation-metrics #confidence-intervals #automation #probability-distributions
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver successful requests against evolving detection at the lowest cost per success — and whoever does that takes the account, because the buyer meters exactly that and switches on it.

## The Problem
Deciding which address, region, session strategy and pacing to use for the next request against a given target, when the payoffs are uncertain and shift as the target adapts, is a textbook sequential decision problem. Bandit algorithms handle exactly this, including the non-stationary case where the best option changes over time. Proxy networks rotate addresses according to rules a person wrote and adjust when somebody notices a drop.

## What Already Exists
Multi-armed bandit algorithms with strong regret guarantees; non-stationary and adversarial bandit variants for changing environments; contextual bandits for conditioning on request features; reinforcement learning for sequential allocation; and adaptive load balancing from serving infrastructure.

## The Customization Gap
The adaptation is to an environment where the payoff mechanism is actively adapting to you. It requires: (1) adversarial rather than stochastic assumptions, since the target changes its detection in response to your behaviour and a stochastic bandit will be exploited — the adversarial variants exist and are the right family, which almost nobody in this market has recognised; (2) a cost of exploration that includes burning an address, because a failed probe does not merely waste a request, it can mark an address as detected and remove it from the pool permanently, which is a much heavier exploration cost than the standard formulation assumes; (3) context features covering target, geography, time of day, session state and address type, which is a natural contextual bandit and is currently a rules table; (4) per-target rather than global policies, since the environments are independent and pooling them loses everything; and (5) explicit non-stationarity handling, because a target deploying a new defence is a change point and a slow-adapting policy spends heavily before noticing.

## Target Customer
Proxy networks, extraction firms operating their own access, and the sequential decision-making research community.

## Impact If Solved
Address selection is a textbook sequential decision problem solved with hand-written rules. The adversarial variants are the right family here, and the heavy exploration cost — a failed probe can permanently burn an address — is the distinctive modelling requirement.
