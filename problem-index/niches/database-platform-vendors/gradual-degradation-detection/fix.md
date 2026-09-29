# Alerting on Latency, Which Is the Symptom

**Niche:** [[niches/database-platform-vendors/gradual-degradation-detection/profile|Gradual Degradation Detection]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Database alerting fires on query latency and connection counts, which are the last things to move, so the alert arrives at the moment the problem becomes an incident.
**Tags:** #change-point-detection #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to warn a team that a database is degrading weeks before it breaks — and whoever does that takes the account, because the engines already expose everything required and interpret none of it.

## The Problem
The monitoring is configured with alerts on average query latency, connection count and processor utilisation. All three are lagging indicators: by the time latency has risen enough to breach a threshold, the plan has already flipped, the pool is already saturated, or the bloat has already accumulated, and the team is now in an incident. The leading indicators — the ones that moved weeks earlier — are available in the same monitoring system and are not alerted on, because nobody knew to configure them and the products do not suggest them.

## Why It's Still Broken
The default alerts shipped with monitoring tooling are the generic infrastructure ones, because those apply to everything and require no engine knowledge. Configuring meaningful database alerts requires knowing which internal series matter, which is exactly the specialist knowledge the organisation lacks — so the defaults stand. And a latency alert does fire eventually, which makes the configuration look adequate until an incident demonstrates otherwise.

## What a Fix Looks Like
Ship leading-indicator alerting as the default. Alert on statistics staleness relative to table churn, which precedes plan instability directly. Alert on plan changes for significant queries, which is detectable and is the single most useful database alert available, because a plan flip is the commonest cause of sudden degradation and is observable the moment it happens. Alert on bloat accumulating faster than it is reclaimed, and on maintenance processes falling behind. Alert on growth approaching structural thresholds rather than on the size itself. Alert on connection pool saturation trends rather than on the count, and on lock wait time growth rather than on a lock count. Alert on replication lag trend rather than on an absolute value. Each of these is engine-specific, entirely standard to a specialist, and absent from every default configuration — and shipping them as defaults transfers the specialist's checklist to every customer at no cost. And report which alerts have ever fired usefully, since a database alert set accumulates exactly as every other alert set in this vault does.

## Who Feels the Pain
Teams whose first indication of a database problem is an incident; on-call engineers paged for a latency spike whose cause began six weeks earlier; and organisations operating databases with the default infrastructure alerting and no specialist.

## Impact If Fixed
The leading indicators are available in the same monitoring system and are simply not configured, which makes shipping them as defaults a packaging change with an outsized effect. Plan change alerting alone addresses the commonest cause of sudden degradation.
