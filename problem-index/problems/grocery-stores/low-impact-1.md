# SNAP Waiver and WIC Item Eligibility Files

**Industry:** [[grocery-stores|Grocery Stores]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Sales-tax engines and POS item files already flag products by jurisdiction; nobody maintains the state-by-state SNAP restriction and WIC approved-product flags a supermarket chain now has to load into every register.
**Tags:** #large-language-models #bert #transformers #decision-trees #compliance #data-integration #automation

## The Problem
A chain's scan coordinator, the headquarters clerk who maintains the item file, used to have one SNAP rule to apply: hot foods, alcohol, tobacco and non-food items are ineligible, and almost everything else is eligible nationwide. In 2026 that changed. USDA granted 23 states waivers to bar SNAP purchases of soda, candy or both, each with its own definitions and start dates. A district court then blocked five of them on 22 June 2026 (Avalara). One state's "soft drink" includes sports drinks, flavoured water and juice drinks under 100% juice. Another's "candy" turns on flour content. Industry groups count more than 650,000 products that need an eligibility review (NACS, search summary). A chain operating in four states now carries four eligibility flags per UPC, and must flip them on a date a court can move.

WIC was already harder. Each state agency publishes an Authorized Product List of UPCs and produce codes, by package size and brand, and expects it loaded to registers, in some states daily (search summary). A wrong flag either blocks an eligible purchase at the register, in front of a customer with a child, or lets an ineligible one through, which is a compliance finding against the store's authorisation.

## What Already Exists
Sales-tax engines (Avalara, Vertex) classify products by tax jurisdiction, and Avalara now sells a database of UPCs ineligible for SNAP under each state's rules. POS systems (NCR Voyix, Toshiba, LOC, ECRS) carry SNAP and WIC flags per item and download state APL files. Item data networks (Syndigo, 1WorldSync, GS1 US) carry product attributes such as ingredients, sugar content and package size. eWIC processors deliver the APL.

## The Customisation Gap
The generic tools classify against stable tax rules and treat SNAP as one national flag. What a grocer needs is a state-by-state eligibility model tied to each waiver's legal text, applied to the chain's own item file, including private label, store-made items, random-weight and deli codes that no outside database carries. It needs effective dates that can be reversed by a court order. It needs a review queue for the borderline items (a protein drink, a granola bar with chocolate chips) with the reasoning recorded for the state. And WIC APL changes must reconcile against the chain's shelf tags, so the tag and the register agree.

## Impact If Solved
For a 100-store chain in four waiver states, an eligibility model that classifies the item file and routes only borderline cases to review could cut the item-file work from ~2,000 to ~200 staff hours per waiver change (estimate), and cut wrongly blocked SNAP and WIC scans, each one a lost basket and a customer confrontation.
