# Level-of-Service Coding on Claim Scrubbers Built for CPT

**Industry:** [[ambulance-services|Ambulance Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Claim scrubbers check codes against codes; an ambulance claim's level of service has to be read out of a crew's narrative, and the gap between basic and advanced, emergency and non-emergency, is the commonest reason those claims fail audit.
**Tags:** #bert #transformers #gradient-boosting #compliance #automation #revenue-impact #quick-win

## The Problem
After every transport an ambulance coder, at the operator or at a billing firm such as Digitech, AIM or Intermedix, opens the ePCR and decides what was delivered. The choices are A0428 or A0429 (basic non-emergency or emergency), A0426 or A0427 (advanced level 1), A0433 (advanced level 2) or A0434 (specialty care), plus loaded miles, origin and destination modifiers, and condition codes. The decision depends on what the narrative supports. Was an ALS assessment medically necessary, or was it an ALS crew doing a BLS job? Was the response an emergency at dispatch? Did the patient's condition make any other transport unsafe? At CY2026 urban rates for a GPCI of 1.000, including the 2% add-on, BLS emergency pays $464.40 against $290.25 for BLS non-emergency, and ALS1 emergency $551.48 (CMS fee schedule PUF). The coder makes that call thousands of times a month, often querying crews days later for an addendum.

Errors run in both directions. Undercoding leaves money behind. Overcoding is what auditors find. Medicare's FY2025 error-rate sample put ambulance claims at a 10.4% improper payment rate, $452.6M projected, with insufficient documentation 46.7% and medical necessity 24.9% of the errors (CMS CERT).

## What Already Exists
General claim scrubbers and clearinghouse edits (the field profiled at [[niches/medical-billing/healthcare-clearinghouses/profile|🔍 Healthcare Claims Clearinghouses]]), denial analytics ([[niches/medical-billing/denial-management-analytics-vendors/profile|🔍 Denial Management Analytics Vendors]]), coding audit firms ([[niches/medical-billing/coding-audit-compliance-firms/profile|🔍 Coding Audit & Compliance Firms]]), and the billing modules of ambulance billing systems, which check that required fields are filled and that the PCS date is valid.

## The Customisation Gap
Scrubbers built for professional claims validate a CPT and ICD-10 pair a clinician already chose. Ambulance coding has no clinician-chosen code to check. The level of service must be inferred from the ePCR, using Medicare's ambulance definitions, the dispatch determinant, the interventions performed and the medic's narrative of why other transport was unsafe. Mileage has to be checked against origin and destination. The tool also needs ambulance-specific edits: emergency versus non-emergency by dispatch, the ALS assessment rule, specialty care only with a qualified crew and interventions, the RSNAT affirmation number on scheduled A0426 and A0428 runs, and state Medicaid rules. A generic scrubber cannot read NEMSIS v3.5 fields or a narrative.

This is the home for the two-week MVP: a PCS and medical-necessity checker on synthetic NEMSIS v3.5 ePCRs. It reads the structured fields and the narrative, assigns A0426–A0429 with the reason, flags runs whose documentation will not support the level or the necessity, checks the PCS on scheduled runs, and prices each claim from the CMS Ambulance Fee Schedule PUF for its locality. No patient data is needed to build or demonstrate it.

## Impact If Solved
A checker that catches unsupported levels before submission would protect the billing firm's retained revenue. A book of 200,000 Medicare transports is paid ~$94M a year at the ~$470 average implied by MedPAC's $5.3B over 11.3 million transports. If audit recoupments ran at 2% of that (an estimate) and the checker cut them by a fifth, ~$375,000 a year would be kept. It would also save coders the minutes per chart now spent reading narratives that a model can pre-screen.
