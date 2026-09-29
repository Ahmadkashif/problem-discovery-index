# Stock Figures With a Confidence Attached

**Niche:** [[niches/retail-pos-platforms/multichannel-inventory-accuracy/profile|Multi-Channel Inventory Accuracy]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every channel integration publishes a stock quantity as a fact, the quantity is frequently wrong, and no product in the category has ever attached an estimate of how wrong it is likely to be.
**Tags:** #bayesian-inference #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #hypothesis-testing #automation #revenue-impact
**Contested on:** Every serious competitor in channel integration is fighting to make the number the system reports match what is physically on the shelf — and whoever closes the gap between system stock and counted stock takes the account.

## The Problem
The system says three. The shelf has two. A marketplace order arrives for the third, is accepted, cannot be fulfilled, and the merchant takes a cancellation and a metric penalty that in some marketplaces threatens their selling privileges. The merchant's response is to hold a safety buffer — publish two when the system says three — applied globally, which means they are refusing sales on the many items whose count is accurate to protect against the few that are not. Both the oversell and the refused sale are consequences of publishing a point estimate for a quantity that is uncertain.

## Why Nobody Has Built This
Inventory has always been modelled as an integer, and attaching uncertainty to it is a conceptual departure that no product in the category has made. Estimating the uncertainty requires knowing how a given item at a given store drifts, which requires count history joined to item characteristics — data that exists across a platform's merchant base and has never been assembled for this purpose. And the commercial framing is awkward: telling a merchant that their inventory number is probabilistic sounds like an admission that the product does not work, when it is in fact the only honest description of a physical count that was last verified weeks ago.

## What to Build
A stock estimate as a distribution rather than an integer. Expected physical quantity and its uncertainty are derived from the last verified count, the movement since, and a drift model estimated per item class and per store from the platform's cross-merchant count history — high-velocity, high-theft-exposure, small-format items drift fast, and slow-moving locked-case items barely at all. Channel publication then follows from the uncertainty and from the channel's own penalty structure: a marketplace with a severe oversell penalty is published conservatively on uncertain items and fully on certain ones, while the merchant's own website can be published at the expectation. Counting priority follows the same estimate, which connects this directly to the targeted cycle counting in the associate niche. And the single most valuable output is the simplest: tell the merchant which items are most likely to be wrong right now, which is a list nobody currently has.

## Target Customer
POS platforms and channel integration vendors, and directly the multichannel independent retailers absorbing oversells and refused sales.

## Impact If Built
Per-item confidence replaces a global buffer with a targeted one, which recovers the sales currently refused on accurate items while reducing oversells on inaccurate ones — both sides of a trade merchants are currently forced to make bluntly. It also makes counting effort allocable by expected error rather than by rotation, which compounds with every other accuracy improvement in the industry.
