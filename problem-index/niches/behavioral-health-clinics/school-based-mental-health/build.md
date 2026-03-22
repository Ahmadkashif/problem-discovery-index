# Unified School-Based Clinical Documentation & Billing Platform

**Niche:** [[niches/behavioral-health-clinics/school-based-mental-health/profile|School-Based Mental Health Providers]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A single platform where school-based therapists receive referrals from teachers, document clinical sessions under HIPAA, link therapy goals to IEP/504 objectives, and bill Medicaid through the district's school-based services program — replacing the current patchwork of Word docs, SIS entries, and disconnected billing vendors.
**Tags:** #large-language-models #attention-mechanisms #transformers #automation #data-integration #workflow-orchestration

## The Problem
School-based therapists currently manage their workflow across four or more disconnected systems: the school's SIS for student demographics and scheduling, a personal system (Word, Google Docs, or paper) for HIPAA-compliant clinical notes, the district's IEP platform (e.g., Frontline IEP, SEIS) for educational plan documentation, and a third-party Medicaid billing vendor (PCG, MAXIMUS) for reimbursement claims. A single therapy session can require documentation in three systems — clinical notes for the therapist's records, a progress update for the IEP team, and a billing-ready session log for Medicaid. Therapists spend 30-45 minutes per student per week on documentation that serves overlapping but distinct audiences, and errors in any system cascade: a missed Medicaid claim means lost revenue for the district; an incomplete IEP progress note means non-compliance at the annual review.

## Why Nobody Has Built This
The intersection of healthcare documentation, educational records, and Medicaid school-based billing is a three-way regulatory collision. HIPAA governs clinical notes, FERPA governs educational records, and state Medicaid rules govern billing — and the rules about what can be shared between these domains are complex and state-specific. EHR vendors see school-based therapy as too small and too complicated. Ed-tech vendors don't understand clinical documentation requirements. Medicaid billing vendors (PCG, MAXIMUS) focus on the billing transaction, not the clinical workflow upstream. No single team has the cross-domain expertise to build this, and the market ($5-8B) has seemed too small to justify the regulatory complexity.

## What to Build
A HIPAA-compliant, school-integrated documentation platform with four modules: (1) a referral intake that receives teacher/counselor referrals and checks Medicaid eligibility automatically, (2) a clinical documentation module with session note templates that auto-extract IEP-relevant progress data, (3) an IEP/504 integration layer that pushes therapy progress updates to the district's IEP platform via API or structured export, and (4) a Medicaid billing module with state-specific rule engines that generate claims from session documentation without manual re-entry. Start with 3-5 states with the highest school-based Medicaid billing volume (NY, CA, TX, FL, IL) and expand.

## Target Customer
School district mental health coordinators managing 10+ school-based therapists, and community mental health agencies contracting with districts to provide school-based services. Secondary buyer: the district CFO who wants to maximize Medicaid reimbursement for services already being delivered. Approximately 5,000 school districts nationally employ or contract school-based mental health providers.

## Impact If Built
Therapist documentation time drops by 50% (from ~8 hours/week to ~4 hours/week) by eliminating duplicate data entry across systems. Districts capture 20-35% more Medicaid reimbursement for school-based services because claims are generated automatically from every eligible session rather than manually and inconsistently. IEP compliance improves because progress data flows from therapy sessions to educational plans without relying on the therapist to remember to update a separate system.
