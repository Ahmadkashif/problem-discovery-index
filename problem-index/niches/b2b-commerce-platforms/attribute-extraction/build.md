# The Thread Pitch Is on Page Four

**Niche:** [[niches/b2b-commerce-platforms/attribute-extraction/profile|Attribute Extraction]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Product information management is mature and catalogues stay incomplete because attributes arrive as manufacturer PDFs and someone has to key them.
**Tags:** #large-language-models #transformers #object-detection #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to turn manufacturer documents into catalogue attributes at an accuracy the distributor will publish without review — and whoever reaches that threshold replaces an entire manual function.

## The Problem
The distributor has the datasheet. It states the thread pitch, the material, the pressure rating, the temperature range and the certification — in a table, in a drawing callout, in a footnote, in a units convention the manufacturer chose. To get those five values into five catalogue fields, a person opens the PDF and types. Four hundred thousand products, thirty attributes each, thousands of manufacturers who each format differently and revise without notice. The storage system is not the constraint and never was. The constraint is a person reading a document.

## Why Nobody Has Built This
Document extraction was not good enough until recently — technical datasheets are dense, tabular, diagram-heavy and full of domain-specific conventions, and general extraction tools produced accuracy that cost more to correct than to key. Product information vendors sell the repository and treat population as the customer's problem. Industry data pools solved it for a few categories and stalled. And the accuracy bar is unusually high, because a wrong specification ships a wrong part.

## What to Build
An extraction pipeline built for technical product documents. Parse the document structure properly — tables, multi-column layouts, drawing callouts and footnotes — since the values are overwhelmingly in structures that flat text extraction destroys, and this is where general-purpose tools fail first. Extract against the category's attribute schema rather than open-endedly, which constrains the problem enormously and is available because the schema already exists in the product information system. Normalise units, formats and vocabularies at extraction, which is the fix note's problem and belongs in the same pass. Emit a calibrated confidence per attribute so the distributor can publish the confident ones and route the rest to review, which is the mechanism that makes the whole thing usable below perfect accuracy — the absence of this is why extraction pilots fail. Handle tables spanning products, where one document covers forty variants and the extraction must map rows to part numbers. Learn from every review correction, since the manager's edits are exactly the labelled data the system needs. Reprocess automatically when a document is revised, which connects to the change detection work. And measure accuracy per attribute type and per manufacturer, so the distributor knows where to trust it and where to keep a person.

## Target Customer
Distributors and manufacturers with large technical catalogues, product information vendors with an unpopulated repository problem, and catalogue operations teams.

## Impact If Built
The storage system was never the constraint — a person reading a document is. Calibrated per-attribute confidence is the mechanism that makes extraction usable below perfect accuracy, and its absence is why pilots fail.
