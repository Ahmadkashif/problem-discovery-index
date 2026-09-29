# Similarity & Derivation Detection

**Parent Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to tell whether an uploaded asset matches something already in the catalogue after retopology, rescaling, recolouring and format conversion — and whoever builds that detector takes the account.

## Profile
**Market Size:** ~$170M US
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** Very low — nothing runs
**Target Buyer:** Marketplace engineering and trust teams
**Automation Potential:** Very high — representation learning over the corpus

## What Makes This a Distinct Niche
This half is computable. The platform holds the files; the question is whether a new upload is substantially the same as an existing one after the transformations sellers actually apply. It is a representation and retrieval problem over geometry, textures, materials and audio, it runs as a detector at upload, and it is worth deploying regardless of what policy regime sits above it. A platform can buy it as a component and decide separately what to do with the matches.

## Current Tools & Gaps
Nothing at most platforms; exact file hashing at a few. The gaps: no geometry representation robust to remeshing; no texture matching under recolouring and resolution change; no cross-format matching; no search across a catalogue of that size at upload latency; and no similarity threshold anyone has calibrated.

## Problems
- [[niches/game-asset-marketplaces/similarity-detection/build|🔨 Build: Matching Through the Transformations Sellers Use]]
- [[niches/game-asset-marketplaces/similarity-detection/buy|🛒 Buy: Near-Duplicate Detection From Image Search]]
- [[niches/game-asset-marketplaces/similarity-detection/fix|🔧 Fix: Rescaled, Recoloured and Relisted]]
