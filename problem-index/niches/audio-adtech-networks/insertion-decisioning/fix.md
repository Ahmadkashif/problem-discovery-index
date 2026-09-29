# The Same Advertisement Eleven Times

**Niche:** [[niches/audio-adtech-networks/insertion-decisioning/profile|Insertion Decisioning]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The frequency cap is applied per show, the listener follows six shows on the same platform, and they hear the same advertisement eleven times in a week.
**Tags:** #evaluation-metrics #descriptive-statistics #automation #confidence-intervals #quick-win #revenue-impact #workflow-orchestration #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to decide which advertisement goes into which slot of which episode for which listener — and whoever optimises that properly extracts more value from the same inventory than anyone bidding harder can.

## The Problem
A listener subscribes to six podcasts served by the same platform. Each show applies a frequency cap of two or three exposures for a given campaign. The listener hears the same advertisement eleven times in a week, sometimes twice in one episode. It is the single most common listener complaint about the medium, it makes the advertiser look careless, and the platform that served all eleven has the session history that would have prevented it. The cap is applied at the level the system happens to organise inventory rather than at the level the listener experiences it.

## Why It's Still Broken
Frequency capping was implemented per campaign per show because that is how the inventory is structured and how the delivery is counted — the cap follows the system's organisation rather than the listener's experience, which is the whole defect. Capping across shows reduces delivered impressions and therefore revenue, which nobody volunteers for. The complaint reaches the host rather than the platform. And nobody measures the actual received frequency distribution.

## What a Fix Looks Like
Cap at the listener, not at the show. Apply frequency across the listener's whole consumption on the platform, which is the fix, uses identity the platform already has for delivery, and directly addresses the medium's most common listener complaint. Report the actual received frequency distribution rather than the configured cap, since the two differ substantially and only one is known — this measurement alone usually shocks the people who set the caps. Prevent repetition within a single episode, which is the most egregious case and is trivially avoidable. Apply competitive separation so two advertisements for competing products do not sit adjacently. Vary the creative where an advertiser supplies multiple versions, which reduces fatigue at no cost to delivery. Model the tolerance cost of each additional exposure, connecting to the fatigue work in messaging, so the cap is derived rather than chosen. Show the advertiser their true frequency distribution, since they are paying for repetition that damages their brand and do not know. Coordinate across host-read and inserted advertising, because a listener who hears a host-read endorsement and three inserted spots for the same product has heard four. Let listeners signal fatigue where the interface permits, which is direct evidence. And report listener complaints against frequency, since the relationship is strong and is currently anecdotal.

## Who Feels the Pain
Listeners hearing the same advertisement eleven times; advertisers whose brand is damaged by repetition they paid for; and hosts who receive the complaints about a decision the platform made.

## Impact If Fixed
The cap follows the system's inventory structure rather than the listener's experience, which is the entire defect. Capping across the listener's whole consumption uses identity the platform already has, and reporting the received frequency distribution usually shocks the people who set the caps.
