# Insurance Agency Commission Software Adapted to Round Turns

**Niche:** [[niches/commodity-brokers/ib-back-office-reconciliation/profile|Introducing Broker Back Office & Commission Reconciliation]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Insurance agencies already reconcile carrier commission statements and pay producers on split schedules; introducing brokers face the same problem with different units.
**Tags:** #feature-engineering #decision-trees #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn the clearing FCM's daily statements and commission runs into a per-account, per-broker book an introducing broker can reconcile, pay its brokers from and show an NFA examiner, and whoever closes the month with no payout disputes and a clean NFA exam takes the account.

## The Problem
IBs receive a commission payment from the clearing FCM and pay their associated persons on individual schedules. The calculation is rebuilt every month in Excel.

## What Already Exists
Commission management software for insurance agencies, which imports carrier statements, reconciles expected against received commissions and runs producer splits.

## The Customization Gap
Futures needs round-turn and half-turn commission conventions; option premium-based commissions; exchange, clearing, NFA and give-up fee pass-throughs that change several times a year (estimate); per-account rates negotiated by the broker; inherited accounts with legacy splits; and the FCM's statement formats rather than carrier ones.

## Target Customer
Introducing brokers whose ag and retail books have several associated persons on different payout terms.

## Impact If Solved
Payouts calculated the same way every month and disputes settled with data, using a proven commission engine rather than a custom build.
