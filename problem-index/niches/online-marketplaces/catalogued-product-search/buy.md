# Learning to Rank and Product Matching

**Niche:** [[niches/online-marketplaces/catalogued-product-search/profile|Catalogued Product Search]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Learning to rank and entity resolution are both mature with strong open implementations, and marketplace offer ranking and product matching are frequently hand-tuned.
**Tags:** #gradient-boosting #k-nearest-neighbors #bayesian-inference #evaluation-metrics #cross-validation #logistic-regression #hypothesis-testing #word-embeddings
**Contested on:** Every serious competitor in this sub-niche is fighting to put the offer a buyer will actually be happy with at the top for an item they already named — and whoever does that takes the transaction, because the same item is one tab away on another marketplace.

## The Problem
Ranking a set of candidates by a learned objective, and deciding whether two listings describe the same product, are both well-solved problems. Learning to rank has mature methods, strong implementations and two decades of deployment. Entity resolution has a formal statistical foundation and good open tooling. Smaller marketplaces frequently rank by a hand-weighted formula and match products by matching identifiers when they exist and by fuzzy title comparison when they do not.

## What Already Exists
Learning-to-rank methods with pairwise and listwise objectives; gradient-boosted ranking implementations; probabilistic record linkage and entity resolution; blocking for scale; product identifier and catalogue reference data; and multimodal matching using images alongside text.

## The Customization Gap
The adaptation is to items whose identity depends on condition and variant. It requires: (1) matching that distinguishes variant and condition rather than collapsing them, since a camera body and the same body with a lens are not the same offer and a matcher that merges them creates disappointment at a scale nobody attributes to matching; (2) images as a primary matching signal for categories where sellers describe badly, which is most of the used-goods world and where the text alone is insufficient; (3) delayed satisfaction labels in the ranking objective, which the build note develops and which is not how learning-to-rank is normally set up; (4) supply-side effects in the objective, since the ranking determines which sellers get exposure and therefore which stay — a consideration web ranking does not have; and (5) counterfactual training from logged interactions, since the ranker's own history determines what was shown and naive training on it reproduces the exposure loop.

## Target Customer
Marketplace ranking and catalogue teams, especially at the many mid-sized marketplaces below the frontier, and the search relevance vendor ecosystem.

## Impact If Solved
Both problems are mature and many marketplaces hand-tune them. Matching that respects variant and condition removes a source of disappointment nobody attributes to matching, and counterfactual training is what stops the ranker learning from a distribution it created.
