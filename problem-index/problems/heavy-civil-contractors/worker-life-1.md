# The Foreman's Cost-Code Time Card at Dusk

**Industry:** [[heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Worker Life Changing
**One-liner:** After a ten-hour shift a heavy civil foreman spends the last of the daylight splitting every worker's and machine's hours across cost codes, guessing quantities and writing a diary for a claim nobody has filed yet. Giving that half hour back, and making the record accurate, is the same fix.
**Tags:** #large-language-models #transformers #feature-engineering #worker-facing #automation #workflow-orchestration #data-integration

## The Problem
A pile-driving foreman on a wharf job runs a crew of ~6–10 (estimate), a crane, a vibratory hammer, a welder and a work barge. When the shift ends, the day has to be turned into records. Hours go to each worker by cost code: driving, splicing, cutoff, barge moves, standby for the inspector. Equipment hours are split the same way, and quantities installed per code are entered, usually from memory or a scrap of paper. Then come time-and-materials tickets for extra work, and a diary of weather, tides, delays, visitors, inspector instructions and anything that looked like a changed condition. On a federal job the hours also feed certified payroll, often under more than one wage determination, because dredging and marine work fall under heavy-construction wage determinations while an approach road may be highway (search summary).

The foreman does this on a phone or tablet in a truck cab or on the barge, after ten or more hours of physical work, and often after the crew has gone home. It takes ~30–60 minutes a day (estimate). It is the least-liked part of the job, so it gets done fast. Hours are charged to whichever code is open, quantities are rounded, and the diary says "normal day" when it wasn't.

## Why It Matters to the Worker
The foreman was promoted for running a crew, not for clerical work, and the paperwork eats into family time on long hitches away from home. Worse, it comes back on them. When the job's production looks bad, the time cards are the evidence, and a miscoded week makes their crew look slow. When a claim is filed two years later, the lawyers read their diary, and "normal day" on the day the owner's barge blocked access loses the contractor money and makes the foreman look careless. They carry accountability for records they had no time to make well.

## What a Solution Looks Like
The foreman talks to the phone for two minutes: who worked, what they did, what got installed, what went wrong. A language model drafts the time card against the job's cost codes, crew roster and equipment list. It pre-fills hours from equipment telematics and timeclock data, proposes quantities from survey or machine data where available, and turns the spoken account into a structured diary with flagged events: delay, owner instruction, condition different from the drawings. The foreman confirms or corrects in a few taps. Corrections train the drafts toward that foreman's crew and habits, and flagged events start the notice clock for the project manager the same night.

## Impact If Solved
If the end-of-shift paperwork falls from ~45 to ~10 minutes (estimate), a foreman gets back roughly 150 hours a year (estimate). The firm gets cost-code actuals clean enough to correct its estimating rates, and diaries that hold up in a claim.
