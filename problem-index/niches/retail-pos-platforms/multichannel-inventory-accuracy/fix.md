# The Safety Buffer Set Globally by a Guess

**Niche:** [[niches/retail-pos-platforms/multichannel-inventory-accuracy/profile|Multi-Channel Inventory Accuracy]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Merchants protect against overselling by holding back a fixed number of units on every item across every channel, chosen by feel, and nobody has ever computed what that buffer costs in refused sales.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in channel integration is fighting to make the number the system reports match what is physically on the shelf — and whoever closes the gap between system stock and counted stock takes the account.

## The Problem
A merchant was suspended from a marketplace once for oversells and now holds back two units on everything. On fast-moving items with genuine uncertainty this is sensible. On the long tail of items where the count is reliable and total stock is three, holding back two means two-thirds of the inventory is invisible to the channel — which for a merchant whose online sales are mostly long tail is a large and entirely self-inflicted revenue loss. Nobody has told them, because nobody computes it.

## Why It's Still Broken
A global buffer is the only control the products offer, and a per-item buffer would require a per-item basis that nothing produces. The cost is also invisible by construction: refused sales do not appear anywhere, because an item that was not published never generated an order to lose. So the merchant sees the oversells they avoided and never sees the sales they forwent, which is a reliable way to end up with a buffer that is far too conservative.

## What a Fix Looks Like
Measure the cost and set the buffer per item. The foregone sales are estimable: for items where held-back stock existed and demand can be estimated from the item's own velocity and the channel's traffic, the expected orders that were not available is computable, and reporting it as an annual number is usually enough on its own to change the merchant's behaviour. Then set buffers per item from the confidence estimate and the channel's penalty — heavy on the uncertain and high-penalty combinations, zero on the reliable ones. Where the merchant prefers a simple policy, offer two or three tiers rather than one number. Track oversells and refused sales together as a pair, because the merchant is making a trade-off and should be able to see both sides of it, which today they cannot.

## Who Feels the Pain
Merchants losing long-tail online sales to a precaution they cannot evaluate; customers who could not buy an item that was sitting in the store; and the platform, whose channel product is quietly suppressing a share of its merchants' inventory.

## Impact If Fixed
Computing foregone sales converts an invisible cost into a number, and per-item buffers typically recover a substantial share of it without raising oversells — because the buffer was protecting against uncertainty that was concentrated in a minority of items. Both figures come from data the platform already holds.
