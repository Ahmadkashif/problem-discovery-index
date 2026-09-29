# Every Merchant Has a Different Word for the Same Category

**Niche:** [[niches/retail-pos-platforms/product-catalogue-enrichment/profile|Product Catalogue Enrichment]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every merchant invents their own category names as they go, so a platform holding hundreds of thousands of merchants cannot compare any two of them, and the merchant's own reporting degrades as the taxonomy drifts.
**Tags:** #bert #word-embeddings #k-means-clustering #evaluation-metrics #confidence-intervals #descriptive-statistics #automation #quick-win
**Contested on:** Every serious competitor in retail catalogue is fighting to populate a specialty item's attributes without the merchant typing them — and whoever holds attribute completeness highest at zero merchant effort takes the account.

## The Problem
One store files a product under "Tops", another under "Shirts", another under "Womens Apparel > Shirts and Blouses", and a fourth under the vendor's name because that is how they think about buying. Within a single store, categories accumulate over years as staff create new ones ad hoc, so the store's own reporting by category becomes unreliable and the owner stops trusting it. Across the platform, no comparison between any two merchants is possible at all, which is what blocks every cross-merchant capability the industry could otherwise offer.

## Why It's Still Broken
A free-text category field is the path of least resistance at product creation, and imposing a taxonomy at that moment slows the merchant down, which vendors have been unwilling to do. Retroactive cleanup is a project nobody has time for. And since the platform has never offered anything that required comparability, the cost of the drift has never been visible — the merchant experiences it as reporting that is vaguely unhelpful rather than as a specific defect.

## What a Fix Looks Like
Map to a canonical taxonomy without making the merchant adopt one. Each item is classified against a standard retail taxonomy automatically from its name, attributes, vendor and image, with the merchant's own category label preserved as their display name. The merchant continues to see "Tops" because that is what they call it, and the platform sees a canonical category underneath, which is what makes comparison and cross-merchant learning possible without asking anyone to change their habits. Surface the drift too: flag when a merchant has three categories that map to the same canonical node, which is usually a cleanup the owner would happily accept once it is pointed out and would never have found. Report to the merchant using canonical grouping where their own is incoherent, with the option to see it either way.

## Who Feels the Pain
Owners whose category reporting has quietly become meaningless; staff creating a new category because they could not find the right one; and the platform, whose entire cross-merchant capability is blocked by a free-text field.

## Impact If Fixed
Canonical mapping under a merchant's own labels is invisible to the merchant and unlocks everything that requires comparability — sell-through curves, benchmarking, markdown modelling and category analytics. The drift detection is a small, welcome cleanup, and the whole thing requires no change to how any merchant works, which is why it is the right way to solve a taxonomy problem in a market that will not adopt a taxonomy.
