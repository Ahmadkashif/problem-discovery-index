# Game Asset Marketplaces

## Profile
**Category:** Gaming & Interactive
**Market Size:** ~$1.5B US in game-ready art, audio, code and tooling sold through marketplaces, plus the wider 3D content market that overlaps it
**Tech Maturity:** Storefront-grade. Unity Asset Store, Epic's Fab, itch.io, ArtStation, TurboSquid and CGTrader run search, payments and delivery competently and treat a shader, a character model, an audio pack and a runtime plugin as interchangeable listings with a thumbnail and a category. The question every buyer is actually asking — will this work in my project, at my engine version, on my target platform, within my performance budget — is answered by buying it and finding out.
**Workforce:** Marketplace and platform engineers, curation and review staff, asset creators selling as individuals or small studios, technical artists and developers on the buying side, licensing and compliance staff

## Key Pain Themes
The purchase decision is made on screenshots and a description, and the cost that matters is not the price. An asset that does not match the buyer's engine version, render pipeline, physics setup or platform target costs hours of integration work or is discarded — and none of that is visible before purchase. Engine upgrades break assets routinely, and the marketplace has no concept of an asset's compatibility surface.

The second theme is provenance, which has become the category's sharpest problem. Marketplaces have always dealt with stolen and resold assets; generative tooling has added a harder question about what a model was trained on and whether a listing is original work, a derivative, or a repackaged scrape. Platforms have adopted disclosure policies of varying strictness and have limited ability to verify any of them.

The third is creator economics. Discovery is concentrated, most listings sell very little, and the creators who do succeed acquire an unbounded support obligation across engine versions that they carry personally and indefinitely.

## Current Tech Landscape
Unity Asset Store and Epic's Fab — which consolidated the Unreal Marketplace, Quixel and Sketchfab — dominate engine-adjacent sales. itch.io serves the indie and experimental end; ArtStation, TurboSquid and CGTrader serve the wider 3D market including non-game uses. Search is keyword and category based with some visual similarity in the more recent products. Review and curation processes exist and are largely manual. Licence terms are standardised per marketplace and enforced reactively. Generative asset disclosure policies have been introduced across the category and rely on creator declaration.

## Problems
- [[problems/game-asset-marketplaces/high-impact|🔴 High Impact: You Cannot Tell If It Will Work Until You Have Bought It]]
- [[problems/game-asset-marketplaces/low-impact-1|🟡 Low Impact: Search That Understands What an Asset Is]]
- [[problems/game-asset-marketplaces/low-impact-2|🟡 Low Impact: Provenance and Licence Verification]]
- [[problems/game-asset-marketplaces/worker-life-1|🟢 Worker Life: The Creator Supporting Six Engine Versions Forever]]
- [[problems/game-asset-marketplaces/worker-life-2|🟢 Worker Life: The Technical Artist Making Other People's Assets Fit]]
- [[problems/game-asset-marketplaces/ml-opportunity|🧠 ML Opportunities]]
- [[problems/game-asset-marketplaces/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These marketplaces hold the assets themselves — geometry, textures, materials, audio, shaders and code — and sell them through an interface that reads only the title, the tags and the thumbnail. Everything a buyer needs to know is computable from the file: polygon and texture budgets, render pipeline dependencies, engine version compatibility, platform feasibility, and similarity to every other asset in the catalogue including the ones it may have been derived from. The category has built a storefront on top of a technical corpus and has never analysed the corpus. Doing so answers the purchase question, the search question and the provenance question at once, which is an unusually good ratio for a single body of work.
