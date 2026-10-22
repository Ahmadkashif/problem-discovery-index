# Coverage Maps for the FCC Drawn by Guesswork

**Niche:** [[niches/wireless-carriers/wisp-operators/profile|Fixed Wireless ISPs (WISPs)]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A WISP must report the locations where it can serve, and with no RF engineer it draws them generously, which invites challenges, or cautiously, which hides coverage that subsidy programmes would otherwise count.
**Tags:** #gaussian-processes #feature-engineering #evaluation-metrics #compliance #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to deliver advertised speeds to rural homes over fixed wireless, but the contest splits in two. Before the sale it is qualifying a specific roofline correctly; after the sale it is keeping evening-peak experience inside the plan on shared and often unlicensed spectrum. The data, people, clocks and vendors differ, so the niche is decomposed into contested sub-niches below.

## The Problem
Fixed wireless providers report serviceable locations in the FCC's Broadband Data Collection twice a year. Many WISPs build the list from a coverage tool's default output, adjusted by the owner's sense of where installs succeed, with no record of how.

## Why It's Still Broken
The owner has the evidence (every successful and failed install) but not the time or method to calibrate a model with it, and the filing comes around only twice a year. Because a WISP reports fixed broadband by location, it faces the same Fabric reconciliation and challenge process as cable and fibre operators, analysed under wired broadband as [[niches/wired-broadband-providers/bdc-availability-filings/profile|⚡ Broadband Data Collection & Availability Filings]], without their engineering staff.

## What a Fix Looks Like
Calibrate the coverage prediction against the WISP's own install outcomes and measured signal levels, generate the location list at a stated confidence, and keep the calibration as documentation for any challenge.

## Who Feels the Pain
WISP owners facing challenges or losing subsidy eligibility, and rural households shown as served when they aren't.

## Impact If Fixed
Filings that match reality, defended with the operator's own data.
