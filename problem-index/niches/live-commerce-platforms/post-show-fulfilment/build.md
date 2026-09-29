# Three Hundred Orders and a Kitchen Table

**Niche:** [[niches/live-commerce-platforms/post-show-fulfilment/profile|Post-Show Fulfilment]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A three-hour show produces hundreds of small orders of uncatalogued items and the host packs them by hand afterwards, which is the real limit on how often anyone can go live.
**Tags:** #workflow-orchestration #automation #dynamic-programming #evaluation-metrics #worker-facing #revenue-impact #quick-win #convex-optimization
**Contested on:** Every serious competitor in this niche is fighting to get a show's worth of one-off orders packed, combined and shipped without the host doing it by hand at midnight — and whoever does that determines how many shows a seller can run.

## The Problem
The show ends at eleven. There are two hundred and eighty orders from a hundred and forty buyers, most of whom bought several things at different points in the night. Nothing was catalogued — the items were held up to a camera and sold. The host now has to work out who bought what, find each physical object among the piles they were pulling from, group each buyer's items together, pack, weigh, buy postage and label. It takes until three in the morning. It is the reason they stream twice a week instead of five times, and no part of it is software's problem as far as any platform is concerned.

## Why Nobody Has Built This
Platforms measure themselves on gross merchandise value and treat fulfilment as the seller's business. The items are unique and uncatalogued, so conventional inventory and pick systems have nothing to operate on — this is the structural obstacle and it is why the obvious tools do not apply. Ecommerce fulfilment software assumes a catalogue and a warehouse. And the workload lands on one person at midnight, which is invisible to everyone.

## What to Build
Build fulfilment around the show rather than around a catalogue. Combine every order from a buyer across the show — and across consecutive shows within a window — into one shipment automatically, which is the single largest saving in both labour and postage and is the thing every host does manually today. Sequence the pack list by where items physically were during the show, using the stream timeline as the location index, since the order things were sold in is the only map of the piles that exists. Capture the item at the moment of sale with a frame from the stream and the host's spoken description, which gives every order a picture without anyone cataloguing anything — this is what makes the rest possible. Estimate weight and dimensions from the captured item and the category, so postage is bought in batch rather than per parcel at a scale. Buy and print labels in one batch run with rates negotiated across the platform's whole seller base, which is a purchasing advantage individual sellers cannot get. Produce a packing view designed for one person working alone at speed, rather than a warehouse pick interface. Handle the buyer who is still bidding — hold their parcel open for the configured window and tell them, which converts into further sales rather than reading as a delay. Track what has been packed and what has not, since the most common failure is simply losing track. And report fulfilment hours per show, because it is the number that decides the seller's streaming frequency and nobody measures it.

## Target Customer
Live sellers running their own fulfilment, live commerce platforms whose supply is limited by seller capacity, and the fulfilment services serving them.

## Impact If Built
Uncatalogued unique items are why conventional pick systems have nothing to operate on, and a frame plus the host's description at the moment of sale creates the record without a cataloguing step. Combining a buyer's wins across the show is the largest single saving in both labour and postage.
