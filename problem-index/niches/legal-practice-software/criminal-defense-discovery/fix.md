# Discovery Arrives and Nobody Knows What Is Missing

**Niche:** [[niches/legal-practice-software/criminal-defense-discovery/profile|Criminal Defense & Digital Discovery]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** A discovery production arrives as a folder of files with no manifest a defense lawyer can check against, so whether every officer's camera, every log and every requested item is actually present is established by noticing an absence.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in criminal defense case management is fighting to make a terabyte of body-worn camera and digital discovery reviewable by one lawyer before the next hearing — and whoever gets time-to-reviewable lowest takes the account.

## The Problem
Four officers were on the scene; the production contains footage from three. The CAD log references a unit that does not appear anywhere. A supplemental report cites an interview whose recording is not included. None of this is flagged, because a production is a pile of files and the absence of a file is not an event. The lawyer finds out — if at all — halfway through review, weeks later, and then has to litigate for the missing item with the hearing date approaching. Establishing what should exist is entirely on the defense, working from the documents inside the production itself.

## Why It's Still Broken
Productions are assembled by agencies with no obligation to produce a machine-checkable inventory and no standard requiring one, and the sharing portals report what was shared rather than what exists. On the defense side, the work of cross-referencing reports against media is manual, tedious and invisible — nobody is thanked for a completeness check that finds nothing. And the practice-area case management systems model discovery as an attachment set, so they have no concept of an expected item, which is what the check requires.

## What a Fix Looks Like
Derive the expected inventory from the production's own paperwork and reconcile it against the files. Reports, CAD logs and charging documents name officers, units, times, locations and recorded events; extracting those names and events is ordinary text work, and turning them into an expected-items list is mechanical. Reconcile against what is present, by officer, by device, by time window, and produce a gap report: which officers are named but have no footage, which time windows have no coverage from a unit that was on scene, which referenced recordings are absent, which files failed to open or are truncated. That report is a discovery motion's first draft, produced on the day the drive arrives instead of three weeks later. Track supplemental productions against the same list so the gap closes visibly.

## Who Feels the Pain
Defense lawyers who discover a gap too late to litigate it; clients whose case turns on footage nobody knew existed; and the investigators and paralegals doing cross-referencing by hand when they do it at all.

## Impact If Fixed
A completeness report on day one converts a discovery dispute from a late-stage scramble into a routine letter, and the shift in timing is the whole value. The extraction involved is undemanding — names, units, times — which makes this the cheapest meaningful improvement available in the niche and the one least dependent on funding the office does not have.
