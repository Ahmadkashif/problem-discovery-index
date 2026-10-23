# Referral Packet Scoring in Ten Minutes

**Niche:** [[niches/skilled-nursing-facilities/referral-admissions/profile|Hospital Referral Intake & Admissions]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An admissions team reads a long hospital packet by hand to decide in an hour whether it can afford and care for a patient, and loses the referral if it takes longer.
**Tags:** #large-language-models #transformers #gradient-boosting #evaluation-metrics #revenue-impact #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to decide on a hospital referral within the hour with the payer authorisation, the cost of care and the risk of readmission already known, and whoever says yes fastest to the referrals that will be authorised, paid and not readmitted takes the account.

## The Problem
The packet holds the hospital course, medications, therapy notes, wound and line details, and payer information, scattered through scanned pages. The admissions coordinator flags anything that looks expensive or unmanageable and calls the DON. High-cost drugs, a missed behavioural history or an unauthorised MA plan turn a referral that looked good into a loss.

## Why Nobody Has Built This
Referral platforms are built for hospitals, whose goal is placement speed, not the facility's margin. EHR vendors start once the resident is admitted. Until LLMs, extracting structured facts from scanned hospital packets was not reliable.

## What to Build
An intake model that reads the packet in minutes and returns a one-page decision brief. It covers predicted PDPM groups and daily rate by payer, estimated drug and supply cost for the stay, care needs the facility can or cannot meet, MA authorisation requirements and the plan's recent approval pattern, and a readmission risk score trained on the operator's own history. It sends a draft acceptance or decline to the hospital portal for the coordinator to confirm.

## Target Customer
Directors of admissions and VP business development at chains competing for hospital referrals in dense markets.

## Impact If Built
Answering in ~15 minutes instead of ~2 hours (estimate) wins more of the referrals worth taking. Short stays carry a 24% fee-for-service Medicare margin (MedPAC), so each extra well-chosen admission is among the most profitable business the building has, and fewer admissions lose money or return to hospital within a week.
