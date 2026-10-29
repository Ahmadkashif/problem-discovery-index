# IPFQR and the New IPF-PAI on Acute-Care Reporting Tools

**Industry:** [[psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every psychiatric facility reports the same IPFQR measures to CMS and from July 2028 must also submit a new standardised patient assessment, and the quality tools it buys were built for acute hospitals' programmes, so restraint logs, transition records and the new instrument are assembled by hand.
**Tags:** #descriptive-statistics #hypothesis-testing #bayesian-inference #data-integration #compliance #quick-win #automation

## The Problem
A psychiatric hospital's quality director, often with one or two chart abstractors, reports the Inpatient Psychiatric Facility Quality Reporting (IPFQR) measures once a year. They include hours of physical restraint and seclusion (HBIPS-2 and -3), screening for metabolic disorders, the transition record sent at discharge, and immunisation. CMS computes the claims-based measures itself: follow-up within 7 and 30 days after discharge (FAPH), medication continuation and 30-day readmission. Restraint and seclusion hours come from paper logs and nursing notes. A facility that fails to report loses 2 percentage points of its annual Medicare update (CMS).

The FY2027 final rule adds work. Every IPF must complete the standardised IPF Patient Assessment Instrument (IPF-PAI) at admission and discharge for patients aged 18 and over, regardless of payer: voluntarily from 1 October 2027 and mandatorily from 1 July 2028. At least 50% of a facility's assessments must have every required item answered for the FY2030 and FY2031 updates, rising to 70% from FY2032. Mobility is collected at admission only and special services, treatments and interventions at discharge only, and CMS estimates 12 minutes per patient (Federal Register 2026-15588). Submission is through CMS's free PARIT web application or a HL7 FHIR API, the first CMS statutory quality programme to take assessment data by FHIR (CMS). The same rule drops the alcohol and tobacco brief-intervention measures from the CY2026 reporting period.

The public results show how uneven the reporting is. In the 2024 data the median facility reported a transition-record rate of 77%, but the 10th percentile reported 0%. Restraint hours ranged from zero to 24.5 per 1,000 patient hours, and 72 facilities had readmission rates worse than the national rate (IPFQR, 1,410 facilities). A quality director sees her own numbers in the preview report. She rarely sees them against facilities like hers until a competitor or a journalist does.

## What Already Exists
Acute-care quality reporting and chart abstraction vendors (Medisolv publishes IPFQR requirements; search summary), eCQM engines in Epic and Oracle Health, and behavioral EHR report packs. Assessment software exists for the post-acute instruments: MDS in nursing homes, IRF-PAI in rehabilitation hospitals and OASIS in home health. Public ratings built from CMS data are mapped at [[niches/general-hospitals/hospital-quality-ratings-publishers/profile|🔍 Hospital Quality Ratings Publishers]].

## The Customisation Gap
- HBIPS measure logic that reads restraint and seclusion start and stop times from digital or scanned logs and nursing notes, including the age bands CMS reports;
- a transition-record check at discharge for each required element;
- the IPF-PAI item set mapped to the behavioral EHR's assessments, validated before submission, with a FHIR export to CMS's specification once it is final;
- a benchmark that places each measure against peers on the Provider Data Catalog (by state, ownership, freestanding or unit, and size) with confidence intervals, so a small unit's single bad quarter is not read as a trend.

The second half of the two-week MVP is that benchmark. It downloads the by-facility IPFQR file, computes each facility's percentile and shrunken estimate within its peer group, and drafts the quality director's one-page summary (ml entry 3).

## Impact If Solved
For a facility with ~$10M a year of Medicare IPF payments, the 2-point penalty is ~$200,000 a year; an assessment pipeline that cannot miss a submission protects it (estimate). Automating HBIPS and transition-record abstraction could save ~200–400 abstractor hours a year per facility, roughly 280,000–560,000 hours across the 1,410 reporting facilities (estimate).
