# A Two-Week Shop-Order Agent on vPIC and a Synthetic Fitment Catalog

**Niche:** [[niches/auto-parts-distributors/vin-fitment-order-matching/profile|VIN & Fitment Matching on Shop Orders]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engineer can show the whole matching loop in two weeks on public data: a shop's text or call transcript in, a VIN decoded through NHTSA's free API, a match against a synthetic ACES/PIES-style catalog, and a priced quote with branch stock out.
**Tags:** #large-language-models #transformers #seq2seq #k-nearest-neighbors #evaluation-metrics #automation #ai-agent #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a shop's call, text or e-catalog request into the one part that fits that VIN, and whoever has the lowest fitment-return rate on the shop orders it matches takes the account.

## The Problem
Vendors and distributors evaluating order-matching agents have no shared, honest demonstration of where VIN-based matching works and where it needs a human, and the real catalog data cannot be shared because the VCdb and suppliers' ACES files are licensed.

## Why Nobody Has Built This
Catalog vendors have no reason to publish a test set; distributors' data is licensed and confidential; and most agent demos use SKU-keyed purchase orders, which skip the fitment step entirely.

## What to Build
Week one: an LLM parser that turns texts and call transcripts ("'14 F-150 5.0, front pads and rotors, good ones, plus right caliper") into vehicle, job and part requests; VIN decoding through vPIC's DecodeVinValues endpoint; and a synthetic catalog of a few hundred applications that mimics ACES structure, including qualifiers vPIC cannot resolve (brake package, production split). Week two: matching with retrieval and rules, a clarifying-question step when candidates remain, pricing on a mock shop matrix, stock from mock branch and hub tables, and an evaluation set of ~200 labelled requests scored on match accuracy and a simulated fitment-return rate. The demo states plainly that production needs the licensed catalog.

## Target Customer
Engineers proving the concept to a chain, programme group or business-system vendor; vendors needing an evaluation harness.

## Impact If Built
A credible two-week demo can shortcut a ~3–6 month vendor evaluation (estimate), and the clarifying-question step alone targets the ~10–30% of lookups that return several candidates (estimate).
