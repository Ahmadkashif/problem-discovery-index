# Hospital Discharge-to-Home Health Handoff

**Industry:** [[home-health-agencies|Home Health Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Hospital discharge referrals arrive via fax and phone, creating a 24-48 hour information gap that delays the critical first home visit and causes patients to bounce back to the ER.
**Tags:** #data-integration #workflow-orchestration #quick-win

## The Problem
When a hospital discharges a patient to home health, the referral contains the patient's diagnoses, medication list, care orders, and functional status. This information arrives at the home health agency via fax, e-fax, or sometimes a phone call — and must be manually entered into the agency's EHR to create the patient record, generate the plan of care, and schedule the first visit (which Medicare requires within 48 hours of discharge). Missing or illegible information triggers phone tag with the hospital discharge planner.

## What Already Exists
Health Information Exchanges (HIEs) and referral platforms like Ensocare (now WellSky), CarePort, and Collective Medical facilitate electronic referrals between hospitals and post-acute providers. ADT (Admit-Discharge-Transfer) notification feeds are increasingly available.

## The Customisation Gap
Generic referral platforms transmit the data but don't translate it into home health-specific workflows: they don't auto-generate a plan of care from hospital orders, don't flag mismatches between ordered services and the agency's capabilities, don't pre-check insurance eligibility for home health benefits, and don't trigger the OASIS assessment scheduling based on admission date. The agency still needs a human to bridge the referral data into their operational workflow.

## Impact If Solved
Reduces referral-to-first-visit time from 36-48 hours to under 24 hours. Eliminates 20-30 minutes of manual data entry per new admission and reduces hospital readmission rates driven by delayed care initiation.
