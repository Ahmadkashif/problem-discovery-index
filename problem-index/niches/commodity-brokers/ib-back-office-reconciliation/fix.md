# The Payout Dispute Found by the Broker

**Niche:** [[niches/commodity-brokers/ib-back-office-reconciliation/profile|Introducing Broker Back Office & Commission Reconciliation]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Payout errors are discovered when an associated person checks their own trades against the cheque.
**Tags:** #gaussian-mixture-models #feature-engineering #evaluation-metrics #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn the clearing FCM's daily statements and commission runs into a per-account, per-broker book an introducing broker can reconcile, pay its brokers from and show an NFA examiner, and whoever closes the month with no payout disputes and a clean NFA exam takes the account.

## The Problem
A trade booked to the wrong AP code, a fee charged twice, an adjustment the FCM made after the statement: each surfaces only when a broker notices a shortfall. By then trust is damaged, and payout disputes are a common reason brokers move their books (estimate).

## Why It's Still Broken
The reconciliation is done once, at month end, by someone who has no per-trade expected value to compare against.

## What a Fix Looks Like
A daily pre-check that computes each trade's expected commission and fees from the account agreement and current schedules, compares it with the FCM's statement line, and queues mismatches with likely causes for correction before the month closes.

## Who Feels the Pain
IB principals, the associated persons whose income depends on the numbers, and customers who notice fee errors on their statements.

## Impact If Fixed
Errors are corrected in days instead of discovered by brokers, which removes a recurring source of broker attrition.
