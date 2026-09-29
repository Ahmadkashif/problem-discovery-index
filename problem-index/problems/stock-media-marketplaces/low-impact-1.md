# Keywording and Discoverability

**Industry:** [[stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** An asset's income depends on metadata supplied by the person who made it, so excellent work with poor keywords earns nothing and nobody ever finds out why.
**Tags:** #contrastive-learning #cnns #bert #word-embeddings #transfer-learning #k-nearest-neighbors #evaluation-metrics #revenue-impact

## The Problem
A buyer searches. The marketplace returns results ranked by a combination of text match, visual relevance, historical performance and commercial signals. An asset that does not surface does not earn.

Surfacing depends heavily on keywords, which contributors supply. Contributors are photographers and videographers, not search engineers, and the keywords they produce are inconsistent: too few, too many, wrong register, describing what the image is of rather than what it is for.

The gap between those two is the whole problem. A buyer searching for "team collaboration" wants an image that communicates a concept; the contributor described a meeting room with four people and a laptop. Conceptual, emotional and use-case vocabulary is what buyers search and what contributors rarely supply.

Keyword stuffing is the predictable response and degrades the search for everyone, so marketplaces limit and police it, which penalises contributors trying to be thorough alongside those gaming it.

Automatic keywording is deployed and helps, and it tends to describe content rather than concept for the same reason contributors do — it reads the image, and the concept is in the buyer's intent.

And the feedback loop is broken in a specific way: contributors see downloads and not searches. An asset appearing in a thousand searches and chosen in none has a different problem from one never surfacing at all, and the contributor cannot tell which they have.

## What Already Exists
Automatic keywording from image content is standard across the major platforms. Multimodal embedding models have made natural-language search over images genuinely effective, reducing keyword dependence. Visual similarity search is mature. Some platforms provide contributor analytics on views and downloads. Controlled vocabularies exist with varying enforcement.

## The Customisation Gap
Search log data is the unused asset. The marketplace knows exactly what buyers type, which results they view, which they license and which searches return nothing satisfying. That maps buyer vocabulary to asset characteristics directly, and contributors are given a keyword guide instead.

Concept and use-case tagging is shallow. What an image communicates, and what it would be used for, is learnable from the licensing behaviour of similar assets rather than from the pixels alone, which is where content-based keywording plateaus.

Gap identification is absent. Searches that return poor results are a direct statement of unmet demand, and telling contributors what buyers are looking for and not finding is the single most valuable thing a marketplace could give them. Nobody does it.

And diagnostics are missing. A contributor should be able to see whether an asset fails at surfacing, at attracting a click, or at converting the click, because those are three different problems with three different remedies.

## Impact If Solved
Discovery determines income distribution across contributors, and it hinges on metadata written by people with no visibility into how buyers search. Learning buyer vocabulary from search logs, tagging for concept rather than content and reporting demand gaps redistributes discovery toward asset quality and gives contributors the first genuine feedback they have ever had.
