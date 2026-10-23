# Payroll PBJ Exports Extended to Contract Labour

**Niche:** [[niches/skilled-nursing-facilities/pbj-staffing-reporting/profile|PBJ Submission & Staffing Data Reconciliation]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payroll platforms export employee hours to PBJ; they do not see the agency and marketplace hours that the same file must include.
**Tags:** #data-integration #large-language-models #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn payroll, timeclock and agency invoices into a PBJ file that matches the hours actually worked, and whoever's submissions pass CMS's PBJ audits and never cost the facility a staffing star takes the account.

## The Problem
Contract hours, which peaked at 10.5% of nursing hours in Q3 2022 and were 5.3% in Q4 2025 (LTCCC), arrive as invoices, portal exports and spreadsheets in each vendor's format.

## What Already Exists
Payroll and workforce platforms such as ADP, Paylocity and UKG generate PBJ XML files from employee timekeeping, with job-code mapping and exclusion rules.

## The Customization Gap
The adaptation needs: (1) ingestion of agency invoices and marketplace exports, parsed into person-day-hours records with PBJ job codes; (2) matching contract workers across vendors to stable identifiers; (3) reconciliation of invoiced hours to sign-in sheets or timeclock; (4) handling of PBJ exclusions such as administrative time for nurses; (5) a single merged file to the current specification.

## Target Customer
Facilities with significant per-diem or agency use, and payroll vendors serving long-term care.

## Impact If Solved
With contract labour at ~5% of nursing hours (LTCCC, CLA), a facility that leaves agency hours out of the file understates staffing by ~0.2 hours per resident day against a national average of 3.76–3.85 (estimate). That is enough to cost a staffing star near a cut point, and the merged file reflects every hour actually worked.
