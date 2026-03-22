# Mobile Dental Unit Operations Platform

**Niche:** [[niches/dental-practices/mobile-dentistry/profile|Mobile Dentistry / Dental Vans]]
**Industry:** [[industries/dental-practices|Dental Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A purpose-built platform managing the full mobile dental workflow — site scheduling with facilities months in advance, batch patient processing with consent tracking, offline-capable field documentation, portable imaging integration, and multi-payer billing across Medicaid, facility contracts, and grant funding — because nothing exists for this workflow today.
**Tags:** #workflow-orchestration #data-integration #automation #large-language-models #transfer-learning #compliance

## The Problem
Mobile dental programs manage a workflow that no existing dental software was designed for. A typical program operates 3-5 mobile units across a metropolitan area, each visiting 150-200 sites per year (schools, nursing homes, group homes, shelters). Coordinating these visits requires: site relationship management (contact person at each facility, parking logistics, power/water access, seasonal availability), advance scheduling (schools book 3-6 months ahead and require confirmation 2 weeks before), consent form distribution and tracking (for minors), batch patient flow management on visit day (50 patients in 6 hours means 7 minutes per patient including documentation), field documentation with unreliable connectivity, portable imaging with separate storage, and post-visit billing across multiple payers. Currently, site scheduling lives in Google Calendar, consent tracking in Excel, clinical documentation in a retrofitted PMS, and billing in a separate clearinghouse — none connected.

## Why Nobody Has Built This
The market is small (~2,000 mobile dental programs in the US) with low per-customer revenue potential ($200-500/month) and a buyer who is often a nonprofit or government-funded entity with limited software budgets. The workflow complexity is high — combining CRM (site relationships), project management (visit scheduling), EHR (clinical documentation), imaging (portable X-ray integration), and billing (multi-payer claims) into a single platform requires significant engineering investment. VC-backed dental tech companies target the 200,000 fixed-location practices, not the 2,000 mobile programs. The offline-capability requirement adds architectural complexity (local-first data with sync) that most SaaS teams avoid.

## What to Build
A mobile-first (tablet-native) platform with 5 integrated modules: (1) Site CRM — manage facility contacts, logistics requirements, visit history, and multi-month scheduling calendar with automated confirmation workflows, (2) Consent Tracker — digital consent form distribution via parent SMS/email, e-signature collection, real-time consent status dashboard by school and classroom, (3) Clinical Documentation — offline-capable dental charting optimized for screenings and preventive care (the procedures most commonly performed on mobile units), with automatic sync when connectivity resumes, (4) Portable Imaging Bridge — integrate with Nomad Pro, DEXIS portable, and other mobile X-ray units, storing images locally and syncing to cloud, (5) Multi-Payer Billing Engine — auto-route claims to the correct Medicaid MCO based on patient enrollment, generate facility contract invoices, and track grant-funded services for reporting. An LLM layer can auto-generate the narrative documentation required for Medicaid claims from structured screening data.

## Target Customer
Mobile dental program directors at FQHCs, nonprofit dental organizations, and school-district-contracted mobile dental providers operating 1-10 mobile units, currently managing operations across 4-6 disconnected tools.

## Impact If Built
Reduces per-visit administrative time by 40-60% (from 3 hours of post-visit data entry and billing to under 1 hour), increases patient throughput per visit day by 15-20% (from faster documentation), and improves Medicaid claim acceptance rates from 70-75% to 90%+ by ensuring documentation completeness at the point of care.
