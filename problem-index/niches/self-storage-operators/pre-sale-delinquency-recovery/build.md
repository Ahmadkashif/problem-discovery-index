# Outreach Ranked by Who Will Pay

**Niche:** [[niches/self-storage-operators/pre-sale-delinquency-recovery/profile|Pre-Sale Delinquency Recovery]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Collections teams call delinquent tenants oldest-first, when the tenants most likely to pay with one nudge and the ones who have already abandoned their units look the same on the list.
**Tags:** #markov-chains #logistic-regression #evaluation-metrics #feature-engineering #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to get past-due tenants paying again before their units reach the lien sale, and whoever recovers the most past-due rent per delinquent unit before the sale date takes the account.

## The Problem
A 100-store operator may carry ~3–6% of units past due 30 days or more (estimate), several thousand files. Each gets the same sequence of reminders, and the collections team calls in days-past-due order. Tenants who would pay after one call wait in the queue. Those who left months ago, whose gate code has not been used since spring, take the same effort.

## Why Nobody Has Built This
Collections modules were built to send the statutory notices on time, not to rank people. Contact outcomes live in call notes and texts, not in the ledger, so there is nothing to train on until someone extracts them.

## What to Build
A roll-rate model of delinquency: a Markov chain over 15, 30, 45 and 60 days past due, sale and cure, with transition probabilities estimated per tenant by logistic regression. The features are tenure, past cures, autopay failure versus missed manual payment, access since the overlock, protection-plan status and contact responses. Outreach is ranked by expected recovery per contact. Files likely abandoned move straight to the statutory track, which is never shortened. A payment-plan offer is generated where it can complete before the sale date.

## Target Customer
Directors of collections at operators and third-party managers; facility platforms selling collections modules.

## Impact If Built
If ranking recovers payment from ~5% more of delinquent tenants before sale (estimate), at ~$300 average past due (estimate), a 100-store operator with ~4,000 delinquent files a year recovers ~$60,000 more a year. It also sends fewer units to auction.
