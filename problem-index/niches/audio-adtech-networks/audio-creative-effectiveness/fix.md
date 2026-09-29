# Measured by a Promotional Code

**Niche:** [[niches/audio-adtech-networks/audio-creative-effectiveness/profile|Audio Creative Effectiveness]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The campaign's creative is judged on promotional code redemptions, which measure people who wanted a discount and remembered a word, and systematically favour one kind of advertiser.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #quick-win #revenue-impact #causal-inference #bert
**Contested on:** Every serious competitor in this niche is fighting to establish what makes an audio advertisement work when there is no click and no visual — and whoever does that gives the channel the creative discipline every other medium has.

## The Problem
The promotional code is the channel's default response measure. It counts people who heard the advertisement, wanted a discount, remembered a word while not looking at a screen, and typed it later. That is a specific and small subset of everyone the advertisement affected. It over-represents direct-response offers and under-represents brand building, it favours simple memorable codes over good creative, and it fails entirely when the host misreads the code. Creative decisions across the channel are made on this signal, which means the channel's creative is being optimised toward code memorability.

## Why It's Still Broken
The code is the only creative-level response signal that is cheap, immediate and requires no measurement infrastructure — availability standing in for validity once more, in a channel where every alternative costs money. It works well enough for direct-response advertisers, who are a large share of the buyers. Its biases are known informally and never quantified. And correcting it requires the measurement the channel does not have.

## What a Fix Looks Like
Use the code as one signal and correct for what it misses. Estimate the code's capture rate by comparing coded to total response during campaign periods, which is the fix, is computable where the advertiser will share aggregate data, and gives a correction factor nobody currently applies. Add vanity addresses and dedicated landing pages, which capture a different and partly overlapping population at negligible cost. Measure aggregate uplift during and after the campaign against a baseline, since that is the quantity that matters and the code is only a proxy for it. Track post-campaign response, because audio response is delayed and a short code window systematically favours impulse over consideration. Correct for the advertiser type, since the code's bias differs enormously between a subscription offer and a brand campaign and a single method serves neither. Run holdouts by show or geography where the volume permits, which is the only clean evidence. Combine code, address, survey and uplift signals rather than choosing one, since each is biased differently. Report what share of response the code plausibly captured, so nobody mistakes it for the total. Use the same method consistently so creative comparisons over time are valid. And stop optimising creative toward code memorability, because that is what the current measurement quietly rewards and it is not the same as making a better advertisement.

## Who Feels the Pain
Brand advertisers whose effect is invisible in the channel's default measure; hosts whose reads are judged on code recall; and the category, whose creative is optimised toward a measurement artefact.

## Impact If Fixed
Availability stands in for validity again, and the channel's creative is being optimised toward code memorability rather than persuasion. Estimating the code's capture rate against total response during the campaign gives a correction factor that is computable today.
