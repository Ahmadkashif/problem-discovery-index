# Hospital Contract Modelling Re-Cut for Percentage-of-CLFS Contracts

**Niche:** [[niches/clinical-laboratories/routine-claims-contract-underpayments/profile|Routine Test Claims & Contract Underpayments]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hospitals already buy contract modelling that flags underpaid claims; it is priced per claim and built for DRGs, not for thousands of $12 lab lines indexed to a moving federal schedule.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to recover underpaid and bundled-away dollars on routine lab claim lines worth a few dollars each, and whoever recovers the most net dollars per thousand claims worked takes the account.

## The Problem
Health-system outreach labs bill under the hospital's revenue cycle stack, where contract modelling is configured for inpatient and outpatient facility claims. Lab lines are a rounding error to that system and rarely get modelled at all, though they are a large share of claim volume.

## What Already Exists
Contract management and underpayment modules in hospital revenue cycle suites (Experian Health, Waystar and EHR-native tools), and contingency-fee underpayment recovery firms that work high-dollar claims.

## The Customization Gap
The adaptation needs fee-schedule versioning by date of service and quarter, PAMA phase-in caps, gapfill and MAC-priced code handling, and proprietary laboratory analysis and ADLT carve-outs. It needs aggregate rather than per-claim variance reporting, so a payer-code pattern is appealed once, and a pricing model per line rather than per claim, since contingency firms will not touch $12 lines.

## Target Customer
Revenue cycle directors at health systems with outreach labs, and lab directors who share outreach P&L responsibility.

## Impact If Solved
Outreach lab lines get the same contract scrutiny as facility claims at no extra licence. That matters most in the years when outreach margins decide whether a health system keeps its lab book or sells it: a 1% recovery on ~$30M of outreach revenue is ~$300,000 a year (estimate).
