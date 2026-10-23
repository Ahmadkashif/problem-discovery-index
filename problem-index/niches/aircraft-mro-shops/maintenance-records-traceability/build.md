# A Pre-Buy Records Review in Hours, Not Days

**Niche:** [[niches/aircraft-mro-shops/maintenance-records-traceability/profile|Aircraft Maintenance Records & Logbook Audits]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A pre-buy records review means an inspector reading every logbook page of a 20-year-old business jet to rebuild its AD and alteration history, and it is done from scratch for every sale.
**Tags:** #large-language-models #transformers #graph-theory #feature-engineering #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to prove an aircraft's history complete (every AD, inspection, major repair and alteration traced through its logbooks) before a buyer's or lessor's records auditor finds the gap, and whoever finds the gap first takes the account.

## The Problem
An aircraft sale triggers a pre-buy at an MRO: a physical inspection and a records review. The records reviewer reads airframe, engine and propeller logbooks, AD compliance records, 337s and work orders, and reconstructs total times, inspection history, AD compliance and damage history. On a business jet this is days of work. Findings feed the price negotiation, and the review is redone at the next sale by a different shop.

## Why Nobody Has Built This
Logbook entries are handwritten or typed in many styles over decades, often by shops that no longer exist. Tracking services hold current status, not the evidence chain. Pre-buy work is fragmented across thousands of shops, each doing a few a month, and the reviewers' judgement about what an old entry means has looked impossible to automate.

## What to Build
An engine that reads scanned logbooks and work orders into a dated event history (inspections, AD compliance entries with method and revision, repairs, alterations, component changes, damage), cross-checks it against the FAA's AD library for the aircraft's configuration, and produces a draft records report: AD compliance matrix, alteration file with 337 status, time-in-service reconciliation, gaps and anomalies. Each line links to its source page. The reviewer edits and signs.

## Target Customer
Pre-buy inspection shops and records departments at business aviation MROs (Duncan Aviation, West Star Aviation, Elliott Aviation and FBO-based shops, names recalled); aircraft brokers and buyers' technical representatives.

## Impact If Built
Cutting a business jet records review from ~3–5 days to ~1 day (estimate) frees ~200–400 reviewer days a year at a shop doing ~100 pre-buys. A missed AD or alteration found before closing can be worth tens of thousands of dollars in price to the buyer (estimate).
