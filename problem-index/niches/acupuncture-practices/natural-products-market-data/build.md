# Taxonomy Maintenance as a Learned System, Not a Backlog

**Niche:** [[niches/acupuncture-practices/natural-products-market-data/profile|Natural Products Channel Data Vendors]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The ingredient and claims taxonomy is the entire product, it is maintained by hand at a rate slower than new SKUs arrive, and none of the hundreds of thousands of past classification decisions are used to make the next one easier.
**Tags:** #bert #transformers #transfer-learning #contrastive-learning #word-embeddings #cnns #object-detection #random-forests #evaluation-metrics #tacit-knowledge-ml #automation #revenue-impact

## The Problem
Everything the vendor sells rests on one operation: taking a new product and placing it correctly in a taxonomy of ingredients, functional claims, certifications, form factors, and category hierarchies. A misplaced SKU corrupts every share number, trend line, and forecast that touches its category, and the client who notices is usually the brand whose share it distorted. The work is done by analysts reading product labels, ingredient panels, and marketing copy, and it is genuinely hard — herbal products carry ingredient names in Latin, pinyin, and English on the same panel, proprietary blends obscure composition, and the difference between two functional claim categories often turns on a single qualifier. New SKUs arrive continuously and the backlog is permanent. Meanwhile hundreds of thousands of prior classification decisions sit in the database as final values, with no record of what the analyst was looking at when they made the call.

## Why Nobody Has Built This
The taxonomy is the moat, which makes it the thing least likely to be handed to an automated process. There is also a real technical obstacle: the decisions are recorded as outcomes rather than as labeled examples. The database says this SKU is in that category; it does not retain the label image, the ingredient string as printed, the marketing copy, or the analyst's reasoning, so the natural training set was thrown away as it was created. And the failure mode is asymmetric — a classifier that is right ninety-five percent of the time introduces systematic error into exactly the categories clients scrutinize most, which is worse commercially than a backlog.

## What to Build
A classification engine that treats the taxonomy as a living model rather than a lookup table. It ingests the full product artifact — label imagery, ingredient panel text, marketing copy, distributor data — and proposes placement with calibrated confidence, routing only genuinely uncertain items to analysts. The design point is the calibration, not the accuracy: the system must be trustworthy about what it does not know, so high-confidence placements flow through and the analyst's time concentrates where judgment is actually required. Every analyst decision from that point forward is captured with its full input context, which builds the training set that was previously discarded. A botanical entity layer resolves Latin, pinyin, common, and proprietary names to single concepts, so the same herb under four naming conventions stops fragmenting a category. And a standing consistency check runs over the existing corpus, surfacing SKUs whose historical placement disagrees with the model — which is how twenty years of accumulated drift becomes visible for the first time.

## Target Customer
VPs of insights and heads of data operations at natural channel data vendors running 50-300 analysts, and the internal category analytics teams at large supplement manufacturers and retailers who maintain parallel taxonomies over the same products.

## Impact If Built
Removes the constraint that caps coverage: the vendor can carry more SKUs, more attributes, and faster refresh without proportional headcount, which directly expands what is saleable. More importantly it converts the taxonomy from a static asset that decays into one that improves — every analyst judgment now trains the system rather than evaporating. Retrospective consistency checking also addresses the quiet liability in the business, which is that nobody currently knows how much historical misclassification is embedded in the trend data clients have been buying.
