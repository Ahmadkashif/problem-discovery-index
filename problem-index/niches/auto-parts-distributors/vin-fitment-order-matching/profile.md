# VIN & Fitment Matching on Shop Orders

**Parent Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to turn a shop's call, text or e-catalog request into the one part that fits that VIN, and whoever has the lowest fitment-return rate on the shop orders it matches takes the account.

## Profile
**Market Size:** ~$3B a year of counter time spent decoding vehicles and matching parts on commercial orders (estimate), plus the cost of wrong-part runs and returns
**Share of Parent Industry:** ~0.8% of the three codes' receipts (estimate)
**Digital Adoption:** Medium — catalogs are digital, but the match on ambiguous lines is made in a counter person's head
**Target Buyer:** VP of store operations or commercial operations; catalog and systems leads
**Automation Potential:** High on clear lines; medium on lines where qualifiers remain after the VIN decode

## What Makes This a Distinct Niche
This is the matching half of shop order intake: from a request in shorthand and a VIN or stated vehicle to the one part that fits. It is distinct from the general distributor intake field at [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]] because the key is a vehicle configuration, not a SKU or customer stock code, and the catalog is the licensed Auto Care VCdb with suppliers' ACES applications. The hard step is the one NHTSA's vPIC decoder doesn't settle: it returns make, model, year, engine and trim, but not the brake package, axle ratio or production split that separate the candidates. Competitors are the chains' own catalogs, business-system vendors, e-catalog networks and parts-identification models such as Partly's, which claims 98.8% parts-list accuracy for estimators (vendor figure) and was hiring engineers in Austin on 2026-10-28. The counter judgement behind it is the industry's tacit problem, set out in [[problems/auto-parts-distributors/high-impact|The Fitment Call Only the Counter Pro Can Make]].

## Current Tools & Gaps
Catalogs return candidate lists; e-catalogs let shops pick for themselves; parts-identification models work from repair estimates. The gaps: no tool asks the shop the one clarifying question that settles a qualifier, and none is scored on fitment returns at the store.

## Problems
- [[niches/auto-parts-distributors/vin-fitment-order-matching/build|🔨 Build: A Two-Week Shop-Order Agent on vPIC and a Synthetic Fitment Catalog]]
- [[niches/auto-parts-distributors/vin-fitment-order-matching/buy|🛒 Buy: Parts-Identification Models Adapted to the Counter]]
- [[niches/auto-parts-distributors/vin-fitment-order-matching/fix|🔧 Fix: The VIN Decode Stops Short of the Qualifier]]
