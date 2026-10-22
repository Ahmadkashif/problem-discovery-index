# The Ticket Closed With the Wrong Resolution Code

**Niche:** [[niches/wired-broadband-providers/hfc-plant-maintenance/profile|HFC Plant Maintenance & Proactive Network Maintenance]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Technicians close jobs by picking a resolution code from a long dropdown at the end of the day, so the operator's record of what was wrong and what fixed it is mostly noise.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to locate an outside-plant impairment from modem telemetry before customers call, and whoever sends the right crew to the right span first, without a premises visit, takes the account.

## The Problem
A maintenance technician replaces a corroded connector and tightens a tap faceplate on the same visit; an installer swaps a modem "to be safe". Both pick whatever code is quickest. Months later, analysts trying to learn which repairs fix which symptoms find "replaced equipment" on half the tickets, no location, and no way to tell which action mattered.

## Why It's Still Broken
Codes are designed for billing and labour reporting, not learning. Technicians are measured on jobs per day, and a detailed closeout costs minutes with no return to them. Nobody downstream checks codes against telemetry.

## What a Fix Looks Like
Replace the dropdown with a short voice or text note and a photo at closeout; a language model maps it to a structured record (element, action, part, location) for the technician to confirm in one tap. Check the record against telemetry: if the signature on downstream modems didn't change, flag the ticket for review rather than accepting the code.

## Who Feels the Pain
Network analytics teams trying to build any predictive model; maintenance managers who can't tell which crews fix things first time; technicians whose good work is invisible in the data.

## Impact If Fixed
A small change at closeout turns every ticket into a usable label, which is the precondition for every localisation or triage model in this niche.
