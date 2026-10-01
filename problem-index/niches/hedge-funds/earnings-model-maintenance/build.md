# Updating the Analyst's Own Template, Not a Vendor's

**Niche:** [[niches/hedge-funds/earnings-model-maintenance/profile|Earnings Model Maintenance]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vendors deliver beautifully standardised models that analysts do not use, because the analyst's view lives in their own template.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #feature-engineering #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to get a reported quarter into the analyst's own model template, correctly mapped and source-linked, before the conference call starts — and whoever does it in the analyst's template rather than a vendor's takes the account.

## The Problem
An analyst's model encodes their view: segments split the way they think about the business, KPIs the company reports only in the presentation, adjustments they make to reported figures. Vendor models are consistent across companies, which is their value and the reason analysts copy numbers out of them rather than adopting them.

## Why Nobody Has Built This
Vendors scale by standardising; building to thousands of individual templates looks like services work.

## What to Build
An extraction and mapping engine that learns each template's line items from its own history — prior quarters show which source figure fed each cell — populates actuals and guidance within minutes of release, links every cell to its source, and flags low-confidence or new items for the analyst.

## Target Customer
Fundamental long/short and event-driven funds; directors of research standardising across pods.

## Impact If Built
The transcription half of earnings season is removed without asking analysts to give up their models.
