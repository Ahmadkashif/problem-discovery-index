# Long-Term Value Optimisation From Reinforcement Learning

**Niche:** [[niches/streaming-video-platforms/discovery-and-personalisation/profile|Discovery & Personalisation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sequential decision-making under a long-horizon reward is a developed field, and recommenders still optimise the next click.
**Tags:** #markov-decision-processes #policy-gradient-methods #temporal-difference-learning #causal-inference #evaluation-metrics #confidence-intervals #model-based-rl #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to get each subscriber to the title that will keep them subscribed rather than the one they will watch tonight — and whoever optimises recommendation for retention rather than for engagement changes what the catalogue is worth.

## The Problem
Optimising a sequence of decisions for a delayed reward is exactly what reinforcement learning addresses: value functions over long horizons, off-policy evaluation, exploration under uncertainty, and the explicit separation of immediate reward from long-term return. The field is mature and the framing fits recommendation precisely. Production recommenders overwhelmingly optimise an immediate proxy because it is easier to train and evaluate.

## What Already Exists
Value-based and policy-based reinforcement learning; off-policy evaluation with importance weighting; exploration strategies under uncertainty; reward shaping and credit assignment; and safe deployment practice for learned policies.

## The Customization Gap
The adaptation is to a reward that arrives monthly and once. It requires: (1) a reward that is a subscription renewal — sparse, binary, monthly and attributable to hundreds of prior decisions, which is an extreme credit assignment problem and is the substantive difficulty; (2) exploration that costs a real subscriber a bad evening, so exploration must be conservative and targeted; (3) off-policy evaluation as the primary tool, since online experiments on a long horizon take months; (4) a catalogue changing continuously as licences begin and end, so the action space is non-stationary; and (5) content valuation depending on the policy, which creates a feedback loop between two of the business's decisions.

## Target Customer
Product and data leadership, recommendation teams, content leadership, and machine learning platform vendors serving media.

## Impact If Solved
The framing fits precisely and production systems use an immediate proxy because it trains easily. The real difficulty is credit assignment across hundreds of decisions to one monthly binary reward, which is where the research and the industry problem meet.
