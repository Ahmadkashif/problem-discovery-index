# Claim-to-Figure Consistency Checking

**Niche:** [[niches/drafting-services/patent-drawing-bureaus/profile|Patent Drawing Bureaus]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nobody checks automatically that every element in the claims appears in a figure with the numeral the specification uses, so examiners find the gaps.
**Tags:** #large-language-models #transformers #object-detection #cnns #compliance #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver figures that show every claimed feature and never draw a drawing objection, inside the filing deadline at a per-figure price, and whoever turns a law firm's sketches into compliant sheets fastest takes its docket.

## The Problem
A patent application is drafted in text by the attorney and in figures by the illustrator, often in parallel and under deadline. Amendments to claims and specification late in drafting are not always carried into the figures. The result is an objection that a claimed feature is not shown, or that numerals in the figures and the specification disagree, and a response with replacement sheets that costs attorney and illustrator time.

## Why Nobody Has Built This
Patent software vendors work on text; illustration is a separate trade. Reading numerals and lead lines on figures reliably needed vision models that have only recently become good enough.

## What to Build
A checker that parses claims and specification for elements and reference numerals, reads every figure for numerals and what they point to, and reports claimed elements not shown, numerals used in one place and not the other, and duplicates, before filing.

## Target Customer
Patent prosecution teams at IP law firms and corporate IP departments; patent illustration bureaus selling a guarantee.

## Impact If Built
Fewer drawing objections and replacement-sheet cycles, and figures that match the application at filing.
