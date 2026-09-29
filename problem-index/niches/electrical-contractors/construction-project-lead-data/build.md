# Project Outcomes as Feedback on Lead Quality

**Niche:** [[niches/electrical-contractors/construction-project-lead-data/profile|Construction Project Lead & Plan Data]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every published lead is a prediction that a real project will go to bid at roughly this scope and value, and the world settles all of them — the project bids, changes, or dies — with none of it fed back.
**Tags:** #gradient-boosting #survival-analysis #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #feature-engineering #time-series-forecasting #data-integration #revenue-impact

## The Problem
A lead asserts that a project exists, at a stage, with a scope and an estimated value, and will bid around a date. Subscribers allocate expensive estimating capacity against those assertions — an electrical contractor pursuing a project that never bids has burned a week of its scarcest resource. Each assertion resolves: the project bids on some date at some value, or is delayed, rescoped, or cancelled. The publisher's own subsequent research usually observes the outcome and records it as an updated project state, overwriting rather than scoring the prediction. So the firm cannot say what fraction of its early-stage leads actually reach bid, how its value estimates perform by project type and region, or which of its sources produce leads that go anywhere.

## Why Nobody Has Built This
Projects are stored as current-state records with change history kept for operations rather than analysis, so recovering what was published when requires reconstruction. Resolution is also less binary than it looks — a project that bids two years late at half the value is neither right nor wrong without a stated rule. And the segment sells on database size and lead volume, which are easy to compare in a procurement bake-off and which accuracy measurement would complicate.

## What to Build
A prediction register treating each published lead as a resolvable claim: stage, scope, value, expected bid timing, and the resolution rule fixed at publication. Outcomes resolve from the firm's own continuing research, which already observes them. The accumulated record supports what the business cannot currently do: conversion rates from each early stage to actual bid, by project type, region, and source, which is the single most useful thing a subscriber could be told and which nobody publishes; value estimate accuracy, so a contractor sizing a pursuit knows the error band; and source quality measurement, which directs the research organization — the firm's largest cost — at the sources that produce leads that go somewhere. Published leads then carry a probability of reaching bid rather than a stage label, which turns a lead list into a pursuit prioritization tool.

## Target Customer
VPs of research and chief data officers at project lead publishers running 300-1,500 researchers, and the chief estimators at contractors who allocate scarce estimating capacity against unscored predictions.

## Impact If Built
Converts a volume product into a decision product. For a subscriber whose binding constraint is estimating capacity, a lead carrying a calibrated probability of reaching bid is worth substantially more than three leads without one — and the record can only be built by the party that both publishes the leads and researches the outcomes.
