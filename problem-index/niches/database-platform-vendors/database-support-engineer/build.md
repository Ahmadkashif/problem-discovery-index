# Reconstructing From What Was Not Recorded

**Niche:** [[niches/database-platform-vendors/database-support-engineer/profile|The Database Support Engineer]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Database support engineers spend their days reconstructing what happened during an incident from logs written afterwards, when the state that would have explained it existed for ninety seconds and was discarded.
**Tags:** #descriptive-statistics #graph-theory #change-point-detection #k-means-clustering #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to capture the state that explains an incident while the incident is happening — and whoever does that takes the support organisation, because reconstruction after the fact is most of what database support does.

## The Problem
A customer reports that the database was unresponsive for four minutes on Tuesday afternoon. The support engineer has metrics at one-minute resolution showing connections climbing and latency rising, a log containing some slow queries, and a customer who says the application was fine before. What they need is what was actually happening at 14:32:10 — which sessions were active, which were waiting on what, what the lock graph looked like, which query held the blocking lock and what its plan was. All of that was available through the engine's own views throughout the incident and was queried by nobody. Two days of exchanges follow, and the conclusion is a plausible hypothesis.

## Why Nobody Has Built This
Capturing session, lock and plan state continuously is expensive, and the engines therefore expose it live rather than recording it, which is the correct engineering trade-off and leaves the diagnostic gap. Triggered capture — record this state when these conditions occur — is the obvious resolution and requires deciding what the conditions are and what to capture, which nobody has specified. Diagnostic collection was designed as a customer action after the fact, which is exactly the wrong time. And the support burden falls on the vendor's own staff, which makes it a cost line rather than a product requirement.

## What to Build
Capture on condition rather than continuously. Define the trigger conditions from what actually precedes incidents — connection count rising sharply, lock wait time crossing a threshold, active session count climbing, a long-running transaction appearing — and snapshot the full diagnostic state when they occur: active sessions with their queries and wait events, the lock graph, running plans, and the relevant configuration. Keep the snapshots briefly and retain them permanently when an incident is subsequently reported, which bounds the cost while preserving the evidence. Capture at incident-relevant resolution, which is seconds rather than minutes, because the propagation of a lock cascade happens faster than a one-minute sample can see. Present the captured state as an assembled narrative rather than as raw views, since the support engineer's skill is the reconstruction and encoding it is the second half of the value. Cluster incidents across customers by their captured signature, since the same patterns recur constantly and each is currently diagnosed independently — which is the cross-tenant aggregation this vault finds unused in every infrastructure category. And give the customer the same capture, since a large share of tickets exist because the customer could not see what happened either.

## Target Customer
Managed database vendors' support organisations, the engineering teams receiving escalations that are really reconstruction requests, and the customers who would prefer to diagnose their own incidents.

## Impact If Built
The state that explains the incident exists during it and is discarded, which makes this a capture design rather than an analysis problem. Condition-triggered snapshots bound the cost while preserving exactly the moments that matter, and cross-customer clustering turns repeated independent diagnoses into one.
