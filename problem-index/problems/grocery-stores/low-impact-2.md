# Traceability Records at the Receiving Door

**Industry:** [[grocery-stores|Grocery Stores]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Warehouse and receiving systems already record what arrived; none captures the lot-level traceability data the FDA rule asks a supermarket to produce within 24 hours for leafy greens, fresh-cut fruit, soft cheese, shell eggs and seafood.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #compliance #data-integration #workflow-orchestration #automation

## The Problem
The FDA Food Traceability Rule requires anyone who receives a food on its Food Traceability List to keep key data elements for each receipt: the traceability lot code, the quantity, the previous source, the location where the lot code was assigned, and the receiving date. The records must be made available within 24 hours of an FDA request (FDA), and in an outbreak as an electronic sortable spreadsheet (recalled). Supermarkets are covered unless they are small, and the list is grocery's highest-risk fresh: leafy greens, herbs, cucumbers, peppers, tomatoes, melons, fresh-cut fruit and vegetables, soft cheeses, shell eggs, finfish and molluscan shellfish. Congress has deferred enforcement to 20 July 2028 (FDA), which gives chains a deadline and no penalty yet.

The work lands on the receiver at the back door and on the produce and seafood clerks. Product arrives from the chain's own warehouse, from wholesalers and from direct-store-delivery vendors. The lot code is printed on the case label, sometimes as a GS1-128 barcode, often as text. Cases are broken, and product is repacked in the department, cut into fruit trays or ground into sushi rice bowls, which creates new lots. In an outbreak, the question "which stores received lot X, and where did it go after that?" is answered today by phone calls and paper invoices.

## What Already Exists
Warehouse management and store receiving systems (Manhattan, Blue Yonder, Oracle Retail, handheld receiving in the POS suite) record PO lines and quantities. Traceability networks (ReposiTrak, iFoodDS, Trustwell) and GS1 standards (GTIN plus lot in GS1-128, EPCIS events) move key data elements between trading partners. Temperature and HACCP logging tools (ComplianceMate, Zest, SmartSense) digitise food-safety checks.

## The Customisation Gap
The generic systems were built for the warehouse, where every case is scanned against an advance ship notice. A store's gap is the mixed back door: DSD vendors without ship notices, lot codes printed as text, store-level transformation that must link the input lot to the tray or bowl it became, and departments that receive from three sources the same morning. The customisation is capture at receiving, by reading the lot code from a case photo when there is no barcode. Then come a rules layer that knows which items are on the list and which store recipes count as transformation, and a 24-hour drill that proves the spreadsheet can be produced before 2028 rather than during an outbreak. The distributor-side services are profiled under [[food-distributors|Food Distributors]].

## Impact If Solved
For a 50-store chain, receiving capture that lifts complete key-data-element records on listed foods from ~30% to ~95% (estimate) turns a multi-day phone hunt into a same-day spreadsheet, and lets the chain pull only the affected lots in a recall rather than clearing every bag of spinach in the region.
