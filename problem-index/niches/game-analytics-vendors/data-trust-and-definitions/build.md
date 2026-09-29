# One Number, One Meaning

**Niche:** [[niches/game-analytics-vendors/data-trust-and-definitions/profile|Data Trust & Metric Definitions]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Four systems report the same metric and none of them agree.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #descriptive-statistics #compliance #automation #sets-and-logic #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make one number mean one thing across every tool and every team, and whoever establishes that takes the account.

## The Problem
A studio runs an analytics platform, an internal warehouse, a publisher reporting requirement and a finance model. Each computes retention, active users and revenue from the same underlying events with different definitions, boundaries and filters. The numbers disagree by amounts large enough to matter. Nobody can say which is right because there is no authoritative definition, and the organisation learns to distrust all of them equally.

## Why Nobody Has Built This
Each system was adopted separately with its own defaults. Defining metrics authoritatively requires a decision nobody has authority to make. The differences are individually small and collectively corrosive. And the reconciliation happens verbally in meetings, so it never becomes a project.

## What to Build
Define the metrics once and compute everything from the definitions. Maintain an authoritative metric definition layer that every consumer computes from, which is the core and is what makes agreement structural rather than negotiated. Express definitions precisely — time boundaries, timezone, inclusion rules, deduplication — since that is exactly where the disagreements live. Reconcile against every existing system and report the differences with their causes, which is how trust is rebuilt rather than asserted. Provide lineage from any number back to the source events, so a disputed figure can be resolved rather than argued. Version the definitions with a change log, because a metric that changes meaning silently is worse than one that disagrees openly. Publish the definitions in language the whole organisation can read rather than as SQL. Flag when a report uses a non-standard definition rather than silently allowing it. Cover the finance-facing metrics too, since that is where the disagreements are most expensive. Assign ownership of the definition set, which is the organisational half. And make adopting a standard definition easier than keeping a local one, which is what determines whether any of it holds.

## Target Customer
Studio data and analytics leadership, game analytics vendors, publishers standardising reporting, and metrics layer and BI vendors.

## Impact If Built
Four systems computing the same metric from the same events with different boundaries disagree by amounts that matter, and nobody can say which is right. An authoritative definition layer with lineage makes agreement structural.
