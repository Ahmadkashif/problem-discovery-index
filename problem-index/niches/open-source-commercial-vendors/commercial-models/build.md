# Converting Use Into Revenue, Without Evidence

**Niche:** [[niches/open-source-commercial-vendors/commercial-models/profile|Commercial Models]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The category's central commercial decisions — what to put behind a licence, what to host, what to charge — are made by argument, because the evidence that would inform them has never been assembled.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor here is fighting to convert use of freely available software into revenue — and that contest is fought against the free edition in one model and against a hyperscaler in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
A vendor's leadership debates whether a new capability should be open or commercial. The arguments are about community goodwill, competitive positioning and what feels fair, and they are conducted entirely without evidence — nobody knows which of the existing commercial features customers actually bought for, which open features drive adoption that later converts, or what the previous boundary decision did to either. The decision is made, defended for two years, and revisited when the pressure returns. This is the most consequential recurring decision in the category and it is made the way it was made in 2015.

## Why Nobody Has Built This
The measurement requires knowing who uses what, which is the adoption visibility problem and is unsolved. Attributing a purchase to a feature requires asking customers systematically or observing usage before and after conversion, neither of which is routine. The decisions are also genuinely strategic, involving community relations and competitive dynamics that no metric captures, which has been used to justify not measuring the parts that are measurable. And the natural experiments that have occurred — licence changes, boundary moves, features opened or closed — have not been evaluated by the companies that ran them.

## What to Build
The evidence layer both sub-niches need. Establish which commercial features are actually used by paying customers and which are used by nobody, which is straightforward for a hosted or licensed product and is the first thing anyone should know before moving a boundary. Attribute purchase to features by asking at the point of conversion and by observing usage in the period before it, since both signals are obtainable and neither is collected systematically. Evaluate past boundary decisions retrospectively — what happened to adoption, to conversion and to community sentiment after each — which is the natural experiment the company already ran and never analysed. Model the substitution properly: a feature behind a licence is bought only if doing without it is harder than paying, and the relevant question is how hard the alternative is rather than how valuable the feature is, which is a different and more answerable question. Track fork and reimplementation risk, since a boundary that provokes a viable community alternative is a decision with a delayed and severe cost. And bring the evidence to the decision rather than producing it afterwards, which is the organisational change and the point of the whole exercise.

## Target Customer
Commercial and executive leadership at open-source companies, and the investors and boards asking whether the model is working.

## Impact If Built
The most consequential recurring decision in the category is made by argument, and several of its inputs are measurable and uncollected. Evaluating past boundary decisions is free — the experiments have already been run — and would inform the next one more than any amount of reasoning.
