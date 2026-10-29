# Transport Adverse Events Buried in the Narrative

**Niche:** [[niches/ambulance-services/critical-care-specialty-transport/profile|Critical Care & Specialty Care Transport Teams]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** An unplanned extubation or a pressor gap is written into the narrative in the team's own words, so the programme cannot count its events, benchmark them or learn from them.
**Tags:** #bert #transformers #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to move ICU-level patients between hospitals without harm en route, and whoever has the fewest in-transport adverse events per 100 critical care transports takes the account.

## The Problem
Quality programmes in transport medicine ask for consistent event definitions, but most ePCRs have no required adverse-event fields for critical care. Events live in free text, described differently by each clinician.

## Why It's Still Broken
Adding required fields lengthens the chart for every run, most of which have no event, and clinicians resist anything that looks like self-reporting an error.

## What a Fix Looks Like
Classify each critical care narrative for candidate adverse events against the programme's definitions, and ask the team to confirm or reject in one tap at chart close. The confirmed list feeds the programme's quality report and external benchmarking without anyone re-reading charts.

## Who Feels the Pain
Programme quality coordinators reading every chart; medical directors reporting to hospital quality committees; and clinicians whose good outcomes go unmeasured.

## Impact If Fixed
For a programme reading 3,000 charts a year at ~6 minutes each (an estimate), pre-classification would save ~250 coordinator hours a year and give a consistent event rate to benchmark.
