# WISP Sector Congestion & Subscriber Experience

**Parent Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche (subscriber-experience platforms, radio controllers and traffic shapers) is fighting to find first which sector, link or interferer is pushing which homes below plan at evening peak and what to change, and whoever diagnoses and fixes that fastest takes the account.

## Profile
**Market Size:** ~$150M a year in subscriber-experience monitoring, traffic shaping, radio management and spectrum tools for WISPs (estimate)
**Share of Parent Industry:** under 1% of industry revenue (estimate)
**Digital Adoption:** High in telemetry, Low in diagnosis — radios and shaping boxes report everything; deciding what to change is the owner's judgement
**Target Buyer:** WISP network engineer or owner
**Automation Potential:** High for detection and diagnosis; Medium for remediation

## What Makes This a Distinct Niche
After installation, a WISP's product is the evening: shared sectors saturate when households stream, unlicensed channels pick up interference from neighbours' gear and other operators, and backhaul links fade in rain. Customers compare against T-Mobile and Verizon fixed wireless and against fibre arriving under subsidy programmes. The people (network engineer, not sales), data (traffic, latency, radio statistics) and clock (nightly peak) differ entirely from qualification.

## Current Tools & Gaps
Preseem for subscriber quality-of-experience and shaping; Ubiquiti UISP and Cambium cnMaestro for radio management; spectrum analysers; LibreQoS and other open-source shaping. The gaps: alerts without root cause; no ranking of which fix (channel change, sector split, plan change, customer move) helps most; and churn risk not linked to experience.

## Problems
- [[niches/wireless-carriers/wisp-sector-qoe/build|🔨 Build: Root Cause and Fix Ranking for a Bad Evening on a Sector]]
- [[niches/wireless-carriers/wisp-sector-qoe/buy|🛒 Buy: Enterprise Network Monitoring Recast for Shared Rural Sectors]]
- [[niches/wireless-carriers/wisp-sector-qoe/fix|🔧 Fix: Channel Plans Changed by Trial and Error at Midnight]]
