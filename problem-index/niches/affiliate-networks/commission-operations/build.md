# Approving Transactions One Screen at a Time

**Niche:** [[niches/affiliate-networks/commission-operations/profile|Commission Operations]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Affiliate managers spend their months approving thousands of transactions one screen at a time, chasing returns that claw back commission after payout, and negotiating rates in email threads that live nowhere.
**Tags:** #workflow-orchestration #automation #data-integration #evaluation-metrics #compliance #descriptive-statistics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to run validation, clawback and rate changes as a system rather than as a person with a spreadsheet — and whoever does that removes the administrative weight that caps how many partners a programme can have.

## The Problem
The monthly validation window opens. Four thousand transactions need approval. Most are obviously fine, some need checking against the order system, a few are from partners under review. The manager works through them. Then the returns file arrives, and commissions already paid must be reversed, matched by order reference to transactions across three months. Then three partners want rate changes, agreed in emails that live in an inbox and typed into a console with no record of who agreed what or why. This consumes the month. The programme cannot grow past the point where this work exceeds one person.

## Why Nobody Has Built This
The networks' operational model assumes a merchant-side human doing the validation, which is how the platforms were designed and nobody has revisited it. Order and returns systems are on the merchant's side and networks integrate shallowly. Rate negotiation is treated as a commercial conversation rather than as a managed object. And the burden falls on a single person whose time is not modelled as a constraint on programme growth.

## What to Build
Turn the monthly grind into a system. Validate automatically against the merchant's own order and fulfilment data, which is the fix for most of the volume — the answer for the overwhelming majority of transactions is already in a system the network is not connected to. Express the real validation policy as rules rather than as a person's judgement, so exceptions are the only thing reaching a human. Reconcile returns automatically by order reference and apply clawbacks with the linkage preserved, which removes the worst monthly task and is the other side of the publisher's clawback problem. Align payout timing to the return window where possible, since paying before the window closes creates the clawback problem in the first place and is a scheduling choice rather than a necessity. Make rate agreements first-class objects with terms, effective dates, approvers and a record, rather than console changes following an email. Support rate structures the platforms cannot express — by product category, by new versus returning customer, by partner role — which is what merchants actually want and cannot have. Flag anomalies for review rather than requiring review of everything, since the exceptions are a small fraction and the remaining volume is ritual. Give finance a reconciliation between commission accrued, paid and reversed, which currently does not exist in a usable form. Report the operational cost per partner, because that number explains why programmes stop growing. And measure hours per thousand transactions, since that is the metric the whole build exists to move.

## Target Customer
Merchant affiliate and finance teams, agencies running programmes on behalf of merchants, and the networks whose platforms create the workload.

## Impact If Built
The answer for almost every transaction sits in the merchant's own order system that the network is not connected to, and a person checks them one at a time instead. Aligning payout to the return window removes the clawback problem at source rather than reconciling it afterwards.
