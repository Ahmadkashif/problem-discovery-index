# Payer-Split Recommender Trained on Remittances

**Niche:** [[niches/optometry-practices/routine-vs-medical-visit-billing/profile|Routine-vs-Medical Visit Billing]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A recommender that reads the finished exam and proposes which payer gets which services, with codes and patient charges, then learns from each plan's remittances what actually pays.
**Tags:** #gradient-boosting #large-language-models #bert #decision-trees #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bill each eye exam to the payer its findings support, vision plan or medical, and whoever collects the most revenue per exam that survives payer audit takes the account.

## The Problem
After each visit a biller decides whether the exam goes to the vision plan, the medical plan, or both, and what the patient pays for the refraction. The decision depends on the chief complaint, the diagnoses, the plan's rules and the patient's coverages. It is made from memory dozens of times a day, and practices that are unsure default to the vision plan.

## Why Nobody Has Built This
The rules are scattered across vision-plan provider manuals behind network portals, Medicare guidance and medical plans' policies. No vendor has turned them into a decision library. EHR vendors build the claim the user chooses; they do not choose it. The feedback that would train a model, which splits were paid and which were recouped, sits in remittance files nobody joins back to the note.

## What to Build
An LLM front end extracts chief complaint, findings and tests from the note. A rules layer encodes each plan's routing and same-day billing rules. A gradient-boosted model trained on the practice's paid and denied claims scores each candidate split. The biller sees one recommended split with a one-sentence reason and a confidence, and accepts or edits it. Edits and remittances feed back weekly.

## Target Customer
Multi-OD groups and rollups with central billing teams first, then independent practices through their EHR vendor or billing service.

## Impact If Built
For a five-OD group billing ~15,000 exams a year, routing 4% more of them correctly to medical at ~$60 more each would add ~$36,000 a year (estimate), with fewer recoupments from the opposite error.
