# Guessing the Word the Creator Used

**Niche:** [[niches/game-asset-marketplaces/asset-discovery/profile|Asset Discovery & Search]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The buyer searched four synonyms, found nothing, and the asset was listed under a fifth.
**Tags:** #quick-win #word-embeddings #evaluation-metrics #descriptive-statistics #data-integration #automation #large-language-models #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to let a buyer find the right asset among hundreds of thousands without guessing the word the creator happened to type — and whoever solves that takes the account.

## The Problem
The everyday failure is vocabulary. Creators name assets in their own terms — regional, stylistic, idiosyncratic, sometimes in another language. Buyers search in theirs. The catalogue contains what the buyer wants and the search returns nothing or a poor approximation. The buyer either buys something worse, goes elsewhere, or commissions the work. None of these outcomes is visible to the platform as a failure.

## Why It's Still Broken
The search matches strings — a lexical index cannot know that two different words name the same thing, and every mismatch looks like an empty catalogue rather than a search failure. Nobody analyses zero-result queries. Tags are creator-supplied and inconsistent. And a failed search leaves no trace anyone reviews.

## What a Fix Looks Like
Mine the failures and expand the vocabulary. Analyse zero-result and no-click queries, which is the fix and immediately names the vocabulary gaps rather than theorising about them. Build a synonym and alias map from those queries plus the catalogue's own language, since the mapping is derivable from data already collected. Expand queries semantically rather than matching strings exactly. Generate supplementary tags automatically from thumbnails and file contents, which fixes the catalogue rather than the query. Suggest better terms to creators at listing time, as most are guessing and would accept help. Handle plurals, spellings and non-English terms, which are a surprisingly large share of the failures. Show near matches rather than an empty page, because an empty result ends the session. Track searches that ended without a purchase as a product metric, which is the missing accountability. Compare the vocabulary buyers use against the vocabulary creators use and publish the gap. And prioritise the categories with the worst failure rates rather than improving search uniformly.

## Who Feels the Pain
Buyers who could not find what existed; creators whose listings are invisible for the wrong reason; marketplaces losing sales they never see; and studios commissioning work they could have bought.

## Impact If Fixed
A lexical index cannot know that two different words name the same thing, and every mismatch looks like an empty catalogue rather than a search failure. Mining zero-result queries names the gaps and fixes them with a synonym map.
