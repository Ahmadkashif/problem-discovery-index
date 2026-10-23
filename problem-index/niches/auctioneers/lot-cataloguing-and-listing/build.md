# A House-Style Cataloguing Model From the Firm's Own Archive

**Niche:** [[niches/auctioneers/lot-cataloguing-and-listing/profile|Lot Cataloguing & Online Listing]]
**Industry:** [[industries/auctioneers|Auctioneers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every auction firm already owns thousands of photo-and-description pairs written in its own style, and none uses them to draft the next catalogue.
**Tags:** #large-language-models #transformers #cnns #transfer-learning #object-detection #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a photo table into a published, searchable catalogue, and whoever gets a sale listed in the fewest cataloguer-hours with the fewest "not as described" disputes takes the account.

## The Problem
Generic photo-to-listing tools write like retail sellers. Auction buyers expect a firm's house conventions: maker first, period and material, measured hedged condition language, and terms such as "as found" or "not tested". Cataloguers rewrite generic drafts, so the time saving shrinks.

## Why Nobody Has Built This
Platforms build for all their auctioneers at once; clerking vendors have not invested in models; and small firms do not know their archive is training data.

## What to Build
Fine-tune a vision-language model per firm on its past catalogues: photos in, lot title, description, condition and category out, in house style and controlled vocabulary, with lotting suggestions from multi-object photos and a confidence flag that routes uncertain lots to a senior cataloguer. Track edit distance per lot to show the saving.

## Target Customer
Auction firms cataloguing several thousand lots a year (estimate) and the clerking vendors that could offer this as a feature.

## Impact If Built
Drafts cataloguers accept with light edits, cutting description time per lot by half or more (estimate), and consistent language that reduces disputes.
