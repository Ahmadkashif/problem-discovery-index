# Plan-Check Comment Prediction by Jurisdiction

**Niche:** [[niches/drafting-services/residential-permit-drafting/profile|Residential Plan & Permit Drafting]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every building department has predictable correction comments for residential plans, and a drafter learns them only by receiving them.
**Tags:** #large-language-models #bert #gradient-boosting #logistic-regression #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to get a homeowner's or builder's plans approved by the local building department on the first submission, and whoever knows each jurisdiction's checklist and plan-check habits best takes the repeat builder and remodeller.

## The Problem
A residential set comes back with a correction letter: missing braced-wall details, an energy compliance form on the wrong version, a stair section without headroom dimensions, a smoke alarm note that does not match the local amendment. Each comment costs a resubmittal and weeks of the builder's schedule (estimate: two to six weeks per cycle in busy jurisdictions). The comments are highly repetitive within a jurisdiction and differ between neighbouring towns.

## Why Nobody Has Built This
Correction letters are scattered across thousands of permit portals and the drafters' inboxes. Code-checking tools target commercial work and model codes, not a town's local habits.

## What to Build
A model trained on correction letters and approved sets by jurisdiction that reads a draft residential set and predicts the comments the department is likely to issue, citing the local requirement and past letters. Public permit records and the drafter's own history provide the corpus.

## Target Customer
Residential drafting firms and home designers serving several jurisdictions; production builders' in-house drafting staff.

## Impact If Built
More first-submission approvals, weeks saved on each builder's schedule, and jurisdiction knowledge that does not retire with one drafter.
