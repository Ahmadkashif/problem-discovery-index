# Segregation, Capital & Regulatory Reporting

**Parent Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to produce the daily segregation, secured-amount and cleared-swap computations and the monthly capital report correctly before the deadline, with every number traceable for the DSRO, and whoever files every computation before noon with no restatements takes the account.

## Profile
**Market Size:** ~$300M a year in regulatory reporting software, reconciliation tools and controller staff time at FCMs (estimate)
**Share of Parent Industry:** ~8% of technology and services spend (estimate)
**Digital Adoption:** Medium — the computations are produced by back-office systems, but inputs from banks, clearing houses and carrying brokers are reconciled by hand every morning
**Target Buyer:** FCM controller / chief financial officer / head of regulatory reporting
**Automation Potential:** Very high — the rules are codified, the inputs are data, and the deadline is daily

## What Makes This a Distinct Niche
No other workflow in the industry is as rule-bound or as clock-driven. CFTC Rule 1.32 requires the segregation computation as of each business day's close, currency by currency, completed before noon the next business day, alongside the Rule 30.7 secured-amount and Rule 22.2 cleared-swap computations. All are reported to the CFTC and the firm's DSRO and summarised in the CFTC's monthly public table ($374B required in August 2026 across 75 registrants). Capital is computed against a requirement that is the greater of $1M or 8% of customer and non-customer risk maintenance margin, among other floors. Since December 2025, CFTC Letter 25-40 has added digital-asset collateral with DCO haircuts and weekly reporting for FCMs that accept it. A missed deadline is itself a violation, as the CFTC's 2009 JPMorgan Futures order shows.

## Current Tools & Gaps
FIS and ION back offices compute the regulatory figures; bank portals, clearing-house reports and reconciliation tools supply inputs; Excel bridges the gaps. The gaps: breaks are investigated manually each morning, there is no forward view of tomorrow's requirement, and explanations of movements are written from scratch.

## Problems
- [[niches/commodity-brokers/segregation-capital-reporting/build|🔨 Build: Tomorrow's Segregation Excess, Forecast Tonight]]
- [[niches/commodity-brokers/segregation-capital-reporting/buy|🛒 Buy: Bank Reconciliation Platforms Adapted to Rule 1.32]]
- [[niches/commodity-brokers/segregation-capital-reporting/fix|🔧 Fix: Breaks Investigated From Scratch Every Morning]]
