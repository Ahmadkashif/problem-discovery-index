# PBJ Submission & Staffing Data Reconciliation

**Parent Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn payroll, timeclock and agency invoices into a PBJ file that matches the hours actually worked, and whoever's submissions pass CMS's PBJ audits and never cost the facility a staffing star takes the account.

## Profile
**Market Size:** ~$250M a year in PBJ software, payroll-vendor modules and the payroll and staffing staff time spent preparing and correcting submissions (estimate)
**Share of Parent Industry:** ~0.1% of facility spending (estimate)
**Digital Adoption:** Medium — files are generated from payroll systems, but agency and contract hours, job-code mapping and exclusions are reconciled by hand in spreadsheets
**Target Buyer:** Payroll or HR manager and administrator; corporate payroll and compliance at chains
**Automation Potential:** Very high — the inputs are structured data, the rules are published, and the output is a file with a fixed specification

## What Makes This a Distinct Niche
Every Medicare- and Medicaid-certified facility must submit daily paid hours for every staff member, including agency and contract staff, by the 45th day after each quarter: 14 February, 15 May, 14 August and 14 November (CMS). The file feeds the Five-Star staffing rating (only 11% of nursing homes hold 5 stars on staffing, MedPAC), two SNF VBP measures, and eligibility for the risk-based survey. In CMS's June 2026 data, 242 facilities were excluded because they had failed a PBJ audit, and 5,692 because their staffing rating was below 3 stars (CMS QSO-26-14-NH). PBJ moved from QIES to iQIES in August 2026 and runs on specification 4.10.0 from April 2026. The work is mechanical and unforgiving. Hours entered wrongly cost stars on the public website for a quarter.

## Current Tools & Gaps
Payroll vendors' PBJ exports (ADP, Paylocity, UKG), specialist tools (Simple's SimplePBJ, SmartLinx), consultants. Gaps: agency and per-diem hours sit on invoices outside payroll; job-title mapping to PBJ codes drifts; nobody previews the star effect or audit risk before submission.

## Problems
- [[niches/skilled-nursing-facilities/pbj-staffing-reporting/build|🔨 Build: A PBJ Pre-Submission Auditor That Predicts Star Effects]]
- [[niches/skilled-nursing-facilities/pbj-staffing-reporting/buy|🛒 Buy: Payroll PBJ Exports Extended to Contract Labour]]
- [[niches/skilled-nursing-facilities/pbj-staffing-reporting/fix|🔧 Fix: Agency Hours That Never Reach the PBJ File]]
