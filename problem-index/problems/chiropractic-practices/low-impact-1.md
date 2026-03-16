# Insurance Billing and Medical Necessity Documentation

**Industry:** [[chiropractic-practices|Chiropractic Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic medical billing tools can submit claims, but they don't know that chiropractic CPT code 98941 (3-4 spinal regions) requires documentation of specific subluxation levels, that most carriers limit chiropractic visits to 12-24 per year, or that the medical necessity language for visit 13 must be dramatically different from visit 1 — and getting it wrong means a denial that costs $75-$150 in lost revenue plus 30 minutes of appeal time.
**Tags:** #llm #text-generation #nlp #compliance

## The Problem
Chiropractic insurance billing is uniquely adversarial. Carriers impose visit limits (typically 12-24 visits per plan year), require pre-authorization for extended treatment plans, and deny claims at rates 2-3x higher than general medical claims. Each visit requires documentation of specific subluxation findings (by spinal level), functional limitations, treatment rendered (by CPT code), and measurable progress toward treatment goals. The documentation language that justifies visit 3 is fundamentally different from what justifies visit 15 — early visits emphasize acute findings and pain reduction, while later visits must demonstrate ongoing functional improvement and medical necessity for continued care. Most DCs are not trained in insurance documentation strategy, resulting in denial rates of 15-25% that could be reduced to 5-8% with proper language.

## What Already Exists
Practice management systems (ChiroTouch, ECLIPSE) handle claim submission. Generic medical billing services process claims but lack chiropractic-specific expertise. Office Ally and Tebra provide clearinghouse services. Some chiropractic billing consultants offer documentation templates. No system dynamically generates medical necessity language calibrated to the patient's visit number, carrier-specific requirements, and documented clinical findings.

## The Customisation Gap
A chiropractic billing system needs to: (1) track visit counts per patient per carrier per plan year and alert when approaching limits, (2) generate medical necessity language that evolves with the treatment course — emphasizing different clinical findings and progress metrics at visit 5 vs. visit 15 vs. visit 25, (3) auto-populate subluxation-level documentation from clinical findings, (4) match CPT codes to documented treatment (distinguishing 98940/98941/98942 based on regions treated), (5) flag documentation gaps that will trigger denials before the claim is submitted, and (6) generate carrier-specific appeal language for denied claims using the patient's documented clinical findings.

## Impact If Solved
Reduces claim denial rate from 15-25% to 5-8%, recovering $30K-$80K annually for a typical solo DC practice. Cuts documentation time from 5-8 minutes per visit to 2-3 minutes by auto-generating medical necessity language. Eliminates the 30-60 minutes per denial spent on appeals by auto-generating appeal letters. Enables DCs to extend treatment plans past carrier visit limits with properly documented medical necessity.
