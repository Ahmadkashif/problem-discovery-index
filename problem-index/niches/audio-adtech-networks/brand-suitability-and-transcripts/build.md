# The Same Blocklist Mistake in a New Medium

**Niche:** [[niches/audio-adtech-networks/brand-suitability-and-transcripts/profile|Brand Suitability & Transcripts]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Transcription made audio content readable, and the industry used it to build the same blunt keyword blocklists that defunded news on the open web.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to judge whether an episode is suitable for a brand rather than whether it contains a word — and whoever does that stops audio repeating the mistake that defunded news on the open web.

## The Problem
An episode of a serious current affairs podcast discusses a conflict. The transcript contains the relevant words. A brand's blocklist excludes it, and excludes most of the show's back catalogue, and the show's advertising revenue falls. Meanwhile a low-value show with no substantive content contains none of the words and is fully monetised. This is precisely what happened on the open web a decade ago, it is documented, the people building audio brand safety know about it, and the tooling being deployed reproduces it — because a word list is what the interface accepts and a transcript makes word matching easy.

## Why Nobody Has Built This
Transcription arrived and the first thing built on it was the thing that was cheapest to build, which was matching — the capability enabled the naive application before anyone designed the sophisticated one. Blocklists are the control advertisers know how to operate. The harm falls on publishers rather than on the party choosing the list. And judging suitability properly requires an advertiser-specific model that nobody sells.

## What to Build
Judge the episode, not the words. Assess suitability from the transcript's meaning using standard language models, which is the fix and is available now at low cost — distinguishing a report about a tragedy from content endorsing one is straightforward for a model and impossible for a list. Make suitability advertiser-specific, since brands genuinely differ and a universal standard suits none of them, which is the same finding as in the programmatic contextual work. Assess at episode and segment level rather than at show level, because a show is not uniform and blocking an entire back catalogue for one episode is the most damaging and most common error. Use the transcript's richness — speaker, tone, segment, framing — which is information a web page does not carry and which nobody is using. Report what a suitability rule costs in reach and inventory quality, so the trade-off is visible at the moment the rule is set. Prune existing lists by testing each term's actual effect, since most terms in a mature list exclude nothing unsuitable and a lot of good content. Give publishers a route to contest exclusion, which surfaces errors nobody else will find. Detect the genuinely unsuitable — the content advertisers actually want to avoid — which is a small and identifiable set that word lists both miss and over-reach. Publish the approach, since the open web's history makes this a credibility issue as much as a technical one. And report exclusion rates by publisher, so systematic defunding of serious audio is visible before it becomes entrenched.

## Target Customer
Advertisers and agencies setting audio suitability policy, platforms implementing it, and the publishers of serious audio whose revenue depends on getting this right.

## Impact If Built
Transcription enabled the naive application before anyone designed the sophisticated one, and the medium is reproducing the open web's documented mistake. Meaning-level assessment is available now at low cost, and segment-level judgement prevents an entire back catalogue being blocked for one episode.
