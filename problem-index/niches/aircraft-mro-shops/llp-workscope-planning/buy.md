# LLP Tracking Extended to Back-to-Birth Proof

**Niche:** [[niches/aircraft-mro-shops/llp-workscope-planning/profile|LLP & Workscope Planning]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Maintenance systems track an LLP's running cycle count; they don't prove where each of those cycles came from.
**Tags:** #large-language-models #graph-theory #feature-engineering #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to build each engine to the cheapest workscope that still delivers the on-wing life the owner needs, with every life-limited part proven back to birth, and whoever predicts module findings and remaining part lives most accurately at induction takes the account.

## The Problem
At induction the shop has to accept the owner's LLP status sheet or verify it. Verification means tracing each disk and shaft through every operator, installation, removal and thrust-rating change since manufacture, from scanned documents. Records analysts spend ~40–80 hours per engine on it (estimate), and a gap found late stops the build.

## What Already Exists
LLP tracking modules in AMOS, TRAX, IFS Maintenix and tracking services (CAMP, Traxxall) keep cycles used and remaining per serial. Records platforms such as flydocs and Bluetail store and index the scanned evidence.

## The Customization Gap
The adaptation needs: (1) extraction of serials, part numbers, dates and cycles from log books, operator utilisation letters, shop visit reports and release tags; (2) a part-history graph per LLP with validation rules (cycles never decrease, installations never overlap, every period covered); (3) thrust-rating and configuration cycle conversions from the engine manual; (4) a gap report naming the missing document and who would hold it; and (5) a source-page link for every number, because the records analyst, not the software, certifies the pack.

## Target Customer
Records managers and powerplant engineering at engine shops; lessor technical teams buying shop visits.

## Impact If Solved
Cutting reconciliation to ~8–12 hours of reviewing flagged gaps per engine (estimate) saves several thousand analyst hours a year at a 100-visit shop, and finds trace gaps at induction instead of at the end of the build, when a replacement LLP can take months to source.
