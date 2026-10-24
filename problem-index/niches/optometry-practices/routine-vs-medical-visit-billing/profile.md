# Routine-vs-Medical Visit Billing

**Parent Industry:** [[industries/optometry-practices|Optometry Practices]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to bill each eye exam to the payer its findings support, vision plan or medical, and whoever collects the most revenue per exam that survives payer audit takes the account.

## Profile
**Market Size:** ~$1.2B a year of billing staff, outsourced billing, EHR billing modules and coding help at optometry practices (estimate)
**Share of Parent Industry:** ~6% of practice revenue spent on billing and claims work (estimate)
**Digital Adoption:** Medium — claims are electronic, but the routing call at checkout is made by hand
**Target Buyer:** Practice owner at independent practices; revenue cycle director at multi-OD groups and rollups
**Automation Potential:** High — the decision follows written plan rules and medical-necessity logic, and remittances supply the feedback

## What Makes This a Distinct Niche
Optometry is one of the few outpatient specialties, with ophthalmology, where most visits can be billed to two different kinds of insurer. A vision plan pays a fixed fee for a routine exam and refraction under its own codes and copays. A medical plan pays for the same visit, at a higher rate and with diagnostic tests, if a medical complaint or finding justifies it. Medicare excludes routine eye exams and refractions by statute (Social Security Act §1862(a)(7); 42 CFR 411.15). Each vision plan writes its own rules on billing medical services, splitting a visit and coordinating with medical coverage. VSP alone paid $4.8B to private practices on 21.4M claims in 2024 (VSP Vision), so small routing errors add up. The routing decision, not claim formatting, is where an optometry practice wins or loses revenue.

## Current Tools & Gaps
Compulink, Eyefinity, RevolutionEHR, Crystal PM and MaximEyes build claims and run generic scrubbers. Clearinghouses check formats, and Eyefinity carries VSP claims. Billing services that specialise in optometry apply the rules by hand, and coding consultants teach them. None recommends the split from the note, keeps a machine-readable library of each plan's routing rules, or learns from remittances which splits each plan pays. Generic specialty billing is analysed at [[niches/medical-billing/single-specialty-billing/profile|🔵 Single-Specialty Billing]].

## Problems
- [[niches/optometry-practices/routine-vs-medical-visit-billing/build|🔨 Build: Payer-Split Recommender Trained on Remittances]]
- [[niches/optometry-practices/routine-vs-medical-visit-billing/buy|🛒 Buy: Claim Scrubbers Adapted to Vision-Plan Routing Rules]]
- [[niches/optometry-practices/routine-vs-medical-visit-billing/fix|🔧 Fix: The Medical Visit Billed as a Routine Exam]]
