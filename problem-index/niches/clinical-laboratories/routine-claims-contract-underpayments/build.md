# An Expected-Payment Engine Indexed to the Lab Fee Schedule

**Niche:** [[niches/clinical-laboratories/routine-claims-contract-underpayments/profile|Routine Test Claims & Contract Underpayments]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contracts say "85% of current CLFS" and nothing computes what that means for every line, every payer and every quarter through a three-year price reset.
**Tags:** #bayesian-inference #change-point-detection #hypothesis-testing #descriptive-statistics #large-language-models #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to recover underpaid and bundled-away dollars on routine lab claim lines worth a few dollars each, and whoever recovers the most net dollars per thousand claims worked takes the account.

## The Problem
A regional lab may hold 60 payer contracts, each pegged to the Medicare CLFS in its own way: current year, a frozen base year, a percentage, a floor, carve-outs for proprietary and locally priced codes. CMS publishes the schedule quarterly. From 1 January 2027 it falls each year for three years, by up to 15% per test per year. Billing staff cannot tell from a remittance whether a lower payment reflects the new schedule, a contract term or a payer error.

## Why Nobody Has Built This
Lab RCM systems compute expected payment only if someone has loaded the terms, and few labs maintain them beyond their largest payers. Hospital variance tools are built for high-dollar claims worked individually. The flat fee schedule of 2020–2026 made the problem small; the PAMA reset makes it large again.

## What to Build
An engine that ingests every CLFS quarter and structures each contract's pricing terms with a language model, confirmed by an analyst. It computes expected payment for every remitted line by date of service and estimates payer-by-code payment ratios with hierarchical models that borrow strength across codes. It detects change points after each schedule load and outputs one recovery packet per payer, with the clause, the schedule version, the claims and the dollars. A demo runs on public CLFS files and synthetic 835s in two weeks.

## Target Customer
Directors of reimbursement at regional and outreach labs with $20–200M of commercial and Medicare Advantage revenue, and lab RCM vendors that want the capability inside their platform.

## Impact If Built
For a lab with $80M of contract revenue, finding a 1% systematic short-pay recovers ~$800,000 a year (estimate) through a handful of payer-level appeals, net of almost no per-claim work.
