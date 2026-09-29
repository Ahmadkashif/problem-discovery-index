# Lineage: Audio Adtech Networks

**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**The tool:** the IAB podcast "download" — the counting rule in the IAB Tech Lab *Podcast Measurement Technical Guidelines* (v1.0 September 2016, v2.0 December 2017): a server-log file request, filtered for bots and pre-loads, counted only past the ID3 header plus one minute of audio, de-duplicated by IP address plus user agent within a 24-hour day
**Builder:** IAB Tech Lab
**Builder in vault:** **ABSENT**
**Verification:** verified — primary documents read; see Sources

## The Problem That Came First

A podcast is a file, not a stream. The player fetches an MP3 over ordinary HTTP, and the IAB's own 2016 document is blunt about what that means: the native Apple players "offer no technology for confirming that a podcast file was played."

That mattered because of who held the listeners. Hosting companies reported to the IAB working group that in April 2016 the iOS Apple Podcast app alone requested about **45–52%** of podcast files, iTunes another 8–13%. Less than 3% of requests came from players that sent anything back.

So every seller counted from its own server logs, and they counted differently. A progressive download leaves several partial requests in the log; an HTML5 page can pre-load a file nobody plays; a bot can fetch a whole back catalogue. **Two hosts with the same audience could report different numbers, and a buyer had no way to tell which was inflated.** The document names the cost: it was "limiting participation of some advertisers."

## What Got Built

A definition precise enough that two log processors should produce the same number.

Version 1.0, released **6 September 2016**, described common practice. Version 2.0, released **December 2017**, turned that into a mandated five-step process: filter, apply a threshold, aggregate uniques, generate metrics, audit.

The mechanics are the tool. A request only counts once "the ID3 tag plus enough of the podcast content to play for 1 minute" has been served — or the whole file, if that can't be computed. Uniques are identified by **IP address plus user agent**: "if the same file is downloaded 10 times by 6 user agents behind one IP address, that would count as 6 users and 6 downloads." The window is a calendar day. Known bots and bogus user agents are stripped first.

The IAB Tech Lab then added a **compliance programme**, so a host could signal to buyers that its downloads were counted this way.

## Who Built It, And Why Them

The IAB, because the problem was a trust problem between competitors, and no single seller's number could fix it.

The v1.0 working group was volunteers from 23 member companies, led by Rockie Thomas of AdsWizz and Ilia Malkovitch of Google, with Amit Shetty as the IAB lead. The membership list is the business case: Libsyn, Podtrac, Blubrry/RawVoice, PodcastOne, Midroll, Wondery, NPR, Triton Digital, WideOrbit, Westwood One. **Every one of them was selling the same unverifiable inventory**, and each had an interest in a common ruler that would let buyers compare them. v2.0 was led by Steve Mulder of NPR.

What nobody in that room controlled was the player. The only party that could have measured listening was Apple, and Apple was not writing an ad standard. So the sellers standardised the one thing they did control — their own logs.

## What It Cost

**It measures delivery and calls it an audience.** The v2.0 text concedes this itself: "log-based measurement counts only the file downloads and not the actual listening." A download of an episode whose ad sits at minute 40 is counted the same as one that reached it.

IP-plus-user-agent was the cheapest unique in a server log, and inherits the IP address's weaknesses — the document itself notes dorms, offices and "recycled mobile IPs." The same household-IP signal later became the basis of attribution matching.

And a counting rule, once certified, is hard to move. v2.0 promised to add "Confirmed" plays once Apple and others shipped client-side metrics. The download is still the currency.

## What You Still Touch

Every podcast rate card priced per thousand downloads is this definition, and the gap it left — between a file served and an ad heard — is the channel's central problem.

- [[problems/audio-adtech-networks/high-impact|🔴 No Click, No Exposure Signal, and the Independent Measurement Was Bought]] — the download standing in for exposure
- [[niches/audio-adtech-networks/exposure-modelling/profile|Exposure Modelling]]
- [[niches/audio-adtech-networks/the-measurement-layer/profile|The Measurement Layer]]
- [[niches/audio-adtech-networks/attribution-and-independence/profile|Attribution & Independence]] — where the IP address was reused for conversion matching

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. IAB Tech Lab, *Podcast Measurement Technical Guidelines* page (version list: v1.0 September 2016, v2.0 December 2017, v2.1 February 2021, v2.2 May 2024; compliance programme); IAB, *Podcast Ad Metrics Guidelines*, "Released September 6, 2016" (primary PDF — working group leads, 23 member companies, April 2016 player share table, <3% client-side, "limiting participation"); IAB Tech Lab, *Podcast Measurement Technical Guidelines v2.0*, December 2017 (primary PDF — Steve Mulder lead, five-step process, ID3 + 1 minute threshold, IP + UA example, calendar-day window, "Confirmed" plays). ⚠️ **Not established:** when the compliance programme began certifying its first hosts, and which vendors were first certified; whether any individual proposed the one-minute threshold (the document gives only the rationale "other mediums use similar or smaller thresholds"). The claim that the IP-match attribution method descends from this rule is the note's argument, not a documented design lineage.
