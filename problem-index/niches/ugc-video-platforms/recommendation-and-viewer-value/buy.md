# Long-Horizon Objectives From Reinforcement Learning

**Niche:** [[niches/ugc-video-platforms/recommendation-and-viewer-value/profile|Recommendation & Viewer Value]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reinforcement learning is built around the difference between immediate reward and long-term return, and recommenders optimise the immediate one.
**Tags:** #markov-decision-processes #policy-gradient-methods #temporal-difference-learning #causal-inference #evaluation-metrics #confidence-intervals #model-based-rl #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to optimise for a viewer who is glad they watched rather than one who watched for longer — and whoever measures that instead of assuming it holds the attention everyone else is burning.

## The Problem
The distinction between immediate reward and long-term return is the founding idea of reinforcement learning, along with the machinery to act on it: value functions over long horizons, discounting, credit assignment, off-policy evaluation and reward shaping. Production recommenders use reinforcement learning framings in places and still overwhelmingly optimise an immediate engagement signal, because it is what can be measured and attributed quickly.

## What Already Exists
Value-based and policy-based methods over long horizons; discounting and credit assignment; off-policy evaluation; reward shaping and multi-objective formulations; and safe policy deployment practice.

## The Customization Gap
The adaptation is to a reward that is a person's judgement about their own time. It requires: (1) a reward signal that must be constructed rather than observed, since satisfaction is not logged and time spent is — constructing it is the substantive work and everything else follows; (2) horizons measured in months of retention rather than in an episode; (3) credit assignment across thousands of recommendations to one retention outcome; (4) a business metric that the new objective must not destroy in the short term, which constrains deployment; and (5) third-party effects on creators, which no standard formulation represents and which are material here.

## Target Customer
Product and data leadership, viewers, regulators, and machine learning platform vendors.

## Impact If Solved
The framing is the founding idea of the field and production systems optimise the immediate signal because it is what is logged. Constructing a satisfaction reward is the substantive work, and everything else in the toolkit is already available.
