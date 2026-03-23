# Estimate Comparison and Dispute Resolution Engine

**Niche:** [[niches/public-adjusters/supplement-tracking/profile|Carrier Negotiation & Supplement Tracking]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automates the line-by-line comparison between a PA's Xactimate estimate and a carrier's counter-estimate, identifying every discrepancy and generating item-level dispute justifications.
**Tags:** #llm #text-generation #nlp #automation #revenue-impact

## The Problem
When a carrier responds to a PA's estimate with their own version, the PA must manually compare the two estimates — often 100-300 line items each — to identify every difference: items the carrier removed, items they repriced, items they added that weren't in the PA's estimate, and quantity differences. This comparison takes 2-4 hours per claim. The PA then writes a narrative justification for each disputed item ("Item 47: Carrier removed 'paint 2 coats' for master bedroom. This item is required because water damage necessitated drywall replacement, and new drywall requires 2 coats of paint per manufacturer specifications. See photo DSC_0147 showing replaced drywall."). Writing these justifications takes another 2-4 hours.

## Why Nobody Has Built This
Xactimate estimates are stored in proprietary ESX format. Comparing two ESX files requires parsing the format, normalizing line items across different category selections (the PA and carrier may have used different Xactimate selectors for the same work), and matching items that are semantically equivalent but coded differently. The justification generation requires understanding both Xactimate line item semantics and insurance claims argument patterns — which items are worth fighting for, what evidence carriers accept, and how to frame the argument.

## What to Build
An estimate comparison engine that imports two ESX files (PA estimate and carrier estimate), performs automated line-by-line matching, categorizes each item as agreed/disputed/missing/added, and for each disputed item, generates a draft justification narrative based on the dispute type (removed item that should be included, repriced item below market, quantity reduction without basis). Outputs a formatted supplement letter ready for submission, with photo references and industry standard citations.

## Target Customer
PAs handling 30+ active claims with ongoing carrier negotiations, spending 4-8 hours per claim on estimate comparison and supplement writing.

## Impact If Built
Reduces supplement preparation time by 60-70% (from 6 hours to 2 hours per claim). Improves supplement quality by ensuring no disputed items are overlooked — currently PAs miss 5-10% of discrepancies in manual comparison. Increases settlement recovery by 8-12% on supplemented claims through more comprehensive dispute coverage.
