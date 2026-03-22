# Behavioral Health Billing

**Parent Industry:** [[industries/medical-billing|Medical Billing]]
**Category:** Underserved

## Profile
**Market Size:** $1.5-2B
**Share of Parent Industry:** ~10%
**Digital Adoption:** Low-Medium — BH-specific EHRs (TherapyNotes, SimplePractice, Valant) handle notes and scheduling but billing modules are basic; most BH billing companies use generic PM systems
**Target Buyer:** Behavioral health billing specialist, BH billing company owner, or group practice billing manager
**Automation Potential:** High — BH billing has unique denial patterns driven by medical necessity documentation requirements and carve-out network complexity that are highly predictable

## What Makes This a Distinct Niche
Behavioral health billing operates in a parallel universe from standard medical billing. The code set is different — 90837 (psychotherapy, 53+ minutes), 90834 (38-52 minutes), 90847 (family therapy), H-codes for substance use disorder (SUD) services, and T-codes for state-funded programs. Authorization patterns are different — many payers require session-by-session or batch authorization with clinical reviews at defined intervals. Payer networks are different — behavioral health is frequently "carved out" to specialty administrators (Optum Behavioral Health, Magellan, Carelon) who have separate provider directories, credentialing processes, fee schedules, and claim submission portals from the medical plan. Privacy is different — 42 CFR Part 2 restricts disclosure of SUD treatment records beyond standard HIPAA, affecting what information can appear on claims and coordination of benefits. Telehealth billing is different — BH was the first specialty to scale telehealth, and modifier requirements (95, GT, place of service 02 vs. 10) vary by state and payer with frequent mid-year policy changes.

## Current Tools & Gaps
BH-specific EHRs (TherapyNotes, SimplePractice, Valant, Kipu for SUD) handle clinical documentation and basic claim generation but have limited denial management, no payer rule intelligence, and minimal reporting. Generic PM systems used by billing companies don't understand BH carve-out networks, authorization cadences, or 42 CFR Part 2 constraints. Clearinghouses process BH claims identically to medical claims, missing BH-specific validation opportunities. The gap is a BH-specific billing intelligence layer that understands psychotherapy documentation requirements, tracks carve-out network rules, manages authorization timelines, and prevents the denial patterns unique to behavioral health.

## Problems
- [[niches/medical-billing/behavioral-health-billing/build|🔨 Build: BH-Specific Denial Prevention Engine]]
- [[niches/medical-billing/behavioral-health-billing/buy|🛒 Buy: BH Billing Module for Generic PM Systems]]
- [[niches/medical-billing/behavioral-health-billing/fix|🔧 Fix: Telehealth Modifier Compliance for Behavioral Health]]
