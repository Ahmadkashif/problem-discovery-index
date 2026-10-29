# Probabilistic Posting Plan Ranked by Level-Zero Risk

**Niche:** [[niches/ambulance-services/system-status-deployment/profile|System Status Management & 911 Unit Deployment]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Posting plans are built on average call volume by hour, when zones go to level zero in the tail: the hour three calls land in one zone while two units sit at a hospital.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #monte-carlo-methods #optimization-fundamentals #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep an available ambulance within reach of every zone of a county 911 contract around the clock, with the unit-hours the contract funds, and whoever has the fewest priority-1 calls arriving when the zone has no available unit (level-zero calls) per 1,000 priority-1 responses takes the account.

## The Problem
Level-zero calls, priority-1 calls that arrive when their zone has no available unit, cluster in the hours when demand spikes in a zone, units are tied up at hospitals and the remaining units are posted for the average hour. Each one means a unit is sent from another zone, which can leave that zone empty in turn. The controller sees the spike as it happens and moves units by feel.

## Why Nobody Has Built This
CAD vendors sell posting modules that use historical averages, and the operators that run the most sophisticated deployment keep it in house. Coverage tools score a static map of drive times; they do not count how often a zone actually had no unit free when a call arrived, so nobody measures the thing the plan is for.

## What to Build
A probabilistic forecast of priority-1 calls by zone and hour, quantiles not means, with forecast hospital wall time for units in transport. A Monte Carlo simulation of the next hours turns them into the expected number of level-zero calls for each candidate posting move. The controller sees moves ranked by level-zero calls avoided per unit-hour, and every override is logged with its outcome so the plan learns which instincts were right.

## Target Customer
Communications directors at private operators running dynamic or hybrid deployment under county 911 contracts.

## Impact If Built
If a contract with 60,000 priority-1 responses a year runs at 40 level-zero calls per 1,000 (both estimates) and the plan cut that by a fifth with the same unit-hours, ~480 fewer priority-1 calls a year would arrive with no unit free in their zone.
