# Integrations Fail Silently and Nobody Is Watching

**Niche:** [[niches/work-collaboration-tools/cross-tool-dependency-graph/profile|Cross-Tool Dependency Graph]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Fix (Pain Point)
**One-liner:** A field gets renamed, a connector stops syncing, no error appears anywhere a human looks, and two teams work from divergent copies of the same status for a fortnight.
**Tags:** #change-point-detection #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #data-integration #automation #quick-win
**Contested on:** Every serious competitor in integration is fighting to turn pairwise field syncing into a single graph of what blocks what across the whole tool estate — and whoever holds that graph owns the question every executive asks and no integration answers.

## The Problem
Someone renames a field in the CRM. The connector that copies opportunity stage into the delivery tracker begins writing nothing, and reports success, because the sync ran. Delivery sees stale stages for two weeks and plans against them. The failure surfaces when a customer asks why the onboarding started late. The person who built the connector left, the integration platform's run log shows green, and nobody had a reason to look at it.

## Why It's Still Broken
Integration platforms report execution status rather than data correctness, so a run that processes zero records successfully is indistinguishable from a run that had nothing to process. Nobody owns integrations after they are built, since they are configured by whoever needed them and then forgotten. Monitoring is an operational discipline that has not been applied to this layer despite being standard everywhere else. And the failure mode is quiet by construction: divergence between two systems is invisible unless someone compares them, which nothing does.

## What a Fix Looks Like
Monitor the data rather than the run. Volume baselines per integration with alerting on deviation, which catches the zero-record success immediately and is the single highest-value check. Divergence detection: sample records that should be consistent across both systems and compare them, which directly measures the thing that matters and is ordinary to implement. Schema change detection on both sides with a warning before a rename breaks a mapping, since the change is observable in the API metadata at the moment it happens. Freshness monitoring per synced field, so a field that has not been updated in three times its usual interval raises a flag. An ownership record per integration, because half the problem is that nobody is responsible. And an inventory — which integrations exist, what they sync, when they last moved data — which most organisations cannot produce at all and which takes an afternoon to assemble.

## Who Feels the Pain
Teams planning against stale data they believe is current; the operations people who discover a fortnight of divergence after a customer complaint; and IT functions that inherit an undocumented estate of integrations built by people who have left.

## Impact If Fixed
Volume baselining and divergence sampling are both straightforward and would catch the large majority of silent failures, which are the dominant failure mode precisely because they are silent. The inventory is the prerequisite and is currently missing almost everywhere.
