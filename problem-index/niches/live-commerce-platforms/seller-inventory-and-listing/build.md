# Stock That Exists Only in Boxes

**Niche:** [[niches/live-commerce-platforms/seller-inventory-and-listing/profile|Seller Inventory & Listing]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Live sellers buy pallets and collections and sell them by holding them up, so the platform has no idea what inventory exists on its own marketplace.
**Tags:** #object-detection #transformers #large-language-models #semantic-segmentation #automation #workflow-orchestration #evaluation-metrics #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to get a seller's stock into the platform without the seller typing it in — and whoever removes that step decides how much inventory the format can carry.

## The Problem
A seller has nine hundred items in boxes in a garage. The platform knows about none of them until each one is held up to a camera and sold. That means the discovery system cannot match a viewer's declared want to available supply, the seller cannot plan a show, no item can be priced against comparables, and anything that does not sell goes back in the box and is effectively lost. The platform is operating a marketplace while blind to its own inventory, and the reason is that entering nine hundred items by hand is a week of work nobody will do.

## Why Nobody Has Built This
The format's appeal to sellers is precisely that it skips listing — asking them to list first removes the reason they chose live selling, which makes every conventional listing tool a non-starter here. Automatic item capture needed image understanding and description generation that was not good enough until recently. Platforms optimise for streams started rather than inventory known. And the cost of blindness is diffuse, showing up as poor matching and low relist rates rather than as a complaint.

## What to Build
Capture inventory as a by-product of handling, never as a separate task. Let a seller photograph or film a box of items in one pass and detect, segment and enumerate the individual items from it, which is the core capability and is what makes nine hundred items feasible in an hour rather than a week. Generate a title, category and attributes from the image, and refine them from the host's own words when the item is later shown on camera. Suggest a price from comparable recent sales on the platform, which sellers currently do from memory and get wrong in both directions. Ingest the show itself as an inventory event, so anything held up is captured whether or not it was pre-entered — this is what makes the system robust to sellers who will never pre-list. Keep unsold items in an available pool rather than letting them disappear, which is the fix note's problem and is where the recurring revenue is. Expose that pool to discovery so a viewer's want can be matched to stock a seller has not shown yet, which connects this niche to the largest one. Let sellers plan a show from the pool, since sequencing and pacing are currently guesswork. Track cost basis where the seller knows it, so margin is visible per item. And keep the whole flow operable one-handed on a phone in a garage, because that is where the work happens.

## Target Customer
Live sellers with unstructured inventory, live commerce platforms blind to their own supply, and resale operations sourcing in bulk.

## Impact If Built
The platform runs a marketplace while blind to its own inventory because listing nine hundred items by hand is a week nobody will spend. Capturing a box in one pass and ingesting the show itself as an inventory event removes the step rather than speeding it up.
