# Audio Adtech Networks

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$8B US digital audio advertising across podcasting and streaming audio; the serving, marketplace and measurement layer takes roughly $1-1.5B of it
**Tech Maturity:** Modern serving, primitive measurement. Megaphone, Art19, AdsWizz, Triton Digital and Acast run dynamic ad insertion at scale with targeting, frequency capping and programmatic marketplaces. What none of them can do is establish that a person heard an advertisement, because audio is the only major channel with no click and no reliable exposure signal.
**Workforce:** Ad operations and trafficking specialists, yield and inventory analysts, measurement and analytics staff, sales and partnership teams, platform and streaming engineers

## Key Pain Themes
The industry's currency is the download. The IAB's measurement standard defines it carefully and it still counts a file request, not a listen — and certainly not a listen that reached the ad. Dynamic insertion made audio targetable and programmatic, and simultaneously widened the gap between an impression served and an advertisement heard, because the insertion point may sit past where most listeners stop.

Attribution is probabilistic in a way no other channel would accept. The standard method matches the household IP address that requested the episode against a visit or conversion on the advertiser's site within a window. That match degrades under carrier-grade NAT, VPNs, IPv6 rotation and shared networks, it cannot see a listener who heard the ad on one device and converted on another outside the household, and its error rate is not published by anyone. The independent measurement layer that grew up to do this was substantially absorbed by a platform, with one of the main providers shut down in 2024, leaving measurement of the channel increasingly in the hands of parties selling it.

The third theme is the split personality of the inventory. A host-read endorsement and a dynamically-inserted programmatic spot are priced in the same marketplace and are not the same product; the first carries the host's credibility and cannot be targeted, the second can be targeted and carries none.

## Current Tech Landscape
Spotify's Megaphone and Ad Exchange, Amazon's Art19, SiriusXM's AdsWizz and Simplecast, iHeart, Audacy and Acast hold most of the serving infrastructure, which means the largest sellers also own the pipes. Triton Digital serves streaming radio. Programmatic audio trades through the major demand-side platforms with limited inventory transparency. Measurement runs on pixel and IP-match attribution from Podscribe, Magellan AI, Claritas and platform-owned tools. Transcription-based contextual and brand suitability analysis from Sounder, Barometer and Podscribe is the newest layer and the most genuinely additive.

## Problems
- [[problems/audio-adtech-networks/high-impact|🔴 High Impact: No Click, No Exposure Signal, and the Independent Measurement Was Bought]]
- [[problems/audio-adtech-networks/low-impact-1|🟡 Low Impact: Inventory Forecasting and Yield Under Dynamic Insertion]]
- [[problems/audio-adtech-networks/low-impact-2|🟡 Low Impact: Contextual Targeting and Brand Suitability From Transcripts]]
- [[problems/audio-adtech-networks/worker-life-1|🟢 Worker Life: The Audio Ad Ops Specialist Between Two Systems]]
- [[problems/audio-adtech-networks/worker-life-2|🟢 Worker Life: The Host Reading the Ad and Pricing It Blind]]
- [[problems/audio-adtech-networks/ml-opportunity|🧠 ML Opportunities]]
- [[problems/audio-adtech-networks/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Audio advertising is bought on faith backed by a household IP match, and the consolidation of measurement into the platforms that sell the inventory has removed the one check the market had. What makes this more tractable than it sounds is that the exposure question — did a listener actually reach the ad — is answerable from telemetry the streaming platforms already collect and do not use for it: position-in-episode listening curves, skip behaviour, completion. An exposure model built from that turns the download into something closer to an impression, and an independent measurement layer built on top of it would be the only credible referee in a channel where every current referee is also a seller.
