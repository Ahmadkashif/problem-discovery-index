# Insurance Billing & Documentation

**Parent Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Category:** Highly Automatable

## Profile
**Market Size:** $3B
**Share of Parent Industry:** 15%
**Digital Adoption:** Medium — Most practices use chiropractic billing software or outsource to billing services, but the clinical documentation that supports billing codes is created manually and frequently doesn't meet payer requirements.
**Target Buyer:** Billing Manager / Clinic Owner
**Automation Potential:** High — Chiropractic billing uses a narrow set of CPT codes (98940-98943, evaluation codes) with well-defined documentation requirements that are highly automatable.

## What Makes This a Distinct Niche
Chiropractic billing is uniquely challenging because of the narrow code set and high denial rates. Chiropractors use primarily 4-6 CPT codes (spinal manipulation by region, evaluation/re-evaluation), but each code has specific documentation requirements that vary by payer. Medicare requires documented subluxation with functional improvement. Private insurers limit visit counts and require pre-authorization for extended treatment. Workers' comp and PI cases have entirely different billing workflows. The average chiropractic practice has a 15-25% claim denial rate — significantly higher than other healthcare specialties — primarily due to documentation insufficiency.

## Current Tools & Gaps
ChiroTouch, ECLIPSE, and Office Ally handle billing and claims submission. Revenue cycle management services (ChiroPay, Billing Precision) outsource the billing function. EHRs provide SOAP note templates. The gap is in the connection between clinical documentation and billing compliance — no tool analyzes a SOAP note in real-time and tells the DC "this note supports 98941 (3-4 regions) but not 98942 (5+ regions) because you documented findings in only 3 spinal regions."

## Problems
- [[niches/chiropractic-practices/insurance-billing/build|🔨 Build: Real-Time SOAP Note to Billing Code Compliance Engine]]
- [[niches/chiropractic-practices/insurance-billing/buy|🛒 Buy: Payer-Specific Documentation Requirements Dashboard]]
- [[niches/chiropractic-practices/insurance-billing/fix|🔧 Fix: Denial Management and Appeals Process Chaos]]
