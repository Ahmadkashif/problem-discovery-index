# Project Scheduling Adapted to Card-Level Blocking

**Niche:** [[niches/aircraft-mro-shops/airframe-heavy-checks/profile|Airframe Heavy Checks & Base Maintenance]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Project scheduling tools handle a construction job's critical path well; a heavy check's critical path is a few hundred task cards each blocked for a different reason.
**Tags:** #optimization-fundamentals #graph-theory #time-series-forecasting #workflow-orchestration #data-integration
**Contested on:** Every serious competitor in this niche is fighting to absorb a check's non-routine findings without moving the redelivery date, and whoever forecasts the non-routine load before the panels come off takes the account.

## The Problem
A check holds thousands of routine cards and hundreds of non-routine ones. On any morning, some are waiting on parts, some on an engineering disposition, some on an inspector with a specific authorisation, some on access because another card must close first. Planners hold this in their heads and in spreadsheets, and the critical path changes daily.

## What Already Exists
Primavera P6, Microsoft Project and MRO system planning modules model task dependencies and durations; e-task-card systems record card status.

## The Customization Gap
The adaptation needs: (1) card-level blocking reasons as structured states (parts, engineering, inspector, access, customer approval) with expected clearance times; (2) zone and access dependencies, so closing a panel blocks every card behind it; (3) inspector authorisations and required-inspection-item buy-backs as finite resources; (4) automatic insertion of non-routine cards as they are raised, with estimated hours from history; and (5) a daily critical-path view that tells the planner which blocked cards actually move redelivery.

## Target Customer
Hangar planners and production managers at heavy-check bases.

## Impact If Solved
Cutting daily manual re-planning from ~2 hours to ~20 minutes per planner (estimate) and catching critical-path blockers a day or two earlier could recover ~1–3 days per check on a typical 3–6 week check.
