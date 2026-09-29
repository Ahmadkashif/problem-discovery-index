# Catalogue Manager Maintaining Product Data

**Industry:** [[b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Worker Life Changing
**One-liner:** A catalogue manager keys technical attributes from manufacturer PDFs into a system that will never be complete, prioritising by intuition, with no way to know which gaps are costing sales.
**Tags:** #large-language-models #bert #cnns #word-embeddings #evaluation-metrics #confidence-intervals #automation #worker-facing

## The Problem
A distributor's catalogue manager maintains product data across hundreds of thousands of items. Manufacturers send updates — new products, discontinued items, specification changes, price files — as PDFs, spreadsheets in different formats each time, and occasionally as portal downloads.

The work is transcription. Open the datasheet, find the attributes, key them into the product record against the category's attribute schema, attach images, set the classification. A complex industrial product may have thirty relevant attributes.

The backlog never clears. New products arrive faster than they can be enriched, and the existing long tail was never done. So the manager prioritises — usually by sales volume, sometimes by whoever asked most recently — and the majority of the catalogue stays thin.

Nobody tells them which gaps matter. A missing attribute on a slow-moving item costs nothing; a missing attribute that prevents customers filtering to a commonly needed specification costs sales continuously. The evidence for that distinction exists in search and support data and does not reach the catalogue team.

## Why It Matters to the Worker
The task is unbounded by construction. There is no state in which the catalogue is complete, because manufacturers keep issuing products, and the manager works permanently against a growing backlog.

The work is invisible when it succeeds. Nobody notices a well-attributed product; everybody notices a wrong specification, which produces a returned part and a complaint.

Prioritising without evidence is the specific frustration. The manager knows the effort is misallocated and has no basis for allocating it better, so they work by volume and by request, which systematically favours the items that already sell.

And the transcription is mechanical work performed by people who develop real product knowledge — a good catalogue manager understands the categories deeply, and that understanding is spent on keying values from PDFs.

## What a Solution Looks Like
Extraction rather than transcription. Manufacturer datasheets are a variable-layout, consistent-content document class, and extracting attributes into a category schema with confidence scores turns the manager's job into review. This is the largest single change available.

Prioritisation from evidence. Which attributes drive findability in each category is derivable from search queries, filter usage, support calls and returns caused by wrong parts, and it should direct the enrichment queue rather than sales volume alone.

Completeness scoring per item against what matters for that category, so the manager can see where the catalogue is genuinely inadequate rather than merely incomplete.

Change detection on manufacturer sources, so a specification change or discontinuation is caught when it is published rather than when a customer orders a part that no longer exists.

Cross-reference generation as a by-product of structured specifications, which is the commercially valuable output and is currently unattainable because the inputs are unstructured.

## Impact If Solved
Catalogue completeness gates the self-service proposition in industrial distribution and is maintained by a permanently backlogged transcription function prioritising blind. Automating extraction and directing effort by measured findability impact turns an unbounded task into a managed one and puts the manager's product knowledge to use on review rather than on keying.
