# CU Revision Request Prevention and Pre-Screening

**Niche:** [[niches/real-estate-appraisers/residential-lending-appraisers/profile|Residential Lending Appraisers]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Fix (Pain Point)
**One-liner:** Appraisers discover CU risk flags only after submitting to UCDP — triggering revision requests from lenders that take 1-2 unpaid hours to resolve, when the flagged issues (adjustment outliers, comp proximity, missing commentary) could have been caught and fixed in 5 minutes before submission.
**Tags:** #gradient-boosting #compliance #automation #quick-win

## The Problem
FNMA's Collateral Underwriter scores every appraisal on a 1.0-5.0 risk scale. Reports scoring above 2.5 trigger "overvaluation flags" that cause the lender or AMC to request revisions — additional comparables, revised adjustments, additional commentary, or a lower value opinion. Each revision cycle takes 1-2 hours of unpaid work (the appraiser already collected their fee). High CU scores also flag the appraiser's profile for increased scrutiny on future reports. An appraiser processing 20 reports/week with a 15% CU revision rate spends 3-6 unpaid hours weekly on revisions.

## Why It's Still Broken
CU scoring happens at FNMA's UCDP portal — the appraiser can't see their score until after submission. FNMA publishes general scoring criteria (large adjustments, inconsistent data, distant comps) but not the specific model. No pre-submission tool replicates CU's scoring logic because FNMA hasn't published it and doesn't offer a pre-submission API. The only option is a predictive model trained on historical CU scores.

## What a Fix Looks Like
A TOTAL plugin that analyzes the completed appraisal report before UCDP submission and predicts: estimated CU risk score, specific fields most likely to trigger flags (e.g., "GLA adjustment on Comp 2 exceeds market norm by 40% — consider Comp X as replacement"), and recommended changes to reduce the predicted score. The appraiser addresses flagged issues in 5-10 minutes before submitting, instead of discovering them 24-48 hours later in a revision request.

## Who Feels the Pain
Every residential lending appraiser who submits to UCDP — approximately 50,000 appraisers nationally, of whom 30-40% receive revision requests on 10-20% of submissions.

## Impact If Fixed
Revision request rate drops from 10-20% to 3-5% of submissions. Each prevented revision saves 1-2 hours of unpaid work — for an appraiser processing 20 reports/week, this recovers 2-6 hours weekly. Appraiser stress from CU anxiety decreases — currently a top-3 complaint in industry surveys.
