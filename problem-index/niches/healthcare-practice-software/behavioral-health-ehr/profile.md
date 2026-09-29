# Behavioral Health & SUD Practice Software

**Parent Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in behavioral health software is fighting to share a patient record with a referring provider while withholding exactly the 42 CFR Part 2 material and proving it did so — and whoever makes that segmentation reliable takes the account.

## Profile
**Market Size:** $1.4B US behavioral health and substance use practice software
**Share of Parent Industry:** ~8% of ambulatory software revenue, growing faster than the category
**Digital Adoption:** Low-Medium — a large share of the provider base is solo or small-group, and the SUD treatment segment in particular still runs substantially on paper because sharing is legally hazardous
**Target Buyer:** Product leads at behavioral health EHR vendors; on the practice side, clinical directors at community mental health and opioid treatment programmes
**Automation Potential:** Medium-High — consent segmentation, measurement-based care scoring and level-of-care documentation are all structurable; the constraint is legal rather than technical

## What Makes This a Distinct Niche
Behavioral health is the one ambulatory setting where the information-sharing default is inverted. Under 42 CFR Part 2, records from federally assisted substance use disorder programmes cannot be disclosed without patient consent that is specific about who, what and for how long — and the redisclosure restriction follows the data. Everywhere else in healthcare, the regulatory pressure since the information-blocking rules has been toward sharing; here, sharing the wrong field is a federal matter. The practical result is that behavioral health providers, who are the most likely of any specialty to be coordinating with a primary care physician, a hospital and a court, are the least equipped to do it. Providers respond by sharing nothing, which is safe and clinically poor, or by sharing a printed summary someone redacted by hand.

## Current Tools & Gaps
Netsmart, Qualifacts, Kipu, Valant and a long tail of small vendors serve this market, and all of them address Part 2 through consent forms and access controls rather than through data-level segmentation. The distinction matters: an access control keeps a user out of a record, but the moment the record is exported — a C-CDA to a referring physician, a payer request, an HIE query — the control does not travel with it. Consent management platforms exist and mostly model consent as a document rather than as an executable policy over fields. Measurement-based care tooling (PHQ-9, GAD-7 collection) is common and shallow, capturing scores without ever feeding them back into level-of-care decisions. And the whole category is exposed to a well-documented reimbursement structure where the clinical note's function is to justify continued authorisation, which shapes what gets written.

## Problems
- [[niches/healthcare-practice-software/behavioral-health-ehr/build|🔨 Build: Consent as an Executable Policy Over Fields]]
- [[niches/healthcare-practice-software/behavioral-health-ehr/buy|🛒 Buy: Measurement-Based Care Instruments Wired to Level-of-Care Decisions]]
- [[niches/healthcare-practice-software/behavioral-health-ehr/fix|🔧 Fix: The Note Written for the Utilisation Reviewer]]
