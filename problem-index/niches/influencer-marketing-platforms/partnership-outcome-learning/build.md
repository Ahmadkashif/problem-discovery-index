# A Corpus Powering a Search Filter

**Niche:** [[niches/influencer-marketing-platforms/partnership-outcome-learning/profile|Partnership Outcome Learning]]
**Industry:** [[industries/influencer-marketing-platforms|Influencer Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platforms hold which creators worked with which brands, with what content, at what price, against what response, across thousands of campaigns — and use it to power a search filter.
**Tags:** #gradient-boosting #bayesian-inference #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact #matrix-decompositions #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn a corpus of thousands of past partnerships into the answer to the only question the category is asked — and whoever closes that loop makes every subsequent selection better than the last.

## The Problem
A platform has run eleven thousand partnerships. It knows the creator, the brand, the category, the brief, the content, the price, the reach and the engagement for every one. What it does not know, in any usable form, is which of them produced sales — because the sale landed in the brand's commerce system and came back, if at all, as an aggregate figure weeks later. So the corpus has every input and almost no labels, and the platform's answer to which creator should we use is a filtered list. The one thing that would make the category's central decision better sits half-assembled in its own database.

## Why Nobody Has Built This
The outcome is held by the brand and returning it feels like giving away an asset, which is the same obstacle running through this whole cluster and is commercial rather than technical. Platforms are bought for workflow, so selection quality is not what wins the deal. The sample per brand is small, which makes naive analysis unconvincing and has discouraged serious attempts. And nobody has made the case to brands that returning outcomes buys them better selection.

## What to Build
Close the loop and learn across it. Build the outcome return path with a clear exchange — the brand returns outcomes and receives selection that improves — which is the prerequisite and is a commercial proposition rather than an engineering one. Accept coarse and aggregate outcome data, since insisting on row-level returns excludes almost everyone and a campaign-level sales figure is enough to learn from when the decision count is small. Model at the creator-brand-category level so learning transfers, because no single brand has enough partnerships to learn alone and the cross-brand corpus is the platform's actual asset. Carry uncertainty honestly, as forty partnerships produce wide intervals and a system that reports point estimates on small samples will be wrong confidently and lose trust permanently. Estimate the counterfactual — what a comparable creator would have produced — since that is the decision-relevant quantity and a raw outcome is not. Use content features as well as creator features, connecting to the performance prediction work, because what was made matters as much as who made it. Feed learning back into selection, pricing and briefing, which is the whole point and is where a report stops and a product starts. Report to brands what their returned data bought them, since the exchange must be visible to persist. Handle the cold start for new creators and new brands, which is most of the interesting cases. And measure selection quality against the follower-count baseline, because that is the claim.

## Target Customer
Influencer platforms with a partnership corpus, brand measurement teams, and the agencies whose selection expertise is currently experiential.

## Impact If Built
The corpus has every input and almost no labels because the sale lands in the brand's system and never returns. The decision count is small enough that coarse campaign-level outcomes are enough to learn from, which makes the exchange easy to propose and the payoff large.
