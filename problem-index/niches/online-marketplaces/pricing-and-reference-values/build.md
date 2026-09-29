# No Reference Price Where It Matters Most

**Niche:** [[niches/online-marketplaces/pricing-and-reference-values/profile|Pricing & Reference Values]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A seller with a one-of-a-kind item has no reference price and guesses, and the marketplace holding every comparable sale it ever processed offers them a range drawn from listings nobody bought.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #k-nearest-neighbors #evaluation-metrics #revenue-impact #hypothesis-testing #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a seller what their one-of-a-kind item is actually worth and a buyer whether a price is fair — and whoever does that takes the transaction, because without a reference both sides are guessing and most guesses end in no sale.

## The Problem
A seller lists a vintage jacket. There is no identical item and never will be. They look at what similar jackets are listed for, pick a number in the middle, and wait. The listings they anchored on are mostly unsold, because unsold listings persist and sold ones disappear, so the visible market is systematically the overpriced half of it. Their jacket does not sell. They reduce it twice, too late and too little, and it expires. The marketplace processed four hundred comparable sales in the same period and used none of that to help.

## Why Nobody Has Built This
Valuing a heterogeneous item requires modelling its attributes, which requires those attributes to be structured, which requires the listing structuring nobody built. Suggesting a price is a commitment a platform is reluctant to make, particularly a lower one. The sold-price data is a genuine platform asset and exposing it feels like giving something away, even though third parties scrape and resell it. And the seller who mispriced attributes the failure to demand rather than to the number.

## What to Build
Build the valuation from completed sales. Estimate value from attributes, images, condition, seller history and season, trained on completed sales rather than on active listings, which is a well-posed problem with abundant labels and is the entire build — and the resulting estimate is better than anything a seller can construct. Express it as a price-to-speed curve rather than as a number: at this price it sells in a week, at that price in three months, at that price probably never — which is the seller's actual decision and is not a decision a single suggested price supports. Report confidence, since some items are well-comparable and some are genuinely singular, and a confident estimate on an unusual item is worse than an honest wide interval. Show comparable completed sales with their attributes, so the seller can see the reasoning and disagree with it informed. Guide repricing as a listing ages, since most sellers reduce too late and by too little and a prompt at the right moment converts an expiry into a sale. Give the buyer a fairness signal, which converts the same model into a demand-side product and reduces the hesitation that kills unique-item purchases. Handle the reserve and negotiation cases, since many of these transactions are negotiated and the model should inform the floor rather than only the ask. And publish aggregate price indices per category, which is genuinely useful to the market and establishes the platform as the reference rather than the third-party scrapers.

## Target Customer
Sellers of unique inventory, buyers hesitating over an unanchored price, and the operators whose sell-through depends on both.

## Impact If Built
The visible market is systematically the unsold half, so a seller anchoring on listings anchors on optimism. A price-to-speed curve from completed sales is the seller's actual decision, and the same model gives the buyer the fairness signal that unblocks the purchase.
