# A Household IP and a Window

**Niche:** [[niches/audio-adtech-networks/attribution-and-independence/profile|Attribution & Independence]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Advertisers buy audio on a household IP matching a website visit, nobody publishes that method's error rate, and the companies that used to check it now belong to the sellers.
**Tags:** #bayesian-inference #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance #graph-theory #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to establish that hearing an advertisement caused something, credibly enough to be believed by a buyer — and whoever does that from a position the sellers do not own becomes the channel's only referee.

## The Problem
A listener downloads an episode from a household address. Later, a visit to the advertiser's site arrives from the same address within a window, and the conversion is attributed to the advertisement. That match degrades under carrier-grade address translation, virtual private networks, address rotation and shared networks, and it cannot see a listener who heard the advertisement at home and converted from an office or a phone on a mobile network. Its false positive rate and its false negative rate are both unknown and both substantial, it is the method the channel's commercial case rests on, and it is operated by parties selling the inventory.

## Why Nobody Has Built This
Better attribution requires either identity the channel does not have or experiments the channel does not run, and both are more expensive than the current method — the cheap method is entrenched because the alternatives cost money and the incumbent does not. Publishing an error rate would reduce reported performance. The independent providers have been acquired, removing the parties who might have improved the method competitively. And advertisers have accepted the arrangement long enough that it reads as normal.

## What to Build
Improve the method and separate the measurer. Publish the error rate, with false positives and false negatives estimated on a validation sample, which is the fix and is the disclosure that would change the market immediately — a method with a stated error rate can be relied on proportionately, and one without cannot be relied on at all. Model the match probabilistically rather than treating it as a binary, since the address evidence has varying strength and a confidence-weighted attribution is both more honest and more useful. Quantify the cross-device and out-of-household loss, which is a known blind spot that nobody sizes and which systematically understates the channel. Use incrementality experiments as the anchor, since geographic and show-level holdouts are runnable in audio and are the only evidence not derived from the match. Combine multiple signals — match, promotional codes, surveys, direct response — with stated weights rather than relying on one. Establish independence structurally through advertiser or industry funding, which is the governance half and is what makes any of the statistical work believed. Standardise the method so seller-produced numbers are comparable. Validate against the advertiser's own data, which is the one source neither seller controls. Report attribution alongside exposure, connecting to the sibling niche, since a conversion attributed to an unheard advertisement is a compounding error. And measure whether the channel's honest effect is larger or smaller than claimed, because it may well be larger and nobody can currently demonstrate it.

## Target Customer
Advertisers and their measurement functions, industry bodies, and the independent measurement operators who could re-form outside the platforms.

## Impact If Built
The cheap method is entrenched because the alternatives cost money and the incumbent does not, and its error rate is unknown in both directions. Publishing that rate lets the method be relied on proportionately, and experiments are the only evidence not derived from the match itself.
