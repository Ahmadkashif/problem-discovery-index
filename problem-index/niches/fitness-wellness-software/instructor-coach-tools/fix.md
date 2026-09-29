# Checking Four Pay Statements Against Your Own Memory

**Niche:** [[niches/fitness-wellness-software/instructor-coach-tools/profile|Instructor & Coach Tools]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Fix (Pain Point)
**One-liner:** An instructor paid by four studios on four schedules with four rate structures — base rates, headcount bonuses, private session splits — has no record of their own to check the statements against, so errors are found by accident or not at all.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor building for instructors is fighting to assemble a week that spans several studios — schedule, sub requests, availability and pay — into one place, and whoever the instructors actually carry takes the layer above the studios.

## The Problem
An instructor's pay from one studio is a base rate per class plus a per-head bonus above a threshold. Another pays a flat rate with a different rate for covers. A third pays a percentage on private sessions. Payments arrive at different times through different methods. Reconciling requires knowing how many people were in each class she taught — which she does not record — and remembering which classes were covers. A missing class or an unpaid bonus is found only if she happens to notice a number looking low. Across a workforce, the aggregate of unnoticed errors is not small, and the party bearing it is the lowest-paid one in the transaction.

## Why It's Still Broken
Instructors are contractors in most of these arrangements and are expected to keep their own records, which nobody does because there is no tool and the work is unpaid. Studios calculate pay from their own systems, which are the same systems that hold the attendance data — so the studio's figure is authoritative and unverifiable by the instructor. Nobody has built the instructor-side record because, as with everything in this niche, the instructor is not a customer.

## What a Fix Looks Like
Give the instructor a record of what they taught. Classes taught, with date, studio, format, cover status and headcount where the studio's system exposes it, accumulate automatically from the aggregated schedule. Rate structures are entered once per studio, so expected pay is computed per class and per period. When a statement arrives, the comparison is automatic and the discrepancies are itemised — which converts a vague suspicion into a specific, polite question with evidence, which is what makes it possible to raise at all. Track payment timing too, since late payment is a common and rarely discussed problem for contract instructors. Where a studio is willing, sharing the headcount and pay calculation directly removes the ambiguity entirely and costs the studio nothing, which is worth asking for.

## Who Feels the Pain
Instructors reconciling four employers from memory and absorbing the errors they do not catch; studio owners fielding occasional pay disputes with no shared record; and the profession, where pay opacity compounds already low earnings.

## Impact If Fixed
A personal teaching record makes pay verifiable for a workforce that currently cannot verify it, which is a straightforward fairness improvement and costs nothing beyond aggregating a schedule the instructor is already keeping in their head. The itemised discrepancy is what turns an unraised suspicion into a resolvable question.
