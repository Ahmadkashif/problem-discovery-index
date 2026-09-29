# Bespoke and Terrifying Every Time

**Niche:** [[niches/database-platform-vendors/schema-migration-live-systems/profile|Schema Migration on Live Systems]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Online schema change tools are mature and well understood, and every significant migration is still a bespoke, anxious operation planned by whoever has done one before.
**Tags:** #graph-theory #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #tacit-knowledge-ml
**Contested on:** Every serious competitor here is fighting to make changing a schema on a live production system routine rather than an event — and whoever does that takes the database team, because every significant migration is currently planned by whoever has done one before.

## The Problem
A team needs to add a column with a default to a large table and change a column's type on another. One engineer has done this before and is asked to plan it. They estimate the duration from a previous migration on a smaller table, book a window at two in the morning, write a runbook, arrange for someone to watch replication lag, and prepare a rollback that will not work if the change is more than half complete. It goes well. It will be planned the same way next time, by the same person, and nobody else in the organisation will have learned anything transferable.

## Why Nobody Has Built This
The change tools were built by database specialists to execute a procedure safely, which they do, and the decision of whether and how to run a given change was left as the operator's judgement — which is the part requiring expertise and is the part that does not scale. The application-compatibility analysis sits outside the database entirely and requires reading the code. Predicting duration and impact requires a model of the specific engine's behaviour under the specific change, which no vendor has built despite operating fleets where every such migration is observed. And the expertise is transmitted by apprenticeship rather than being encoded.

## What to Build
Analyse the change before executing it, and make the analysis the product. Classify the proposed change against the engine and version's actual behaviour — which changes are metadata-only, which rewrite the table, which take an exclusive lock and for how long, which are safe concurrently — since this is a known matrix that varies by version and is currently held in people's heads and scattered documentation. Predict duration and impact from the table size, the change type, the hardware and the observed write rate, with an interval, so the window is sized rather than guessed. Analyse application compatibility: whether the code can operate against both schemas during the transition, which is the expand-contract requirement and is where the worst failures originate — a static analysis over the application's queries against the old and new schema answers most of it. Generate the full procedure including the application deployment sequence, since a schema migration and a code deployment are one operation and are planned as two. Execute with continuous monitoring and automatic pause on replication lag or lock contention, which is what the experienced operator watches for manually. And make it reversible by construction wherever possible, planning the reversal before starting rather than discovering it is unavailable at sixty percent.

## Target Customer
Database and platform engineering teams, managed database vendors for whom this is the highest-anxiety customer operation, and the online schema change tool projects.

## Impact If Built
The procedures are mature and the judgement is not encoded, which is why the same migration is planned from scratch by the same person every time. The change-behaviour matrix and duration prediction are both derivable from fleet observation, and the application-compatibility analysis addresses the failure class that causes the worst outcomes.
