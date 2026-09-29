# Attribution After Deterministic Tracking

**Industry:** [[d2c-brand-operators|D2C Brand Operators]]
**Type:** High Impact
**One-liner:** Every channel claims the same conversions, the platform numbers exceed actual orders, and marketing budget is allocated by people who know the attribution is wrong and have no better basis.
**Tags:** #causal-inference #bayesian-inference #time-series-forecasting #hypothesis-testing #confidence-intervals #linear-regression #evaluation-metrics #revenue-impact

## The Problem
Before mobile platform privacy changes, a brand could follow a customer from an ad impression through to a purchase with reasonable fidelity. That signal is largely gone, and nothing has replaced it.

What a brand has now is a set of disagreeing accounts. Meta reports conversions using its own modelling and a generous attribution window. Google reports its own. The analytics platform reports something different again. Sum the platform-claimed conversions and the total commonly exceeds actual orders, sometimes substantially.

The brand's own order data is the only ground truth, and it does not say where the customer came from. Post-purchase surveys asking how the customer heard about the brand are the most honest signal many brands have, which is a remarkable statement about the state of a heavily instrumented industry.

Decisions get made anyway. Budget shifts between channels weekly, based on numbers everyone in the room knows are unreliable. Incrementality — whether an ad caused a purchase that would not otherwise have happened — is the question that matters and is almost never answered, because answering it requires deliberately withholding spend, which nobody wants to do.

The consequence is systematic misallocation. Channels good at claiming credit for purchases that would have happened anyway are overfunded; channels that genuinely create demand and cannot demonstrate it are underfunded.

## Why It's Unsolved
The signal loss is structural and permanent. It is a deliberate platform design decision, and no amount of technical work restores deterministic cross-site tracking.

Media mix modelling is the correct statistical answer and is hard to apply at this scale. It requires substantial variation in spend across channels over time to identify effects, and most brands change spend in correlated ways in response to the same conditions. Smaller brands have too little history and too much noise.

Incrementality testing is the gold standard and requires deliberate holdouts — turning off spend in a geography or for a cohort — which costs revenue in the short term and which growth teams under monthly pressure will not do.

The vendors filling the gap mostly read platform data back with a different attribution model applied. That is a presentation improvement, not a measurement one, and the resulting numbers still rest on the platforms' own claims.

And the honest answer is uncomfortable: for many brands, the level of attribution certainty they had five years ago is not recoverable, and planning should adapt to that rather than pretend otherwise.

## What a Solution Looks Like
Incrementality as the primary measurement, made cheap enough to run continuously. Geographic holdouts, staggered rollouts and matched-market designs give causal estimates without abandoning a channel, and the reason they are rare is operational friction rather than cost. A brand running one properly designed test per quarter learns more than one buying three attribution tools.

Media mix modelling anchored on those tests. The persistent weakness of these models is that they are fitted to observational data with correlated spend; calibrating them against a small number of real experiments resolves most of the identification problem and is the approach the serious practitioners use.

Honest uncertainty. A channel contribution reported as a range, with the range widening where the data cannot support precision, is more useful for a budget decision than a false point estimate.

Customer-level economics as the anchor. The brand's own data supports the questions that actually matter — what a cohort acquired through a given channel is worth over time, whether repeat rates differ by acquisition source — and those are measurable without any platform cooperation.

## Impact If Solved
Marketing is the largest controllable cost for most direct-to-consumer brands and it is allocated on numbers everyone involved knows are wrong. Cheap continuous incrementality testing calibrating a mix model is the established method, is within reach of any brand with real spend, and is the difference between allocating on evidence and allocating on the platforms' own marketing.
