# Multi-Channel Inventory Reconciliation

**Industry:** [[retail-pos-platforms|Retail POS Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Channel sync is a competitive, mature product category and independent retailers still oversell online and hold phantom stock in the store, because syncing quantities is not the same as knowing what is actually on the shelf.
**Tags:** #bayesian-inference #gradient-boosting #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #data-integration

## The Problem
A retailer sells in the store, on its own site, and on one or more marketplaces. The inventory record must be right across all of them, in something close to real time, or the merchant either oversells — taking an order for something that is not there — or under-sells by holding back buffer stock that never gets offered.

Sync products exist and work at the level they operate: when a unit sells on one channel, decrement it everywhere. That is the easy half.

The hard half is that the recorded quantity is frequently wrong. Shrink, receiving errors, mis-scans, returns processed incorrectly, items moved between locations, damaged goods never written off. The system says three and the shelf has one. Sync propagates the wrong number faithfully to every channel.

Merchants respond with buffer stock — refusing to sell the last two units online — which is a permanent tax on availability applied because nobody trusts the count.

## What Already Exists
Channel management and sync tools are numerous and competent. Marketplace APIs support inventory updates. POS platforms handle multi-location inventory. Cycle counting features are standard. RFID is transformative where it is deployed and remains too expensive for most independents. Barcode scanning is universal.

## The Customisation Gap
Nobody models inventory record accuracy, which is the actual problem. The recorded quantity is an estimate with an error distribution that varies enormously by category, by price point, by store layout and by how long it has been since the item was counted. Treating it as a certainty is what produces both overselling and buffer stock.

A probabilistic view — this SKU's count is reliable, that one has not been verified in four months and its category has high shrink — changes the decision. High-confidence items can be sold to the last unit; low-confidence items get a buffer or a count triggered before the listing goes live.

That view also directs cycle counting, which is currently done alphabetically or by walking the store. Counting should be prioritised by expected error and by the cost of being wrong, which is computable from sales velocity, price and time since last verified.

The third gap is diagnosis. Discrepancies have causes — receiving errors, theft, mis-scans at the register — and each has a different remedy. Distinguishing them from the pattern of when and where discrepancies appear is straightforward analysis nobody performs.

## Impact If Solved
Overselling costs a marketplace account rating and a customer; buffer stock costs availability on every unit held back. Both derive from an inventory number treated as certain when it is not, and modelling the uncertainty is cheaper and more effective than any attempt to make the number perfect.
