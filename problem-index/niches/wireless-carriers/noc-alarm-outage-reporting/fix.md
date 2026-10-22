# Outage User-Minutes Estimated by Hand for NORS

**Niche:** [[niches/wireless-carriers/noc-alarm-outage-reporting/profile|NOC Alarm Correlation & Outage Reporting]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Whether an outage must be reported to the FCC depends on users affected times duration, and during the outage a NOC analyst estimates that number in a spreadsheet.
**Tags:** #linear-regression #feature-engineering #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a flood of network alarms into the handful of incidents that need action, with a cause attached, fast enough to restore service and file the FCC outage report on time, and whoever gives the shortest time from first alarm to correct incident takes the network-operations contract.

## The Problem
FCC Part 4 reporting turns on thresholds such as affected user-minutes and on whether 911 service is affected. For a wireless outage, "users affected" must be estimated from the sites down, the traffic they normally carry at that hour and overlap with neighbouring coverage. Analysts do it by hand under time pressure, so carriers over-report out of caution or miss the window.

## Why It's Still Broken
Traffic and coverage data sit in engineering systems the NOC doesn't use, and the method varies by analyst.

## What a Fix Looks Like
Estimate affected users automatically from the incident's site list, historical traffic for that hour and day, and coverage overlap. Show the threshold status and the reporting deadline in the incident, and draft the NORS notification for review.

## Who Feels the Pain
NOC analysts and regulatory compliance staff, and the carrier facing enforcement for late or inaccurate reports.

## Impact If Fixed
On-time, consistent reports and less analyst time during the worst hour of an outage.
