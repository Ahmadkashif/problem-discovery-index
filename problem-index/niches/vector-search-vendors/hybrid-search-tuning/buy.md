# Learning to Rank

**Niche:** [[niches/vector-search-vendors/hybrid-search-tuning/profile|Hybrid Search Tuning]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Web search solved combining many relevance signals into one ranking twenty years ago with learning to rank, and vector search combines two signals with a constant.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #cross-validation #hypothesis-testing #confidence-intervals #transfer-learning #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to set the balance between lexical and dense retrieval from the customer's own evidence rather than from a documentation default — and whoever does that takes the account, because the setting is free to change and nobody knows what theirs should be.

## The Problem
Combining heterogeneous relevance signals into a ranking is the problem learning to rank was built for, with a substantial literature, mature implementations, well-understood objectives and established practice for training from implicit feedback. Search engines have used it at scale for two decades. Vector search combines a lexical score and a dense score with a weighted sum whose weight is a constant in a configuration file.

## What Already Exists
Learning-to-rank methods spanning pointwise, pairwise and listwise objectives with mature gradient-boosted implementations; click models for deriving relevance from implicit feedback while correcting for position bias; counterfactual and unbiased learning-to-rank for training on logged interactions; feature engineering practice for ranking; and online evaluation with interleaving.

## The Customization Gap
The adaptation is to few signals, sparse feedback and a consumer that is a language model. It requires: (1) working with tens or hundreds of labels rather than millions of clicks, which makes the heavy models inappropriate and a well-regularised simple one correct — this constraint is the main departure and is under-appreciated, since the field's instinct is to reach for the large model; (2) feedback signals that are generation acceptance rather than clicks, where the click model machinery transfers with the position bias correction intact; (3) set-level objectives, because the consumer reads several documents together and complementarity matters in a way pure ranking objectives do not capture; (4) query-conditional weighting rather than a single global model, which is where most of the gain is and which the literature supports directly; and (5) interleaving for online evaluation, which is the cheapest reliable way to compare two retrieval configurations and is unused in this category.

## Target Customer
Vector search vendors, retrieval engineering teams, and the search relevance community for whom this is a large adjacent market with none of its methods.

## Impact If Solved
Learning to rank is twenty years mature and this category uses a constant. The binding constraint is sparse labels, which argues for a small regularised model rather than the field's instinct, and interleaving is the cheapest reliable comparison nobody here runs.
