# Recommendation Objectives Beyond Watch Time

**Industry:** [[ugc-video-platforms|UGC Video Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The recommender optimises time spent, which is measurable and immediate, and nobody measures whether the viewer was glad afterwards.
**Tags:** #markov-decision-processes #causal-inference #bayesian-inference #survival-analysis #transformers #confidence-intervals #evaluation-metrics #policy-gradient-methods

## The Problem
Recommendation on these platforms is optimised against engagement — watch time, session length, completion, return frequency. Those targets are immediate, abundant and unambiguous, which is why they were chosen, and they are also systematically biased toward content that holds attention without satisfying anyone. The failure mode is familiar to every user: an hour spent, no memory of what was watched, a mild sense of having been had.

The consequences run further than individual regret. Objectives that reward retention favour the emotionally activating, which shapes what creators make — because creators optimise against the recommender, and a system that rewards outrage produces outrage. That is not an unintended side effect of a mysterious process; it is the objective function working correctly.

Platforms have made real attempts at this. Survey-based satisfaction signals, downranking of borderline content, and explicit quality adjustments have all been deployed and have improved things at the margin. The core objective remains engagement because it is what the advertising business monetises and what the measurement infrastructure was built around.

## What Already Exists
These are the most sophisticated recommender systems in existence, with substantial published research behind them. Satisfaction surveys are run at scale and fed into ranking at several platforms. Sequence models capture long-horizon session structure. Some platforms expose limited controls — not interested, don't recommend this channel — and reduced-distribution mechanisms for borderline content. Well-being features such as time reminders exist and are generally weak by design.

## The Customisation Gap
The gap is that long-horizon viewer value is estimable and is not the objective. Whether a viewer returned over months, whether their sessions became more or less satisfying, whether a recommendation led to sustained interest in a subject or to a single compulsive evening — these are measurable at the individual level over long windows, and optimising for them is a reinforcement learning problem with a delayed and noisy reward rather than an impossible one.

Regret is the specific missing measurement. It can be approached directly — asking, sparsely and non-intrusively, whether time was well spent — and indirectly, through behavioural signatures that distinguish absorbed viewing from compulsive viewing: abrupt session termination, immediate app closure after a long autoplay chain, the return pattern that follows. Very few platforms have published serious work on this and it is the quantity the whole debate concerns.

The creator-side effect needs measuring too. What the recommender rewards determines what gets produced, and a platform can estimate the elasticity — how the content mix shifts when ranking weights change — from its own historical ranking changes. That would make the production consequences of an objective change visible before it ships rather than after it has reshaped a genre.

And the viewer should have real control. Meaningful, persistent, granular preferences — less of this subject, more of this depth, not this pattern — currently exist as weak signals absorbed into a model, and a system that honoured them explicitly would be a different product.

## Impact If Solved
The objective function of these recommenders is the single most consequential design choice in consumer media, shaping both what a billion people watch and what a generation of creators makes. Measuring regret and long-horizon viewer value gives the debate a metric instead of an argument, and estimating the production-side elasticity means an objective change can be evaluated for its effect on the ecosystem before it is deployed rather than discovered in its aftermath.
