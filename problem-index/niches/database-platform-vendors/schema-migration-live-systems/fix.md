# The Migration Nobody Can Reverse

**Niche:** [[niches/database-platform-vendors/schema-migration-live-systems/profile|Schema Migration on Live Systems]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A migration is half applied when a problem appears, and the rollback script was written on the assumption that it would either complete or not start.
**Tags:** #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #workflow-orchestration #automation
**Contested on:** Every serious competitor here is fighting to make changing a schema on a live production system routine rather than an event — and whoever does that takes the database team, because every significant migration is currently planned by whoever has done one before.

## The Problem
A migration begins at two in the morning. Forty minutes in, replication lag is climbing and the application is showing errors. The engineer wants to stop. The rollback script drops the new column — which the application, already deployed, is now writing to. Stopping means either continuing forward under pressure or reverting the application deployment first, which nobody has rehearsed. They continue, it completes, and the incident review records that the migration succeeded. The actual finding is that the operation had no safe abort at any point, which nobody noticed because it worked.

## Why It's Still Broken
Rollback scripts are written as the inverse of the forward migration, which assumes an all-or-nothing transition and ignores the intermediate states a long-running change passes through. The coupling to the application deployment is the harder half and is rarely considered — reversing the database without reversing the code is frequently worse than continuing. And the abort path is never exercised, because migrations are rare and stopping one feels like failure, so its absence is discovered only in the situation where it was needed.

## What a Fix Looks Like
Plan the abort rather than the rollback. Enumerate the intermediate states the operation passes through and define, for each, what stopping means and what must also be reverted — which converts an assumption into a plan and is the core change. Establish an abort point beyond which forward is genuinely the only safe direction, and state it in advance, so the decision at forty minutes is looking up a fact rather than reasoning under pressure. Couple the database and application reversals into one sequence, since reverting one without the other is the specific way this goes badly. Automate the abort with the same care as the forward path, and rehearse it in a non-production environment with realistic data volumes, because an unrehearsed abort is an untested critical path in the most consequential possible position. Define the pause conditions — replication lag, lock waits, error rate — and enforce them automatically rather than relying on somebody watching a dashboard at two in the morning. And record what actually happened, since the fleet-wide record of which migrations needed to abort and why is exactly the knowledge that would make the next plan better and is currently in nobody's hands.

## Who Feels the Pain
Engineers deciding at two in the morning whether to continue a migration that is going wrong; teams whose only option is forward; and organisations whose migration procedures have an untested failure path.

## Impact If Fixed
Planning per intermediate state rather than writing an inverse script converts an assumption into an actual abort capability. Stating the point of no return in advance removes the worst decision from the worst moment, and rehearsing the abort tests the path that is otherwise exercised only in an emergency.
