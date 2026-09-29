# Search That Understands What an Asset Is

**Industry:** [[game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Hundreds of thousands of assets are searched by keyword against creator-written titles, so finding the right one depends on guessing the word the creator used.
**Tags:** #contrastive-learning #cnns #transformers #bert #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #autoencoders

## The Problem
Marketplace search operates on titles, tags and descriptions written by creators who are optimising for discoverability, which produces listings stuffed with every plausibly relevant term. A search for a specific kind of environment prop returns hundreds of results dominated by large packs whose titles mention everything, and the specific thing the developer wants is either buried or described using a word they did not try.

Style matching is the harder failure. A developer building a coherent project needs assets that sit together visually, and style is the property no keyword captures. The usual workaround is finding one creator whose work fits and buying everything they make, which constrains the project to that creator's catalogue.

Visual search exists in some products and is generally similarity over thumbnails, which matches the rendered presentation rather than the asset. Two models with identical geometry can have completely different thumbnails, and two visually similar thumbnails can be a game-ready low-poly asset and a film-quality one unusable in real time.

## What Already Exists
All the major marketplaces have keyword search with category filters and sorting. Sketchfab, now part of Fab, brought genuine 3D preview and some similarity search. ArtStation and the wider 3D marketplaces have visual browsing. Quixel's library established structured, consistently-captured scan data as an alternative to heterogeneous marketplace listings. Recommendation exists in basic collaborative forms. Some marketplaces support filtering by polygon count and format where creators supply the metadata, which they do inconsistently.

## The Customisation Gap
Search should operate on the asset, not on the listing text. Representations learned from geometry, materials, textures and — for audio and code — their own content, support retrieval by what the thing actually is, independent of what the creator called it. That is the foundational fix and it removes the keyword-guessing game entirely.

Style is the second dimension and is the one developers most need. A learned style representation lets a buyer search for assets that sit with what they already have — by uploading their own project's existing assets as the query — which is the real task and which no marketplace supports in any form.

Technical filtering should be automatic rather than creator-declared. Polygon budget, texture resolution, material complexity and platform feasibility are extractable from the files, and making them reliable filters rather than optional metadata immediately removes the mismatch between film-quality and game-ready assets that visual similarity conflates.

And the collection-level structure matters. Buyers typically need a set that works together, not a single asset, and retrieval that assembles a coherent set spanning several creators — matching style, scale, budget and pipeline — is a different and much more useful query than ranking individual listings.

## Impact If Solved
Discovery in these marketplaces is bounded by creator-written text against a catalogue too large to browse, which concentrates sales on a small number of well-marketed listings and leaves most of the corpus unfindable. Content-based retrieval with style matching and automatic technical filtering would surface the long tail, serve the buyer's actual task of assembling a coherent set, and reduce the mismatched purchases that generate refunds and abandoned assets.
