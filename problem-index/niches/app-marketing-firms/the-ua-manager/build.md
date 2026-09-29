# A Seven-Figure Decision Every Monday

**Niche:** [[niches/app-marketing-firms/the-ua-manager/profile|The UA Manager]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The user acquisition manager allocates a seven-figure budget every week across four disagreeing sources and unscored predictions, and carries full accountability for the payback.
**Tags:** #worker-facing #convex-optimization #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #optimization-fundamentals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give the manager a defensible allocation instead of a weekly judgement across four disagreeing sources — and whoever does that changes how a large share of mobile advertising spend is decided.

## The Problem
Monday. Reconcile four sources that disagree. Apply the mental discount to each network's self-reported numbers. Adjust for the aggregated signal being incomplete for the recent period. Judge which campaigns are genuinely working from predictions whose accuracy nobody has measured. Account for the campaigns whose signal is suppressed. Decide where seven figures goes. Do this every week, under a payback target, with the whole thing resting on judgement accumulated over years. It works well enough that the business continues, it is entirely unexamined, and it lives in one person's head.

## Why Nobody Has Built This
Tools in this category were built for buying and reporting rather than for deciding, so the actual decision is the one step with no software — the vendors serve the operations around the judgement and not the judgement itself. Each manager's adjustments are personal and undocumented. The decision is made under time pressure in a spreadsheet. And expertise is valued as a personal asset, which makes systematising it feel like a threat.

## What to Build
Support the decision itself. Consolidate the reconciled view and the scored predictions into one allocation surface, which is the foundation and puts the inputs in one place for the first time. Recommend an allocation with its reasoning, treating it as a constrained optimisation against payback with the uncertainty carried through, since the manager is solving this mentally and a stated optimisation makes the trade-offs explicit. Encode the manager's adjustments as explicit parameters rather than leaving them as instinct, which is the fix note's subject. Show the sensitivity of the allocation to each uncertain input, so the manager knows which of their unknowns actually matter this week. Flag what changed since last week and why, which is most of what the weekly review is for. Handle the suppressed and low-volume campaigns explicitly rather than leaving them to judgement. Record every allocation decision and its outcome, which is the basis for the manager improving and for the organisation retaining what they know. Support the scenario question directly, since the conversation with leadership is always about what happens if we spend more or less rather than about last week. Preserve the manager's override with the reasoning captured, because the judgement is genuinely good and the aim is to support it rather than replace it. And measure allocation quality against realised payback, since that comparison is the only way anyone learns whether the judgement is working.

## Target Customer
User acquisition managers and growth leadership, agencies allocating client budgets, and the tooling vendors serving everything around the decision.

## Impact If Built
Tools serve the operations around the judgement and not the judgement itself, so the actual decision is the one step with no software. Consolidating the inputs and recommending an allocation with sensitivity shown makes explicit what one person is currently solving mentally every Monday.
