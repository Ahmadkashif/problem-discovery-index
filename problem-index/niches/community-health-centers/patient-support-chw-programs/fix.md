# Rides and Interpreters Logged Where UDS Cannot Count Them

**Niche:** [[niches/community-health-centers/patient-support-chw-programs/profile|Patient Support Services & Community Health Worker Programmes]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** CY2026 UDS counts patients who received case management, eligibility help, transport and language assistance, but centers record rides in a broker portal and interpreter time on paper, so the new lines will be undercounted.
**Tags:** #data-integration #feature-engineering #descriptive-statistics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a health center's high-risk patients in care through outreach, transport, interpretation and case management, and whoever keeps the largest share of a care team's high-risk panel with a kept visit inside its clinical interval takes the account.

## The Problem
Table 6A lines 35–38 are new for CY2026 (the OMB-approved 2026 UDS tables (ICR 202606-0915-002, approved 3 September 2026)). The services happened all year, but the records are spread across a ride broker, an interpreter vendor's invoices, eligibility workers' spreadsheets and EHR notes.

## Why It's Still Broken
Patient support was reported as staff FTEs and costs, not as services to patients, so nobody built patient-level capture. Vendors' portals do not write back to the chart.

## What a Fix Looks Like
Daily imports from ride and interpreter vendors matched to patients and visits, a structured EHR entry for case management and eligibility help, and a monthly count by line, so the CY2026 numbers exist before January.

## Who Feels the Pain
Patient support directors who cannot show what their teams did, and UDS analysts rebuilding counts in February.

## Impact If Fixed
A center with 3,000 patients receiving support services (estimate) may otherwise report half that number, understating to HRSA and funders the work behind ~9% of its workforce.
