# Feasibility — SOAP Note Generation from Examination Room Audio

**Industry:** [[veterinary-practices|Veterinary Practices]]
**Problem:** [[problems/veterinary-practices/low-impact-2|SOAP Note Generation from Examination Room Audio]]
**Problem type:** Low Impact

**Problem summary:** Ambient AI documentation tools exist for human medicine but aren't trained on veterinary clinical language, multi-species terminology, or the specific documentation patterns of a vet managing an uncooperative patient while narrating findings aloud.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Respect HIPAA/42 CFR, integrate with the EHR, and pair NLP/decision-support with clinician review.

## Open Source Data
Open data is limited because of PHI; public clinical vocabularies and de-identified research sets help, but production models need each clinic's own notes and outcomes.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
