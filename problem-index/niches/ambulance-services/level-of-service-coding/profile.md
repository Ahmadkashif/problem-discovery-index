# Level-of-Service Coding & Medical-Necessity Review

**Parent Industry:** [[industries/ambulance-services|Ambulance Services]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to code each transport at the level its chart supports, and whoever keeps the most collected dollars per transport after denials and audit recoupments takes the account.

## Profile
**Market Size:** ~$0.6B a year of ambulance coding, chart review, crew query and claim-edit work inside outsourced billing fees and in-house billing offices (estimate; billing fees commonly run ~4–8% of collections, estimate)
**Share of Parent Industry:** ~3% of 621910 receipts (estimate)
**Digital Adoption:** High for claims, low for the decision — coders read narratives on screen and decide by experience
**Target Buyer:** Billing firm chief operating officer or operator revenue-cycle director
**Automation Potential:** High — narrative reading, level assignment and pricing automate; disputed charts stay with a senior coder

## What Makes This a Distinct Niche
An ambulance claim has no clinician-chosen code to check. The coder infers the level of service (A0426–A0429, A0433, A0434) from dispatch priority, the assessment, interventions and the narrative. She checks medical necessity and mileage against origin and destination, and for scheduled runs the PCS and RSNAT affirmation. At CY2026 urban rates for a GPCI of 1.000, including the 2% add-on, BLS emergency pays $464.40 against $290.25 non-emergency, and ALS1 emergency $551.48 against $348.30 non-emergency (CMS PUF). Errors are costly in both directions. Ambulance claims had a 10.4% improper payment rate and $452.6M projected improper payments in Medicare's FY2025 sample, 46.7% of it insufficient documentation and 24.9% medical necessity (CMS CERT). Competitors are ambulance billing firms (Digitech, AIM, Intermedix, Emergicon, regional billers), in-house coders and new AI entrants such as Overdrive Health. This niche hosts the two-week MVP: a PCS and medical-necessity checker on synthetic NEMSIS v3.5 ePCRs that assigns A0426–A0429 and prices from the CMS Ambulance Fee Schedule PUF. The shared revenue cycle field is already profiled at [[niches/medical-billing/single-specialty-billing/profile|🔵 Single-Specialty Billing]], [[niches/medical-billing/denial-management-appeals/profile|⚡ Denial Management & Appeals]] and [[niches/general-hospitals/clinical-denials-status-appeals/profile|🎯 Clinical Denials & Inpatient Status Appeals]]. This niche keeps to what is ambulance-specific.

## Current Tools & Gaps
Billing modules of ambulance billing systems, clearinghouse edits, crew-query workflows and coding audits. Gaps: no model reads the narrative to recommend a level, no pre-bill necessity check, and no feedback to crews on which documentation habits get claims recouped.

## Problems
- [[niches/ambulance-services/level-of-service-coding/build|🔨 Build: Pre-Bill Level and Necessity Checker on Every ePCR]]
- [[niches/ambulance-services/level-of-service-coding/buy|🛒 Buy: Computer-Assisted Coding Taught Ambulance HCPCS]]
- [[niches/ambulance-services/level-of-service-coding/fix|🔧 Fix: Crew Addendum Requests Sent Days After the Run]]
