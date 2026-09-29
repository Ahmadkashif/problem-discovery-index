# Experiments When It Matters

**Niche:** [[niches/robo-advisors/drawdown-intervention/profile|Drawdown Intervention]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nobody knows whether the reassuring email prevents panic sales, makes them worse, or does nothing, and it has been sent in every drawdown for a decade.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #revenue-impact #descriptive-statistics #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to find out what actually stops a client selling at the bottom — and whoever has run the experiments owns causal evidence nobody else in the industry has.

## The Problem
When markets fall, platforms send commentary, show banners, and call their largest clients. Whether any of it reduces panic selling is unknown. It is plausible that a message drawing attention to a decline increases selling among clients who had not noticed. It is plausible that a friction step helps some clients and enrages others. These are causal questions with a clean experimental design available and a population of millions, and the industry has run essentially no experiments because market events feel like the wrong moment to withhold reassurance from anyone.

## Why Nobody Has Built This
Withholding an intervention during a crisis feels indefensible, so no control group is ever held out — and without a control nothing is ever learned, which guarantees the next crisis is equally uninformed. Interventions are owned by marketing and measured on open rates. Market events are rare and unplanned, so there is never a prepared design. And an experiment that showed the standard message makes things worse would be unwelcome.

## What to Build
Prepare the experiments before the event. Design the intervention trials in advance, which is the core — the reason none exist is that nobody has a protocol ready when a drawdown starts, and building it in calm markets removes every practical objection. Randomise across intervention types rather than against no intervention at all, since comparing message A to message B raises none of the ethical objections and answers most of the question. Define the outcome as realised behaviour — did the client sell, by how much, and what did it cost them — rather than as engagement. Estimate heterogeneous effects, because the intervention that helps a nervous new client may harm a disengaged long-term one, and a single average effect will hide it. Target by predicted risk from the measurement side, so the trial concentrates where the behaviour is at stake. Test delay and friction as interventions, since they are the most plausible mechanisms and the least tested. Include a call from a licensed associate as an arm, because it is the most expensive intervention and its effect is entirely assumed. Measure harm as carefully as benefit, as an intervention that increases selling must be findable. Accumulate results across events into a standing body of evidence, which is what compounds. And publish what is learned, since the credibility of being the platform that knows is substantial.

## Target Customer
Product and marketing leadership, investment leadership accountable for client outcomes, licensed service teams whose calls are unmeasured, and behavioural researchers with no experimental access.

## Impact If Built
No control group is ever held out during a crisis, which guarantees nothing is learned and the next crisis is equally uninformed. Comparing intervention arms rather than withholding removes the objection entirely and answers the question.
