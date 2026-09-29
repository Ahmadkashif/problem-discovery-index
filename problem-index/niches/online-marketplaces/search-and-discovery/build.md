# One Search Box Over Two Different Problems

**Niche:** [[niches/online-marketplaces/search-and-discovery/profile|Search & Discovery]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same ranking system serves a buyer who knows exactly which product they want and a buyer who is browsing for something they could not name, and optimising for either degrades the other.
**Tags:** #k-nearest-neighbors #gradient-boosting #evaluation-metrics #word-embeddings #confidence-intervals #hypothesis-testing #contrastive-learning #descriptive-statistics
**Contested on:** Not terminal — the contest differs by whether a catalogue exists, and the decomposition is recorded in the profile.

## The Problem
A marketplace runs one ranking model trained on clicks and purchases. It learns what most traffic does, which is search for identifiable products and buy the cheapest reliable offer. Unique inventory has few impressions, fewer clicks and no repetition, so it contributes almost nothing to training and is ranked by a model that has effectively never seen it. The marketplace's differentiated inventory — the reason buyers come rather than going to a general retailer — is systematically disadvantaged by the system meant to surface it, and every improvement to overall relevance metrics makes it slightly worse.

## Why Nobody Has Built This
One ranking system is simpler and its aggregate metrics improve, which is what teams are measured on. The unique inventory's poor performance is invisible in a metric dominated by head traffic. Separating the two requires classifying intent, which nobody built because the search box does not ask. And the buyers who leave because they could not find anything distinctive do not report why.

## What to Build
Detect which problem a session is in and serve it differently. Classify query and session intent — known-item, category browse, open-ended discovery — since serving all three from one ranking is the root of the problem and the classification is tractable from query shape, session behaviour and inventory type. Report relevance metrics separately by intent and by inventory type, because the aggregate is dominated by head traffic and hides that the differentiated inventory is failing — this segmentation alone changes what a search team optimises. Build the browse experience as a first-class surface rather than as a search fallback, since a buyer who cannot name what they want is the marketplace's most valuable visitor and is currently served by a grid sorted by relevance to a query they did not make. Use a different objective for unique inventory, where the goal is exposure and discovery rather than immediate conversion, and measure it accordingly. Share the substrate — the query and item representations, the attribute extraction, the personalisation — since those genuinely generalise and are where the engineering investment belongs. Handle the transition, because a session frequently starts open-ended and becomes specific, and a system that cannot follow that loses the buyer at the moment they became valuable. And report coverage of the inventory in results, since a ranking that only ever shows the same ten percent of listings is a liquidity problem wearing a relevance costume.

## Target Customer
Marketplace search and discovery teams, the operators whose differentiation depends on unique inventory, and the sellers of it.

## Impact If Built
One ranking trained on head traffic systematically disadvantages the inventory that differentiates the marketplace. Reporting relevance by intent and inventory type is what makes that visible, and a first-class browse surface serves the buyer who cannot name what they want.
