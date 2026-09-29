# Which One Spent Is Not Which One Worked

**Niche:** [[niches/app-marketing-firms/creative-performance-measurement/profile|Creative Performance Measurement]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Networks consume dozens of video and playable variants a week and report which one spent, which under aggregated attribution is not the same as which one worked.
**Tags:** #hypothesis-testing #confidence-intervals #transformers #evaluation-metrics #causal-inference #gradient-boosting #monte-carlo-methods #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to establish which creative actually worked when attribution arrives aggregated — and whoever does that recovers the measurement the privacy regime removed from the one lever still worth pulling.

## The Problem
The team ships forty variants a week across several networks. The networks allocate spend among them using their own models. The aggregated attribution signal that returns carries no creative dimension. So the only creative-level information available is how each network chose to spend, which reflects that network's objective and its own prediction rather than the advertiser's realised outcome. Creative is simultaneously the most important remaining lever and the one whose measurement was most completely removed, and the industry's response has been to accept the proxy.

## Why Nobody Has Built This
The aggregation genuinely removes the creative breakdown, so the easy path is closed and what remains requires design rather than reporting — this is a real constraint rather than neglect, which distinguishes it from most gaps in this cluster. Controlled creative testing costs budget and organisational discipline. Variants are too numerous and individually too small to measure separately. And the network's allocation is available and free.

## What to Build
Recover the signal by design rather than by reporting. Aggregate to the concept level so there is enough volume to measure anything, which is the foundation — forty variants of six concepts is six measurable things and forty unmeasurable ones. Run structured creative tests with controlled allocation, isolating concepts in separate campaigns or geographies where the measurement can attach, since designing the measurement into the buy is the only route once reporting has been removed. Use geographic and temporal variation as a natural experiment, which is available at no extra cost and is currently unexploited. Measure against cohort value rather than installs, so a concept that acquires cheap low-value users is correctly identified. Extract creative attributes automatically so findings transfer across concepts and campaigns, which is what makes the learning cumulative rather than per-asset. Compare the network's allocation against the measured outcome, which quantifies how much the proxy misleads and is the finding that justifies the whole programme. Pool across accounts where an agency can, since creative findings generalise better than most and individual accounts lack power. Detect fatigue at concept level, since that is the operational decision made weekly and is currently made on spend. Feed findings back to production, connecting to the producer niche. And report creative-level measurement coverage honestly, because a team that knows which of its creative decisions are evidenced can concentrate testing where it is not.

## Target Customer
User acquisition and creative leadership, agencies whose creative is their deliverable, and the measurement vendors whose products lost the creative dimension.

## Impact If Built
The aggregation genuinely removed the easy path, so the signal must be designed into the buy rather than read out of a report. Concept-level aggregation turns forty unmeasurable variants into six measurable things, and geographic variation supplies a natural experiment at no cost.
