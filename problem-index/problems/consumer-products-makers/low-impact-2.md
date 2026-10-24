# A Certificate, a Warning and a Label for Every SKU

**Industry:** [[consumer-products-makers|Consumer Products Makers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Product-compliance software is built for electronics and chemical makers; a candle, pen or lighter maker needs the same certificate, warning and label work mapped to its own handful of rules, and from July 2026 it has to be filed at the border for every shipment.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #compliance #automation #data-integration

## The Problem
A consumer products maker with a few hundred SKUs carries a compliance file for each. A candle with a metal-cored wick needs a General Certificate of Conformity under CPSC's 2003 ban on lead-cored wicks (16 CFR 1500.17(a)(13)) and the statement on its outer shipping cartons. A disposable lighter needs child-resistance testing under 16 CFR 1210. Markers, crayons and paints need a toxicologist's review under the hazardous art materials labelling law and ASTM D4236. Fragranced products need the supplier's IFRA certificate and safety data sheets, and every product sold in California needs a decision on Prop 65 warnings, which drew 1,535 settlements and about $66M in payments in 2025. Retailers add their own layer: third-party test reports against ASTM F2417 and F2058 for candles, chemical registrations, and packaging and labelling manuals.

From 8 July 2026 the importer of record must transmit certificate data for CPSC-regulated products to Customs at entry, with the product identifier, the rules certified, the testing lab and the date. A maker that imports finished candles, vessels or pens, or assembles them from imported parts, now has to keep certificate data per SKU accurate enough to file shipment by shipment.

## What Already Exists
Regulatory-content services (Enhesa, 3E, Compliance & Risks) track rules worldwide; supply-chain compliance platforms such as Assent collect supplier declarations; UL and the large testing labs sell test programmes and certificate tools; Complir and several customs brokers sell CPSC eFiling; and Prop 65 is handled by outside counsel and warning-label vendors. Testing laboratories themselves are an industry in the vault, [[testing-laboratories|Testing Laboratories]].

## The Customisation Gap
The general platforms are priced and built for manufacturers with thousands of components and dedicated regulatory staff. What a small maker needs is narrower and more specific: a rule map for its actual product types (wick construction, lighter type, art-material formulation, fragrance load); a link from each SKU's recipe or bill of materials to the certificate it needs; automatic GCC drafting from test reports with the lab's CPSC-accepted status; Prop 65 screening of fragrance, dye and pigment declarations against the listed chemicals; candle caution labels checked against ASTM F2058 wording; and an export of the eFiling data elements to the broker. It is configuration work on top of existing data, not a new science.

## Impact If Solved
The coordinator who keeps these files stops rebuilding them for every retailer and every import entry, new SKUs reach listing without a compliance hold, and the maker can show CPSC, a retailer or a Prop 65 enforcer what it certified and why in ~15 minutes rather than ~2–3 days (estimate).
