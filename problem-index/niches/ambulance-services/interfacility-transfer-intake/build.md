# Level-of-Care Questionnaire Graded Against What the Crew Found

**Niche:** [[niches/ambulance-services/interfacility-transfer-intake/profile|Interfacility Transfer Intake & Level-of-Care Matching]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The level of care for a transfer is chosen from a phone description, and nobody compares it with what the crew found at the bedside or what the claim could support.
**Tags:** #logistic-regression #gradient-boosting #large-language-models #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a hospital's or nursing facility's transport request into the right crew at the door, and whoever has the lowest share of interfacility transports billed at a different level of service from the one dispatched takes the account.

## The Problem
A call-taker asks a case manager whether the patient needs oxygen, a monitor, IV fluids or medications en route, and picks a level. The answers are vague ("on a little oxygen", "has an IV"), and the call-taker is not a clinician. The crew's ePCR and the coder's level later tell the true story, but neither goes back to intake.

## Why Nobody Has Built This
Intake, ePCR and billing are separate systems, often from separate vendors, and the mismatch is recorded only as a cancelled run, an upgrade note or a downcoded claim. No one owns the metric.

## What to Build
A structured intake questionnaire, by voice agent or web form, that maps answers to Medicare's level definitions: active IV medications, cardiac monitoring, ventilation, the need for an ALS assessment. A model then predicts the level the crew will find and the level the claim will support from the answers, the requesting unit and the diagnosis. Every run is graded on dispatched against billed level, and the questionnaire and model improve from the mismatches.

## Target Customer
Operators with hospital transfer contracts, and hospital systems that run their own transfer centres and ambulance fleets.

## Impact If Built
If 8% of interfacility runs are billed at a different level from the one dispatched (an estimate) and the questionnaire halved that, an operator running 40,000 transfers a year would avoid ~1,600 upgrades, cancellations or downcodes.
