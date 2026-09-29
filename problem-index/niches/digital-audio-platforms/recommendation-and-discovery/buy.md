# Exploration From Bandit Practice

**Niche:** [[niches/digital-audio-platforms/recommendation-and-discovery/profile|Recommendation & Discovery]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Exploration under uncertainty is a solved field and recommenders exploit, which is why a hundred thousand daily arrivals go unheard.
**Tags:** #markov-decision-processes #monte-carlo-methods #matrix-decompositions #evaluation-metrics #confidence-intervals #policy-gradient-methods #causal-inference #contrastive-learning
**Contested on:** Every serious competitor in this niche is fighting to surface the right track from a catalogue receiving a hundred thousand arrivals a day, against an objective that reliably favours what is already familiar.

## The Problem
Balancing exploration against exploitation is a well-developed area: bandit algorithms, optimism under uncertainty, Thompson sampling, and the explicit understanding that a system which only exploits never learns about anything new. Recommenders use exploration at the margins, tuned to avoid harming engagement metrics, which means the exploration budget is set by the metric that exploration reduces in the short run.

## What Already Exists
Bandit algorithms and exploration schedules; optimism and uncertainty-driven selection; off-policy evaluation; cold start strategies for new items; and exploration budget tuning practice.

## The Customization Gap
The adaptation is to items whose exposure is someone's income. It requires: (1) exploration as a distributional obligation rather than only an information-gathering strategy, since a new track's commercial existence depends on it — this reframes the exploration budget as a policy choice rather than a tuning parameter; (2) a hundred thousand new items daily, which is a far larger cold start problem than most bandit deployments face; (3) items that are creative works with long tails rather than products with short relevance; (4) an adversary injecting fake engagement, which corrupts the exploration signal specifically; and (5) a listener whose experience must not degrade, bounding how much exploration is tolerable.

## Target Customer
Product and data leadership, artists and labels, and recommendation platform vendors.

## Impact If Solved
The exploration literature is mature and the budget is set by the metric exploration reduces. Reframing it as a distributional obligation rather than a tuning parameter is the adaptation, and the daily arrival rate makes it the hardest cold start problem anywhere.
