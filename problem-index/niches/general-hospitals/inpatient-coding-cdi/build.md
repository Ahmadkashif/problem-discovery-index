# CDI Queries Ranked by Audit Survival, Not Just Dollars

**Niche:** [[niches/general-hospitals/inpatient-coding-cdi/profile|Inpatient Coding & Clinical Documentation Integrity]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** CDI tools rank open charts by the revenue a query might add, then the hospital gives part of that revenue back when payers audit and reverse the weakest DRG shifts.
**Tags:** #gradient-boosting #bert #large-language-models #survival-analysis #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to assign the DRG the documentation truly supports before the claim drops, and whoever captures the most legitimate severity with DRG shifts that survive payer audit takes the account.

## The Problem
Sepsis, acute respiratory failure, malnutrition and encephalopathy are the diagnoses CDI targets most and payers audit most (recalled). A query that adds an MCC on thin clinical evidence raises the DRG today and invites a validation audit and reversal later, plus appeal cost. CDI worklists score the upside and ignore the clawback.

## Why Nobody Has Built This
Audit outcomes arrive months later on different remittances and live in denial tools, not CDI systems. Vendors are paid on captured revenue or volume, not net of reversals.

## What to Build
A model that, for each query opportunity, estimates both the DRG gain and the probability that the payer reverses it, using clinical evidence strength (the criteria a payer will apply, such as Sepsis-3 indicators), payer and diagnosis audit history, and the hospital's appeal outcomes. It ranks opportunities by expected net revenue and shows reviewers the evidence gaps that would make a shift defensible.

## Target Customer
CDI directors and revenue integrity leaders at hospitals with rising DRG-validation denials.

## Impact If Built
Shifting effort from fragile to defensible severity capture keeps CMI gains while cutting downgrade denials and appeal cost (estimate: ~20–30% fewer reversals).
