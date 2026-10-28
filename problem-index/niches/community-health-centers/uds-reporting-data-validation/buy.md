# eCQM Engines Adapted to UDS Universe Rules

**Niche:** [[niches/community-health-centers/uds-reporting-data-validation/profile|UDS Reporting & Data Validation (CY2026 Tables)]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Certified eCQM engines already compute CMS quality measures, but UDS counts a different universe of patients and visits, so the engine's output does not match the table without health center rules layered on.
**Tags:** #descriptive-statistics #data-integration #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to produce a health center's UDS tables directly from patient-level records, and whoever submits the CY2026 report with the fewest unresolved HRSA edit flags at review takes the account.

## The Problem
Aligning Tables 6B and 7 with CMS's 2026 eCQM specifications from CY2026 was proposed in the December 2025 notice (FR 2025-22443); final manual not seen. The center's eCQM engine, built for MIPS, uses its own definition of eligible encounters and providers.

## What Already Exists
Certified eCQM engines in EHRs, registry and QCDR measure calculators, and the CMS measure specifications and value sets.

## The Customization Gap
- UDS's universe: patients with a countable visit, including dental and behavioral visits;
- health center provider types and sites, including mobile units and school-based sites;
- reconciliation of measure denominators with Table 6A diagnoses and Table 4 patient counts;
- the year-on-year difference from the old UDS logic, patient by patient.

## Target Customer
Centers whose EHR vendor's UDS package lags the manual, and HCCNs standardising reporting across members.

## Impact If Solved
Reusing a certified engine instead of hand-written queries removes ~20–30 hours of measure building per report (estimate).
