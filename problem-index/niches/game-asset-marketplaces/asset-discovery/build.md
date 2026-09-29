# Searching the Content, Not the Title

**Niche:** [[niches/game-asset-marketplaces/asset-discovery/profile|Asset Discovery & Search]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The marketplace holds the assets and searches the titles.
**Tags:** #contrastive-learning #word-embeddings #k-nearest-neighbors #dimensionality-reduction #evaluation-metrics #transformers #data-integration #manifold-learning
**Contested on:** Every serious competitor in this niche is fighting to let a buyer find the right asset among hundreds of thousands without guessing the word the creator happened to type — and whoever solves that takes the account.

## The Problem
A buyer needs a medieval market stall that fits a stylised art direction, under a polygon budget, for a mobile target. They type words into a box that matches against titles and tags written by thousands of creators with no shared vocabulary. The right asset exists and is described as a "fantasy vendor booth". The search fails, the buyer scrolls, and a substantial share of purchase intent is lost at exactly this point.

## Why Nobody Has Built This
Keyword search was adequate when catalogues were small and has scaled badly without anyone re-examining it. Content-based retrieval over 3D assets is genuinely harder than over text. Creators supply tags for free. And search quality is diffuse — nobody owns a number that measures it.

## What to Build
Index the content and let the buyer search by example. Build joint embeddings over geometry, texture and rendered appearance so assets can be retrieved by content rather than by label, which is the core and is the capability the whole category lacks. Support search by example — an image, a reference asset, a sketch — since buyers frequently know what they want and cannot name it. Interpret natural-language queries semantically rather than lexically, which closes the vocabulary gap between buyer and creator. Let style be a browsing dimension, as art direction is the actual constraint and no facet expresses it. Combine content search with the technical profile so results are both right and usable, which is where this compounds with compatibility analysis. Rank by what buyers kept and used rather than by what sold, since a returned asset is a failed result. Generate tags automatically for the existing catalogue, which immediately improves even the keyword path. Show similar assets from other creators on every listing, which converts a near-miss into a purchase. Handle audio with its own representation rather than by name alone. And measure search success by whether the buyer purchased and kept, which is the number nobody currently owns.

## Target Customer
Asset marketplaces and storefronts, studios buying at volume, 3D search vendors, and engine ecosystem operators.

## Impact If Built
Finding the right asset currently depends on guessing the word the creator typed. Joint content embeddings with search by example close the vocabulary gap where most purchase intent is lost.
