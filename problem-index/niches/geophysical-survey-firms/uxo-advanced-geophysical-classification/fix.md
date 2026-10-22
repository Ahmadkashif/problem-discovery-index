# The Missed Seed and the Re-Survey

**Niche:** [[niches/geophysical-survey-firms/uxo-advanced-geophysical-classification/profile|UXO Advanced Geophysical Classification]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Fix (Pain Point)
**One-liner:** When a blind QC seed buried by the government's QA team is not detected or not classified as a target, work stops for a root-cause analysis that takes days of manual digging through logs.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to cut digs of harmless debris while holding DoD's zero-missed-target line, and whoever delivers the shortest defensible dig list under DAGCAP accreditation takes the munitions response task order.

## The Problem
Munitions response quality relies on seeds: inert items buried at known positions, some by the contractor's own QC and some blind by the government. A missed seed is a failure that triggers root-cause analysis and corrective action — was it coverage, sensor function, positioning, inversion or the classifier? — and often a re-survey of the affected area.

## Why It's Still Broken
The evidence is spread across the sensor logs, positioning files, daily function tests, inversion outputs and dig lists, in different software. Analysts reconstruct the chain by hand while crews wait.

## What a Fix Looks Like
An automatic trace for any seed: the coverage at its location, sensor and positioning quality at the time it was passed, the inversion fit and library match, and the classifier's rank and threshold — with the most likely failure point highlighted and the other affected areas listed for targeted re-survey rather than blanket rework.

## Who Feels the Pain
Project geophysicists, field crews on standby, and government QA reviewers waiting for corrective action plans.

## Impact If Fixed
Root causes found in hours rather than days and re-surveys targeted to what actually failed.
