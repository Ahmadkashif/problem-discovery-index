# The Break Written Off Below the Threshold

**Niche:** [[niches/payment-processors/settlement-and-reconciliation/profile|Settlement & Reconciliation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** Differences under a threshold are written off without investigation, the threshold was set years ago, and nobody has checked whether the write-offs are random or systematic.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #quick-win #revenue-impact #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to prove that money moved across networks, currencies and fee schedules adds up — and whoever does that automatically removes the largest manual finance function in payments.

## The Problem
Reconciliation produces breaks. Investigating each one costs a person's time, so a threshold was set below which differences are written off. The threshold is applied per break, and thousands of breaks a month fall under it. If those differences were random they would roughly cancel and the write-off would be reasonable. If they are systematic — a fee condition being applied incorrectly, a rounding convention differing, a currency rate applied at the wrong moment — they accumulate in one direction and the write-off is a standing leak. Nobody has looked at the sign distribution, which would settle it in an afternoon.

## Why It's Still Broken
The threshold was a practical response to investigation cost and became a permanent policy without anyone testing its assumption — the assumption that small breaks are random has never been examined and is the whole question. Each break is individually trivial. The aggregate is not reported. And the finance team is measured on closing the reconciliation rather than on the residual.

## What a Fix Looks Like
Test whether the residual is random. Report the sign and magnitude distribution of written-off breaks, which is the fix, takes an afternoon, and immediately reveals whether the leak is systematic — a distribution skewed in one direction is a finding with money attached. Aggregate by counterparty, fee type and currency, since a systematic cause will concentrate and the aggregate hides it. Investigate the largest aggregate causes rather than the largest individual breaks, which reorders the work toward where the money actually is. Recompute fees independently to find the schedule misapplications, which are a common systematic cause and are invisible when the counterparty's calculation is accepted. Automate investigation of the recurring causes, which makes the threshold unnecessary for those. Lower the threshold once investigation is cheap, since the threshold exists because of investigation cost and that cost is the thing being removed. Report the total written off as a standing number, which most processors do not compute and which is a real cost line. Raise systematic differences with the counterparty, since a fee misapplication is recoverable and is currently absorbed. Track the residual's trend, because a growing one indicates a change somewhere. And review the threshold periodically, because a policy set for one volume and cost structure persists unexamined into entirely different ones.

## Who Feels the Pain
Processors leaking money in small systematic increments; finance teams closing a reconciliation they cannot fully explain; and merchants receiving payouts computed from figures that were approximately right.

## Impact If Fixed
The threshold was a practical response to investigation cost and its central assumption — that small breaks are random — has never been tested. The sign distribution of written-off breaks settles it in an afternoon and turns a tolerated leak into a recoverable finding.
