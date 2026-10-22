# Root Cause and Fix Ranking for a Bad Evening on a Sector

**Niche:** [[niches/wireless-carriers/wisp-sector-qoe/profile|WISP Sector Congestion & Subscriber Experience]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A WISP's monitoring says a sector had a bad evening; it doesn't say whether the cause was congestion, interference, a weak backhaul or two heavy users, or which change would fix it.
**Tags:** #graph-neural-networks #gradient-boosting #causal-inference #time-series-forecasting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche (subscriber-experience platforms, radio controllers and traffic shapers) is fighting to find first which sector, link or interferer is pushing which homes below plan at evening peak and what to change, and whoever diagnoses and fixes that fastest takes the account.

## The Problem
Evening latency spikes and throughput drops on a sector can come from airtime saturation, a few customers at poor modulation using most of the airtime, co-channel interference from another operator, backhaul fade or upstream congestion. The fixes differ completely. A small team guesses, changes one thing and waits a day to see.

## Why Nobody Has Built This
Monitoring vendors stop at detection and shaping; radio vendors see only their own gear; and few WISPs record what they changed and whether it helped, so there is no outcome data to learn from.

## What to Build
A model over the WISP's network graph (backhaul, tower, sector, customer radio) that attributes each degradation to a cause using airtime, modulation, noise floor, backhaul and traffic telemetry. It ranks candidate fixes by expected improvement learned from logged past changes across many WISPs, and checks the result the next evening.

## Target Customer
Network engineers and owners at WISPs with tens to hundreds of sectors.

## Impact If Built
Problems are fixed in one evening instead of a week of guesses, and the subscribers most at risk are protected before they shop elsewhere.
