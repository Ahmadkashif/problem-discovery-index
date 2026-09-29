# Every Item Is a Cold Start

**Niche:** [[niches/online-marketplaces/unique-item-discovery/profile|Unique Item Discovery]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Recommendation learns from how items have been interacted with, and a one-of-a-kind item has no history and never will, so the system that drives most discovery is structurally blind to this inventory.
**Tags:** #k-nearest-neighbors #contrastive-learning #transfer-learning #evaluation-metrics #confidence-intervals #dimensionality-reduction #quick-win #gradient-boosting
**Contested on:** Every serious competitor in this sub-niche is fighting to put a one-of-a-kind item in front of a buyer who could not have named it — and whoever does that takes the market, because the competitor is the buyer giving up and going somewhere generic.

## The Problem
Behavioural recommendation works by observing that people who liked this also liked that. A unique item sells once and disappears, so it accumulates a handful of views and no purchase history, and by the time it has any signal it is gone. The recommender therefore cannot place it, defaults to popular inventory, and the marketplace's differentiated supply is excluded from the surface that drives most discovery. This is not a tuning problem; it is the collaborative approach being structurally wrong for the inventory, and it applies to every item in this category permanently rather than for a warm-up period.

## Why It's Still Broken
Collaborative methods work extremely well on repeat inventory and are what recommendation teams know. The cold start is framed as a temporary condition to be bridged, which is true for a product and false for a unique item. Content-based approaches were historically weaker and that comparison has not been revisited since multimodal representation became good. And the failure is silent, since the recommender always returns something.

## What a Fix Looks Like
Recommend from content, and transfer the behaviour. Make content-based similarity the primary mechanism for unique inventory rather than a cold-start fallback, since the cold start is permanent here and the fallback is the correct main path — reframing it that way is the fix. Transfer behavioural signal through the representation, so that what buyers did with similar items informs a new item that has no history of its own, which is how a collaborative signal can be used on inventory that cannot accumulate one. Recommend at the seller and style level as well as the item level, since a seller's other work and a style cluster do have history where an individual item does not. Use the session rather than the profile, because these purchases are frequently one-off and a long-run taste profile is thin where a session trajectory is rich. Measure recommendation coverage over unique inventory explicitly, since the aggregate metrics are dominated by repeat items and hide that this inventory is never recommended. Evaluate on discovery outcomes rather than click-through, since a good recommendation here surfaces something the buyer did not know existed and a click-through metric rewards the familiar. Handle the disappearance gracefully, since an item that sells is gone and a recommender trained on it must not keep suggesting it. And test content-based against collaborative on this inventory specifically, because the comparison everyone remembers was run on different data with older models.

## Who Feels the Pain
Sellers of distinctive inventory excluded from the surface that drives discovery; buyers shown popular items on a marketplace they came to for the unusual; and operators whose differentiation is invisible in their own product.

## Impact If Fixed
The cold start is permanent for this inventory, which makes the content-based fallback the correct main path. Transferring behavioural signal through the representation is how collaborative knowledge reaches items that can never accumulate a history of their own.
