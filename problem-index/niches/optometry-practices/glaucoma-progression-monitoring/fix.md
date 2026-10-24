# The Progression Baseline Lost When the OCT Is Replaced

**Niche:** [[niches/optometry-practices/glaucoma-progression-monitoring/profile|Glaucoma Monitoring & Progression Detection]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Fix (Pain Point)
**One-liner:** When a practice replaces or adds an OCT from a different maker, every glaucoma patient's trend starts again from zero.
**Tags:** #transfer-learning #cnns #data-integration #evaluation-metrics #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to catch glaucoma progression at the first visit it shows, and whoever leaves the smallest share of progressing eyes flagged a visit late takes the account.

## The Problem
New OCT, new normative database, new thickness values. The progression analysis needs two or three new baseline scans before it can call change. For a patient seen twice a year, that is a year or more with no trend.

## Why It's Still Broken
Makers' layer measurements differ, and conversion between them is published only for some pairs and some layers. Practices replace devices on financing cycles, rollups standardise fleets after acquisitions, and each change resets the baselines.

## What a Fix Looks Like
Before the old device leaves, scan a set of patients on both machines and fit a per-practice conversion. The old series is then carried forward onto the new scale, with a confidence band, so the trend continues.

## Who Feels the Pain
Glaucoma patients whose progression goes unseen during the reset, and ODs who must rebuild baselines by hand.

## Impact If Fixed
For a practice following ~1,000 glaucoma and suspect patients, carrying baselines across one device change avoids ~2,000 extra baseline scans (estimate) and about a year of blind spot.
