# Automated Comp Pre-Selection with CU Score Prediction

**Niche:** [[niches/real-estate-appraisers/residential-lending-appraisers/profile|Residential Lending Appraisers]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool recommends the optimal comparable sales for a specific subject property while predicting the Collateral Underwriter (CU) risk score that each comp combination will produce — forcing appraisers to select comps through experience and intuition, then discover CU flags only after submission.
**Tags:** #gradient-boosting #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
An appraiser searches the MLS for recent sales similar to their subject and must select 3-5 comparable sales that: are reasonably similar in physical characteristics (minimizing total adjustments), are geographically proximate, sold recently, and — critically — will pass FNMA's Collateral Underwriter review without generating a high risk score. CU evaluates whether the appraiser's comp selection and adjustments are consistent with market norms. An experienced appraiser who has processed 1,000+ reports in the same market develops an intuitive sense for which comps CU will flag — they know that CU penalizes large GLA adjustments more than condition adjustments in certain markets, or that using a comp from a different school district triggers proximity flags. This tacit knowledge takes 3-5 years to develop, and junior appraisers learn it through trial-and-error (submit, get flagged, revise, resubmit).

## Why Nobody Has Built This
CU scoring logic is proprietary — FNMA publishes general guidelines but not the specific scoring model. Building a CU prediction model requires training on thousands of CU-scored appraisals with known comp selections, which requires a data partnership with a large AMC or a la mode. The comp selection optimization problem also requires appraiser acceptance: appraisers are professionally responsible for comp selection and may resist automated recommendations.

## What to Build
A comp recommendation engine that: analyzes the MLS candidate pool for a subject property, ranks candidates by a multi-factor similarity score (incorporating physical characteristics, location, recency, and estimated adjustment magnitude), and predicts the CU risk score for the top comp combinations. The appraiser sees: "Comp set A is predicted CU 1.8 (low risk); Comp set B is predicted CU 3.1 (high risk) — the difference is the GLA adjustment on Comp 3." Integration with TOTAL for direct comp import.

## Target Customer
Residential lending appraisers processing 8+ AMC orders per week — approximately 30,000-40,000 appraisers nationally. Average contract value: $100-$200/month.

## Impact If Built
Comp selection time drops from 30-45 minutes to 10-15 minutes per report. CU revision requests decrease 40-60% because appraisers pre-screen comp combinations. At $350/assignment and 20 assignments/week, saving 20 minutes per report recovers 6+ hours weekly — equivalent to 1-2 additional assignments worth $700-$1,000 per week.
