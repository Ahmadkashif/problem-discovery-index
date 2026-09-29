# Order-to-Cash Practice

**Niche:** [[niches/bnpl-providers/returns-and-instalment-reconciliation/profile|Returns & Instalment Reconciliation]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise order-to-cash handles partial shipments, credits and adjustments against a payment schedule as routine, and instalment providers work it out in support.
**Tags:** #workflow-orchestration #data-integration #automation #compliance #evaluation-metrics #descriptive-statistics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to reconcile a merchant's return policy with a consumer's instalment schedule — and whoever does that removes the most common and most infuriating failure in the product.

## The Problem
Reconciling order changes against a payment arrangement is ordinary enterprise practice. Order-to-cash systems handle partial shipment, partial delivery, credit notes, returns, adjustments and instalment terms, and they maintain the relationship between the order lines and the amounts due throughout. The data model supports it because business-to-business commerce has always had partial fulfilment and staged payment. Consumer instalment providers face the same structure with a simpler schedule and handle it manually.

## What Already Exists
Order-to-cash data models linking lines to payment obligations; credit note and adjustment handling; partial fulfilment and delivery tracking; instalment terms within receivables; and automated reconciliation between orders and payments.

## The Customization Gap
The adaptation is to a three-party arrangement where the provider owns the schedule and the merchant owns the order. It requires: (1) the order and the payment obligation living in different companies' systems, which is the structural difference from an enterprise receivables ledger where both are internal — the integration is the whole problem; (2) consumer-facing timing expectations, since a consumer who returned an item expects the next payment not to be taken and a business-to-business credit note cycle takes weeks; (3) returns that are frequent and small rather than exceptional, which makes automation necessary rather than convenient; (4) merchants with wildly different return policies, requiring configurable rather than standard treatment; and (5) the consumer as a party who must be told what happened, which receivables reconciliation has no equivalent of.

## Target Customer
Provider operations teams, merchants and commerce platforms, and order management vendors for whom third-party instalment reconciliation is an unserved case.

## Impact If Solved
Business-to-business receivables has always handled partial fulfilment against staged payment and the data model supports it. The order and the obligation living in different companies' systems is the structural difference, and consumer timing expectations make the reconciliation urgent rather than monthly.
