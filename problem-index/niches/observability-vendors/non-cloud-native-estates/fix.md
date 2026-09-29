# Two Monitoring Worlds With No Shared View

**Niche:** [[niches/observability-vendors/non-cloud-native-estates/profile|Non-Cloud-Native Estates]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Operational technology and information technology are monitored by different systems owned by different teams, so a failure that crosses the boundary belongs to nobody and is diagnosed by two groups arguing.
**Tags:** #graph-theory #descriptive-statistics #change-point-detection #hypothesis-testing #confidence-intervals #quick-win #data-integration #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to bring modern observability to systems that are not ephemeral, not containerised and frequently not connected — and whoever does that takes the industrial and enterprise estate, because the current tooling assumes a world these systems do not live in.

## The Problem
A production line stops. The plant's control systems show a communication fault with a supervisory server. The information technology team's monitoring shows the server is healthy — it responds, its metrics are normal. The plant team is certain the problem is the network; the platform team is certain it is the controller. Both are looking at real data in separate systems with different timestamps, different vocabularies and no shared view, and the line is down while two groups compare screenshots. The eventual cause is a switch configuration change made that morning and visible in a third system belonging to neither team.

## Why It's Still Broken
The two worlds have different histories, different vendors, different safety and change-control regimes and, frequently, deliberate network separation for good security reasons. The separation of the monitoring followed the separation of the estates and nobody owns the join. The data models are genuinely different — tag-based process historians versus label-based metric stores — so even a willing integration is real work. And the incidents that cross the boundary are a minority of each team's workload, which is why it has never been anyone's priority despite being the most expensive kind.

## What a Fix Looks Like
Build the shared view for the boundary rather than merging the estates. A common timeline that both teams look at during an incident, carrying events from both sides — process alarms, controller states, network events, server metrics, change records — with clocks reconciled, which is the single most valuable artefact and is mostly a matter of agreeing a time source and a schema. Map the dependency across the boundary explicitly: which control systems depend on which servers, networks and applications, which nobody has documented and which determines the blast radius of every platform change. Translate vocabulary in both directions, since the same condition has different names on each side and the argument is frequently about terminology. Include change records from both regimes, since the cause is very often a change made by the other side. Define ownership for boundary incidents in advance rather than discovering during one that neither team owns it. And respect the separation: the shared view can be read-only and one-directional, which addresses the security objection that has stopped previous attempts.

## Who Feels the Pain
Plant and platform teams diagnosing across a boundary with no common picture; operations leaders whose most expensive downtime is the kind that spans both; and organisations where a network change can stop a production line and nothing connects the two.

## Impact If Fixed
A shared read-only timeline is modest engineering and addresses the most expensive incident class in these environments directly. The cross-boundary dependency map is the second half and is what turns a platform change from a surprise into a planned one.
