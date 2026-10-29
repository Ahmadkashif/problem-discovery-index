# Digital Rounding That Feeds the Charge Nurse's Escalation Model

**Niche:** [[niches/psychiatric-hospitals/observation-seclusion-restraint/profile|Observation Rounds, Seclusion & Restraint Records]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Fifteen-minute observation entries are the richest behavioural record a psychiatric unit keeps, and on paper they predict nothing.
**Tags:** #tacit-knowledge-ml #survival-analysis #gradient-boosting #time-series-forecasting #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to keep agitated and suicidal patients safe with the least coercion, and whoever has the fewest combined restraint and seclusion hours per 1,000 patient hours takes the account.

## The Problem
A 20-bed unit writes ~1,920 observation entries a day. Pacing, isolation and sleep loss show up there hours before an escalation, and the sheets are filed in the chart unread.

## Why Nobody Has Built This
Rounding apps digitise the sheet for compliance and stop there. Escalation models need the charge nurse's decisions and the outcomes joined to the entries, which no product captures.

## What to Build
A handheld rounding app with location beacons and one-tap behaviour codes, plus a handover screen where the charge nurse rates worry and records actions. Joined to medication and restraint records, the data trains the escalation model in ml entry 1, which adds at most two unflagged patients per handover. Demonstrations use synthetic unit data.

## Target Customer
Chief nursing officers at chains and freestanding hospitals above the 75th percentile for restraint hours.

## Impact If Built
If a hospital at the 90th percentile (0.63 hours per 1,000) moves halfway to the median, a 100-bed hospital avoids ~220 restraint hours a year (estimate, at 85% occupancy).
