# Paper Batch Records and Manual Ingredient Traceability

**Niche:** [[niches/food-manufacturing/artisan-and-craft-food-producers/profile|Artisan & Craft Food Producers]]
**Industry:** [[industries/food-manufacturing|Food Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** When FDA or a retailer asks "which ingredient lots went into the product batch that generated this customer complaint?", artisan producers must dig through paper batch records, handwritten ingredient logs, and supplier invoices to reconstruct traceability — a process that takes hours or days and may produce incomplete results.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
FDA FSMA requires food manufacturers to maintain records that enable traceability — linking each finished product lot to the ingredient lots that went into it, and linking each ingredient lot to the supplier and receiving date. For a recall, the producer must identify all affected finished products within 24 hours. Artisan producers track this on paper: the batch record notes which ingredients were used, but the ingredient lot numbers are recorded inconsistently (sometimes on the batch record, sometimes on the receiving log, sometimes not at all). When a traceability exercise is required — mock recall for HACCP verification, actual recall, or customer complaint investigation — the producer spends hours or days cross-referencing paper records to reconstruct the traceability chain.

## Why It's Still Broken
Paper batch records persist because they're the simplest form of documentation — the producer writes down what they did as they do it. Digital alternatives require data entry during production, which feels burdensome in a small kitchen where the production team is 2-4 people working simultaneously. Previous attempts to digitize (generic spreadsheets, Google Forms) failed because they required too many steps during the production flow. The traceability gap remains because the consequences (a recall investigation that can't trace products to ingredients) are rare enough that producers accept the risk rather than change their workflow.

## What a Fix Looks Like
A barcode-based ingredient tracing system: at receiving, scan the supplier's lot barcode on each ingredient delivery (or manually enter if no barcode). At production, scan or select each ingredient being used — the lot number is captured automatically. The batch record is a digital log that the producer creates by scanning ingredients as they use them, with timestamps and quantities, rather than by writing notes after the fact. Traceability query: given any finished product lot, instantly display all ingredient lots that went into it; given any ingredient lot, instantly display all finished products that contain it. Mock recall response time drops from hours to minutes.

## Who Feels the Pain
Founders who dread mock recall exercises because the paper record trail is incomplete, and who face FDA 483 observations citing inadequate traceability records during facility inspections.

## Impact If Fixed
Achieves FDA-compliant traceability with minimal workflow change — scanning is faster than writing lot numbers by hand. Reduces mock recall response time from 4-8 hours to under 15 minutes. Prevents the worst-case scenario: a real recall where the producer can't identify affected products and must recall everything (estimated cost $50,000-$500,000 for a small producer vs. $5,000-$50,000 for a targeted lot-level recall).
