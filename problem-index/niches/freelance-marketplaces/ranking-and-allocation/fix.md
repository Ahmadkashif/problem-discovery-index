# Fix: Ranking Changes That Move Incomes Without Notice

**Niche:** [[niches/freelance-marketplaces/ranking-and-allocation/profile|Ranking & Allocation]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** A ranking model ships on Tuesday, a freelancer's inbound work halves on Wednesday, and nobody on either side of the platform can connect the two.
**Tags:** #change-point-detection #causal-inference #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #worker-facing #automation
**Contested on:** Whether the platform can detect, before the support queue does, which freelancers a ranking change materially displaced.

## The Problem

Ranking models ship continuously. Each release reshuffles placement across millions of freelancer-query pairs, and the aggregate metrics the release is judged on — overall click-through, overall contract rate — can improve while a substantial minority of the supply side loses most of their inbound volume.

The platform sees the aggregate. The freelancer sees their income drop and has no way to know whether the cause was a model release, a seasonal shift in their category, a change in their own response time, a client who stopped returning, or nothing at all. They write to support. Support has the same aggregate dashboards and answers with the help article about best practices. The distributional effect of the release is never computed, so nobody knows how many people it happened to.

## Why It's Still Broken

Partly it is that nobody asked for the number. A release is evaluated against the metric it was built to move, and the experiment framework reports treatment effects on means. Reporting the tail — how many accounts lost more than half their impressions, and who they were — requires a different query against the same experiment data, and it produces a number that makes shipping harder.

Partly it is genuinely confounded. Freelancer volume is noisy at the individual level; most people have few enough impressions that a week-to-week halving is well within normal variation. Separating a model-induced displacement from ordinary noise requires a per-account counterfactual, and the experiment's own holdout is the obvious source of one that few teams think to use this way.

And partly the incentive runs the wrong way. A platform that could name the freelancers a release displaced would then be asked what it intends to do about them. The measurement creates an obligation that not measuring avoids.

## What a Fix Looks Like

Compute the distributional effect of every ranking release, as a standing part of the release process, using the holdout that already exists.

For each freelancer with enough exposure to estimate, compare impressions, invitations and contracts in treatment against the same account's holdout-arm counterpart over the experiment window. Aggregate into a displacement distribution rather than a mean: what fraction of accounts lost more than 25%, more than 50%, more than 75%, and what those accounts have in common — category, tenure, price point, geography, new-versus-established. Report it alongside the headline metric, with intervals, so a release is approved knowing both numbers.

Detect the individual case too. Run change-point detection on each freelancer's own inbound series with their category's seasonal baseline removed, so that a genuine step change is distinguishable from ordinary variance, and attribute a detected change against the release calendar. When a freelancer writes to support asking why their work dried up, the agent should see a dated series with a detected change point and either a named cause or an honest "nothing changed on our side in that window" — which is itself a far better answer than the help article.

The cheap half is worth stating separately: even the descriptive displacement histogram, with no modelling at all, is computable from data every platform already holds in its experiment store, and it is the single number the category has never looked at.

## Who Feels the Pain

Freelancers whose income tracks placement, most acutely those in competitive categories where a small ranking move is the difference between a full week and an empty one. Support agents who take the complaint and have nothing to offer. And the platform itself, which loses experienced supply to churn it never attributes to its own releases, because the attribution was never computed.

## Impact If Fixed

Releases get judged on their distribution rather than their mean, which changes which releases ship. Support answers a question with evidence instead of a platitude. And the platform learns, for the first time, the actual rate at which its own model deployments displace the people it depends on — a number that is either reassuringly small or the most important thing the marketplace does not currently know.
