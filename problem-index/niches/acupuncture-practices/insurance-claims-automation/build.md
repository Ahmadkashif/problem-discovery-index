# Acupuncture-Specific Eligibility Verification Engine

**Niche:** [[niches/acupuncture-practices/insurance-claims-automation/profile|Insurance Eligibility & Claims Processing]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No eligibility verification tool provides acupuncture-specific benefit details — visit limits, covered codes, diagnosis requirements, and state mandate applicability — in a single automated lookup.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #automation #revenue-impact

## The Problem
Before treating an insured patient, an acupuncture clinic needs to know: Does this plan cover acupuncture? For which diagnoses? With what visit limits? Which CPT codes are allowed? Is the state mandate applicable to this plan type? Does the patient need a referral from a PCP? Generic eligibility tools return "acupuncture: covered/not covered" with no specifics. Getting the actual benefit details requires a 15-30 minute phone call to the payer — often with hold times exceeding 20 minutes. For a clinic verifying 10-15 new patients per week, this consumes 5-10 hours of biller time.

## Why Nobody Has Built This
Acupuncture benefits are stored in payer systems as unstructured text in benefit documents, not as structured data fields. Standard EDI 270/271 eligibility transactions return a service type code for acupuncture but rarely include visit limits, code restrictions, or diagnosis requirements in machine-readable format. Building this requires either parsing payer benefit PDFs at scale or maintaining direct data feeds from major payers — both expensive for a niche market.

## What to Build
An eligibility engine that takes patient insurance information, runs the standard 270/271 check, then supplements it with payer-specific acupuncture benefit data scraped from provider portals and benefit documents. Output: "Blue Shield CA PPO — acupuncture covered for M54.5, M79.3 — 24 visits/year — CPT 97810, 97811, 97813, 97814 — no referral required — patient has used 8 visits." Total verification time: under 30 seconds versus 20+ minutes.

## Target Customer
Acupuncture billing services and clinic billing managers processing 100+ eligibility verifications per month.

## Impact If Built
Saves 8-15 hours/week of phone-based verification per biller, eliminates surprise denials due to unknown benefit limitations, and enables clinics to collect accurate patient responsibility amounts at time of service.
