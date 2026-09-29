# Which Article Actually Did It

**Niche:** [[niches/digital-native-publishers/subscriber-causation/profile|Subscriber Causation]]
**Industry:** [[industries/digital-native-publishers|Digital Native Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reader read forty articles over eight months and then subscribed, and the fortieth gets the credit.
**Tags:** #causal-inference #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #monte-carlo-methods #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to identify which journalism causes a reader to become a subscriber and stay one — and whoever separates that from the articles that merely attract readers who were already going to subscribe changes where every publisher spends its editorial budget.

## The Problem
Subscription is the outcome of a relationship built over months of reading. The record of that relationship is complete and sits in the publisher's warehouse. Attributing it is genuinely hard: the article a reader hit the paywall on is not the article that persuaded them; an investigation that brought in a hundred thousand casual readers may have converted fewer of them than a niche column read by two thousand committed ones; and readers who choose to read a certain kind of article differ from readers who do not, which means correlation between reading and subscribing proves very little.

## Why Nobody Has Built This
The question requires causal methods the analytics team does not have, so the industry has stayed on correlation and last-touch — a hard inference problem with no available expertise defaults to the easiest available proxy. Selection bias is the whole difficulty and is invisible in a dashboard. Editorial resists being measured at all, which makes a flawed measurement worse than useless politically. And the data engineering to join reading to subscription is real work nobody funded.

## What to Build
Treat it as the causal problem it is. Model the reading chain rather than the last touch, which is the core — a subscription follows a sequence and attributing it to one article is the error everything else inherits. Address selection explicitly with matching and sensitivity analysis, since readers who choose an article differ from those who do not and this is the central threat to every conclusion. Use paywall and access variation as natural experiments, because publishers change access rules constantly and each change is an experiment nobody analysed. Run deliberate experiments where possible — free access to a piece for a random subset — as that is the cleanest evidence available and is cheap. Measure retention contribution and not only conversion, since a subscriber acquired by a viral piece and lost in three months is a cost. Model the habit-forming articles separately from the converting ones, because they are different roles in the same chain. Express uncertainty honestly, as the estimates will be imprecise and overclaiming will destroy editorial trust permanently. Report by beat, desk and format so the findings are actionable. Validate prospectively on subsequent cohorts, which is what makes the method credible to a newsroom. And present it as evidence for editors rather than as a verdict on them, since adoption is the binding constraint.

## Target Customer
Data and editorial leadership, subscription teams, publisher analytics vendors, and media researchers.

## Impact If Built
A hard inference problem with no available expertise defaults to the easiest proxy, so the industry uses last touch. Modelling the reading chain with selection handled properly is what turns a correlation nobody trusts into evidence a newsroom can act on.
