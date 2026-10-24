# Routing Each Exam to the Vision Plan or the Medical Plan

**Industry:** [[optometry-practices|Optometry Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Claim scrubbers check codes generically, but the call that decides an optometry practice's revenue, whether a visit is a routine vision exam or a medical visit and how to split it, is still made by a biller from memory of each plan's rules.
**Tags:** #gradient-boosting #large-language-models #bert #decision-trees #automation #compliance #revenue-impact

## The Problem
A patient with a VSP card comes in for an annual exam and mentions floaters, or itchy eyes, or a diabetes diagnosis. The doctor dilates, finds blepharitis or a retinal finding, and orders an OCT. The visit now has a routine half and a medical half. The practice's biller has to decide after the visit which payer gets which part: bill the whole visit to the vision plan, bill it to the medical plan with the refraction charged separately to the patient, or split it where the plans allow. The answer depends on the chief complaint, the diagnosis codes, the plan's rules on billing both on one day, whether the vision plan also covers medical eye care, and the patient's coordination of benefits. Medicare excludes routine eye exams and refractions, even when performed alongside a covered diagnosis (Social Security Act §1862(a)(7); 42 CFR 411.15), so the advance beneficiary notice and refraction fee have to be right too.

Getting it wrong costs money both ways. A medical visit billed to the vision plan collects a fixed exam fee instead of a higher medical payment for the visit and diagnostic tests. A routine visit billed to medical without a qualifying complaint is denied or recouped at audit. Many practices default to billing everything to the vision plan because it is simpler, and leave medical revenue uncollected.

## What Already Exists
Optometry EHRs (Compulink, Eyefinity Encompass, RevolutionEHR, Crystal PM, MaximEyes) include claim builders and generic scrubbers that check code validity, modifiers and missing fields. Clearinghouses (Availity, Waystar, Eyefinity for VSP) check payer formats. Coding consultants sell guides on routine-versus-medical billing, and the AOA publishes coding resources. None of them makes the routing decision: the scrubber validates the claim the biller already chose to build.

## The Customisation Gap
What's missing is a router that reads the visit and recommends the payer split. It needs a library of each vision plan's rules on medical billing, same-day services and refraction (many sit in provider manuals behind network portals), the patient's active coverages and coordination-of-benefits order, and the medical-necessity logic that links chief complaint and diagnosis to each test. It should propose the split, the codes and modifiers, the patient's refraction charge and the Medicare notice, and explain its reasoning so the biller can accept it in one click. It also needs to learn from remittances which splits each plan actually pays.

## Impact If Solved
A practice seeing ~4,000 exams a year that routes even 5% more visits correctly to medical would collect roughly ~$20,000–$40,000 more a year (estimate) and cut the audit recoupments that come from defaulting the other way. Billers would stop rebuilding the same decision from memory dozens of times a day.
