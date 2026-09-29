# Forecasting a Career

**Niche:** [[niches/creator-talent-agencies/trajectory-forecasting/profile|Trajectory Forecasting]]
**Industry:** [[industries/creator-talent-agencies|Creator Talent Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nobody in the industry forecasts a trajectory; they observe one and call it a signing decision.
**Tags:** #survival-analysis #time-series-forecasting #gradient-boosting #evaluation-metrics #confidence-intervals #cross-validation #hypothesis-testing #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to predict whether an individual creator's career will sustain, from signals available before the peak — and whoever forecasts durability better than a follower count signs the people everyone else misses and declines the ones everyone else overpays for.

## The Problem
The question at signing is whether this person will still be earning in three years. The available evidence is rich and public: how their audience grew, whether the growth came from one piece of content or many, whether their audience returns, how consistently they publish, whether they exist anywhere other than one platform, what their income depends on. None of it is combined into a forecast. The decision is made on the level of the number rather than on anything about its durability.

## Why Nobody Has Built This
The decision is made by a person whose value is their judgement, so a model reads as a challenge to the thing they are paid for — a profession that sells instinct does not commission a forecast of the same question. Outcomes take years and are not recorded. Sample sizes at any one agency are small. And the industry is young enough that nobody has assembled a history.

## What to Build
Model survival from the signals that exist before the peak. Build a survival model of creator income persistence, which is the core and is the right framing — the question is not how big but how long. Use growth shape rather than level, since a compound build and a viral spike look identical in a follower count and completely different in a curve. Measure audience retention across releases, as a returning audience is the durable asset and reach is not. Measure format and platform concentration, because dependence on one thing is the dominant failure mode. Include off-platform presence and revenue mix, since diversification is the creator's own resilience and is visible. Assemble the outcome history from public data across many creators rather than only from one agency's signings, which is how the sample size problem is solved. Express the forecast as a probability with an interval, because certainty here would be false and would be correctly distrusted. Present it as one input to a manager's judgement, as adoption depends entirely on not appearing to replace them. Validate on held-out cohorts, which is possible with public data and is what would make it credible. And record every signing decision and its reasoning, so the firm's own evidence accumulates.

## Target Customer
Signing and talent leadership, agency investors, creators negotiating terms, and talent analytics vendors.

## Impact If Built
A profession that sells instinct does not commission a forecast of the same question, so trajectory is observed rather than predicted. Growth shape, audience retention and format concentration are public, and the outcome history can be assembled across the whole market.
