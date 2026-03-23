# ACA Reporting Engine for Complex Self-Insured Groups

**Niche:** [[niches/insurance-tpa/regulatory-reporting/profile|Regulatory Reporting & Compliance]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ACA reporting tools exist but fail on the edge cases that define TPA-administered self-insured plans — controlled groups, variable-hour employees, multi-state lookback measurements, and mid-year plan changes.
**Tags:** #automation #compliance #data-integration

## The Problem
TPAs must generate IRS Form 1095-C for every full-time employee of their self-insured employer clients. For simple groups, this is straightforward. For complex groups — franchises with controlled group determinations, staffing agencies with variable-hour employees requiring lookback measurement periods, employers with mid-year plan changes or mergers — the 1095-C coding logic becomes extremely complicated. A single coding error on the offer-of-coverage line (Line 14/15/16) can trigger IRS penalties of $330 per form.

## What Already Exists
ACA reporting vendors (ACAwise, Integrity Data, ADP) generate 1095-C forms from payroll and benefits data. These work well for direct employers with simple plan structures. They fail for TPA-administered plans because the TPA has benefits data but not payroll data, the employer has payroll data but not benefits data, and the ACA reporting tool needs both to correctly determine full-time status, measurement periods, and offer-of-coverage codes.

## The Customization Gap
The gap is a TPA-centric ACA reporting engine that accepts benefits eligibility and enrollment data from the TPA and payroll/hours data from the employer (or their payroll provider), merges them into a unified dataset, applies lookback measurement logic for variable-hour employees, determines controlled-group status for related employers, and generates correctly coded 1095-C forms. Must handle the TPA's unique position as the data holder for benefits but not employment.

## Target Customer
TPAs administering plans for employers with complex workforce structures — staffing agencies, franchise groups, seasonal employers, and multi-entity controlled groups.

## Impact If Solved
Eliminates 1095-C coding errors that currently trigger $100K-$500K in IRS penalties per filing season for mid-market TPAs. Reduces ACA reporting preparation time from 200-400 hours to 40-80 hours per filing season.
