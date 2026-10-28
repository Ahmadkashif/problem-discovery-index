# Heat and Pesticide Exposure Recorded as Free Text

**Niche:** [[niches/community-health-centers/agricultural-worker-health-programs/profile|Agricultural Worker Health Programmes]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** Clinicians see heat illness, pesticide exposure and work injuries in farmworkers but record them as free text, so the center cannot follow up, report patterns or show funders what it treats.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep a mobile agricultural worker's chronic care continuous as the worker moves between seasons, farms and states, and whoever keeps the largest share of returning workers with hypertension or diabetes still controlled at their first visit of the season takes the account.

## The Problem
"Dizzy after working in the field, sprayed yesterday" sits in a note. No occupational code is entered, no follow-up is scheduled for the rest of the season, and the next clinic never sees it.

## Why It's Still Broken
Occupational history fields are optional and rarely used, and clinicians under time pressure write narrative. Workers fear retaliation if exposures are reported.

## What a Fix Looks Like
An NLP pass over notes that suggests occupational exposure codes and follow-up for clinician confirmation, carries confirmed exposures into the worker's season summary, and produces de-identified counts by county and month for the programme's grant reports.

## Who Feels the Pain
Migrant health clinicians, programme directors writing 330(g) reports, and workers whose exposure history is lost.

## Impact If Fixed
If ~10% of a programme's 5,000 workers have an exposure or work-injury visit in a season (estimate), structured capture of even half turns ~250 buried notes into a follow-up list and a defensible count for its grant reports.
