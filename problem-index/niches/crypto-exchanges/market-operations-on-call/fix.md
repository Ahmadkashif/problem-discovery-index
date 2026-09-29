# Paged by a Bull Run

**Niche:** [[niches/crypto-exchanges/market-operations-on-call/profile|Market Operations On Call]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** The market moves, forty alerts fire, thirty-nine are the market, and the engineer has to check all of them.
**Tags:** #worker-facing #change-point-detection #quick-win #automation #evaluation-metrics #descriptive-statistics #workflow-orchestration #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to page a human only when the market's behaviour is actually a system fault — and whoever separates a violent but ordinary market from a broken exchange makes a permanently staffed function survivable.

## The Problem
A significant move starts at two in the morning. Latency alerts, queue depth alerts, order rate alerts, price divergence alerts and withdrawal backlog alerts all fire within minutes. The engineer knows most of them are the market, but one of them might not be, and the only way to find out is to check each one. This happens on every meaningful market day, which in this asset class is often, and it is the single largest reason the rota churns.

## Why It's Still Broken
Each alert was added after an incident, so the set grew by accretion and nobody ever pruned it against how it behaves during a move — the alerts were never evaluated as a system. Correlated alerts are not grouped. The market context that would resolve most of them in a glance is on a different screen. And the fix is always deferred because the storms happen when there is no time.

## What a Fix Looks Like
Group, contextualise and suppress. Group correlated alerts into a single incident rather than paging for each, which is the fix and removes most of the volume immediately. Attach the market context to the page — price move, volume, peer venue comparison — since that resolves the majority of alerts in one look and currently requires three dashboards. Suppress the downstream alerts that are known consequences of a detected upstream cause, because the storm is mostly one event expressed many times. Show which alerts fired during the last comparable market move and what each turned out to be, as that history is the fastest triage available and is never surfaced. Mark the alerts that have never once indicated a real fault, since a rule that has been wrong two hundred times should not page a person at two in the morning. Review the alert set after every storm while it is fresh, which is the only moment the knowledge exists. Set market-conditional thresholds as an interim step, because full regime modelling takes time and this does not. Route market-caused alerts to a dashboard rather than a page, so the information is available without waking anyone. Track pages per night and their outcomes, which makes the rota's condition visible to leadership. And ask the on-call engineers which alerts to delete, since they know and are never asked.

## Who Feels the Pain
On-call engineers woken by ordinary market days; teams losing staff to rota burnout; and exchanges whose real faults are buried in storms of market noise.

## Impact If Fixed
The alert set grew by accretion after incidents and was never evaluated as a system. Grouping correlated alerts and attaching peer-venue market context resolves most of a storm before anyone has to open a dashboard.
