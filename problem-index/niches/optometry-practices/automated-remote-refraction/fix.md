# The Non-Adapt Nobody Traces to the Prescription

**Niche:** [[niches/optometry-practices/automated-remote-refraction/profile|Automated & Remote Refraction]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Fix (Pain Point)
**One-liner:** When a patient can't adapt to new glasses, the practice remakes them without recording whether the prescription, the measurements or the lens design was at fault.
**Tags:** #logistic-regression #evaluation-metrics #feature-engineering #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce final spectacle prescriptions without the optometrist's full manual refraction, and whoever has the fewest prescription-related remakes per hundred refractions takes the account.

## The Problem
Patients come back saying the new glasses feel wrong. The optician re-measures, the doctor re-checks, and a remake is ordered. The cause goes unrecorded, so the practice cannot tell which doctors, devices or prescribing habits produce non-adapts.

## Why It's Still Broken
Remakes are logged as optical events with a reason chosen from a vague list, if at all. Nobody links them back to the refraction or reviews them as a quality measure.

## What a Fix Looks Like
A structured remake reason (prescription, fitting measurements, lens design or frame), captured at the counter and linked to the exam. A monthly report by doctor and refraction method.

## Who Feels the Pain
Patients who wait weeks for usable glasses, opticians who absorb the complaint, and owners paying for remakes.

## Impact If Fixed
Cutting prescription-related remakes from ~3% to ~2% of ~2,500 yearly eyewear orders saves ~25 remakes a year (estimate), and gives the practice the outcome measure automated refraction needs.
