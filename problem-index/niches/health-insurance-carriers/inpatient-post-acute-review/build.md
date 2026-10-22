# Length-of-Stay Decisions Graded by Readmission

**Niche:** [[niches/health-insurance-carriers/inpatient-post-acute-review/profile|Inpatient & Post-Acute Concurrent Review]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every end-of-stay decision has an observable consequence within 30 days, and no plan grades its reviewers or criteria on it.
**Tags:** #survival-analysis #causal-inference #gradient-boosting #large-language-models #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to set each inpatient and post-acute stay's length from the clinical record in daily review, and whoever's length-of-stay decisions hold through appeals and peer-to-peer reviews with no rise in readmissions takes the account.

## The Problem
A concurrent review nurse decides that a member's skilled nursing stay can end on day 18, or that a hospital day is no longer acute. The decision is recorded with the criterion cited. What follows is also recorded, but elsewhere: a fast-track appeal to the Medicare quality improvement organisation, a readmission on day 24, a home health episode or a fall. The plan never compares the two, so it cannot tell which reviewers' stay decisions are followed by harm or by successful appeals, or which criteria predict them.

## Why Nobody Has Built This
Post-acute vendors that predict length of stay are paid on reduced days, not on outcomes. Plans fear what an outcome-graded record would show in discovery. And the functional evidence that decided the case, the therapy notes, is rarely captured in structured form.

## What to Build
Extraction of functional status (mobility, self-care, cognition scores) from facility notes at each review. A record of each stay decision with the evidence used. And survival models of readmission, emergency use and appeal by decision, reviewer and criterion, adjusted for member risk. The output is a quality signal, not a cost lever: a monthly report of the decisions most often followed by readmission or overturn, which the medical policy committee reviews.

## Target Customer
Chief medical officers and care management leaders at MA plans and their post-acute management vendors, under litigation and regulatory scrutiny.

## Impact If Built
Plans could show that their stay decisions are clinically sound, find the reviewers and criteria that are not, and cut the readmissions that cost more than the days saved.
