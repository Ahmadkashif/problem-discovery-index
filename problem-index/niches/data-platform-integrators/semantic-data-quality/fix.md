# The Status Code That Started Meaning Something Else

**Niche:** [[niches/data-platform-integrators/semantic-data-quality/profile|Semantic Data Quality]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** An upstream team added a new status value in March and every conversion metric has been wrong since.
**Tags:** #quick-win #change-point-detection #descriptive-statistics #evaluation-metrics #data-integration #automation #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to catch the data failures that matter — a field whose meaning changed — when the monitoring watches freshness and volume against thresholds somebody set at deployment.

## The Problem
A source system adds a status value, or repurposes an existing one, or changes when a field is populated. The change is routine from the source team's perspective and is not communicated. Downstream, transformations that filter or group on that field silently exclude or miscategorise records. Every metric derived from it is wrong, nothing alerts, and the discovery comes when a business user queries a figure that does not match their expectation.

## Why It's Still Broken
Nobody watches the values — a monitor that checks whether a column is null cannot notice that a new value has appeared in it, and no monitor watches the value set. Source teams have no obligation to notify. The transformation handles the unknown value silently. And the detection depends on a human noticing a wrong number.

## What a Fix Looks Like
Watch the distinct values, which is the cheapest semantic check there is. Alert on any new or disappeared distinct value in categorical fields, which is the fix and is a query per field per day. Fail loudly rather than silently when a transformation encounters an unexpected value, since silent handling is what converts a detectable change into an invisible one. Monitor the proportion of each category, as a reused code shows up as a shifted mix rather than a new value. Establish which fields matter for reporting and monitor those rather than everything, keeping it cheap. Ask source teams to notify on value changes, which most will do if asked and nobody asks. Record every detected change and whether it was legitimate, so the noise falls over time. Assess which reports are affected when a change is found, which is what makes the alert actionable. Backfill and correct the affected history rather than only fixing forward. Tell the business users whose numbers were wrong, which is the part most often skipped. And review the full value set on a cadence for the fields that matter most.

## Who Feels the Pain
Business users who acted on wrong numbers for months; data engineers blamed for a change they were not told about; source teams unaware their routine change broke something; and trust in the platform, which erodes with each occurrence.

## Impact If Fixed
A monitor that checks whether a column is null cannot notice that a new value has appeared in it, and no monitor watches the value set. A daily distinct-value check on the fields that matter is the cheapest semantic monitoring available.
