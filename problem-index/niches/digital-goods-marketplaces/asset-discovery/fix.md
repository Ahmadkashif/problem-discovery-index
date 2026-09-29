# The Tags the Creator Guessed

**Niche:** [[niches/digital-goods-marketplaces/asset-discovery/profile|Asset Discovery]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Findability depends entirely on words the creator typed once, in a hurry, with no idea what buyers search for, and nobody ever tells them it was wrong.
**Tags:** #word-embeddings #bert #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact #automation #worker-facing
**Contested on:** This niche is not terminal — matching an aesthetic intent and establishing technical fit are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A creator uploads an asset and fills in a tag field. They write the words that describe it to them. Buyers search with different words entirely — a different vocabulary, different level of abstraction, different use-case framing. The asset is never returned for the queries it would have satisfied. The creator sees no sales and concludes the work was not good enough, changes what they make, and the actual cause was a vocabulary mismatch that the platform could measure precisely and has never mentioned. Nothing in the interface tells a creator which searches they nearly matched.

## Why It's Still Broken
Tagging is treated as data entry the creator owes the platform, rather than as a discovery decision the platform should support. Query logs live in the discovery team's systems and never reach creators. There is no shared vocabulary for style or use case, so neither party can converge on one. And the failure is silent — an asset that is never returned produces no signal the creator can see.

## What a Fix Looks Like
Close the loop between queries and tags. Show creators the searches their asset nearly matched but lost, which is the fix, requires only the query logs the platform already keeps, and is immediately actionable — a creator shown ten near-miss queries will fix their listing in five minutes. Suggest tags from the asset itself rather than asking, since the file contains far more than the creator will type and automatic suggestion outperforms manual entry consistently. Map buyer vocabulary to creator vocabulary and translate between them at query time, so the mismatch stops mattering regardless of what anyone types. Publish the searched terms in each category, which tells creators what buyers actually ask for and is information no platform shares. Flag assets with impressions and no clicks separately from those with no impressions, because one is a presentation problem and the other a findability problem and they need opposite fixes. Extract structured attributes automatically — dimensions, formats, software, layers, colours — which are facts about the file rather than opinions and should never have been asked of a creator. Show the creator their asset's impression and click-through counts, which is the basic instrumentation any seller needs and which most platforms withhold. Detect duplicate and near-duplicate tags across a creator's catalogue, since self-competition is common and unnoticed. Let buyers contribute vocabulary through what they save and reject, which is a far larger and better-calibrated source than creators. And measure findability per asset directly, because the assets that are never seen are invisible in every existing report.

## Who Feels the Pain
Creators whose work is good and unfindable; buyers who never see the thing they wanted; and platforms whose catalogue is mostly inert.

## Impact If Fixed
An asset that is never returned produces no signal the creator can see, so they change what they make instead of what they wrote. Showing near-miss queries from logs already kept is a five-minute fix per listing, and file-derived attributes should never have been a creator's job.
