# The Alarm Panel Nobody Knew Was on Copper

**Niche:** [[niches/wired-broadband-providers/copper-retirement-migration/profile|Copper Retirement & Customer Migration]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Fix (Pain Point)
**One-liner:** At cutover, lines that looked like plain voice turn out to carry burglar alarms, elevator phones, fax machines or medical alert devices, and they stop working.
**Tags:** #gradient-boosting #feature-engineering #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche (migration programme integrators, field-service contractors and telcos' own transformation offices) is fighting to move each remaining copper line, attached device included, onto fibre or a working substitute before the wire center's retirement date, and whoever completes those migrations with the fewest lost lines and failed devices takes the account.

## The Problem
Account records say "residential voice" or "business line". The alarm company, the elevator inspector or the family of a customer with a medical pendant finds out the line is gone when the device fails to call out, which is both a safety risk and a regulatory complaint.

## Why It's Still Broken
Telcos never recorded what customers plugged into their lines. Call-detail patterns hint at it (short, regular calls to known alarm-monitoring numbers, fax tones) but nobody analyses them before cutover.

## What a Fix Looks Like
Classify each line before migration from call-detail patterns and known monitoring-centre numbers, flag likely device lines, and schedule them for a technician visit or a compatible substitute ahead of the wire-center date.

## Who Feels the Pain
Elderly and small-business customers; alarm and elevator service companies; telco migration teams dealing with escalations; regulators fielding complaints.

## Impact If Fixed
Fewer safety incidents and complaints at cutover, and fewer emergency extensions that delay retirement.
