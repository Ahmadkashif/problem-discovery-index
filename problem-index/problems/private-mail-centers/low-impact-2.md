# Multi-Carrier Rate Shopping at a Retail Counter

**Industry:** [[private-mail-centers|Private Mail Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Multi-carrier shipping software is a solved category for ecommerce shippers, and none of it is built for a walk-in counter that charges retail, earns carrier incentives and absorbs the billing adjustments when its own measurements were wrong.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #data-integration #revenue-impact #automation

## The Problem
A customer asks, "What's the cheapest way to get this to Denver by Thursday?" The associate weighs and measures the box, keys the dimensions, and the point-of-sale system returns a dozen services across UPS, FedEx, USPS and DHL at the store's retail prices. The store earns the gap between the retail price it charges and the account rate it pays, plus incentives that differ by carrier programme: FedEx Authorized ShipCenter stores, for example, receive a quarterly incentive for packages dropped off on customers' own accounts. Which service the associate steers toward decides the store's margin on that sale.

Three things go wrong. Dimensions are taped by hand and rounded, so the carrier re-measures and bills an adjustment weeks later, which lands on the store's account and is rarely passed back to the customer. Surcharges (residential, delivery area, additional handling for long or heavy items) are applied after the quote. And carriers change rates every January and adjust programme terms on short notice; the FedEx ShipCenter exhibit allows changes on 30 days' notice. The owner sees margin on the monthly carrier invoice, long after the counter decision that created it.

## What Already Exists
Ecommerce multi-carrier platforms (ShipStation, Shippo, EasyPost) rate-shop across carriers, buy labels at discounted rates and audit invoices. Parcel audit firms recover refunds for large shippers; the vault analyses them under [[last-mile-delivery|Last-Mile Delivery]]. Pack-and-ship point-of-sale systems such as PostalMate and ShipRite NEXT rate across carriers at retail prices and print labels.

## The Customisation Gap
Ecommerce tools optimise one shipper's cost. A retail counter needs to optimise margin and the customer's choice at once: retail price against account cost and programme incentive for every service shown; expected surcharges and the probability of a dimension adjustment, given who measured and which box from the store's own wall was used; a check against the carrier's additional-handling thresholds before the label prints; and adjustments on the carrier invoice traced back to the counter transaction and the associate. Pack-and-ship point-of-sale systems have the counter workflow but not the invoice reconciliation or the learned adjustment risk.

## Impact If Solved
For a store shipping ~40 parcels a day (estimate), catching dimension and surcharge adjustments before the label prints and steering toward the higher-margin service the customer would accept anyway could recover a few hundred dollars a month. Most of that money now leaks unseen between the counter and the invoice.
