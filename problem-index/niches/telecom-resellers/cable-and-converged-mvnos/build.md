# Offload Steering That Knows Where the Phone Will Be

**Niche:** [[niches/telecom-resellers/cable-and-converged-mvnos/profile|Cable & Converged MVNOs]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A cable MVNO pays wholesale for every gigabyte that leaves its Wi-Fi, and nobody predicts, subscriber by subscriber, when the phone could have stayed on the operator's own network.
**Tags:** #time-series-forecasting #gradient-boosting #markov-chains #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche (home Wi-Fi and gateway analytics vendors, offload and connection-management suppliers, and the operators' own network teams) is fighting to carry each subscriber's traffic on the operator's own Wi-Fi and small cells instead of the host's macro network without the subscriber noticing the handoff, and whoever cuts the most wholesale gigabytes per line takes the account.

## The Problem
A subscriber's day follows a pattern: home Wi-Fi in the morning, commute on cellular, an office or café with or without an operator hotspot, home again. Big downloads, such as app updates, video and photo backups, often happen at the worst moment, on the host network at wholesale cost. Operators set static device policies and hotspot auto-join rules, then read the result as a monthly average.

## Why Nobody Has Built This
Device makers control connection management, and hosts have no reason to help a reseller use less of their network. The data needed (gateway telemetry, device connection logs from the operator's app, wholesale usage by line) sits with three different teams. Offload also has a quality cost: forcing a phone onto a weak hotspot produces the complaints that end the bundle.

## What to Build
A per-subscriber model of location and connectivity over the day and week, predicting when the phone will sit near a good operator access point. The operator's app and network settings use it to defer large background transfers to those windows, recommend gateway fixes where home coverage is poor, and prioritise new small-cell or hotspot placement where predicted wholesale savings are highest. Every intervention is measured against a holdout in wholesale gigabytes and complaint rates.

## Target Customer
Heads of mobile network strategy and mobile product at cable and converged operators running an MVNO.

## Impact If Built
Each percentage point of traffic moved off the host network falls straight to mobile margin. Gateway fixes also improve the broadband product the mobile line is meant to protect.
