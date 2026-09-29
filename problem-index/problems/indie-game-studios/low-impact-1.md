# Store Presence and Wishlist Conversion

**Industry:** [[indie-game-studios|Indie Game Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Capsule art, trailer, screenshots and the first paragraph determine whether anyone wishlists, and studios choose them by asking their Discord.
**Tags:** #cnns #transformers #bert #contrastive-learning #gradient-boosting #hypothesis-testing #evaluation-metrics #confidence-intervals

## The Problem
A store page is the conversion surface for every marketing effort a studio makes. Capsule art determines whether a browsing player clicks; the trailer's first eight seconds determine whether they keep watching; the screenshots and short description determine whether they wishlist. These assets are produced once, early, usually by whoever on the team can draw, and revised rarely.

Nobody knows whether they work. A studio sees wishlist totals and cannot decompose them into impressions, click-through and conversion in any actionable way, so a page that converts poorly looks identical to a game nobody has heard of. Platform-side experimentation exists in limited form and is unfamiliar to most small studios, and the sample sizes available to a game with modest traffic make naive comparison unreliable.

The stakes are concentrated. Festival and sale visibility events deliver a large impression spike into the same page; a page converting at half the rate it could wastes the one moment of attention a studio gets.

## What Already Exists
Steam provides wishlist reporting, traffic sources, and limited store page experimentation for eligible titles. Third-party services estimate visibility and sales from review counts. Trailer and capsule art critique circulates through developer communities, conference talks and consultancies, as craft knowledge rather than as evidence. Marketing agencies serving games do this work for a fee, drawing on their own portfolio experience. Genre conventions are strong and well understood by practitioners, and enforced largely by imitation.

## The Customisation Gap
The craft knowledge is real and is entirely uncalibrated. Advice like "show gameplay in the first three seconds" or "make the capsule readable at thumbnail size" is probably right and has never been measured against outcomes across a corpus, so a studio cannot distinguish the rules that matter from the rules that are fashion.

The measurable version needs a corpus: capsule art, trailers and store copy across many titles, coded by content attributes and joined to conversion performance by genre and traffic source. That supports the question a studio actually has, which is not "is my art good" but "does this specific choice convert for this genre" — and it transfers across studios in a way one studio's A/B test never can.

The second gap is that experimentation is inaccessible where it matters most. Small titles have too little traffic for reliable within-title tests, which is exactly the population that most needs the answer. Borrowing strength from a cross-title model is the only route, and it is what a corpus makes possible.

The third is timing. Asset decisions are made once at the start of a campaign, when the studio knows least, and rarely revisited before the visibility event where they matter most. Treating the store page as something that is iterated against evidence through the pre-launch period is a change in practice that the current tooling neither supports nor suggests.

## Impact If Solved
Store conversion multiplies every other marketing effort and is set by a handful of assets chosen on instinct. A cross-title attribute model lets a small studio benefit from evidence its own traffic could never produce, and it targets exactly the moment — the festival or sale spike — where a conversion difference converts directly into the launch velocity that determines everything downstream.
