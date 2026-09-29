# A Buyer Who Cannot Name What They Want

**Niche:** [[niches/online-marketplaces/unique-item-discovery/profile|Unique Item Discovery]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The buyer for a one-of-a-kind item is browsing for something they could not describe, and the interface offers them a search box and a category tree built by somebody else.
**Tags:** #contrastive-learning #k-nearest-neighbors #word-embeddings #cnns #evaluation-metrics #manifold-learning #dimensionality-reduction #transfer-learning
**Contested on:** Every serious competitor in this sub-niche is fighting to put a one-of-a-kind item in front of a buyer who could not have named it — and whoever does that takes the market, because the competitor is the buyer giving up and going somewhere generic.

## The Problem
A buyer wants something for a room. They know the feeling they are after and cannot name the style, the period, the material or the maker. They type a word, get results that are technically relevant and completely wrong, browse two category pages, and leave. Elsewhere on the same marketplace sits an item they would have bought instantly on seeing it. The distance between them is a representation problem: the item's photograph contains what the buyer wants and the platform's index is built on the seller's words and a category somebody chose from a dropdown.

## Why Nobody Has Built This
Search interfaces came from text retrieval and the search box is the default even where it does not fit. Visual and stylistic representation was expensive until recently and the assumption that it is exotic has not updated. Browse is treated as what happens when search fails rather than as the primary mode for this inventory. And the buyer who leaves generates a session with no query and no click, which is the least analysed event in the platform.

## What to Build
Build the representation and the browse surface together. Represent every item from its images primarily and its text secondarily, in a joint space where similarity means what a buyer means by similar — which is the foundation and is now tractable at a cost that would have been prohibitive three years ago. Let a buyer express preference by example rather than by query: more like this, less like that, this but in wood, which is how these buyers actually think and which no marketplace interface supports. Build a browse surface that learns within a session, since a buyer's taste becomes apparent over a dozen interactions and starting each page from the same ranking discards it. Interpret the seller's description rather than indexing it literally, extracting style, period, material, technique and condition from prose written by somebody with no vocabulary for the platform's taxonomy. Surface complements and adjacencies, since a buyer looking at one thing is frequently open to a related thing they would never have searched for. Use the browse behaviour of buyers who did convert as the training signal, since clicks on unique items are sparse and session trajectories are not. Report discovery outcomes separately from search outcomes, because this surface's success is a purchase the buyer could not have initiated and no search metric captures it. And treat the no-query session as a first-class event to analyse, since it is currently the most common and least examined thing that happens.

## Target Customer
Marketplaces whose differentiation is unique inventory, the buyers browsing them, and the sellers whose distinctive items are invisible.

## Impact If Built
The item's photograph contains what the buyer wants and the index is built on the seller's words. A joint visual and textual representation with preference-by-example is how these buyers actually think, and the no-query session is the most common event nobody analyses.
