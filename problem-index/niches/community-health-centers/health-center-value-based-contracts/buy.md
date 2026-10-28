# Population Health Platforms That Follow Patients Through Medicaid Churn

**Niche:** [[niches/community-health-centers/health-center-value-based-contracts/profile|Health Center Value-Based Contracts & FQHC-Led ACOs]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Population health platforms attribute patients from the payer's member file, but a health center's patients drop off Medicaid and come back months later, and the platform forgets them in between.
**Tags:** #survival-analysis #gradient-boosting #data-integration #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to earn quality and shared-savings payments for a health center's attributed Medicaid and Medicare patients on top of the PPS floor, and whoever books the most value-based revenue per attributed patient takes the account.

## The Problem
From 2027, six-month renewals and work requirements will push more patients through short coverage gaps. Each gap removes them from the plan's attribution file, breaks the quality denominator and resets care management, even though the center keeps seeing them on the sliding fee.

## What Already Exists
Innovaccer, Arcadia, Azara DRVS, Relevant, EHR population health modules and ACO enablers ingest claims and EHR data and produce gap lists.

## The Customization Gap
The health center layer:

- patient identity kept across coverage gaps, using the center's own records rather than the payer's;
- churn risk at each renewal date, linked to the eligibility team's caseload;
- quality denominators recomputed the way each payer will compute them, with the gap months shown;
- outreach effort tied to the contract measure it moves.

## Target Customer
FQHC-led ACOs and networks, and centers with three or more Medicaid managed care incentive contracts.

## Impact If Solved
If churn removes ~10% of attributed patients a year (estimate), re-attributing half of them protects quality scores and ~$20–$40 per member per month of contract revenue on those patients (estimate).
