# SNAP & WIC Item-Eligibility Compliance

**Parent Industry:** [[industries/grocery-stores|Grocery Stores]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to keep every register's SNAP and WIC eligibility flags right across states, waivers and court orders, and whoever has the fewest wrongly blocked or wrongly allowed benefit scans per million takes the account.

## Profile
**Market Size:** ~$250M a year of item-data, eligibility-database, POS configuration and staff spend at supermarkets on SNAP and WIC item eligibility (estimate)
**Share of Parent Industry:** In FY2021 supermarkets redeemed $33.9B (27.0%) of ~$125B of SNAP benefits, and supermarkets and super stores together ~$100B (79%), with super stores including supercenters outside this industry (USDA FNS); the compliance spend is a tiny fraction of either (estimate)
**Digital Adoption:** Medium — POS systems carry eligibility flags and download WIC files, but the flags are set by people reading rules
**Target Buyer:** Director of item data or POS at a chain; owner at an independent
**Automation Potential:** Very High — eligibility is a rule applied to item attributes, repeated over hundreds of thousands of items and changed on known dates

## What Makes This a Distinct Niche
SNAP is grocery's largest single payer outside cash and cards. Supermarkets alone redeemed 27.0% of benefits ($33.9B) in FY2021, and supermarkets and super stores together 79% while being 15% of authorized firms (USDA FNS). The super store class includes supercenters, which belong to the queued general merchandise retailers industry. For decades SNAP eligibility was one national rule. In 2026 it became a state-by-state rule set. USDA granted 23 states waivers to restrict soda or candy, and a court blocked five on 22 June 2026 (Avalara), so the item file must carry a flag per state with dates a judge can move. WIC was always state-specific, with Authorized Product Lists by UPC and package size that registers load frequently. Errors in either direction cost money: a blocked eligible item loses the basket, and an allowed ineligible item is a violation against the store's authorisation.

## Current Tools & Gaps
POS systems (NCR Voyix, Toshiba, LOC, ECRS), Avalara's SNAP-ineligible UPC database, item-data networks (Syndigo, 1WorldSync, GS1 US), and eWIC processors that deliver APLs. Gaps: private label and store-made items are outside the databases, waiver definitions need judgement, and court-driven date changes are applied by hand. Benefit screening for households is a different job, profiled at [[niches/nonprofits-social-services/benefits-eligibility-screeners/profile|⚡ Benefits Eligibility Screeners]].

## Problems
- [[niches/grocery-stores/snap-wic-item-eligibility/build|🔨 Build: An Eligibility Engine That Cites the Clause]]
- [[niches/grocery-stores/snap-wic-item-eligibility/buy|🛒 Buy: Sales-Tax Classification Engines Adapted to Benefit Rules]]
- [[niches/grocery-stores/snap-wic-item-eligibility/fix|🔧 Fix: The Shelf Tag and the Register Disagree]]
