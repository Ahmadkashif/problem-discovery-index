# Leakage Counted Only When a Notice Is Mailed

**Niche:** [[niches/parking-operators/unpaid-session-enforcement/profile|Unpaid-Session Recovery & Private-Property Enforcement]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Fix (Pain Point)
**One-liner:** An operator reports notices sent and collected, never the unpaid sessions that were not pursued, so leakage looks smaller than it is.
**Tags:** #descriptive-statistics #data-integration #compliance #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn unpaid parking sessions into collected revenue. That produces two contests with different winners: making payment happen before the car leaves, won by camera and PARCS platforms on the share of sessions paid without a notice, and recovering the sessions that slip through by mailed notice, won by notice processors on the share of notice value collected under each state's rules. Decomposed into contested sub-niches below.

## The Problem
Sessions with unreadable plates, out-of-state plates or lots where notices are not allowed are dropped silently. The owner's statement shows notice income but not what was never billed.

## Why It's Still Broken
Nobody is paid to count what was not pursued, and the counts sit in two vendors' systems.

## What a Fix Looks Like
A monthly per-lot table: total sessions, paid at exit, paid late, noticed, not noticed (with reason), collected, voided. It goes to the owner with the statement.

## Who Feels the Pain
Owners of gateless lots, operator revenue control and anyone deciding whether a gateless conversion paid off.

## Impact If Fixed
Seeing that 4% of sessions on a $1M lot were never pursued (estimate) puts ~$40K a year on the table and makes the gateless decision measurable.
