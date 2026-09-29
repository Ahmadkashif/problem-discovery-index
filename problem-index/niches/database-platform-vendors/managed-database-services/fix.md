# Migration Is a Project in Both Directions

**Niche:** [[niches/database-platform-vendors/managed-database-services/profile|Managed Database Services]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Moving a production database to a managed service, between services, or back out is a multi-month project every time, which is the actual lock-in regardless of what any vendor says about open formats.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #quick-win #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to run a database well enough that the customer never thinks about it — and that contest is fought on latency in one market and on query cost at scale in another, which is why this niche is not terminal and is decomposed below.

## The Problem
A company wants to move a production database to a different managed service. The data can be replicated; the difficulty is everything else. Stored procedures use engine-specific syntax. The application relies on behaviour that differs subtly — collation, isolation level defaults, type coercion, sequence semantics. Extensions in use are unavailable on the target. Connection behaviour differs under load in ways that only appear in production. The cutover must happen with minimal downtime and must be reversible. The result is a six-month project with a risky evening at the end, which is why most organisations do not move, which is the real lock-in.

## Why It's Still Broken
Replication tooling exists and solves the visible part, so the problem appears solved until the compatibility work begins. The incompatibilities are numerous, individually small and discovered one at a time during testing, which makes the project's duration impossible to estimate and therefore frightening. Vendors have every incentive to make migration in easy and none to make migration out easy, so the tooling is asymmetric by design. And each organisation discovers the same incompatibility set independently.

## What a Fix Looks Like
Make the incompatibility surface knowable in advance. Analyse the source database and the application's usage against the target automatically: syntax, extensions, data types, collation, isolation semantics, sequence and identity behaviour, and the specific engine behaviours the application depends on — producing a complete incompatibility report before the project starts, which is what converts an unbounded estimate into a scoped one. Draw on accumulated migration knowledge, since the same incompatibilities recur across every migration between the same pair of engines and each organisation currently rediscovers them. Verify behaviour rather than only schema, by replaying a captured production workload against the target and comparing results, which catches the subtle semantic differences that testing misses. Rehearse the cutover repeatedly with real data, which is what makes the evening survivable. Keep reverse replication running after cutover so reversion is possible for a period, since the fear of an irreversible switch is what delays these projects more than the work. And publish the incompatibility matrix between engine pairs openly, which is a public good, a strong competitive claim for whoever does it, and is the thing every organisation currently reconstructs alone.

## Who Feels the Pain
Platform teams facing a six-month project to change a database; organisations locked in by a migration cost rather than by a format; and vendors whose customers cannot adopt them for the same reason their own customers cannot leave.

## Impact If Fixed
The incompatibility set recurs across every migration between the same engines and is rediscovered independently every time, which makes a published matrix immediately valuable. Workload replay with result comparison catches the semantic differences that cause the late failures, and reverse replication removes the fear that delays the decision.
