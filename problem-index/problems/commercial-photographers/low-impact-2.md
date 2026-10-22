# Sample-to-SKU Tracking for Mid-Sized Ecommerce Studios

**Industry:** [[commercial-photographers|Commercial Photographers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** An independent studio shooting a few hundred SKUs a day for several brands tracks physical samples, shot lists and each retailer's image specification in spreadsheets, because the platform built for this is priced for the retailers' own studios.
**Tags:** #object-detection #large-language-models #feature-engineering #data-integration #workflow-orchestration #automation #quick-win

## The Problem
A mid-sized ecommerce studio has six sets and works for fifteen brands. Every morning, boxes of samples arrive: shoes in three colourways, a rack of dresses, a carton of skincare with two new sizes. Each sample has to be checked in against the brand's style list, matched to its SKU, steamed or prepped, assigned to a set and a shot list (front, back, detail, on-model, flat lay), shot, checked out and returned or held. Each brand wants its images delivered to its own specification, and often to several retailer specifications as well: crops, margins, background values, file names, shadow treatment and colour space all differ by retailer.

The tracking lives in a spreadsheet per client and a whiteboard. Samples go missing between sets. A colourway gets shot twice and another never, and the gap surfaces only when the brand's listing deadline arrives. File names are typed by hand, so the retailer's ingest rejects a batch over a misplaced underscore.

## What Already Exists
Creative Force covers sample management, production planning, capture integration and delivery, and is sold to retailers' and big brands' in-house studios, listed from ~$2,900 a month. Generic work-management tools (Airtable, Monday.com, Asana) and barcode inventory apps cover parts of the flow. Product information management systems hold the brand's SKU data, and product-content syndication services map assets to retailer specifications. That service layer is analysed under [[ecommerce-sellers|E-Commerce Sellers]].

## The Customisation Gap
An independent multi-client studio needs: sample check-in by scanning the brand's barcode or photographing the label, matched to the style list automatically; shot lists generated from the SKU's category and the brand's guide; per-client and per-retailer delivery profiles that rename, crop and validate files before they leave; colourway and size coverage checks against the brand's launch list; and sample custody records the studio can show when a brand claims a sample was lost. It also needs pricing per seat or per SKU that a studio with $1–5M in revenue can carry. The generic tools lack the domain objects (sample, colourway, shot list, retailer spec). The enterprise platform has them but is priced and scoped for one brand's in-house operation.

## Impact If Solved
For a six-set studio, removing manual check-in, renaming and spec checking plausibly saves one to two coordinator roles and cuts reshoots from missed colourways and rejected batches. Those reshoots are the main way such a studio loses margin on a fixed per-SKU price.
