# Two Hundred Calls a Day and No Record of Why They Failed

**Niche:** [[niches/freight-tech-platforms/carrier-capacity-matching/profile|Carrier Capacity Matching]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A carrier sales rep makes two hundred calls a day, almost all of which are declines, and the system records that a call happened — not whether the rate was wrong, the direction was wrong, or the truck was already loaded.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #large-language-models #workflow-orchestration #worker-facing #quick-win
**Contested on:** Every serious competitor in load matching is fighting to cover a load on the first carrier contacted, at a rate that carrier will accept — and whoever holds first-tender acceptance rate highest takes the account.

## The Problem
The rep calls, offers a load, and the dispatcher says no. She logs the call. The reason — the rate was two hundred short, the carrier does not run into that receiver, their truck is already committed, or they would take it at a different pickup time — is the single most valuable piece of information in the exchange and it goes unrecorded, two hundred times a day, across every brokerage in the country. So the next rep calls the same carrier about a similar load next week and gets the same answer, and the model that could predict it has no labels.

## Why It's Still Broken
Logging a reason costs the rep a moment on a call they are trying to end so they can make the next one, and reps are measured on calls and coverage rather than on data quality. The reason taxonomy was never designed, so where a field exists it is free text or a list nobody agreed on. And the benefit accrues to a future matching capability that does not exist yet, which is a hard case to make to someone with forty loads to cover today.

## What a Fix Looks Like
Make capture free rather than cheap. Reason codes are two taps on the call screen — rate, direction, timing, equipment, committed, not interested in this shipper — and the list is short enough to be muscle memory. Where calls are recorded and consent is in place, the reason is extractable from the conversation automatically, which removes the cost entirely; that is now ordinary technology and is the version worth building. Counteroffers are captured explicitly, because a decline at $2,400 with a counter at $2,700 is worth far more than a decline, and reps currently keep counters in their heads. Report the aggregate back to the reps and to pricing: which lanes are consistently declined on rate, which carriers have stopped answering, which shippers carriers avoid. That last one is a finding brokerages rarely surface and should — a receiver that carriers refuse is a rate problem the brokerage is absorbing.

## Who Feels the Pain
Carrier sales reps repeating conversations their colleagues already had; pricing teams setting rates without knowing what is being declined; and carriers receiving calls about freight they have declined ten times.

## Impact If Fixed
Decline reasons are the labels every matching and pricing improvement in this niche depends on, and they are generated two hundred times a day and discarded. Automatic extraction from recorded calls makes capture free, and the immediate reporting — which lanes fail on rate, which shippers carriers avoid — is actionable before any model is built.
