# Visual Search Practice

**Niche:** [[niches/digital-goods-marketplaces/asset-discovery/profile|Asset Discovery]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Visual and multimodal search is a strong, widely available capability, and it was built to find pictures of things rather than assets that feel right and work with your software.
**Tags:** #contrastive-learning #transformers #transfer-learning #evaluation-metrics #dimensionality-reduction #word-embeddings #confidence-intervals #revenue-impact
**Contested on:** This niche is not terminal — matching an aesthetic intent and establishing technical fit are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Multimodal retrieval is one of the better-served capabilities available: joint image-text embedding models are strong, open, cheap to run and straightforward to integrate, and stock photography and ecommerce have deployed them successfully. Digital goods marketplaces adopted the same models and got a modest improvement, because those models were trained to associate images with descriptions of their content, and the queries here are about style, usability and technical compatibility rather than about what is depicted.

## What Already Exists
Joint image-text embedding models; approximate nearest neighbour infrastructure at scale; visual similarity and more-like-this retrieval; multimodal query understanding; and learned ranking over retrieval candidates.

## The Customization Gap
The adaptation is from content retrieval to intent-and-fit retrieval. It requires: (1) style representations learned separately from subject, since general embeddings entangle them and a buyer wanting a restrained feel gets results about restrained subjects — this entanglement is the specific technical obstacle and general models will not resolve it; (2) the asset itself rather than a preview image as the object of search, because a template's value is in its structure, its layers and its editability, none of which a thumbnail expresses; (3) constraint filtering on technical attributes as a hard requirement rather than a soft ranking signal, which retrieval stacks treat as an afterthought and which here decides whether the purchase is usable at all; (4) interactive refinement as the primary interface, since the query cannot be stated up front and one-shot retrieval is the wrong interaction model; and (5) creator income as an explicit ranking consideration, because a pure relevance ranking concentrates earnings in a way that erodes the supply side.

## Target Customer
Digital goods and creative asset marketplaces, stock and template platforms, and search vendors for whom aesthetic and compatibility retrieval is unserved.

## Impact If Solved
General embeddings entangle style with subject, which is the specific obstacle and one that better general models do not fix. Searching the asset rather than its preview, and treating technical constraints as hard filters, are what make results usable.
