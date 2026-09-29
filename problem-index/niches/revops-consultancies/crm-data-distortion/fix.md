# The Close Date That Moves Every Fortnight

**Niche:** [[niches/revops-consultancies/crm-data-distortion/profile|CRM Data Distortion]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Fix (Pain Point)
**One-liner:** The deal has been closing in two weeks for eight months and the forecast has counted it every time.
**Tags:** #quick-win #descriptive-statistics #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to quantify the specific ways CRM data is distorted by the people entering it, because every model built on it inherits those distortions silently — and whoever measures them takes the account.

## The Problem
The perpetually slipping close date is the most visible distortion in any CRM and one of the least measured. A deal is forecast to close at the end of the quarter; at the end of the quarter it moves to the next one; this repeats. The forecast counts it each time, the pipeline looks healthier than it is, and the pattern is obvious in the record to anyone who queries the change history — which nobody does.

## Why It's Still Broken
Nobody queries the revision history — a close date that has been revised eleven times looks identical in the pipeline to one set accurately last week, because only the current value is ever reported. Change history is not surfaced. Reporting shows state. And the slipping deal is in everyone's interest to keep counting.

## What a Fix Looks Like
Count the revisions, which the CRM already records. Report the number of times each deal's close date has been revised, which is the fix and is a query against history the platform keeps. Flag deals revised more than a threshold, since those behave completely differently from the rest of the pipeline. Measure the realised close rate of frequently-revised deals separately, which will be dramatically lower and immediately changes the forecast. Discount or exclude them from the forecast on a stated rule rather than leaving it to judgement. Show the same for stage regressions and amount changes, which have their own patterns. Report the distribution by representative and manager, which locates where the practice is concentrated. Track deal age against the segment's typical cycle, as an overdue deal is a distinct category. Surface it in the forecast call rather than in a hygiene report nobody reads. Coach rather than penalise, since the aim is a better forecast and not a disciplinary process. And feed the revision count into the forecast weighting directly, which is an immediate accuracy improvement.

## Who Feels the Pain
Revenue leaders committing on a pipeline padded with deals that will not close; representatives keeping a dead deal alive because removing it is worse; analysts who can see it and have no mandate; and the forecast, wrong in a knowable direction.

## Impact If Fixed
A close date revised eleven times looks identical in the pipeline to one set accurately last week, because only the current value is reported. Counting revisions is a query against history the CRM already keeps.
