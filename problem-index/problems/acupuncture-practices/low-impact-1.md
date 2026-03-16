# Insurance Billing for Acupuncture Services

**Industry:** [[acupuncture-practices|Acupuncture Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Medical billing software can submit claims, but it doesn't know that acupuncture CPT 97810 (initial 15 minutes without electrical stimulation) can only be billed once per session, that 97811 is the add-on for each additional 15 minutes, that most carriers cap at 20-26 visits per year, or that California and New York have fundamentally different scope-of-practice rules affecting billable services.
**Tags:** #llm #text-generation #nlp #compliance

## The Problem
Acupuncture insurance billing sits at the intersection of a rapidly expanding coverage mandate (39 states plus DC now require some form of acupuncture coverage) and a profession that historically operated on cash-pay. Most acupuncturists received minimal billing training in school. The CPT code set is small (97810-97814) but nuanced: 97810 is initial needling without electrical stimulation (one unit per session), 97811 is each additional 15 minutes without stimulation, 97813/97814 are the equivalents with electrical stimulation. Many practitioners underbill by using only 97810 when the session length and technique qualify for additional units. Carrier-specific rules vary wildly: some require referral from an MD, some accept self-referral; some cover only specific ICD-10 diagnoses (chronic low back pain under the ACA mandate), some cover broadly; visit limits range from 12 to 52 per year.

## What Already Exists
Jane App and Unified Practice include basic billing modules. Office Ally and Availity provide clearinghouse services. A handful of acupuncture-specific billing services (AcuBill, East West Billing) offer outsourced billing expertise. No system provides real-time CPT code optimization during charting (suggesting the correct number of units based on session duration and technique), carrier-specific rule enforcement, or visit-limit tracking with pre-authorization alerts.

## The Customisation Gap
An acupuncture billing system needs to: (1) track visit limits per patient per carrier per plan year with alerts as limits approach, (2) suggest optimal CPT code combinations based on treatment rendered (session length, techniques used, electrical stimulation yes/no), (3) enforce carrier-specific rules (referral requirements, covered diagnoses, authorization requirements), (4) map TCM diagnoses to the ICD-10 codes most likely to be covered by the specific carrier, (5) generate medical necessity documentation in biomedical language from TCM clinical findings, and (6) flag claims that are likely to be denied before submission based on carrier pattern analysis.

## Impact If Solved
Increases average reimbursement per session by 15-25% through proper unit billing (many practitioners leave $20-$40 per session on the table by under-coding). Reduces denial rate from 20-30% to 8-12% through carrier-specific documentation. Saves 3-5 hours per week currently spent on billing inquiries and appeal letters. Enables practices to accept insurance patients profitably, expanding their addressable market by 40-60%.
