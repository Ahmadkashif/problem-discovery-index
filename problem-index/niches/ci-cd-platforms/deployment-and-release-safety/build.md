# Deploy to Everyone and Watch

**Niche:** [[niches/ci-cd-platforms/deployment-and-release-safety/profile|Deployment & Release Safety]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most organisations release a change to everybody and rely on somebody noticing that something broke, which is a detection mechanism whose latency and coverage nobody has measured.
**Tags:** #hypothesis-testing #confidence-intervals #change-point-detection #causal-inference #evaluation-metrics #time-series-forecasting #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to make a bad release stop itself before most users see it — and whoever does that takes the release account, because the alternative is that a human notices and reacts, which is what happens almost everywhere.

## The Problem
A release goes out at two in the afternoon to all users. Error rates rise slightly — enough to matter, not enough to breach any alert threshold. Forty minutes later a support ticket arrives, then two more. Somebody correlates them with the release, confirms it, and initiates a rollback that takes another twenty minutes. An hour of degraded service for everybody, caused by a change that would have been visibly bad in the first two minutes on two percent of traffic, and stopped automatically by a comparison the organisation had all the data to make.

## Why Nobody Has Built This
Progressive delivery requires the deployment system to know whether the service is healthy, which means joining delivery tooling to observability — two products, two owners, and an integration nobody is accountable for. Health evaluation is offered as a static threshold, which inherits every problem the alerting niche describes and performs badly enough that teams distrust automatic promotion and supervise it manually, which removes most of the benefit. The correct comparison — canary against control — requires a control population that the deployment system must deliberately maintain, and most implementations compare the canary against a global baseline that includes it. And the cost of the current approach is absorbed as ordinary incident time rather than attributed to the release process.

## What to Build
Make the release evaluate itself against a genuine control. Maintain an explicit control population receiving the previous version, and compare the canary against it rather than against a historical baseline — this is the single most important design decision and is what makes the evaluation valid, since it controls for time, traffic mix and everything else happening concurrently. Evaluate on a set of signals rather than one: error rate, latency distribution, saturation, and business signals such as conversion or transaction completion, which frequently move before the technical ones. Use sequential testing so the decision can be made as early as the evidence allows without inflating false positives, since the value is entirely in stopping quickly. Automate the decision in both directions, promoting and reverting without a human, because a human in the loop at two in the morning is the latency the whole thing exists to remove. Integrate feature flags and deployments as one decision surface, since they are two mechanisms for the same choice and managing them separately produces changes that are live in one and not the other. And measure the exposure — how many users saw a bad release, for how long — which is the metric the release process should be judged on and which nobody reports.

## Target Customer
Site reliability and release engineering teams, CI and deployment vendors, and the feature flag platforms approaching the same decision from the other side.

## Impact If Built
The alternative to automatic evaluation is a human noticing, which has a latency and coverage nobody measures. A genuine control population is what makes the comparison valid, and sequential testing is what lets the decision be made in minutes rather than hours.
