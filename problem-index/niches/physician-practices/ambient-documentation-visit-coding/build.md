# An Audit-Defensibility Score for Every Ambient Note

**Niche:** [[niches/physician-practices/ambient-documentation-visit-coding/profile|Ambient Documentation & Office Visit Coding]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Ambient scribes write the note and suggest a level, but none of them scores whether that level and each risk-adjusting diagnosis would survive a payer or RADV audit, traced back to what was actually said in the room.
**Tags:** #bert #large-language-models #logistic-regression #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn the office visit into a signed note that supports the billed E/M level and risk-adjustment codes before the physician leaves for the day, and whoever closes the most notes the same day with no downcoding on payer or RADV audit takes the account.

## The Problem
A practice that adopts an ambient scribe gets longer, more complete notes, and often a shift toward higher E/M levels and more documented chronic conditions. Some of the shift is real: physicians were under-documenting before. Some is not, and the practice cannot tell which. Payer audits arrive months later, and RADV audits of MA diagnoses years later, with extrapolated penalties.

## Why Nobody Has Built This
Ambient vendors are paid to save physicians time, and a score that tells the physician "this 99215 is weak" works against adoption. Coders audit a small sample by hand. Audit outcomes sit in denial letters and compliance files that never return to the documentation tool.

## What to Build
A scoring layer that reads the transcript, the note and the claim together. For each billed level, it checks the MDM elements (number and complexity of problems, data reviewed, risk of management) against the 2021 rules and points to the sentence in the transcript that supports each one. For each HCC diagnosis, it checks for evidence that the condition was monitored, evaluated, assessed or treated in this visit. Scores are calibrated on the practice's coder audits and payer audit outcomes, and weak notes are routed back to the physician before signature, not after the claim drops.

## Target Customer
Compliance officers and revenue cycle leaders at 20–500 physician groups and MSOs that adopted ambient scribes in 2025–2026, especially those in MA risk contracts.

## Impact If Built
Catching unsupported levels and diagnoses before billing could cut audit takebacks by ~30%–50% (estimate). It would also protect legitimate gains, since a 5% share of visits correctly moved from 99213 to 99214 is worth ~$25,000 a year per primary care physician (estimate).
