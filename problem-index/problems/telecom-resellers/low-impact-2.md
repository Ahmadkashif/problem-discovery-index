# Reconciling the Host Network's Wholesale Bill

**Industry:** [[telecom-resellers|Telecom Resellers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** An MVNO pays its host network by the line and the gigabyte on a wholesale invoice it didn't compute, and the generic reconciliation and expense tools it could use were built for enterprises checking a phone bill, not for a reseller checking a million lines against its own subscriber records.
**Tags:** #gradient-boosting #k-means-clustering #feature-engineering #descriptive-statistics #revenue-impact #data-integration #automation

## The Problem
Every month the host network sends an MVNO a wholesale invoice and usage files. They charge active lines at the contracted rate, data usage against pooled or tiered buckets, roaming, international, eSIM and SIM provisioning events, and premium features. The MVNO's own records say which lines it believes are active, suspended, ported out or in a grace period, and what each subscriber used. The two never agree exactly. Lines the MVNO deactivated keep billing because a deactivation message failed. Ported-out numbers bill for part of a month. Usage lands in the wrong tier. Lifeline or promotional lines are charged at the standard rate. Thin margins make the gap matter: an MVNO selling unlimited plans makes its money in the difference between the retail price and the host's per-gigabyte cost, and that difference can be gone after a few percent of billing leakage and a handful of heavy users.

## What Already Exists
Telecom expense management platforms such as Tangoe and Calero audit enterprise telecom invoices against contracts. Financial close tools such as BlackLine reconcile accounts. MVNO enablers' BSS platforms, such as Telgoo5, rate the MVNO's own subscribers and produce usage reports. The host network supplies call detail and usage files in its own format.

## The Customisation Gap
Expense management tools check whether an enterprise was billed the contracted price for its own lines. An MVNO needs a line-level, event-level match between two subscriber ledgers of millions of rows, where each party is the system of record for half the truth. The industry-specific logic is the host's rate-plan structure (pooled buckets, overage tiers, throttling thresholds, roaming zones); the lifecycle events that change billing (activation, suspension, port-out, SIM swap, plan change) and their effective-time rules; the classification of disputed charges by root cause so disputes can be filed inside the contract's dispute window; and a margin view that joins wholesale cost to retail revenue by plan and cohort.

## Impact If Solved
A reconciliation that runs before the dispute window closes recovers billing errors the MVNO currently absorbs, often a low single-digit share of wholesale cost (estimate). It also shows which plans and subscriber segments lose money on the host network, which is the information an MVNO needs before the next wholesale renegotiation.
