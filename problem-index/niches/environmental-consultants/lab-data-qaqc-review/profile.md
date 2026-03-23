# Lab Data QA/QC Review

**Parent Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2-4B (embedded in consulting project costs — represents the data validation step required for every analytical dataset)
**Share of Parent Industry:** ~5%
**Digital Adoption:** Low — data validation is performed by manually reviewing lab reports, checking holding times, comparing duplicate results, and flagging qualifiers using spreadsheets and highlighters
**Target Buyer:** Data validator or project chemist at an environmental consulting firm responsible for certifying analytical data quality
**Automation Potential:** High — QA/QC validation follows deterministic rules defined by EPA methods, state programs, and project-specific QAPPs, making it ideal for automated checking

## What Makes This a Distinct Niche
Every environmental data point — from groundwater contaminant concentrations to air emission measurements — must pass QA/QC validation before it can be used for regulatory decisions. Data validation involves checking 15-25 quality criteria per sample: holding time compliance, method blank contamination, laboratory control sample recovery, matrix spike recovery, duplicate precision, field blank results, and data qualifier assignment (U for non-detect, J for estimated, R for rejected). A project with 20 groundwater wells and 30 analytes generates 600+ data points per sampling event, each requiring validation against these criteria. This validation is performed by trained data validators or project chemists who manually review lab reports — a process that takes 8-20 hours per sampling event and is performed quarterly across dozens of active projects.

## Current Tools & Gaps
EQuIS includes data validation modules, but they require EQuIS licensing ($15,000+/year) and significant configuration. ERS (Environmental Review Software) provides some validation automation but has limited state-specific criteria support. Most firms validate data in Excel: importing lab results, manually checking each quality criterion against method-specific and program-specific requirements, and applying data qualifiers. This manual process is error-prone and time-consuming.

## Problems
- [[niches/environmental-consultants/lab-data-qaqc-review/build|🔨 Build: Automated Environmental Data Validator]]
- [[niches/environmental-consultants/lab-data-qaqc-review/buy|🛒 Buy: Lab EDD Normalizer for Multi-Lab Data Integration]]
- [[niches/environmental-consultants/lab-data-qaqc-review/fix|🔧 Fix: Data Qualifier Inconsistency Across Validators]]
