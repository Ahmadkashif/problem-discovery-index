# History: Podcasting Networks

**Industry:** [[industries/podcasting-networks|Podcasting Networks]]
**Primary Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**Secondary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Origin Parent:** none — see below
**Episode Tier:** 1
**Transferable Pattern:** Before assuming a measurement was withheld, check whether anyone ever actually computed it — an open format can go two decades without a working definition of its own core metric, and that is a missing join, not a policy choice.

> **Origin Parent — omitted.** No `origins/` industry claims this one, and radio — the closest broadcast-era analogue — is not in the origin spine either. Podcasting's founding technology, RSS, predates Wave 10 by roughly a decade and was not built for audio distribution at all. This industry is the structural exception in this batch worth stating plainly up front: **it is the one Wave 10 child whose distribution layer was never enclosed by a single platform**, and most of this file is about what has and has not been done to change that.

## Before Radio Had No Rival

Spoken-word audio distribution meant broadcast radio: a limited number of licensed frequencies, scheduled programming, and a national or local reach determined by transmitter placement and regulatory allocation, not by anything a creator could control. Publishing an audio show to an audience of any size required either a broadcast licence or a station willing to carry the programme.

## The Origin Event — a Spec, Not a Platform

Podcasting's origin is unusually well documented and unusually free of a founding company. **Tristan Louis proposed attaching audio and video enclosures to RSS feeds in October 2000**; **Dave Winer**, RSS's own format author, implemented the enclosure mechanism. The word did not exist yet. **BBC journalist Ben Hammersley coined "podcast"** — a portmanteau of iPod and broadcast — **in a February 2004** article, and the term reached the community that August via the iPodder-dev mailing list before **Adam Curry**, a former MTV VJ, adopted it and launched *Daily Source Code* that same month, becoming the format's most visible early evangelist. **Apple added native podcast support to iTunes with version 4.9 in June 2005** — the moment that took podcasting from a hobbyist's RSS trick requiring separate client software to something any iPod owner could subscribe to inside the software they already had.

**No company owns this origin, and no company had to grant permission for it to happen.** RSS is an open specification; anyone who can host an audio file and write a feed can publish a podcast, and any app that can parse RSS can play it. That is the single fact every other section of this file has to be read against.

## What Became Cheap

**Publishing spoken-word audio to anyone, on any device, without a broadcast licence, a network's approval, or a platform's editorial sign-off.** This is the sharpest contrast in the whole Wave 10 cohort: [[history/ugc-video-platforms|UGC video]] required accepting a specific platform's hosting, ranking and monetisation terms from day one. Podcasting required nothing but a feed URL.

## The Contest — an Attempt to Enclose an Open Format, and Its Retreat

If there is a fight in this industry, it is not creator-versus-platform in the Wave 10 default shape. It is **platform-versus-format**: an attempt, mounted specifically by Spotify from 2019, to buy enough exclusive content that podcasting's open distribution would stop mattering in practice.

Spotify acquired **Gimlet Media in February 2019**, **Parcast the following month**, and **The Ringer in February 2020** — direct ownership of studios rather than licensing deals. The marquee move was licensing, not acquisition: **The Joe Rogan Experience** — launched December 2009, by then podcasting's largest single show — signed an exclusive deal with Spotify **announced May 2020, reportedly worth around $200 million**, taking the show off RSS entirely and off YouTube's full-episode uploads from December 2020 onward.

**The retreat is the more interesting half of the story, and it happened faster than the enclosure did.** In **February 2024**, Spotify renewed the Rogan deal at a reported **$250 million — and made it non-exclusive**, returning full episodes to Apple Podcasts, YouTube and the open RSS ecosystem. Four years of the platform's largest exclusivity bet ended with the content going back to the format it tried to leave. **This vault should not overclaim what that proves** — Spotify's own competitive and subscriber-growth calculus, not a principled commitment to openness, most plausibly drove the reversal — but the fact stands: **the open format proved durable enough that even the best-funded attempt to enclose it retreated within four years**, which is not a sentence that could be written about YouTube's video-hosting monopoly or TikTok's algorithm.

## The Graveyard — a Company, Not the Format

