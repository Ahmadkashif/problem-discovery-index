# Structured Finance Trustee Reporting

**Parent Industry:** [[industries/trust-companies|Trust Companies]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to compute every payment-date waterfall, coverage test and investor report correctly from the deal documents and the servicer's or manager's data before the distribution date, and whoever does it with the fewest restatements takes the account.

## Profile
**Market Size:** ~$300M a year in reporting technology, collateral administration tooling and data services at corporate trustees (estimate)
**Share of Parent Industry:** ~60% of corporate trust tooling spend (estimate)
**Digital Adoption:** Medium — data arrives electronically, but each deal's waterfall is coded or spreadsheeted individually
**Target Buyer:** Head of Structured Finance Trust Services / Head of CLO Collateral Administration
**Automation Potential:** High

## What Makes This a Distinct Niche
For a performing securitisation or CLO, the trustee's (or collateral administrator's) job is arithmetic on a hard clock. Every month or quarter it takes the servicer's or manager's data, applies the priority of payments, runs coverage and quality tests, computes distributions to each tranche and publishes the report investors and rating agencies read, before the distribution date fixed in the documents. CLO administration adds trade-by-trade compliance testing. An error means a restatement, a misdirected payment and a claim. Competitors are the large trustees (U.S. Bank, BNY, Computershare, Citi, Deutsche Bank) and specialist collateral administrators; the investor-side deal modelling vendors are profiled in [[niches/sales-finance-companies/auto-abs-deal-analytics/profile|🔍 Auto ABS Deal Modelling & Surveillance Analytics]], the issuer-side reporting work in [[niches/sales-finance-companies/warehouse-and-abs-reporting/profile|⚡ Warehouse & ABS Collateral Reporting]], and trust banks' collateral custody and file verification for the same pools in [[niches/sales-finance-companies/warehouse-collateral-custody/profile|🔍 Warehouse Collateral Custody, Verification & Backup Servicing]].

## Current Tools & Gaps
In-house calculation engines, deal-specific code and spreadsheets, investor reporting portals. The gaps: waterfall logic hand-translated from documents for every deal and amendment; servicer data validated by eye; and no systematic regression test against prior distributions when logic changes.

## Problems
- [[niches/trust-companies/structured-finance-trustee-reporting/build|🔨 Build: Waterfall Code Generated From the Indenture and Tested Against History]]
- [[niches/trust-companies/structured-finance-trustee-reporting/buy|🛒 Buy: Deal Modelling Libraries as the Trustee's Book of Record]]
- [[niches/trust-companies/structured-finance-trustee-reporting/fix|🔧 Fix: Servicer Data That Arrives the Night Before Determination Date]]
