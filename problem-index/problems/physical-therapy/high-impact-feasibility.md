# Feasibility — Authorization Lifecycle Automation

**Industry:** [[physical-therapy|Physical Therapy]]
**Problem:** [[problems/physical-therapy/high-impact|Authorization Lifecycle Automation]]
**Problem type:** High Impact

**Problem summary:** PT clinics never deliver a visit without valid authorization again — every patient's authorization status, remaining visits, and upcoming expiration is tracked automatically, and extension requests are triggered before limits are hit.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Respect HIPAA/42 CFR, integrate with the EHR, and pair NLP/decision-support with clinician review.

## Open Source Data
Open data is limited because of PHI; public clinical vocabularies and de-identified research sets help, but production models need each clinic's own notes and outcomes.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
