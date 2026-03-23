# Student Visa Compliance Operations

**Parent Industry:** [[industries/language-schools|Language Schools]]
**Category:** Highly Automatable

## Profile
**Market Size:** $200-400M (embedded operational cost)
**Share of Parent Industry:** Embedded cost (~3-5% of IEP operating expenses, concentrated in F-1/M-1 student programs)
**Digital Adoption:** Low — SEVIS is the mandatory federal system, but DSOs interact with it through a clunky web portal with manual data entry; no mainstream school SIS integrates with SEVIS, so every enrollment change, address update, and program extension requires dual entry
**Target Buyer:** Designated School Official (DSO) at an IEP, university, or vocational school enrolling F-1 or M-1 visa students
**Automation Potential:** High — SEVIS reporting follows strict federal rules with defined triggers (enrollment changes, address changes, program extensions, authorized absences), defined data fields, and defined deadlines — a perfectly rule-based workflow

## What Makes This a Distinct Niche
Schools enrolling international students on F-1 (academic) or M-1 (vocational) visas must comply with SEVP (Student and Exchange Visitor Program) regulations through the SEVIS system. DSOs are responsible for: creating initial I-20 documents, reporting enrollment status each session, updating SEVIS within 21 days of address changes, reporting reduced course loads with authorization, filing program extension requests before I-20 expiration, and reporting any status violation (dropping below full-time, unauthorized employment). A single missed or late SEVIS update can terminate a student's legal status — with life-altering consequences for the student and potential SEVP certification loss for the school.

## Current Tools & Gaps
The SEVIS portal (studyinthestates.dhs.gov) is the sole interface for immigration compliance reporting. Schools use SIS platforms (Terra Dotta, Sunapsis, ISSM) for immigration case management, but these tools require manual synchronization with SEVIS — the DSO enters data in the SIS, then re-enters or pushes it to SEVIS. No SIS has achieved reliable, bidirectional SEVIS integration due to SEVP's limited API availability and strict data validation requirements. The result: every compliance event requires double data entry and manual verification.

## Problems
- [[niches/language-schools/visa-compliance-ops/build|🔨 Build: Automated SEVIS Compliance Monitoring and Alert System]]
- [[niches/language-schools/visa-compliance-ops/buy|🛒 Buy: SIS-to-SEVIS Data Synchronization Layer]]
- [[niches/language-schools/visa-compliance-ops/fix|🔧 Fix: DSO Workload During Enrollment and Status Change Peaks]]
