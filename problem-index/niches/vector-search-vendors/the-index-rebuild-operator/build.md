# Double the Memory and a Maintenance Window

**Niche:** [[niches/vector-search-vendors/the-index-rebuild-operator/profile|The Index Rebuild Operator]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Site reliability engineers schedule and babysit index rebuilds that consume double the memory and hours of wall clock, without any measurement telling them whether the rebuild was needed.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #graph-theory #time-series-forecasting #worker-facing #descriptive-statistics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make an index rebuild something that happens automatically, online and on evidence, rather than something a person schedules and watches — and whoever does that takes the account, because the rebuild is the category's worst operational experience.

## The Problem
The rebuild is scheduled for Saturday at 02:00. The engineer is online because the operation needs the cluster to hold two copies of the index and the headroom is tight, because there is no progress indicator beyond a log line every few minutes, and because if it fails at hour four they will need to decide whether to retry before the window closes. It completes at 06:40. Nobody measures recall before or after, so whether it was worth the night is unknown. The cluster stays provisioned for two copies for the next month so this can happen again.

## Why Nobody Has Built This
Online rebuild is real engineering — serving from one structure while building another under continuous mutation — and vendors prioritised query performance features that demo better. The double-memory requirement is disclosed and treated as a property of the world rather than as a product deficiency. Reliability engineers are not in the sales conversation. And the pain is concentrated on a small number of nights, which makes it feel episodic rather than structural even though the capacity cost is continuous.

## What to Build
Make the rebuild an unattended background operation. Build online rebuild with bounded memory overhead — construct incrementally in segments and swap progressively rather than holding two complete copies — which removes the permanent over-provisioning and is the largest single cost saving available to this buyer. Make it resumable from checkpoints, so an interruption costs minutes rather than the whole operation, which is what allows it to run outside a window at all. Report progress and a completion estimate, since the absence of one is why a person is awake. Throttle against live traffic with a stated latency impact, so the operation can run during the day under a bound the operator sets. Trigger it from measured degradation rather than from a calendar, which the fix note develops. Measure and report recall before and after, so the operation justifies itself and a rebuild that achieved nothing is visible. Support partial rebuilds of damaged shards or regions, since the damage is rarely uniform and rebuilding everything is usually unnecessary. And report the capacity that the online path frees, because that is the number that gets it prioritised.

## Target Customer
Site reliability and platform operations teams, the finance functions paying for doubled capacity, and the vendors whose worst operational surface this is.

## Impact If Built
The double-memory requirement is a permanent capacity cost for a monthly operation, and it is treated as a property of the world. Segmented online rebuild removes it, and resumability is what makes the operation run unattended outside a window at all.
