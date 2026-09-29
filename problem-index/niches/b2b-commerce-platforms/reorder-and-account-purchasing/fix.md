# The Part That Was Discontinued

**Niche:** [[niches/b2b-commerce-platforms/reorder-and-account-purchasing/profile|Reorder & Account Purchasing]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A buyer reorders a part they have bought for years, discovers at the cart that it is discontinued, is offered nothing in its place, and calls the rep — who knows the replacement immediately.
**Tags:** #k-nearest-neighbors #evaluation-metrics #data-integration #automation #confidence-intervals #revenue-impact #quick-win #graph-theory
**Contested on:** Every serious competitor in this sub-niche is fighting to make a repeat order faster and more certain than phoning the rep — and whoever does that takes the volume, because the buyer knows what they want and is choosing between channels rather than between products.

## The Problem
A part is superseded by the manufacturer. The distributor's system knows: the item is flagged obsolete and a successor part exists in the same record. The storefront shows the item as unavailable. The buyer, who has ordered it for six years and does not track manufacturer supersessions, has no idea what to order instead. They call. The rep says the replacement number in four seconds. Everything the rep knew was in the data, the storefront's response to an obsolete item was to hide it, and the call the storefront exists to prevent was caused by the storefront.

## Why It's Still Broken
Availability was inherited from consumer commerce, where an out-of-stock item is simply unavailable and a supersession does not exist as a concept. Supersession and cross-reference data lives in the product information system and is not surfaced in the buying flow. Maintaining the relationships is catalogue work nobody prioritises. And the rep resolves it instantly, so the failure converts into a call rather than into a complaint.

## What a Fix Looks Like
Never show unavailable without an alternative. Surface the successor part wherever an item is obsolete, in the buyer's order history as well as on the product page, which uses data the distributor already holds and is the fix — the relationship exists and is not displayed. Notify buyers proactively when a part they regularly order is superseded, before their next order rather than during it, which is a service moment and prevents the call entirely. Maintain supersession and cross-reference relationships as a catalogue priority, since they are what makes a technical catalogue usable and are consistently under-maintained. Offer functional equivalents where no formal successor exists, from attribute matching, with the differences stated so the buyer can judge. Handle temporary stock-outs differently from permanent discontinuations, since the buyer's response to each is different and the storefront currently shows both as unavailable. Keep obsolete items visible with their history and their replacement rather than removing them, since the buyer searches by the number they know. Report how often a reorder hits an unavailable item with no alternative shown, which is a direct measure of calls the storefront is generating. And feed supersession relationships back from what reps actually recommend, since their knowledge is ahead of the catalogue.

## Who Feels the Pain
Buyers who cannot complete a routine order; reps interrupted for a four-second answer; and distributors whose storefront generates the calls it was built to prevent.

## Impact If Fixed
The successor relationship is in the data and is not displayed, and hiding the obsolete item is the response inherited from consumer commerce. Proactive notification before the next order prevents the call entirely rather than answering it.
