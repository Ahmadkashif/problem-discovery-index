# The Branded Search Conversion

**Niche:** [[niches/retail-media-networks/incrementality-and-cannibalisation/profile|Incrementality & Cannibalisation]]
**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Type:** Fix (Pain Point)
**One-liner:** A shopper types the brand name, clicks the sponsored result for that brand, and the network books it as a sale the advertisement produced.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #causal-inference #confidence-intervals #quick-win #revenue-impact #bert
**Contested on:** Every serious competitor in this niche is fighting to report what a sponsored placement actually caused, net of the organic sale it displaced — and whoever brands trust to produce that number sets the terms on which the category's spend is renewed.

## The Problem
A large share of retail media conversions come from queries containing the advertised brand's own name. The shopper already knew what they wanted, typed it, and clicked the top result, which happened to be sponsored. These conversions have the highest reported return in the account and the lowest plausible incrementality of anything in advertising, and they are aggregated into the same headline number as genuinely discovered purchases. Brands are therefore paying the retailer to intercept their own existing demand, at a price set by an auction against their own competitors, and being shown a return figure that makes it look like the best money they spend.

## Why It's Still Broken
Reporting aggregates across query types, which merges the least incremental conversions with the most and makes the distinction invisible — a single split would expose it and no report offers one. Defending a brand's own terms against competitor bids is a genuine need, which gives the practice a legitimate-sounding rationale that has never been tested. The retailer earns most from exactly these clicks. And brands fear that withdrawing lets a competitor take the slot.

## What a Fix Looks Like
Split the reporting by intent. Report branded, category and generic query performance separately as a standard breakdown, which is the fix, requires only a query classification the network already has, and changes the conversation the moment it is produced. Measure branded-query incrementality directly by suppressing the brand's own advertisement on its own terms for a shopper sample, which is a clean, cheap experiment and settles the argument with evidence rather than assertion. Report what the organic listing achieves without the advertisement above it, since that is the comparison the brand needs and is trivially observable during suppression. Test the defensive rationale, as whether a competitor actually takes the slot and converts is an empirical question that is answered in a week and is universally assumed rather than checked. Show the price paid for intercepting existing demand explicitly, which is the number brand finance teams ask for and never receive. Give the retailer credit where it is genuine, because the discovery cases are real and lumping them with branded defence damages the honest half of the business. Let brands set different targets by query type, which is how any rational buyer would operate and which current tooling does not permit. Report category-level cannibalisation alongside, since brands bidding on each other's terms transfers margin to the retailer without growing the category. Standardise the breakdown across retailers, so brands can compare. And publish the branded share of reported return, because that one figure reframes every conversation in the category.

## Who Feels the Pain
Brands paying to intercept demand they already had; category merchants whose organic ranking quality is unrewarded; and retailers whose most defensible business is obscured by its least defensible part.

## Impact If Fixed
Branded conversions have the highest reported return and the lowest plausible incrementality, and aggregation merges them with genuine discovery. A query-type split uses a classification already held, and suppressing a brand's own advertisement on its own terms settles the defensive rationale in a week.
