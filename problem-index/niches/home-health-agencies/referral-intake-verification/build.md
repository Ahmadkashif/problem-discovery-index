# Intelligent Referral Acceptance Engine

**Niche:** [[niches/home-health-agencies/referral-intake-verification/profile|Referral Intake & Insurance Verification]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Auto-process incoming referral faxes — OCR the document, extract patient demographics and orders, verify insurance eligibility in real-time, check service area, match to available clinicians, and present an accept/reject recommendation within minutes instead of hours.
**Tags:** #large-language-models #transfer-learning #cnns #attention-mechanisms #feature-engineering #automation #workflow-orchestration #revenue-impact #quick-win

## The Problem
A home health referral arrives as a faxed discharge summary — a 3-8 page document containing patient demographics, diagnoses, physician orders for home health services, insurance information, and the patient's home address. An intake coordinator manually reads the fax, types the patient demographics into the EMR, calls the insurance company to verify eligibility and home health benefits, checks whether the patient's address falls within the agency's service area, reviews the ordered services against available clinician specialties, and determines whether to accept or reject the referral. This takes 2-4 hours per referral, and an agency processing 10-15 referrals per day needs 2-3 full-time intake coordinators. The hospital expects a response within hours; delays mean the referral goes to a competitor.

## Why Nobody Has Built This
The input is unstructured (faxed documents in varying formats from hundreds of different hospitals), the eligibility verification requires real-time API calls to multiple payers, and the accept/reject decision involves judgment calls about clinician capacity and geographic feasibility that change hour-by-hour. Building this end-to-end requires: document OCR and extraction (solved by modern vision-language models), payer eligibility API integration (partially solved by Availity/Waystar), service area geocoding (solved), and clinician availability matching (requires EMR integration). No single vendor has assembled these components into a home health-specific intake automation workflow.

## What to Build
A referral processing engine that: (1) receives faxed or electronic referrals and uses vision-language models to extract structured data (patient demographics, insurance ID, diagnoses, ordered services, physician information, patient address), (2) auto-verifies insurance eligibility and home health benefits via payer API integrations, (3) geocodes the patient address against the agency's service area and identifies the nearest available clinicians, (4) matches ordered services (skilled nursing, PT, OT, SLP, MSW) to clinicians with matching skills and schedule availability, (5) calculates a referral acceptance score based on payer mix, geographic efficiency, and staffing capacity, and (6) presents the intake coordinator with a pre-populated accept/reject recommendation with supporting data — reducing the 2-4 hour process to 10-15 minutes of review and confirmation.

## Target Customer
Medicare-certified home health agencies processing 8+ referrals per day, particularly multi-branch agencies where intake is centralized and referral volume creates a bottleneck that directly limits census growth.

## Impact If Built
Reducing referral processing time from 3 hours to 15 minutes would allow agencies to respond to hospitals within 30 minutes instead of 4-6 hours, increasing referral acceptance rates by an estimated 20-30%. For an agency processing 50 referrals per week, converting an additional 10-15 referrals per week into admissions represents $500K-$1M in annual revenue. Intake coordinator headcount could be reduced from 3 to 1 for the same referral volume.
