# Block Time Released Two Days Before It Is Needed

**Niche:** [[niches/general-hospitals/perioperative-or-block-scheduling/profile|Perioperative Services & OR Block Scheduling]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** Block policies commonly allow release up to ~48–72 hours before the day (recalled), by which time no ready case can be scheduled into it.
**Tags:** #time-series-forecasting #workflow-orchestration #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn released and unused OR block minutes into staffed, completed cases, and whoever fills the most released minutes without adding overtime takes the account.

## The Problem
Surgeons hold blocks in case a patient books and release them late because late release carries no penalty. A case needs pre-op testing, authorisation and patient availability, which take a week or more. Time released at 72 hours is effectively unusable.

## Why It's Still Broken
Release deadlines are set by negotiation with surgeons who value flexibility, and the hospital has no shared, trusted measure of each block's likely use to justify earlier release.

## What a Fix Looks Like
A tiered rule backed by a forecast: blocks with under-use predicted at 14 days are flagged to the surgeon with the evidence. Release at 14 days earns credit in the utilisation calculation that decides next year's allocation. Release at 3 days earns none.

## Who Feels the Pain
OR schedulers back-filling at the last minute; staff on standby; patients waiting weeks for a slot that went empty.

## Impact If Fixed
Moving even a third of releases from 72 hours to 14 days (estimate) makes those minutes schedulable and lifts prime-time utilisation by several points.
