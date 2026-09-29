# The Hour a Day Nobody Counts

**Niche:** [[niches/field-service-software/field-technician-tools/profile|Field Technician Tools]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** Technicians spend roughly an hour a day on administration, much of it after hours, and no contractor measures it — so it is invisible in every capacity calculation, every productivity target and every conversation about pay.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #worker-facing #compliance #quick-win #revenue-impact
**Contested on:** Every serious competitor building for technicians is fighting to have the visit record complete before the truck pulls out of the driveway, without the technician typing — and whoever gets time-from-last-task-to-moving lowest takes the technician's loyalty and the owner's account.

## The Problem
A contractor plans six calls a day per technician based on job durations and drive times. The administration between and after those calls is not in the plan, so the technician either compresses it, does it in the evening, or the day runs long. Owners describe technicians as slow; technicians describe the paperwork. Neither has a number. In trades where technicians are paid partly on billable hours or commission, unbilled administrative time is also a pay question that nobody has quantified, which is a live source of resentment in a workforce that is already hard to retain.

## Why It's Still Broken
Time between jobs is recorded as drive time or as nothing, and no system separates administration from travel or from a break. Measuring it requires either explicit logging, which technicians will reasonably resent, or inference from application usage and location, which shades toward surveillance if handled carelessly. So nobody measures it, and an hour a day across a workforce stays invisible — which suits nobody, since the owner is planning capacity wrong and the technician is doing unrecognised work.

## What a Fix Looks Like
Measure it from the application's own telemetry, in aggregate first, and tell the technicians what is being measured and why before measuring anything. Time from last task completion to vehicle movement, time in the application after the last job of the day, and time spent per form are all derivable without tracking a person's location beyond what dispatch already uses. Report it in aggregate to the business — administrative minutes per job by job type — which is the number that belongs in capacity planning and does not currently exist anywhere. Report it individually only to the technician, as their own information. Then use it as the evaluation metric for every interface change, so the vendor and the contractor can tell whether a redesign actually helped rather than assuming. Where the measured time is genuinely unpaid, that is a finding the owner should have to look at, and the measurement is what makes the conversation possible.

## Who Feels the Pain
Technicians doing an hour of unrecognised work a day; owners planning six calls against a day that fits five and a half; and dispatchers whose schedules fail for a reason nobody has named.

## Impact If Fixed
Putting administrative time into the capacity model corrects schedules that are systematically over-packed, which reduces the end-of-day overruns that drive technician attrition. The measurement also gives every subsequent improvement in this niche an honest evaluation metric, and it puts a real number into a pay conversation that currently runs on assertion from both sides.
