# Hold Expiries Tracked on a Whiteboard

**Niche:** [[niches/psychiatric-hospitals/involuntary-hold-commitment-paperwork/profile|Involuntary-Hold & Commitment Paperwork]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** On many units the only record of when each patient's hold expires is a whiteboard in the nurses' station, so a hold that began at 11:40 p.m. on a Friday can lapse before anyone notices on Monday.
**Tags:** #workflow-orchestration #compliance #worker-facing #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep every involuntary hold, certification and court petition on its statutory clock, and whoever has the fewest holds ended by a procedural defect rather than a clinical decision takes the account.

## The Problem
The hold started in an ED at another hospital, the paperwork arrived by fax, and the clock was running before the patient reached the unit.

## Why It's Still Broken
EHRs record legal status as a free-text field or a scanned document, with no clock, and the hold often begins outside the hospital.

## What a Fix Looks Like
Capture the hold's start time and type at intake, show each patient's remaining time on the unit board and the attending's list, and alert at set intervals before expiry, including weekends.

## Who Feels the Pain
Charge nurses, attending psychiatrists on weekend cover, and patients held without authority or released without review.

## Impact If Fixed
If ~2% of ~1,500 holds a year at a 100-bed hospital lapse or overrun unnoticed (estimate), clocks on the board would catch ~30 of them.
