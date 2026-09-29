# Cutting the Clips by Hand

**Niche:** [[niches/ux-research-agencies/report-production/profile|Report & Deliverable Production]]
**Industry:** [[industries/ux-research-agencies|UX Research Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The researcher is scrubbing through recordings at eleven at night to find the moment they already marked during analysis.
**Tags:** #quick-win #automation #workflow-orchestration #worker-facing #data-integration #evaluation-metrics #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to produce the deliverable without a day of slide building, and whoever automates it takes the account.

## The Problem
Highlight clips are the most persuasive part of a research deliverable and the most tedious to produce. The researcher marked the relevant moments during analysis, in one tool, and then finds them again by scrubbing through recordings in another, trims them by hand, and assembles them into a reel. The information needed to do it automatically was recorded hours earlier and is not connected to anything.

## Why It's Still Broken
The mark and the video live in different tools — a timestamp recorded during analysis that the editing tool cannot see makes the researcher find the moment twice. Clip production is treated as editing rather than as export. Nobody measures the time. And it happens last, when nobody is looking.

## What a Fix Looks Like
Connect the mark to the recording and export rather than edit. Export clips directly from the timestamps marked during analysis, which is the fix and removes the second search entirely. Mark moments with a single action during the session and during review, so the marks exist in the first place. Add a standard buffer before and after rather than trimming each clip precisely, since precision is rarely needed. Generate captions automatically from the transcript, which is expected now and is a further manual step. Produce the reel in the order the findings argue rather than chronologically. Keep clips linked to the finding they support so they are reusable in other deliverables. Anonymise faces and names where the consent requires it, automatically rather than by editing. Store clips against the study so they are available to the repository later. Produce a short and a long version, which is currently two passes. And make regeneration cheap so a changed finding does not mean recutting.

## Who Feels the Pain
Researchers doing video editing at night; deliverables that ship without clips because there was no time; clients who would have been persuaded by thirty seconds of footage; and the analysis, whose best evidence goes unused.

## Impact If Fixed
A timestamp recorded during analysis that the editing tool cannot see makes the researcher find the moment twice. Exporting from the marks turns clip production from editing into export.
