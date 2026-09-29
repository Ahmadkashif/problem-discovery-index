# Product Recognition and Catalogue Enrichment

**Niche:** [[niches/recommerce-platforms/catalogue-attribute-automation/profile|Catalogue & Attribute Automation]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail product recognition, attribute extraction and catalogue enrichment are mature capabilities with vendors, and recommerce listing is a person at a keyboard.
**Tags:** #cnns #object-detection #large-language-models #word-embeddings #evaluation-metrics #transfer-learning #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn a photograph into a complete, findable listing without a person typing — and whoever does that takes the cost out, because listing labour is a fixed cost on every item regardless of what it is worth.

## The Problem
Recognising a product from an image, extracting its attributes, matching it to a catalogue entry and enriching the listing is a capability retail has built and productised, with vendors serving large merchants and open models available to anybody. Generating a title and description from structured attributes is now trivial. The recommerce operation has an image, needs a listing, and assembles it by hand.

## What Already Exists
Product recognition and fine-grained classification from images; attribute extraction for apparel and accessories; catalogue matching against reference product databases; text generation from structured attributes; image quality assessment and automatic cropping; and enrichment services filling attributes from reference data.

## The Customization Gap
The adaptation is to used, damaged, altered and unlisted items. It requires: (1) recognition robust to wear, alteration and unusual photography, since retail models are trained on catalogue images of new products and the input here is a worn item on a rack — this domain shift is the substantive technical work and is why off-the-shelf recognition underperforms; (2) condition observed alongside identity, since the same pass through the image should produce both and treating them as separate systems doubles the cost; (3) matching to a reference catalogue that may not contain the item, because much of this inventory is old, discontinued or was never in a structured catalogue, so graceful degradation to attribute-only listing is required; (4) confidence calibrated well enough to drive the exception routing, since the whole labour saving depends on trusting the high-confidence path; and (5) attributes chosen for findability rather than for completeness, since the filters buyers use are a small subset and filling everything is wasted effort.

## Target Customer
Catalogue operations, recommerce platforms, and the retail product recognition vendors for whom used goods are an adjacent and harder market.

## Impact If Solved
The capability is mature on new-product catalogue images and the input here is a worn item on a rack, which is the domain shift that makes off-the-shelf recognition underperform. Extracting condition in the same pass as identity halves the cost of both.
