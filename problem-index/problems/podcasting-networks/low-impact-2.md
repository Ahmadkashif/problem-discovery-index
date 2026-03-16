# Cross-Promotion Audience Overlap Analysis

**Industry:** [[podcasting-networks|Podcasting Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Networks cross-promote shows blindly, wasting promo slots on audiences that already subscribe to both shows instead of targeting listeners most likely to convert.
**Tags:** #gradient-boosting #recommendation #tabular-ml

## The Problem
Podcast networks routinely insert cross-promo ads — "If you like this show, check out our other show" — across their catalog. The selection of which shows to cross-promote is driven by producer intuition or simple category matching, not by actual audience overlap data. A network with 30 shows has 870 possible pairwise cross-promo combinations; choosing the right ones determines whether promo slots drive incremental subscribers or waste inventory on listeners who already follow both shows.

## What Already Exists
Chartable's SmartPromos product measures cross-promo attribution (did listener X subscribe to Show B after hearing a promo on Show A) but only evaluates campaigns after they run. Spotify's internal tools provide some overlap data for Spotify-exclusive shows, but this data is not available to independent networks. No tool proactively recommends cross-promo pairings optimized for incremental reach.

## The Customisation Gap
The needed system combines download-timing correlation analysis (listeners who download Show A and Show B within the same session vs. different days), content similarity scores (transcript-level topic overlap), and demographic overlap estimates to classify each show pair as high-overlap (promo will waste a slot), low-overlap-high-affinity (promo will convert), or low-overlap-low-affinity (promo will not convert). This requires podcast-specific behavioral signals that generic recommendation frameworks do not model — particularly the distinction between "overlapping audience" and "adjacent audience likely to convert."

## Impact If Solved
Networks could increase cross-promo conversion rates by 2-3x, adding 500-2,000 incremental subscribers per promoted show per month — compounding into meaningful audience growth that directly increases ad revenue and show viability.