**Odeo**, a podcasting directory and hosting company founded in 2004 by Noah Glass and Evan Williams, launched July 2005 — one month after Apple's iTunes 4.9 absorbed the exact function Odeo was building a business around. *(Widely told in tech histories that Apple's native support gutted Odeo's core business specifically, prompting its 2006 internal pivot — this vault could not independently confirm that causal account from a primary source this session, and the detail should be treated as a commonly repeated narrative rather than a verified one.)* What is fully documented is the outcome: Odeo's internal hack-week work that year produced **Twitter**, and Evan Williams went on to found Obvious Corporation specifically to develop it. **Whatever the precise cause, a podcasting company died and the world got Twitter instead** — a tidy illustration that an open format can starve a platform business built on top of it even without any hostile act, simply by not needing an intermediary.

## The Missing Join — Podcasting's Own Measurement Was Never Built, Not Withheld

Every other file in this batch describes a platform that holds a measurement and shares it selectively. Podcasting is different, and the difference matters: **the industry has never had a reliable measurement of listening at all, not because someone declined to share it, but because a "podcast download" and "a person listened to the episode" have never been the same event, and nobody, including the hosting platforms, has ever closed that gap.**

The **IAB's Podcast Measurement Technical Guidelines** exist specifically to standardise what counts as a download — a request for the audio file of a defined minimum size, from a de-duplicated source, within a defined window — precisely because, absent a standard, competing measurement firms (Podtrac, Chartable and others) were producing incompatible download counts for the same show. Even a fully standardised download count answers "was the file requested," not "did a person listen, and for how long." A download can be a scheduled app pre-fetching the next episode overnight to a phone whose owner never presses play. **This is the missing join this vault's method distinguishes from a declined one: nobody chose to withhold listen-through data from producers, because nobody — not Apple, not Spotify, not the ad networks pricing against the number — has ever computed it reliably at industry scale.** Sponsors buy against downloads because downloads are the number that exists, not because it is the number that matters, and every producer in this industry knows the difference without having a better number to use instead.

## What's Still Open

- [[problems/podcasting-networks/high-impact|🔴 Show Audience Retention Prediction]]
- [[problems/podcasting-networks/low-impact-1|🟡 Sponsor-Show Matching for Mid-Size Shows]]
- [[niches/podcasting-networks/audio-audience-measurement/profile|Audio Audience Measurement]]
- [[niches/podcasting-networks/podcast-hosting-platform-analytics/profile|Podcast Hosting Platform Analytics]]
- [[niches/podcasting-networks/programmatic-audio-marketplaces/profile|Programmatic Audio Marketplaces]]

## The Transferable Pattern

> **Before assuming a measurement was withheld, check whether anyone ever actually computed it. An open format can run for two decades without a working definition of its own core metric, and that is a missing join, not a policy choice.**

The instinct this vault has trained, correctly, in every other Wave 10 file is to ask who holds the measurement and why they won't share it. Podcasting is the case that punishes applying that instinct automatically. There is no villain here withholding listen-through data from producers — there is an unsolved measurement problem that nobody has been sufficiently incentivised to solve, because the download proxy is good enough to sell ads against and nobody's revenue depends on it being accurate rather than merely available. For an FDE, that is a different, often more valuable opportunity than exposing a withheld number: **building the first credible instrument for a measurement an entire industry has been pricing around a proxy for, for twenty years, because nobody built the real one.**

**Sources:** Wikipedia, *Podcast* (RSS enclosure proposal, Tristan Louis, Oct 2000; Dave Winer implementation; Ben Hammersley coining "podcast," Feb 2004; Adam Curry and *Daily Source Code*, Aug 2004; Apple iTunes 4.9, June 2005); Wikipedia, *Odeo* (founding 2004, launch July 2005, Evan Williams and Obvious Corporation); Wikipedia, *Spotify* (Gimlet Feb 2019, Parcast Mar 2019, The Ringer Feb 2020 acquisitions); Wikipedia, *The Joe Rogan Experience* (launch Dec 2009; Spotify exclusive deal announced May 2020, ~$200M; February 2024 non-exclusive renewal, ~$250M); IAB Podcast Measurement Technical Guidelines (download definition and standardisation rationale); this vault's `industries/podcasting-networks.md`.
