# Basket Capacity Computed on the Wrong EBITDA

**Niche:** [[niches/hedge-funds/covenant-and-document-monitoring/profile|Covenant & Document Monitoring]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Covenant capacity depends on EBITDA as the document defines it, add-backs included, and analysts routinely compute it from reported figures instead.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every credit agreement and amendment in a portfolio into a structured, comparable record of what the borrower is permitted to do — and whoever does it fastest after a document drops sees liability-management risk first.

## The Problem
Debt and payment baskets are sized as multiples of a defined EBITDA that typically includes negotiated add-backs — projected synergies, cost savings, one-off items. Analysts short of time compute capacity from reported EBITDA and understate what the borrower can do.

## Why It's Still Broken
The definition is long, the add-backs require judgement, and the inputs come from different documents.

## What a Fix Looks Like
Extract the EBITDA definition and its add-backs, compute document-defined EBITDA from reported financials and disclosed adjustments with each step shown, and recompute basket capacity each quarter.

## Who Feels the Pain
Credit analysts and PMs who underestimate borrower flexibility until it is exercised.

## Impact If Fixed
Capacity numbers that match the document, refreshed each quarter, at the cost of a computation rather than a reading.
