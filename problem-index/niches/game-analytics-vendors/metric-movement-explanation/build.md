# Answering Why Rather Than What

**Niche:** [[niches/game-analytics-vendors/metric-movement-explanation/profile|Metric Movement Explanation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every artefact the platform produces describes what happened and every question asked of it is why.
**Tags:** #causal-inference #change-point-detection #time-series-forecasting #confidence-intervals #evaluation-metrics #gradient-boosting #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to say why a metric moved, when the dashboard can only say that it did — and whoever answers it takes the account.

## The Problem
Analytics platforms in this category are descriptive by construction. They show a metric, they segment it, they compare periods. The studio's question is causal: what did this, and was it us. Answering requires joining the metric to the studio's own build, configuration and content history, to its acquisition mix, and to what comparable games were doing at the same time — three different data problems, none of which the platform attempts.

## Why Nobody Has Built This
The pipeline and dashboard business is well understood and profitable, and causal work is harder to productise. The build and config history sits in the studio's systems rather than the vendor's. The market comparison requires using cross-customer data, which is contractually and commercially sensitive. And an analyst absorbs the gap.

## What to Build
Produce ranked candidate explanations rather than a chart. Join metric movements to the studio's own event history — builds, configuration changes, content releases, acquisition campaigns — which is the core and is the single largest available improvement. Bring comparable-title context into the answer so the studio can tell its own movement from the market's, which is the question only the vendor can answer. Detect the change point rather than comparing arbitrary periods, since where the movement began is most of the diagnosis. Rank candidate explanations with evidence and confidence rather than presenting one, as an analyst can evaluate three hypotheses quickly and cannot evaluate a verdict. Decompose the movement across segments to find where it concentrated, which frequently identifies the cause outright. Distinguish composition effects from behavioural ones, because an acquisition mix shift and a product regression look identical in aggregate. Record every explanation against what was later confirmed, which is how the system earns trust and improves. Deliver it within the analyst's actual deadline rather than as a research exercise. Show the reasoning rather than a conclusion, since an unexplained attribution will be ignored. And handle the honest answer that the movement is within normal variation, which is frequently true and never said.

## Target Customer
Game analytics vendors, studio data and product leadership, publishers with portfolio views, and analytics tooling providers.

## Impact If Built
Every artefact describes what happened and every question is why, so an analyst bridges the gap by hand each week. Joining movements to build and content history, with comparable-title context, turns a chart into a ranked explanation.
