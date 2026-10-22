# Field-Level Error Prediction at Origination

**Niche:** [[niches/mortgage-lenders/hmda-regulatory-reporting/profile|HMDA & Regulatory Data Reporting]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** HMDA errors are created by a handful of people entering a handful of fields, and found by compliance months later in a register-wide scrub.
**Tags:** #gradient-boosting #random-forests #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to produce a HMDA register and NMLS Mortgage Call Report that pass every edit and an examiner's sample test without a pre-deadline scrub, and whoever catches data-field errors at the point of origination rather than in February takes the account.

## The Problem
The federal platform's edits catch impossible values, not wrong ones: an application date taken from the wrong event, a rate spread computed on the wrong lock date, a property value from the wrong document, an action taken coded inconsistently. Examiners test samples against the file, and an error rate above their threshold forces resubmission.

## Why Nobody Has Built This
HMDA tools validate the register against the specification; none learns from the lender's own correction history which fields, loan types, branches and staff produce errors.

## What to Build
A model trained on every past scrub correction and examiner finding that scores each loan's HMDA fields for error risk at key milestones (application, action taken, closing), cross-checks risky fields against the source documents, and routes probable errors to the person who entered them while the file is still open.

## Target Customer
Chief compliance officers and HMDA managers at lenders reporting thousands to hundreds of thousands of records.

## Impact If Built
Errors fixed where they are made, a smaller year-end scrub, and a lower risk of resubmission in an examination.
