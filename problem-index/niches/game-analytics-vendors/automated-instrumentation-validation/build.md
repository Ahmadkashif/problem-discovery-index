# Catching the Break When It Breaks

**Niche:** [[niches/game-analytics-vendors/automated-instrumentation-validation/profile|Automated Instrumentation Validation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Broken instrumentation flows into every report until somebody notices a number looks odd.
**Tags:** #automation #change-point-detection #data-integration #evaluation-metrics #descriptive-statistics #workflow-orchestration #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to catch broken instrumentation when it breaks rather than when a metric looks wrong weeks later — and whoever automates that check takes the account.

## The Problem
Instrumentation breaks constantly and quietly. A refactor removes a call site, a parameter changes type, a condition changes so an event fires in different circumstances, a platform build omits something. The pipeline accepts whatever arrives. The break propagates into dashboards, models and reports, and is discovered when a human finds a number implausible — usually long after decisions have been made on it.

## Why Nobody Has Built This
Pipelines are built to ingest rather than to judge, and rejecting data risks losing it. Expected behaviour per event is not defined anywhere, so there is nothing to validate against. Validation is nobody's feature. And the failures are attributed to analysis.

## What to Build
Define what each event should look like and check continuously. Establish expected volume, distribution and null-rate baselines per event per platform and version, which is the core and is what makes automatic detection possible at all. Alert on departure from baseline within hours rather than waiting for a human, since the cost of a silent break scales with how long it runs. Validate on build release specifically, as that is when most breaks occur and the correlation makes diagnosis immediate. Check parameter types, ranges and cardinality, which catches a large share mechanically. Detect semantic drift where volume holds and the distribution shifts, which is the failure no simple check finds. Run instrumentation tests before a build ships, which moves the detection before the damage. Report which metrics are affected by a detected break, so consumers can be warned rather than misled. Quarantine suspect data rather than silently including it. Track break frequency by team and event, which identifies where the instrumentation practice needs attention. And make the baselines self-maintaining, since a validation layer that requires manual upkeep will decay.

## Target Customer
Studio data platform teams, game analytics vendors, publishers, and data quality monitoring vendors.

## Impact If Built
Broken instrumentation propagates into every report until a human finds a number implausible, and the cost scales with how long it runs. Per-event baselines with hourly alerting moves the detection from weeks to hours.
