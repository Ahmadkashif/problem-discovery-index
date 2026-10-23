# NP and PA Work Credited to Someone Else's NPI

**Niche:** [[niches/physician-practices/nps-pas-in-physician-offices/profile|Nurse Practitioners & Physician Assistants in Physician Offices]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Incident-to and split visits bill under the physician's NPI, so the NP's or PA's productivity disappears from RVU reports, compensation and payer quality data.
**Tags:** #descriptive-statistics #data-integration #feature-engineering #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bill each NP and PA visit under the right rule (incident-to under the physician or the clinician's own NPI), with the state's supervision or collaboration terms met, and whoever captures the most compliant revenue per advanced practice clinician takes the account.

## The Problem
When a PA sees a patient incident-to, the claim carries the supervising physician's NPI. Work RVUs, payer quality attribution and the group's productivity dashboard credit the physician. At bonus time the PA's productivity looks low. In MIPS and payer directories the PA barely exists.

## Why It's Still Broken
Billing systems report by rendering NPI because that is what claims carry. The EHR knows who saw the patient, but compensation reports are built from billing data. Fixing it means joining the EHR's encounter provider to the claim, which few practices do.

## What a Fix Looks Like
A shadow productivity ledger that credits each visit to the clinician who performed it, using the EHR encounter record. Compensation, staffing and quality reports run from it, with the billing NPI kept alongside for reconciliation.

## Who Feels the Pain
NPs and PAs whose pay depends on credited productivity; group leaders deciding how many to hire; physicians credited with work they did not do.

## Impact If Fixed
Accurate attribution affects bonus pools worth ~5%–15% of NP and PA compensation (estimate). It also gives the group a true cost per visit by clinician type, the number it needs to decide its staffing mix.
