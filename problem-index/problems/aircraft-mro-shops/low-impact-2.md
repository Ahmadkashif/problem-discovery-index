# LLP Back-to-Birth Packs Assembled by Hand

**Industry:** [[aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document scanning and records software store an engine's history, but proving each life-limited part's cycles back to birth, across operators, thrust ratings and shop visits, is still done by a records analyst with a spreadsheet and a stack of PDFs.
**Tags:** #large-language-models #transformers #graph-theory #feature-engineering #data-integration #compliance #automation

## The Problem
Every turbofan carries life-limited parts (fan disks, compressor and turbine disks and shafts) that must be retired at a published cycle limit. When an engine comes into a shop, the MRO has to establish each LLP's cycles used and remaining before it can plan the workscope or release the engine. Buyers and lessors won't accept a part unless the trace runs unbroken back to its manufacture ("back-to-birth"). The evidence is a chain of documents: the original certificate of conformity, each operator's utilisation records, engine log book entries for every installation and removal, the shop visit reports, the 8130-3 or EASA Form 1 tags issued at each release, and the conversion of cycles when the engine ran at a different thrust rating or configuration.

A records analyst assembles this by hand. They open hundreds of scanned pages, transcribe serial numbers and cycle counts into a spreadsheet, chase missing operator statements by email, and reconcile disagreements between documents. A single gap — one operator's utilisation for eighteen months missing, a part number superseded without a note — can strand a part worth hundreds of thousands of dollars (estimate). Untraceable LLPs lose most of their value (recalled industry practice). The AOG Technics case, which put over 60,000 suspect CFM56-family parts into the supply chain on forged paperwork, showed why buyers now read every page.

## What Already Exists
Records platforms (flydocs, Bluetail, AMOS and TRAX records modules) scan, index and store documents. Tracking services such as CAMP and Traxxall keep running totals for LLPs on the aircraft they track. General-purpose OCR and document-AI tools extract fields from PDFs. Records consultancies audit packs for transactions.

## The Customisation Gap
Storing documents is not the same as proving a chain. The engine-specific logic is a part-history graph: each LLP serial as a node, each installation, removal and shop visit as a dated edge carrying cycles and thrust rating; validation rules that check cycles never decrease, installation dates never overlap and every operator period is covered; conversion of cycles between ratings according to the engine manual's tables; and a gap report that names the exact missing document and who would hold it. The tool has to read the messy evidence (handwritten log entries, operator utilisation letters in different formats, tags with superseded part numbers) and show the source page for every number. The same logic serves the MRO's shop visit induction and the lessor's lease return, but the MRO is the one that has to release the engine.

## Impact If Solved
Cutting an LLP back-to-birth reconciliation from ~40–80 analyst hours per engine to ~8–12 hours of reviewing flagged gaps (estimate) frees a records team handling ~100 shop visits a year to do several thousand hours of other work. Finding a gap at induction rather than at sale protects parts worth ~$3–5M per engine stack (estimate).
