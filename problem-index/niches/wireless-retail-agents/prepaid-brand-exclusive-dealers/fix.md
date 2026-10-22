# The Recharge That Didn't Happen

**Niche:** [[niches/wireless-retail-agents/prepaid-brand-exclusive-dealers/profile|Prepaid Brand-Exclusive Dealers]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Fix (Pain Point)
**One-liner:** Prepaid activation commissions are clawed back when the customer doesn't make the first recharge, and the store finds out from the statement rather than in time to help the customer pay.
**Tags:** #logistic-regression #survival-analysis #evaluation-metrics #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche (master agents, the brands' dealer portals and prepaid POS vendors) is fighting to tell an owner-operator, store by store and day by day, what the month's activation commissions, bill-pay fees and first-recharge chargebacks will net to, and whoever makes that cash figure trustworthy takes the dealer's stores.

## The Problem
A prepaid customer activates, uses the first month and then lets the line lapse, often because cash was short that week or a competitor offered a deal, not because they meant to leave. If the commission depends on a first payment or recharge (a common trigger, per dealer-side explainers), the store loses it, and the brand loses a customer the store could have kept with a reminder.

## Why It's Still Broken
The store doesn't see the account after activation. The brand's own reminders go out generically, and the dealer learns of the lapse only as a chargeback weeks later.

## What a Fix Looks Like
At activation, with the customer's consent, the store records the recharge due date and sends a reminder a few days before, with the store's address and hours for cash payment. A simple risk score on the activation flags customers likely to lapse so the rep can walk them through autopay or the brand app before they leave. Each month the reminder list is reconciled against the chargebacks that still arrive, so the store can tell whether the reminders worked.

## Who Feels the Pain
Prepaid owner-operators who lose commission; reps whose pay is reduced; customers who lose their number by accident.

## Impact If Fixed
If first-recharge failures are a large share of prepaid chargebacks (estimate), even a modest cut in lapses recovers real commission and repeat bill-pay traffic at almost no cost.
