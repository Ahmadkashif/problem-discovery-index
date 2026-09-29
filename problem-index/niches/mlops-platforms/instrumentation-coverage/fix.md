# The Untracked Model Carrying the Most Risk

**Niche:** [[niches/mlops-platforms/instrumentation-coverage/profile|Instrumentation Coverage]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Organisations do not know how many models they are running, and the ones missing from the platform are systematically the oldest, the most business-critical and the least understood.
**Tags:** #compliance #data-integration #descriptive-statistics #evaluation-metrics #automation #graph-theory #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to make tracking work on the training code an organisation actually runs rather than on the frameworks the vendor supports — and whoever does that takes the account, because the unsupported code is where the important models live.

## The Problem
A regulator asks a bank how many models influence customer outcomes. The answer comes from a spreadsheet maintained by a risk function, assembled by asking teams, last updated ten months ago. The ML platform shows sixty models. The spreadsheet shows four hundred. Neither is right. Somewhere in the estate is a scoring rule written in 2014 by someone who left, running nightly, affecting decisions, with no owner, no documentation, no retraining history and no monitoring. Everyone knows this is true and nobody knows which one it is.

## Why It's Still Broken
There is no definition of a model that a discovery process could apply — a gradient boosted tree, a logistic regression in a stored procedure and a hand-tuned scoring formula all make decisions, and only the first looks like a model to a platform. Inventory is owned by governance functions who ask rather than detect. Platform adoption metrics count what is on the platform, which makes the denominator invisible by construction. And the effort to find the rest is unbounded, so it never starts.

## What a Fix Looks Like
Discover the estate rather than surveying it. Detect model-shaped artefacts and workloads mechanically — serialised model files in storage, scoring libraries imported in production services, scheduled jobs producing prediction-shaped outputs, database procedures computing scores — which finds a large share of the estate in weeks and is the practical starting point. Define a model by its function rather than its technology, since the stored procedure computing a risk score is in scope for every question anybody is actually asking and is excluded by every technology-based definition. Reconcile discovery against the governance inventory and report both directions, because the items on one list and not the other are individually interesting and the gap is the finding. Attach an owner to everything found, treating unowned as an escalation rather than a data quality issue. Rank the untracked by exposure — decisions affected, populations touched, regulatory relevance — so remediation starts where it matters rather than where it is easy. Publish coverage as a standing organisational metric, since what is not measured here is not resourced. And make onboarding a discovered model cheap enough that finding one is not punitive, or teams will stop reporting them.

## Who Feels the Pain
Risk and governance functions answering regulators from a survey; platform teams whose coverage metrics conceal the denominator; and the customers affected by a scoring rule nobody has reviewed in a decade.

## Impact If Fixed
Inventory is assembled by asking and should be assembled by detecting. Defining a model by function rather than technology is what brings the stored procedures and scoring rules into scope, which is where the unexamined risk actually sits.
