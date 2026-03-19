# Feasibility — Real-Time Insurance Eligibility Verification at Check-In

**Industry:** [[urgent-care|Urgent Care]]
**Problem:** [[problems/urgent-care/low-impact-1|Real-Time Insurance Eligibility Verification at Check-In]]
**Problem type:** Low Impact

**Problem summary:** Generic insurance verification APIs exist but aren't integrated into urgent care check-in workflows in a way that resolves the payer-specific edge cases (copay tiers, urgent-care-specific benefit structures) that cause billing errors downstream.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Respect HIPAA/42 CFR, integrate with the EHR, and pair NLP/decision-support with clinician review.

## Open Source Data
Open data is limited because of PHI; public clinical vocabularies and de-identified research sets help, but production models need each clinic's own notes and outcomes.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
