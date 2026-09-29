# Forty Versions of the Same Photograph

**Niche:** [[niches/stock-media-marketplaces/search-and-discovery/profile|Search & Discovery]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The first page is one shoot, forty frames apart, and the buyer has to scroll past all of it.
**Tags:** #quick-win #contrastive-learning #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #matrix-decompositions #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to return the asset a buyer actually wanted from a library of hundreds of millions — and whoever ranks on what buyers licensed rather than on what they clicked decides which contributors earn anything.

## The Problem
Contributors upload every usable frame from a shoot, which is rational — more assets means more chances to be found. The result is that a search returns forty nearly identical images from one session, occupying the space where forty different approaches to the subject should be. The buyer, who is looking for variety in order to choose, sees one idea repeated. The contributors with genuinely different work are pushed off the first page by the volume.

## Why It's Still Broken
Ranking scores assets independently, so a set of near-identical high-scoring images all rank highly together — a system that ranks items has no concept of the result set as a whole. Contributors are incentivised by asset count. Near-duplicate detection exists for policy purposes and not for ranking. And result diversity is not measured.

## What a Fix Looks Like
Diversify the result set. Cluster near-duplicates and show one representative with the rest available behind it, which is the fix and immediately multiplies the effective variety of the first page. Measure result set diversity as a ranking metric, since it does not currently exist and is what the buyer experiences. Detect shoot-level grouping rather than only pixel similarity, as frames from one session are the actual unit. Let the buyer expand a cluster, because sometimes the twelfth frame is the right one and hiding it entirely is wrong. Report how much of the catalogue is near-duplicate, which is a number nobody publishes and which reframes several other decisions. Adjust contributor incentives so uploading every frame is not rewarded, since the behaviour is a rational response to the current rules. Apply the same clustering in the review queue, as reviewing forty near-identical submissions individually is the reviewer-side version of the same problem. Test whether diversified results improve licensing, because the hypothesis is testable and the answer would settle it. Show contributors which of their assets are redundant with their own others, as many would prefer to upload fewer and better. And measure buyer scroll depth and refinement, which is the direct symptom and is observable.

## Who Feels the Pain
Buyers scrolling past one idea repeated; contributors with distinctive work crowded out; reviewers processing near-identical submissions; and a catalogue whose apparent size overstates its actual variety.

## Impact If Fixed
A system that ranks items has no concept of the result set as a whole, so near-identical assets rank together. Clustering by shoot and showing one representative multiplies the effective variety of the first page without changing the ranking model.
