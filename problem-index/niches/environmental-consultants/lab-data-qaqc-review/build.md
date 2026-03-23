# Automated Environmental Data Validator

**Niche:** [[niches/environmental-consultants/lab-data-qaqc-review/profile|Lab Data QA/QC Review]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A validation engine that ingests lab analytical data packages, applies EPA method-specific and program-specific QA/QC criteria, and generates a complete data validation report with qualifier assignments — replacing 8-20 hours of manual spreadsheet review per sampling event.
**Tags:** #automation #anomaly-detection #tabular-ml #compliance #data-integration

## The Problem
Environmental data validation at USEPA Level 2 or Level 3 requires checking each analytical result against 15-25 quality criteria defined by the analytical method (EPA 524.2, EPA 8260, EPA 8270, EPA 6010, etc.), the project's Quality Assurance Project Plan (QAPP), and state-specific requirements. For each sample, the validator must: verify holding times were met, check that method blanks show no contamination, confirm laboratory control sample recoveries are within acceptance limits, evaluate matrix spike and matrix spike duplicate results, assess field duplicate precision, review calibration data, and assign data qualifiers (U, J, UJ, R) based on any quality exceedances. A Level 3 validation of a 20-well groundwater monitoring event with volatile organics, metals, and general chemistry parameters takes 15-25 hours of a trained validator's time.

## Why Nobody Has Built This
Validation criteria vary by analytical method (each EPA method has different holding times, recovery limits, and precision criteria), by regulatory program (CERCLA, RCRA, state VCP — each with different data quality objectives), and by project-specific QAPP requirements. Building a comprehensive rules engine requires encoding hundreds of method-specific criteria and program-specific overrides. The lab data packages that contain the QA/QC information (calibration data, blank results, spike recoveries) are delivered in inconsistent formats — PDFs, proprietary LIMS exports, and semi-structured EDDs — requiring a flexible parsing engine. The market of trained data validators is small and specialized, limiting the addressable customer base.

## What to Build
A web-based validation platform that: (1) imports lab analytical data in standard EDD formats (EQUIS, state-specific, custom), (2) imports the QA/QC summary data from the lab package (method blanks, LCS, MS/MSD, duplicates, calibration), (3) applies method-specific validation criteria (holding times, recovery windows, RPD limits) from a pre-built rules database covering the 20 most common EPA methods, (4) applies project-specific criteria from the QAPP (custom recovery limits, elevated detection limits, specific qualifier assignment rules), (5) generates qualifier assignments (U, J, UJ, R) with the rationale for each qualification, and (6) produces a formatted data validation report suitable for regulatory submission. The validator reviews and approves rather than performing each check manually.

## Target Customer
Data validators and project chemists at environmental consulting firms processing 10+ data packages per quarter, currently validating in Excel with manual criterion lookups.

## Impact If Built
Reduces validation time from 15-25 hours to 2-4 hours of review per data package. For a firm processing 40 data packages per year, this saves 520-840 hours annually — equivalent to a quarter of a full-time validator position. Eliminates the 3-5% qualifier assignment error rate inherent in manual validation.
