# Medical Transfer-Back Risk Check on Every Referral

**Niche:** [[niches/psychiatric-hospitals/intake-ed-referrals-medical-clearance/profile|Psychiatric Intake, ED Referrals & Medical Clearance]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Intake clinicians judge medical stability from faxed ED packets by experience, and no tool estimates which referred patients will need to go back to an acute hospital within 72 hours.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn emergency-department referrals into admissions the unit can treat safely, and whoever has the lowest share of admissions transferred back to an acute hospital within 72 hours takes the account.

## The Problem
An older patient with a urinary infection presenting as psychosis, a patient on day two of alcohol withdrawal with a history of seizures, a patient who overdosed twelve hours ago: each looks psychiatric on the packet and may be medical by morning.

## Why Nobody Has Built This
Referral packets are faxed images, outcomes are spread across two hospitals, and few psychiatric hospitals record declines or transfers back in a usable form.

## What to Build
Read the packet (ED notes, vitals, labs, toxicology, medications) into structured fields with a document model; score transfer-back risk with a gradient-boosted model trained on the hospital's own accepted referrals and their 72-hour outcomes; and list the missing tests the unit's medical criteria need. The intake clinician decides. Development runs on synthetic packets.

## Target Customer
Intake directors and medical directors at freestanding hospitals, especially those taking geriatric and detox patients.

## Impact If Built
If medical transfers back fall from ~3% to ~2% of admissions (estimate), a hospital admitting 3,000 patients a year avoids ~30 ambulance transfers and the lost bed-days around them.
