# Capability as a Checkbox

**Niche:** [[niches/print-on-demand-platforms/facility-routing/profile|Facility Routing]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A facility's capability is recorded as a set of ticked boxes from onboarding — does embroidery, does direct-to-garment — and a tick means it is possible rather than that it is done well.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #compliance #automation #quick-win #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to send each order to the facility that will produce it well rather than the one that is nearest — and whoever does that takes the quality, because quality is the variable the routing decision currently omits.

## The Problem
A facility ticked direct-to-garment during onboarding two years ago. They have one machine, limited experience with dark substrates and no colour management, and they can indeed print direct-to-garment. The routing engine treats that tick as equivalent to a facility with six machines, a profiled workflow and a specialist operator. Orders are routed to both on the same basis. The tick is a statement of possibility that the system reads as a statement of competence, and nothing has updated it since the day it was entered.

## Why It's Still Broken
Capability flags came from partner onboarding, which is a commercial process asking what a facility can do rather than a technical one measuring how well. Updating the record would require an assessment nobody schedules. The outcome data that would populate a real score is in another system. And a flag is the data type the routing engine expects.

## What a Fix Looks Like
Replace the flag with a measured score. Compute competence per facility per work type from realised outcomes — reprint rate, complaint rate, turnaround, colour accuracy where measured — which is a query against existing data and immediately turns a two-year-old tick into a current measurement, and is the fix. Assess capability at onboarding with a physical test print rather than a questionnaire, which is a day's work and establishes a baseline before any customer order is risked. Reassess periodically and on drift, since equipment, staff and processes change and a capability record is a perishable asset. Distinguish can from does well explicitly, so a facility that is technically able but poor at a work type is not offered it. Report their scores to facilities with the specific failure modes, since most will improve if told and currently receive nothing. Tie volume to score, which is the mechanism that makes the measurement matter. Record capability at the granularity that routing needs — method, substrate, colour complexity, product family — rather than as a category tick. Handle new facilities with a deliberate ramp rather than full routing or none, so they build a record safely. And remove capabilities that are not exercised, since an untested capability is a claim.

## Who Feels the Pain
Customers whose orders were routed to a facility technically able to produce them; facilities judged by a tick they made two years ago; and platforms whose routing treats a claim as a measurement.

## Impact If Fixed
A tick states possibility and the routing reads it as competence, and it has not been revisited since onboarding. Competence per work type from realised outcomes is a query against existing data, and tying volume to the score is what makes the measurement change anything.
