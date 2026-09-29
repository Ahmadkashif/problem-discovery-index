# Every Dig Is a Labelled Example and Nobody Feeds It Back

**Niche:** [[niches/plumbing-contractors/lead-service-line-inventory-consulting/profile|Lead Service Line Inventory & Replacement Consulting]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Crews verify thousands of service lines a year, the ground truth arrives with a photograph and a GPS point, and the classification model that predicted it never hears the answer.
**Tags:** #evaluation-metrics #automation #workflow-orchestration #data-integration #worker-facing

## The Problem
Verification happens constantly and at scale. Crews pothole, excavate, or inspect at the meter, and record what the line actually is. Replacement crews expose lines every working day. Water meter replacement programmes surface material observations incidentally across an entire system.

Each of these is a labelled example: predicted material versus actual material, at a known address, often with a photograph.

The loop is not closed. Field verification results go into the inventory as an updated classification for that address and stop there. They are not compared against what was predicted, they are not used to correct the classification approach, and they are rarely propagated to neighbouring addresses whose classification rested on the same assumption that just proved wrong.

Consequences follow immediately. Systematic errors persist for the life of a programme — if the rule for a particular construction era is wrong in a particular neighbourhood, every address in that neighbourhood stays misclassified until someone digs each one. Nobody can state the inventory's accuracy, which is what a state agency will eventually ask. And crews carrying the most current knowledge about what they are finding have no channel to report it beyond a per-address record.

## Why It's Still Broken
The field workflow and the inventory workflow are different systems owned by different parties. Excavation is often a contractor's work order system; the inventory is the consultant's database; the utility's asset system is a third. Verification results move between them by periodic file transfer, and only the fields the regulator requires make the trip.

Nobody is paid for the loop. The engagement was scoped to produce an inventory and a replacement plan. Accuracy improvement across a programme is a benefit to the client's future spending and to the consultant's next engagement, and it appears in no deliverable.

And there is a quiet discomfort about measurement. A programme that formally tracked prediction accuracy would generate a record of how often its classifications were wrong, in a domain with public notification obligations and active litigation.

## What a Fix Looks Like
**Store the prediction, not just the classification.** Every address should carry what was predicted, on what basis, and with what confidence, alongside whatever verification later found. Without the first, the second teaches nothing.

**Make verification capture structured at the point of the dig.** Material at both ends, connection type, photograph, GPS, and crew — captured on a phone in the trench, not transcribed from a paper form that evening. Crews will use a form that takes thirty seconds and will not use one that takes five minutes.

**Recompute neighbours on every surprise.** A verification that contradicts the prediction is evidence about every address that shared its reasoning. Propagating that immediately is where most of the value is, and it happens today only when someone notices.

**Report accuracy by cohort, continuously.** Prediction accuracy by era, neighbourhood, record type and confidence band, updated as verifications arrive. This is the number the state agency will eventually ask for, and the programme that already has it is in a much better position than the one that has to reconstruct it.

**Harvest incidental observations.** Meter replacement, leak repair and main work all expose service lines. Those crews are not part of the inventory programme and see material constantly. A lightweight reporting path turns routine utility operations into a continuous verification stream at almost no cost.

## Who Feels the Pain
The utility, which is spending capital on a replacement order derived from classifications of unmeasured accuracy; the consultant, whose model cannot improve because it never learns; the field crews, who know things nobody collects; and residents, who receive notification letters based on a classification that may already have been contradicted two doors down.

## Impact If Fixed
Verification is the most expensive data in the programme and it is currently spent once. Feeding it back turns a national replacement effort that will run for decades into something that gets more accurate every week — and gives the consultancy a measured accuracy record that is both a regulatory asset for its clients and the strongest possible answer in a competitive procurement.
