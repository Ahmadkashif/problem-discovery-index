# A Quote That Knows What the Carrier Will Bill

**Niche:** [[niches/private-mail-centers/rate-shopping-retail-margin/profile|Multi-Carrier Rate Shopping & Retail Margin]]
**Industry:** [[industries/private-mail-centers|Private Mail Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The counter quote assumes the hand-taped dimensions are right and the surcharges are known; the carrier's bill weeks later says otherwise, and the store absorbs the difference.
**Tags:** #gradient-boosting #linear-regression #cnns #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show the walk-in customer the service they will accept at the store's best net margin after programme incentives, surcharges and adjustments, and whoever prices the counter quote closest to what the carrier finally bills takes the account.

## The Problem
Each quote is computed from a weight on the scale and three numbers keyed by an associate. Carriers re-measure on automated equipment and bill the difference, plus surcharges for residential delivery, remote areas and additional handling that the quote may not have applied. These land on the store's account. Customers have left; the store eats them.

## Why Nobody Has Built This
Adjustment data lives on carrier invoices that point-of-sale vendors do not ingest, each store sees too few adjustments to learn from, and carriers have no reason to help a reseller anticipate their billing.

## What to Build
A quote-time model, trained on pooled counter transactions joined to invoice adjustments, that predicts for each service shown the probability and size of an adjustment, given the box from the store's own stock, the associate, the item class, the destination type and the dimensions. A fixed overhead depth camera supplies dimensions as a second reading. The quote shown to the customer includes the expected cost, and the associate sees when to re-measure or choose a different box.

## Target Customer
Point-of-sale vendors (PostalMate, ShipRite) and franchisors, which hold the transactions and can pool invoices across stores.

## Impact If Built
If adjustments run at a few percent of shipping revenue (estimate), catching most of them before the label prints is worth hundreds of dollars a month to a busy store. More durably, the store can quote with confidence rather than padding prices.
