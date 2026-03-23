# Salon-Specific Commission & Compensation Calculator

**Niche:** [[niches/hair-salons-independent/commission-payroll/profile|Stylist Commission & Booth-Rent Payroll]]
**Industry:** [[industries/hair-salons-independent|Independent Hair Salons]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No payroll tool natively calculates salon-specific compensation — tiered commissions, guaranteed minimums, retail spiffs, backbar charges, and booth-rent deductions — without manual spreadsheet work.
**Tags:** #automation #data-integration #workflow-orchestration #quick-win

## The Problem
A salon owner paying 6 stylists under different commission structures spends 4-8 hours per pay period on payroll calculations. Stylist A earns 45% commission on services under $8,000/month and 50% above $8,000, with a $600/week guaranteed minimum, plus 10% on retail, minus $50/month for backbar supplies. Stylist B is booth-rent at $250/week but uses the salon's booking system and product supply room for an additional $75/week. Stylist C is a new hire at $15/hour guaranteed for 90 days, then transitions to 40% commission. These calculations require pulling service totals from the POS, applying per-stylist rules, comparing against guarantees, adding retail commissions, deducting charges, and reconciling tips — all in a spreadsheet that breaks every time the compensation structure changes.

## Why Nobody Has Built This
General payroll companies (Gusto, ADP) handle hourly and salary calculations at scale but see salon commission structures as an edge case. Salon POS companies (Vagaro, Booker) build basic commission calculation but not the full payroll integration (tax withholding, direct deposit, compliance). Neither side has built the end-to-end solution because the salon market's per-location revenue is too small to justify custom payroll engine development.

## What to Build
A commission calculation engine that integrates with salon POS data and outputs payroll-ready numbers: (1) configurable per-stylist compensation structures (flat commission, tiered, guaranteed minimum, hourly+commission hybrid), (2) automatic service revenue pull from POS by stylist, (3) guaranteed minimum reconciliation (pay whichever is higher), (4) retail commission calculation at separate rates, (5) backbar/supply charges deduction, (6) tip aggregation and distribution, (7) booth-rent invoice generation for 1099 contractors, and (8) export to Gusto/ADP/QuickBooks for final payroll processing.

## Target Customer
Salon owners with 4+ stylists under mixed compensation structures who spend 4+ hours per pay period on manual commission calculations.

## Impact If Built
Saves 4-8 hours per pay period (8-16 hours/month), eliminates calculation errors that create stylist distrust and potential wage disputes, and enables salon owners to model compensation structure changes ("what if I move everyone to tiered commission?") before implementing them.
