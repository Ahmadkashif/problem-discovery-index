# Copied-Forward Progress Notes That Undercut the Day

**Niche:** [[niches/psychiatric-hospitals/continued-stay-utilization-review/profile|Continued-Stay Review & Medical-Necessity Defence]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** Psychiatrists copy yesterday's progress note forward, so the record shows the same symptoms for a week and neither the payer reviewer nor a later auditor can see what changed or why the patient still needed the bed.
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #worker-facing #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to get each psychiatric day the record supports paid and kept paid. But managed-care concurrent review is won by the lowest share of reviewed days denied, while Medicare recertification and audit defence is won by the lowest share of audited paid days recouped, with different staff, vendors and failure modes. Decomposed into contested sub-niches below.

## The Problem
"Patient remains paranoid, poor insight, continue current plan" appears on days 4 through 11. The reviewer denies day 9 for lack of progress or new information; an auditor later calls days 6–11 custodial.

## Why It's Still Broken
EHR templates make copying forward the fastest option for physicians rounding on 20 patients, and nothing flags a note that adds nothing.

## What a Fix Looks Like
At signing, compare the note with the previous three days, nursing and technician entries and the medication record, and prompt the psychiatrist with what changed (a restraint overnight, a dose increase, a refused hearing) to add in one line.

## Who Feels the Pain
UR coordinators arguing days with nothing new to say, psychiatrists asked to do peer-to-peers, and compliance officers facing audits.

## Impact If Fixed
If change-prompted notes win back ~1 of every 20 days now denied for lack of progress (estimate), a 100-bed hospital denied ~1,500 days a year keeps ~75 days, ~$75,000 at ~$1,000 a day.
