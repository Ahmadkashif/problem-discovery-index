# Routine Test Claims & Contract Underpayments

**Parent Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to recover underpaid and bundled-away dollars on routine lab claim lines worth a few dollars each, and whoever recovers the most net dollars per thousand claims worked takes the account.

## Profile
**Market Size:** ~$2B a year in billing, variance and appeals work on routine chemistry, haematology, microbiology and immunology claims (estimate)
**Share of Parent Industry:** ~4% of industry revenue (estimate)
**Digital Adoption:** Medium — remits are electronic, contracts are PDFs and variance is checked by spreadsheet on the biggest payers only
**Target Buyer:** Director of reimbursement or revenue cycle at a regional, outreach or reference lab
**Automation Potential:** High — expected payment is computable, and variance detection is statistical

## What Makes This a Distinct Niche
Routine tests are paid a few dollars to a few tens of dollars a line, mostly under commercial and Medicare Advantage contracts priced as a percentage of the Medicare CLFS. Margins are made or lost in aggregate: a 3% systematic short-pay by one payer across 400 codes is invisible claim by claim. The 2027–2029 PAMA phase-in reprices every such contract each January, with preliminary CY2027 rates about 16% lower on average across 1,171 reduced codes, so payer systems will load new schedules at different times and with different errors. The same lines carry the bundling edits behind 59.4% of routine lab denials. The hospital version, where contracts run on DRGs and APCs, is [[niches/general-hospitals/payer-contract-modelling-underpayments/profile|🎯 Payer Contract Modelling & Underpayment Recovery]]; the lab version is a smaller-ticket, higher-volume contest that hospital tools are not priced or built for.

## Current Tools & Gaps
XiFin and Telcor compute expected payment from loaded terms; hospital contract-management modules exist; most labs check their top payers in Excel after each update. The gaps: no schedule-version awareness by date of service, no statistical detection across small lines, and no payer-level recovery packet.

## Problems
- [[niches/clinical-laboratories/routine-claims-contract-underpayments/build|🔨 Build: An Expected-Payment Engine Indexed to the Lab Fee Schedule]]
- [[niches/clinical-laboratories/routine-claims-contract-underpayments/buy|🛒 Buy: Hospital Contract Modelling Re-Cut for Percentage-of-CLFS Contracts]]
- [[niches/clinical-laboratories/routine-claims-contract-underpayments/fix|🔧 Fix: The January Reset Nobody Re-Prices]]
