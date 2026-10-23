# Year-to-Date Conversion Reconciled to the Prior Provider's Filings

**Niche:** [[niches/professional-employer-organizations/client-onboarding-conversion/profile|New-Client Onboarding & Mid-Year Conversion]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mid-year client brings six months of wages and taxes from another provider, and if those numbers are loaded wrong the PEO overpays wage-based taxes and issues wrong W-2s eight months later.
**Tags:** #large-language-models #seq2seq #descriptive-statistics #evaluation-metrics #automation #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to convert a signed client's year-to-date wages, deductions, benefit elections, state tax accounts and workers' comp classes onto the PEO by the effective date, and whoever delivers a correct first payroll with coverage active on day one, and no amended filings afterwards, takes the account.

## The Problem
When a client joins in July, the PEO must load each employee's year-to-date gross, taxable wages by tax type and state, withholdings, retirement deferrals and pre-tax deductions. Only then do Social Security and unemployment wage bases stop at the right point and year-end forms add up. The prior provider's reports differ in format and coding. Implementers key totals from PDFs, and a misread line becomes a year-end correction.

## Why Nobody Has Built This
Platform import tools assume clean files in the platform's own layout. Reconciling year-to-date figures to the prior provider's quarterly returns requires those returns, which clients rarely send unprompted, and the tax logic for successor wage bases varies by state.

## What to Build
A conversion engine that reads the prior provider's registers, year-to-date reports and quarterly returns (941s and state returns), maps every earning and deduction to the PEO's codes with tax treatment, loads year-to-date balances, and reconciles them to the filed returns before the first payroll. It passes the loaded balances to the payroll tax team's wage-base rules (see [[niches/professional-employer-organizations/suta-multistate-payroll-tax/fix|Wage Bases Restarted When a Client Joins Mid-Year]]) and lists every unexplained difference for an implementer to resolve with the client.

## Target Customer
Implementation and payroll tax leaders at PEOs onboarding mid-year clients in volume, and acquirers moving acquired PEOs' clients onto a new platform.

## Impact If Built
Fewer amended returns, overpaid wage-based taxes and corrected W-2s, at a few hours saved per conversion and far fewer year-end fire drills (estimate).
