# The Conversion Window Nobody Justified

**Niche:** [[niches/programmatic-ad-platforms/outcome-feedback-and-bid-valuation/profile|Outcome Feedback & Bid Valuation]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every number in the campaign depends on a thirty-day window and a last-touch rule that were set by convention years ago and have never been tested against anything.
**Tags:** #hypothesis-testing #causal-inference #confidence-intervals #evaluation-metrics #descriptive-statistics #revenue-impact #quick-win #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to join the sale back to the impression that caused it and price the bid against that rather than against a click — and whoever closes that loop changes what every impression in the market is worth.

## The Problem
Thirty days post-click, one day post-view, last touch. Those three conventions determine which channel gets credit for every sale an advertiser makes, which determines where the budget goes next quarter, which determines what the whole market bids. Nobody chose them for this advertiser, this product, this purchase cycle. A business selling a considered purchase with a four-month cycle and one selling an impulse item use the same window, and both report their results as if they were measurements. The convention is so embedded that its arbitrariness is no longer visible to the people relying on it.

## Why It's Still Broken
The conventions came from early tooling defaults and became the basis of contracts, benchmarks and bonus structures, which makes changing them look like moving the goalposts. Testing a window requires an experiment rather than a report, and nobody owns running one. Every party's reported performance depends on the current settings, so nobody is motivated to discover they are wrong. And the numbers look authoritative in a dashboard.

## What a Fix Looks Like
Derive the window instead of inheriting it. Estimate the actual conversion delay distribution per advertiser and product from their own data, which is a short piece of analysis on data already held and typically shows the standard window is badly wrong in one direction or the other — this is the fix and it needs no new infrastructure. Report the share of conversions falling outside the current window, which is the single most persuasive number available and is almost never computed. Show results under several windows side by side so the sensitivity is visible, since a result that reverses between a seven and a thirty day window was never a finding. Replace last touch with a stated model whose assumptions are written down, not because any model is correct but because an unexamined rule is worse than an examined one. Validate the choice against incrementality experiments where they exist, which is the only external check and connects this to the experimentation niche. Separate the window used for optimisation from the one used for reporting, as they serve different purposes and conflating them is why neither is right. Handle the long tail explicitly for considered purchases, where most of the value sits outside any conventional window. Recompute periodically, since purchase cycles change with price, product and season. Publish the methodology to the advertiser, because a number whose derivation is unstated will be renegotiated rather than trusted. And track how much reported performance moves when the window is corrected, which tells everyone how much of the current reporting was an artefact.

## Who Feels the Pain
Advertisers allocating budget on artefacts; channels credited or starved by a default; and platforms optimising to a target nobody has justified.

## Impact If Fixed
Three inherited conventions determine credit for every sale and therefore what the whole market bids. Estimating the real delay distribution per advertiser is short analysis on data already held, and the share of conversions falling outside the current window is the number that ends the argument.
