# Night-Time Agitation and Exit-Seeking Patterns per Resident

**Niche:** [[niches/assisted-living-communities/memory-care-residents/profile|Memory Care Residents Living with Dementia]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Experienced memory care staff know which residents get restless at sundown and try the door at 2 a.m.; nobody has turned that into a per-resident pattern a new aide can use.
**Tags:** #tacit-knowledge-ml #hidden-markov-models #change-point-detection #survival-analysis #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a caregiver to a resident living with dementia before the unwitnessed fall or the open door, and whoever cuts the minutes from event to caregiver arrival takes the account.

## The Problem
Agitation, exit-seeking and night-time wandering follow patterns: time of day, a missed meal, pain, a new medication, a family visit. Veteran aides learn them over months and pre-empt them with a walk, a snack or a toilet trip. Agency and new staff do not know them, and that is when falls and elopements happen.

## Why Nobody Has Built This
Behaviour charting is a checkbox at the end of the shift. Sensor and video vendors detect events but do not model each resident's day. The patterns are individual, so models need weeks of per-resident data before they help.

## What to Build
Per-resident sequence models over sensor and video events (bed exits, corridor walking, door approaches, bathroom visits), call lights, meals, medications and visits. They learn each resident's rhythm and flag rising risk hours ahead: "Mrs. K. usually walks the east hall between 1 and 3 a.m. after a skipped dinner; she skipped dinner." Shift briefings and the night caregiver's phone get two or three residents to watch, with what has worked before.

## Target Customer
Memory care directors and chief clinical officers at chains; sensor vendors adding a care-planning layer.

## Impact If Built
If pattern-led pre-emption cuts night-time falls in a 24-resident neighbourhood by ~20% (estimate), it avoids ~5–10 falls a year, each with the ED visits, family distress and move-out risk they carry.
