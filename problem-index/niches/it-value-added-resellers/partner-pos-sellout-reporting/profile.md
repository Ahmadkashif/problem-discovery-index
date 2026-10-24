# Partner POS & Sell-Out Reporting

**Parent Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to file each vendor's point-of-sale and sell-out report in that vendor's format with the end-customer and serial detail it requires, and whoever gets the highest share of reported lines accepted on first submission takes the account.

## Profile
**Market Size:** ~$300–500M a year of distributor and reseller labour and software spent formatting, correcting and resubmitting POS and sell-out data for IT vendors (estimate)
**Share of Parent Industry:** ~0.1% of receipts (estimate), governing access to the far larger incentive pool mapped in [[niches/it-value-added-resellers/vendor-incentive-mdf-claims/profile|Vendor Rebates, Incentives & MDF Claims]]
**Digital Adoption:** Medium — reports move by EDI 867 or flat file, but corrections and rejections are worked by hand
**Target Buyer:** Director of vendor operations at the distributor; finance or programme operations at the reseller
**Automation Potential:** Very high — formatting, enrichment and validation against each vendor's specification are mechanical

## What Makes This a Distinct Niche
IT vendors run two-tier channels and want to see every sale through to the end customer: who bought, which reseller, which serial numbers, under which registration or special-pricing number. Distributors report sell-through for every vendor they carry; resellers report end-customer detail for registrations, special pricing and programme credit. Each vendor publishes its own specification and rejects lines that don't match — a misspelt end customer, a missing serial, an unknown registration number — and a rejected line is incentive, rebate or special-pricing credit at risk. Model N's own guidance once said 80% of data from reporting partners is bad (vendor claim, older material, search summary). The contest is data acceptance, measured per line, which is why it is kept apart from the incentive-claim contest, measured in dollars recovered.

## Current Tools & Gaps
Distributor EDI teams, vendor POS portals, channel data managers on the vendor side (E2open, which owns Zyme; Model N; Vistex; CMR's ChannelPOS), spreadsheets at resellers. The gaps: one specification per vendor maintained by hand, end-customer entity matching against the vendor's account master, and rejections worked line by line after the fact.

## Problems
- [[niches/it-value-added-resellers/partner-pos-sellout-reporting/build|🔨 Build: Lines Validated Against Each Vendor's Rules Before They Leave]]
- [[niches/it-value-added-resellers/partner-pos-sellout-reporting/buy|🛒 Buy: EDI Platforms That Know Each Vendor's POS Specification]]
- [[niches/it-value-added-resellers/partner-pos-sellout-reporting/fix|🔧 Fix: The End Customer Spelt Three Ways]]
