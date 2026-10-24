# Underpayments on Contracts Priced Off the Lab Fee Schedule

**Industry:** [[clinical-laboratories|Clinical Laboratories]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Contract-variance tools already exist for hospitals; a lab's commercial and Medicare Advantage contracts are priced as a percentage of a Medicare fee schedule that resets on 1 January 2027, and no tool re-prices thousands of small lines against it.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #bayesian-inference #data-integration #revenue-impact #automation #quick-win

## The Problem
Most lab payer contracts don't list prices. They say "100% of the current Medicare Clinical Laboratory Fee Schedule", "85% of CLFS", or "CLFS as of 2019 plus 5%", with carve-outs for proprietary codes and a default for codes Medicare prices locally. When the fee schedule moves, every contract moves with it, and the payer's claims system has to load the new rates correctly for every code. Some load them late, some apply the wrong year, and some pay locally priced and new codes at a default nobody agreed to.

That movement is about to be large. CMS's preliminary CY2027 schedule, built from 6,304 labs' private payer data, lowers 1,171 of 1,947 codes, by about 16% on average and 22% in molecular pathology. Cuts are capped at 15% per test per year from 2027 to 2029, and final rates are due in November 2026. Over three years, every percentage-of-CLFS contract reprices three times. A lab's billing team sees remittances arrive at $14.20 instead of $16.80 on a line and cannot tell, across 400 codes and 60 payers, whether that is the new schedule, a contract term or an error.

## What Already Exists
Hospitals use contract management and variance tools (Experian Health, Waystar and similar modules in hospital revenue cycle suites; the hospital version of this problem sits under [[general-hospitals|General Hospitals]]), built around DRGs, APCs and fee-schedule percentages for professional services. Lab RCM systems (XiFin, Telcor) compute expected payment from loaded contract terms. CMS publishes the CLFS quarterly as public files.

## The Customisation Gap
A lab needs expected payment computed per line against the right fee schedule version for the date of service. That means carrying each contract's index, percentage, effective-date rules, phase-in caps and code carve-outs, with special handling for codes priced by gapfill or by the local MAC and for advanced diagnostic laboratory tests. Variance has to be detected statistically across thousands of $10–40 lines, because no one will work them individually: payer-by-code change points after each quarterly update, and systematic short-pays separated from one-off adjustments. The output is a recovery packet per payer, not per claim. A two-week demo can be built on the public CLFS files and synthetic 835 remittances; a live one runs on the lab's own remits and contracts, which the lab owns.

## Impact If Solved
Labs collect what their contracts already promise through the 2027–2029 reset. A regional lab with ~$80M of commercial and Medicare Advantage revenue that finds a 1% systematic short-pay recovers ~$800,000 a year (estimate) with one appeal per payer instead of thousands.
