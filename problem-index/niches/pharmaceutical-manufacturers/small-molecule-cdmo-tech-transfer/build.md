# A Transfer Risk Score From the CDMO's Own History

**Niche:** [[niches/pharmaceutical-manufacturers/small-molecule-cdmo-tech-transfer/profile|Small-Molecule CDMO Tech Transfer & Commercial Supply]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A CDMO has run hundreds of tech transfers and cannot say, for a new one, which features of the product predict a failed engineering or PPQ batch.
**Tags:** #gradient-boosting #gaussian-processes #feature-engineering #transfer-learning #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bring a sponsor's process into its plant and through validation, and whoever passes the highest share of process performance qualification batches first time takes the account.

## The Problem
Each transfer starts with a gap assessment: equipment differences between the sponsor's site and the CDMO's, scale-up of granulation or coating, analytical method transfer, API particle size, excipient grade. MSAT engineers judge risk from experience, and the plan and price follow. When a PPQ batch fails, the lesson goes into a report and the engineer's memory.

## Why Nobody Has Built This
Each transfer's data belongs partly to the sponsor and sits in project folders. Engineers move between CDMOs. Validation tools record what was executed, not what predicted trouble.

## What to Build
A transfer ledger built from the CDMO's own project history: product and process attributes (dosage form, drug load, API properties, unit operations, scale factor, equipment train), the gap assessment as made, and the outcome (engineering batches needed, deviations, PPQ pass or fail, days to approval). Models score a new transfer's risk by unit operation, suggest which engineering studies to add, and calibrate quotes. Sponsor-confidential process details stay inside the project; the ledger learns from de-identified attributes and outcomes.

## Target Customer
Heads of MSAT and business unit leaders at mid-size and large CDMOs.

## Impact If Built
If one in five transfers needs an extra engineering or PPQ batch today (estimate), cutting that rate by a third would save a batch cost and weeks of schedule on many projects a year, and would be the CDMO's best evidence in a competitive bid.
