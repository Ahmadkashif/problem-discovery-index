# The Pricing Data Sitting in the PDFs

**Niche:** [[niches/creator-talent-agencies/deal-pricing-and-market-data/profile|Deal Pricing & Market Data]]
**Industry:** [[industries/creator-talent-agencies|Creator Talent Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The agency has the market's pricing record and reads it one contract at a time when someone remembers to look.
**Tags:** #large-language-models #gradient-boosting #data-integration #evaluation-metrics #confidence-intervals #revenue-impact #descriptive-statistics #bert
**Contested on:** Every serious competitor in this niche is fighting to turn a year of signed deals into a pricing model rather than a folder of PDFs — and whoever structures it negotiates from evidence while everyone else negotiates from memory.

## The Problem
Every deal the agency signs contains the information the industry most lacks: what this brand paid, for which deliverables, on which platforms, with what usage rights, exclusivity and payment terms, for a creator of this size in this category. Multiply by hundreds of deals a year. The information is in prose inside signed documents, is not extracted, and is therefore available only to whoever negotiated it and only while they remember it.

## Why Nobody Has Built This
Contracts are legal artefacts, so they are stored rather than parsed — a document filed for its enforceability is not filed for its content. Extraction from prose was hard until recently. Managers treat pricing knowledge as personal expertise, which is also their career capital. And the agency has never framed itself as holding a dataset.

## What to Build
Extract the terms and build the model. Extract structured terms from every signed deal — deliverables, platforms, usage window, exclusivity, whitelisting, approval rounds, payment terms, fee — which is the core and turns a document store into a dataset. Model price against creator attributes, deliverable type and brand category, so a manager enters a negotiation with a distribution rather than a recollection. Price the components separately, since usage rights and exclusivity are routinely given away because they are not priced as line items. Track which rights brands actually exercise, because the difference between what is bought and what is used is the clearest evidence about what each term is worth. Record brand behaviour — negotiating patterns, payment timeliness, approval burden — as that is institutional knowledge currently held individually. Benchmark across the roster so junior managers price like senior ones, which is the fastest capability improvement available. Surface the model at the moment of negotiation rather than in a report, as that is when it is used. Feed it into the industry-level question of what creator work is worth, which is a product in itself. Retain the knowledge when a manager leaves, since that is the structural reason to do this at all. And measure realised prices against the model to see who is underpricing and where.

## Target Customer
Commercial and agency leadership, managers negotiating from memory, creators being represented, and deal management vendors.

## Impact If Built
A document filed for its enforceability is not filed for its content, so the pricing record stays unread. Extracting structured terms turns hundreds of contracts into the market's only pricing model and keeps it when the manager leaves.
