# Held to a Payback Somebody Else Determines

**Industry:** [[game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Worker Life Changing
**One-liner:** The UA manager is measured on cohort payback, and cohort payback is determined mostly by what the game team ships in the six months after the install.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #confidence-intervals #time-series-forecasting #evaluation-metrics #worker-facing #revenue-impact

## The Problem
A user acquisition manager is accountable for return on ad spend and payback period. Those numbers are produced by two things: the players acquired, which UA influences, and what the game does with them, which UA does not.

A cohort acquired before a strong content run, a well-designed event or a monetisation improvement performs well. An identical cohort acquired before a quiet quarter, a poorly-received update or a balance change that upset the community performs badly. The manager's performance review does not distinguish these.

The information flow makes it worse. UA frequently learns about content and monetisation changes at the same time as players, and is expected to have forecast a payback that depends on them. Spend commitments are made months ahead against a content roadmap that moves.

And the direction of blame is asymmetric. When cohorts underperform, the diagnosis starts with acquisition source quality and creative, because those are the things UA controls and can be examined. When cohorts overperform, the game team's content is credited. Both readings are available in the same data and only one gets used.

## Why It Matters to the Worker
This is accountability without control, in a role that is measured with unusual numerical precision — which makes it worse rather than better, because the number looks objective. A UA manager can do excellent work and post poor payback, and have no defensible way to demonstrate the difference.

It also distorts behaviour. A manager who knows they will be judged on a number they partly do not control optimises toward the sources that look good on the metrics reported quickly, which is a bias toward short-horizon retargeting-like traffic and away from the exploration that finds new audiences.

And it poisons a relationship that ought to be collaborative. UA and the game team both want the same outcome and are placed in an implicit dispute about credit, with no evidence available to either side, repeated every quarter.

## What a Solution Looks Like
Decompose the cohort outcome. The same acquisition sources are observed across many content periods, which makes it estimable how much of a cohort's realised value is attributable to acquisition and how much to what shipped afterwards. That analysis is straightforward and nobody runs it, because neither function benefits from raising it and both would benefit from having it.

Report performance against a content-adjusted baseline. A UA manager evaluated on how their cohorts performed relative to what comparable cohorts did in the same content period is being evaluated on their actual contribution, which is what a fair metric looks like.

Put the roadmap into the forecast. Payback projections that incorporate the planned content cadence — and that update when the roadmap moves — make the dependency explicit and turn a hidden risk into a stated assumption.

Fix the information flow. UA knowing what is shipping, when, and what it is expected to do to retention and monetisation is a coordination problem with no technical difficulty and considerable value, and its absence is the clearest symptom of the two functions being managed as separate businesses.

## Impact If Solved
UA is one of the most quantitatively rigorous functions in any consumer business and is evaluated on a number that is jointly determined with a team it does not control. Decomposing the contribution, reporting against a content-adjusted baseline and building the roadmap into the forecast would make the metric fair — and would convert a recurring quarterly dispute into a shared planning problem, which is what it actually is.
