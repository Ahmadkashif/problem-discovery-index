# Audit Report Generation Across Standards

**Industry:** [[energy-auditors|Energy Auditors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic document generation exists but cannot translate a single audit dataset into HERS, BPI 2400, and ASHRAE Level II reports without hours of manual reformatting.
**Tags:** #llm #text-generation #nlp #automation

## The Problem
A single residential or light-commercial audit produces data that must be packaged differently depending on the audience: a HERS Index report for real estate transactions, a BPI 2400-compliant report for weatherization programs, an ASHRAE Level I or II report for commercial building owners, and a homeowner-friendly summary for the sales process. Auditors spend 1-3 hours per audit reformatting the same underlying data into these different templates, adjusting language, including the right compliance statements, and ensuring measure descriptions match each standard's terminology.

## What Already Exists
General-purpose document generation tools (Jasper, ChatGPT, even mail-merge in Word) can produce templated reports. Energy modeling software exports basic PDF reports in their own format. Neither handles the cross-standard translation problem: converting a single audit dataset into multiple standards-compliant outputs with correct terminology, required fields, compliance language, and calculation presentation formats.

## The Customisation Gap
Each reporting standard has specific required sections, defined terminology (e.g., "air leakage rate" vs. "infiltration reduction" vs. "ACH50"), mandated calculation display formats, and compliance attestation language that changes with standard revisions. The generation system needs to understand the semantic meaning of each audit data point and map it to the correct field and phrasing in each target standard — not just fill a template, but reason about which measures qualify under which program rules and how to present savings calculations in the format each standard requires.

## Impact If Solved
Auditors reclaim 1-3 hours per audit on report writing — roughly 15-25% of total audit time. For a firm doing 10 audits per week, that is 10-30 hours recovered, enabling either higher throughput or more time spent on the high-value field assessment work.
