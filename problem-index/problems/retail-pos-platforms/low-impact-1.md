# Specialty Product Catalogue Enrichment

**Industry:** [[retail-pos-platforms|Retail POS Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** UPC lookup services solve catalogue entry for packaged goods and do almost nothing for the specialty categories where independents actually compete, so every merchant types the same attributes for the same products the vendor sells to two thousand other stores.
**Tags:** #bert #word-embeddings #cnns #large-language-models #k-nearest-neighbors #transfer-learning #evaluation-metrics

## The Problem
Adding a product to a retail system means recording what it is: name, category, brand, price, cost, and the attributes customers search and filter by. For packaged goods with a UPC, this is a lookup and largely solved.

Specialty retail is where independents survive, and specialty goods break the lookup. Apparel needs size, colour, fit, material, season and style. Outdoor equipment needs technical specifications. Jewellery, books, toys, pet supplies, cycling, home goods — each has an attribute vocabulary that no general product database carries. Vendor catalogues arrive as spreadsheets or PDFs with inconsistent columns and account-specific style codes.

So merchants type. A new season means hundreds of items entered by hand, usually by the owner, usually in the evening. The same items are being entered, at the same time, by every other retailer carrying that vendor's line.

Poor catalogue data then degrades everything downstream: the website's filters, the marketplace listing, the reorder decision, and any analysis that requires knowing what an item actually is.

## What Already Exists
UPC and GTIN databases cover packaged goods well. Vendor EDI catalogues exist for larger suppliers. Shopify and its peers have product taxonomies and attribute schemas. Image recognition for retail products is mature. Marketplace listing tools handle attribute mapping to channel requirements. Some verticals have industry catalogue standards.

## The Customisation Gap
The gap is the long tail and the attribute schema. General taxonomies are shallow where specialty retail is deep — a category tree that stops at "footwear" is useless to a running shop that needs drop, stack height and pronation support.

The unexploited asset is the platform's own aggregate catalogue. The same vendor's item has been entered by hundreds of merchants, each contributing a partial description. Reconciling those into a canonical product record with a rich attribute set is entity resolution over the merchant base, and it means the next merchant to carry that line types nothing at all.

Vendor document ingestion is the second half. A season's line sheet arrives as a PDF or spreadsheet, and extracting it into products with attributes is a well-shaped task on documents merchants already receive and currently retype.

Attribute schemas per specialty vertical are the third piece — they need to be built, and they can be induced from what merchants in each vertical actually record rather than authored from scratch.

## Impact If Solved
Catalogue entry is the largest recurring administrative burden in specialty retail and the quality ceiling on every downstream capability, from website search to markdown analytics. It is also pure duplication — the same work performed independently by every merchant carrying the same line.
