# Prior Authorization Automation

**Parent Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Category:** Highly Automatable

## Profile
**Market Size:** $0.3-0.5B embedded (touches all pharmacies processing PBM-adjudicated prescriptions)
**Share of Parent Industry:** Cross-cutting — every independent pharmacy handles 5-15 prior authorizations per day
**Digital Adoption:** Low-Medium — CoverMyMeds handles PA submission for ~75% of pharmacies but does not automate clinical data collection, alternative suggestion, or patient follow-up; the 15-30 minutes of human labor per PA is largely unchanged
**Target Buyer:** Pharmacist and pharmacy technician handling PA requests — the pharmacist provides clinical judgment, the technician handles faxing, calling, and tracking, and both lose productive time on a process that yields no direct revenue for the pharmacy
**Automation Potential:** Very High — PA workflows follow rule-based patterns (identify PA requirement, collect clinical data, match to formulary criteria, submit to PBM) with clear automation opportunities at every step, particularly clinical data collection and formulary alternative identification

## What Makes This a Distinct Niche
Prior authorization is the most universally despised workflow in pharmacy — it generates no revenue for the pharmacy, consumes 15-30 minutes of staff time per request, and directly causes patient abandonment (30% of prescriptions requiring PA are never picked up). The process begins when a prescription is rejected at adjudication with a "PA required" response. The pharmacy must then: (1) identify why PA is required (formulary exclusion, step therapy, quantity limit, age restriction), (2) contact the prescriber's office to obtain clinical justification (diagnosis, prior medication trials, clinical notes), (3) complete the PBM-specific PA form with the clinical information, (4) submit the PA electronically or via fax, (5) track the PA status over 24-72 hours, and (6) notify the patient and prescriber of the outcome. Steps 2 and 5 are the bottlenecks — the prescriber's office is often unresponsive, requiring multiple calls, and PA status tracking is manual (checking the PBM portal repeatedly). A busy independent pharmacy handles 5-15 PAs per day, consuming 1.5-7.5 hours of staff time that could be spent on revenue-generating activities like dispensing, immunizations, or MTM consultations.

## Current Tools & Gaps
CoverMyMeds (acquired by McKesson) is the dominant PA submission platform, handling electronic PA submission to most PBMs. It standardizes the submission form and provides electronic routing, reducing the submission step from fax to click. However, CoverMyMeds does not: collect clinical data from the prescriber (the pharmacy still calls or faxes the prescriber's office), suggest formulary alternatives that wouldn't require PA (the pharmacist must know the PBM's preferred alternatives), pre-fill the PA form with available clinical information, or track patient abandonment when PAs take too long. The 15-30 minutes of human labor per PA is compressed into the data collection and prescriber communication steps that CoverMyMeds does not automate.

## Problems
- [[niches/pharmacy-independents/prior-authorization-automation/build|🔨 Build: End-to-End PA Automation Agent with Clinical Data Collection and Alternative Suggestion]]
- [[niches/pharmacy-independents/prior-authorization-automation/buy|🛒 Buy: CoverMyMeds with Formulary Alternative Engine and Prescriber Auto-Communication]]
- [[niches/pharmacy-independents/prior-authorization-automation/fix|🔧 Fix: Patient Abandonment Tracking and Recovery for PA-Delayed Prescriptions]]
