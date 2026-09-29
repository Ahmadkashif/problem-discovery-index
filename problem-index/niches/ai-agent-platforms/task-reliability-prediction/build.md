# Answered With a Demo and a Pilot

**Niche:** [[niches/ai-agent-platforms/task-reliability-prediction/profile|Task Reliability Prediction]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Customers need to know before deployment what fraction of tasks an agent will complete correctly and which ones it will fail, and the category answers with a demo and a pilot.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #gradient-boosting #cross-validation #large-language-models #descriptive-statistics #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to tell a buyer, before deployment, what fraction of their tasks the agent will complete correctly and which ones it will fail — and whoever does that takes the account, because no other claim in this market is checkable.

## The Problem
A support organisation evaluates an agent for refund processing. The demo is excellent. The pilot runs two hundred tickets, mostly selected by the vendor's forward-deployed engineer as representative, and reports a high resolution rate. In production the agent meets the ticket types nobody picked for the pilot — partial refunds across two orders, a customer in a jurisdiction with different rules, a case where the order record is inconsistent — and fails on a meaningful share of them, several times in ways that cost money. Nothing in the evaluation predicted this, because the evaluation sampled from the wrong distribution and reported an aggregate.

## Why Nobody Has Built This
Predicting performance on the buyer's distribution requires the buyer's historical tasks, which arrive late in a sales cycle and are messy. Reporting a segmented estimate produces uncomfortable numbers on exactly the segments the buyer cares most about. The category is young and growing on demos, so the pressure to become measurable has not yet arrived. And making a number contractible means being held to it.

## What to Build
Estimate over the buyer's own distribution and name the failures. Sample the buyer's historical task log, characterise it into types, and run the agent against a stratified sample — which replaces a curated pilot with a representative measurement and is the core of the build. Report the estimate per task type rather than in aggregate, since the aggregate hides that the agent is excellent on the eighty percent that are easy and unreliable on the twenty that are expensive, and that segmentation is the buyer's actual decision input. Name the failure modes with examples, because a buyer can design around a known failure and cannot design around an unknown rate. Compare against the human baseline on the same sample, which is the comparison the buyer is implicitly making and which frequently flatters the agent in ways nobody has demonstrated. Report uncertainty, since a pilot of two hundred cannot resolve a five-point difference and the current practice quotes single figures. Predict per-task confidence at run time, so the agent can defer on the cases it is likely to fail, which is where the reliability question meets the authorisation question. Track predicted against realised reliability after deployment, which is what makes the estimate trustworthy the second time. And attach a commitment, because a number nobody stands behind is a demo in numeric form.

## Target Customer
Buyers evaluating agent deployments, the risk owners who must approve them, and the vendors whose genuinely reliable agents cannot currently prove it.

## Impact If Built
A curated pilot samples the wrong distribution and reports the wrong statistic. A stratified estimate over the buyer's own task log, segmented by type with failure modes named, is what turns a leap of faith into a procurement decision.
