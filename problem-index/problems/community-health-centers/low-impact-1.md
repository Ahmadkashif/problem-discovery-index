# CY2026 UDS Tables Rebuilt From Patient-Level Records

**Industry:** [[community-health-centers|Community Health Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every health center's data analyst must rebuild the UDS for the CY2026 revisions (new patient support and diagnosis lines, a consolidated revenue table and, as proposed, 2026 eCQM specifications), while generic BI tools and EHR report packs only reproduce last year's tables.
**Tags:** #large-language-models #descriptive-statistics #hypothesis-testing #evaluation-metrics #data-integration #compliance #quick-win

## The Problem
Each February, every health center and look-alike submits its Uniform Data System report to HRSA: patient demographics, staffing, diagnoses and services, quality measures, costs and revenue. HRSA estimates 185 hours of work per report, and OMB approved 304,616 burden hours across 2,107 responses for 2026, including grant reports (ICR 202606-0915-002). One or two analysts at each center, often a quality manager who also runs PCMH and grant reporting, do most of it.

The CY2026 report, due in February 2027, changes in ways a reused query will miss. According to the OMB-approved 2026 UDS tables (ICR 202606-0915-002, approved 3 September 2026), Table 6A drops service lines such as mammograms, Pap tests and sealants, though the COVID diagnosis lines proposed for removal stay. It adds Type 1 diabetes (9a), intellectual and developmental disabilities (20g), autism screening (26g), four patient support service counts (35–38: case management, eligibility assistance, transportation, language assistance) and four upstream-drivers-of-health lines (39–42: screening, food insecurity, housing instability, financial insecurity). Table 8A folds enabling-service cost detail into one patient support line. Table 9D, now accrued patient service revenue, drops the wraparound columns and managed-care payer lines and adds net patient service revenue. Appendix D asks what share of revenue sits in value-based contracts. Moving Tables 6B and 7 to CMS's 2026 eCQM specifications was proposed in the December 2025 notice (FR 2025-22443); final manual not seen. The analyst learns which numbers will not reconcile only when HRSA's edit checks flag them during review.

## What Already Exists
EHR vendors (OCHIN Epic, NextGen, eClinicalWorks, athenahealth) ship UDS report packages, typically updated late in the reporting year. Azara DRVS and Relevant compute UDS measures and gap lists for their clients, and HCCNs run shared reporting for members. Generic BI tools (Power BI, Tableau, Looker) can show anything once someone writes the logic. HRSA publishes the manual, the table specifications and every center's prior-year results. The vendor-side version of this problem, one encounter record that feeds UDS, sliding fee and 340B, is [[niches/healthcare-practice-software/fqhc-health-center-software/profile|🟣 FQHC & Community Health Center Software]].

## The Customisation Gap
The center-specific layer is a readiness check, not another dashboard:

- mapping the center's local codes, templates and screening forms to the new lines, especially lines 35–42, where patient support services are often logged outside the EHR in spreadsheets and transport vendor portals;
- recomputing 6B and 7 under the 2026 eCQM value sets, if the final manual adopts the proposed alignment, and showing which patients move in or out of each numerator compared with the 2025 logic;
- running HRSA-style cross-table edits before submission (patients by age and sex across Tables 3A and 4, visits against staffing in Table 5, revenue against costs);
- benchmarking every measure against the center's own history and HRSA's public state and national tables, so implausible movements are found in January, not at review.

A two-week MVP does this on Synthea synthetic patients: generate a 20,000-patient FHIR population, compute the CY2026 tables, inject typical mapping errors, and flag them against HRSA's published 2025 national and state distributions. Patient-level UDS+ files can be an optional output, since HRSA put UDS+ on hold in April 2025 (search summary).

## Impact If Solved
A readiness check could cut the ~185 hours per report by a third (estimate), about 60 analyst hours per report or ~96,000 hours across 1,605 UDS reports (the December 2025 notice's respondent count). It would also cut the HRSA reviewer questions that otherwise run into April.
