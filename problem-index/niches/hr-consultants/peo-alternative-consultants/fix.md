# Workers' Comp Audit Data Assembly Across Disconnected Payroll Systems

**Niche:** [[niches/hr-consultants/peo-alternative-consultants/profile|PEO Alternative Consultants]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Annual workers' comp audits require payroll data broken down by job classification code — but the client's payroll system doesn't track classification codes, so the HR consultant spends 4-8 hours per client manually categorizing 12 months of payroll data to match NCCI class codes.
**Tags:** #automation #data-integration #compliance #worker-facing

## The Problem
Workers' compensation insurance premiums are based on payroll dollars per NCCI (National Council on Compensation Insurance) class code. Annual audits require the employer to report total payroll by class code for the policy period. PEOs handle this automatically because they control the payroll system and track classification codes. PEO-alternative clients run standalone payroll systems (Gusto, Paychex) that track employee job titles but not NCCI class codes. When the annual workers' comp audit arrives, the HR consultant must: (1) export 12 months of payroll data, (2) map each employee to an NCCI class code based on their actual job duties, (3) allocate payroll dollars by class code, and (4) compile the audit submission. For a client with 50 employees, this takes 4-8 hours per annual audit.

## Why It's Still Broken
Payroll systems don't track NCCI class codes because workers' comp classification is outside their scope — it's an insurance function, not a payroll function. The mapping from job title to class code requires judgment: a "project manager" at a construction company might be Class 8810 (clerical) if they work from an office, or Class 5606 (contractor — executive) if they regularly visit job sites. This classification judgment is part of the HR consultant's expertise, but the data assembly work (exporting payroll, building the classification matrix, calculating totals) is pure administrative overhead.

## What a Fix Looks Like
A workers' comp audit preparation tool that: (1) connects to the client's payroll system via API, (2) maintains a mapping table of employee → NCCI class code (set up once by the consultant and updated when roles change), (3) automatically pulls 12 months of payroll data and allocates dollars by class code, (4) generates the audit submission in the format required by the insurance carrier, and (5) flags employees whose roles may have changed during the policy period (job title change, department transfer, split-class allocation). The consultant reviews and approves the pre-built audit rather than assembling it from raw payroll exports.

## Who Feels the Pain
HR consultants who manage workers' comp audits for 20-30 clients each year, spending 4-8 hours per client on data assembly, and clients who receive incorrect audit results (and incorrect premium adjustments) due to classification errors.

## Impact If Fixed
Reduces audit preparation from 4-8 hours to 30-60 minutes per client. For a consultant managing 25 client audits per year, this saves 87-175 hours annually. Reduces classification errors that can result in premium overcharges of $5,000-20,000 per client.
