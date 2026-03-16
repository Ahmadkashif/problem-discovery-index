# Medicaid Trip Billing and Verification Automation

**Industry:** [[non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic billing automation exists — but none of it understands Medicaid trip authorization matching, state-specific documentation rules, or the broker reconciliation workflow that causes 20-30% of claims to require manual rework.
**Tags:** #llm #named-entity-recognition #nlp #compliance #automation

## The Problem
Every completed NEMT trip must be matched to a Medicaid authorization, documented with exact pickup/dropoff times, odometer readings, driver and patient signatures, and submitted through broker-specific portals or state Medicaid EDI systems. Billing specialists spend 3-5 minutes per trip verifying documentation completeness, cross-referencing authorization numbers, and correcting discrepancies between GPS logs and driver-reported times. A 200-trip-per-day operator dedicates 2-3 full-time staff to this process, and 20-30% of initial submissions are denied or pended for missing fields, mismatched authorization codes, or documentation gaps — each requiring 15-30 minutes of rework and resubmission.

## What Already Exists
General medical billing platforms (e.g., Kareo, AdvancedMD) handle CPT/ICD coding and insurance claim submission, but they have no concept of trip-based billing, Medicaid transportation authorization structures, or broker-specific submission formats. CTS Software and TripMaster include basic billing modules that pre-populate trip data, but they still require manual verification of every field and cannot detect documentation gaps before submission.

## The Customisation Gap
NEMT billing requires understanding the relationship between trip authorizations (which specify allowed dates, service levels, and mileage caps), actual trip execution data (GPS breadcrumbs, timestamps, signatures), and broker/state-specific submission rules that change quarterly. An NLP layer needs to extract and validate authorization details from broker communications (often PDFs, faxes, or portal downloads), match them against trip records, flag discrepancies (e.g., trip logged as wheelchair but authorized as ambulatory), and format submissions to each broker's unique portal requirements. State Medicaid rules on shared-ride billing, mileage rounding, and attendant surcharges vary by jurisdiction and must be encoded per-contract.

## Impact If Solved
Billing staff per operator drops from 3 to 1 for a 200-trip/day fleet, saving $80K-$120K annually in labor. First-pass claim acceptance rises from 70-80% to 95%+, accelerating cash flow by 15-20 days and recovering $50K-$150K in currently written-off denials per year.
