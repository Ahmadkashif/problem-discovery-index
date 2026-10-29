# IPFQR Reporting & IPF-PAI Submission

**Parent Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to produce a psychiatric facility's IPFQR measures and its new IPF-PAI assessments straight from the record, and whoever submits the highest share of fully complete IPF-PAI assessments takes the account.

## Profile
**Market Size:** ~$0.15B a year of abstractor and quality-analyst time, reporting software and the coming IPF-PAI build (estimate)
**Share of Parent Industry:** ~0.5% of receipts (estimate)
**Digital Adoption:** Medium — claims measures are computed by CMS; chart measures and restraint logs are abstracted by hand
**Target Buyer:** Director of quality and performance improvement; behavioral EHR product leads
**Automation Potential:** High — measure specifications and the assessment's items are published and repeat every year

## What Makes This a Distinct Niche
All ~1,430 IPFs report the same measures, and 1,410 appear in CMS's 2026 public file. Missing data costs 2 points of the annual Medicare update (CMS). The FY2027 rule adds the standardised IPF-PAI, an admission and a discharge assessment submitted through CMS's PARIT application or a FHIR API. Submission is voluntary from 1 October 2027 and mandatory from 1 July 2028. CMS counts an assessment toward compliance only if every required item is answered, and requires at least 50% of a facility's assessments to be complete for the FY2030 and FY2031 updates and 70% from FY2032 (Federal Register 2026-15588). It also drops the alcohol and tobacco intervention measures from the CY2026 reporting period. Nursing homes went through the same kind of change with the MDS ([[niches/skilled-nursing-facilities/mds-pdpm-reimbursement/profile|🔵 MDS Assessment & PDPM Reimbursement]]), and health centers with the UDS. Competitors are acute-care quality vendors (Medisolv; search summary), behavioral EHR vendors adding the instrument (Netsmart, Qualifacts, Kipu), and in-house quality teams. CMS's measure contractors are profiled at [[niches/general-hospitals/cms-quality-measure-contractors/profile|🔍 CMS Hospital Quality Measure Contractors]]. The win condition measures the IPF-PAI half of the niche and cannot be observed until voluntary submissions open on 1 October 2027; the IPFQR half is held to it because the same record and pipeline produce the chart-abstracted measures.

## Current Tools & Gaps
CMS's Hospital Quality Reporting system, manual abstraction and EHR report packs. Gaps: no validator for IPF-PAI items before submission, no FHIR export in most behavioral EHRs yet, and no peer benchmark beyond the national and state averages.

## Problems
- [[niches/psychiatric-hospitals/ipfqr-ipf-pai-reporting/build|🔨 Build: IPFQR Peer Benchmark and IPF-PAI Pre-Submission Validator]]
- [[niches/psychiatric-hospitals/ipfqr-ipf-pai-reporting/buy|🛒 Buy: Post-Acute Assessment Software Adapted to the IPF-PAI]]
- [[niches/psychiatric-hospitals/ipfqr-ipf-pai-reporting/fix|🔧 Fix: Restraint Hours Abstracted From Handwritten Logs]]
