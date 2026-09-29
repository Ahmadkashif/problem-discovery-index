# Joining the Change History to the Metric

**Niche:** [[niches/game-analytics-vendors/internal-cause-attribution/profile|Internal Cause Attribution]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Everything that could have moved the metric is recorded, in four systems, none of which are joined to it.
**Tags:** #causal-inference #data-integration #change-point-detection #confidence-intervals #evaluation-metrics #gradient-boosting #hypothesis-testing #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to establish which of a studio's own actions moved a metric, from data the studio already holds in four different systems — and whoever joins them takes the account.

## The Problem
A studio's actions are all recorded. Builds are versioned with timestamps and rollout percentages. Configuration changes are logged. Content releases and live events have schedules. Acquisition campaigns have spend and source data. Every one of these can move retention, and none of them is joined to the metric. The analyst reconstructs the timeline manually every time a question is asked, from four interfaces, under deadline.

## Why Nobody Has Built This
The systems belong to different teams and integrating them has never been anyone's project. Analytics vendors do not have access to the studio's build and config systems. The join looks like plumbing rather than product. And the analyst's manual reconstruction works, slowly.

## What to Build
Build the unified timeline first, then attribute against it. Ingest build, configuration, content and campaign history into the analytics platform as first-class events, which is the core and is the integration the whole capability rests on. Attribute metric movements to candidate changes with staggered rollout used as natural experiments wherever the studio has them, since a phased build rollout is an experiment nobody analyses. Check each candidate against the segments it should have affected, as that test eliminates most false attributions immediately. Decompose composition effects from behavioural ones, because an acquisition mix shift mimics a product change exactly. Detect the change point and match it to the change timestamp rather than to the reporting period. Handle multiple simultaneous changes honestly by reporting that they cannot be separated, which is often the truth. Encourage staged rollouts specifically to make attribution possible, which is a product recommendation with real analytical value. Record confirmed causes so the attribution calibrates against reality. Alert when a change is followed by a movement rather than waiting to be asked. And make the timeline itself available even before any attribution, since it is useful on its own.

## Target Customer
Studio data platform teams, game analytics vendors, publishers with portfolio analytics, and data integration tooling providers.

## Impact If Built
A phased build rollout is a natural experiment nobody analyses, and four systems hold everything needed to explain a movement. Ingesting change history as first-class events is the integration the whole capability rests on.
