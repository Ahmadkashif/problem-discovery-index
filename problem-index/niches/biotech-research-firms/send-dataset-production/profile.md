# SEND Dataset Production

**Parent Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to produce SEND datasets that pass FDA's technical rejection criteria and match the study report the first time, from whatever system the study ran on, and whoever closes the gap between report and dataset fastest takes the account.

## Profile
**Market Size:** ~$300M global spend on SEND conversion services, software and validation (estimate)
**Share of Parent Industry:** <1% of NAICS 541714 receipts (estimate)
**Digital Adoption:** High in principle, uneven in practice — data starts in validated systems, but mapping, controlled terminology and reconciliation with the report are manual
**Target Buyer:** Head of Data Standards or SEND Manager at the CRO; sponsor regulatory operations lead
**Automation Potential:** High — a rule-governed transformation with a defined target

## What Makes This a Distinct Niche
FDA requires nonclinical study data in CDISC SEND for commercial IND studies started after 17 December 2017 at CDER, and after 15 March 2023 at CBER, and it enforces the requirement through technical rejection criteria. Between September 2021 and February 2023, 453 nonclinical studies failed rule 1734, and 73% of those failures were simply a missing trial summary file. The work is a pure data transformation with a defined target, done for every GLP study, often by the CRO and sometimes by a specialist vendor for legacy or multi-site studies.

## Current Tools & Gaps
Instem SEND Solutions and Submit, Pinnacle 21 (Certara) validation, Xybion and PDS tools, and in-house SAS programs. Gaps: data from contributing sites and older systems mapped by hand; controlled terminology choices inconsistent across studies; and no automated check that the dataset says what the signed report says.

## Problems
- [[niches/biotech-research-firms/send-dataset-production/build|🔨 Build: Report-to-Dataset Reconciliation Before Submission]]
- [[niches/biotech-research-firms/send-dataset-production/buy|🛒 Buy: Clinical Data Mapping Tools Fitted to Nonclinical Domains]]
- [[niches/biotech-research-firms/send-dataset-production/fix|🔧 Fix: The Missing Trial Summary File]]
