# Information Retrieval and Ranking Evaluation

**Niche:** [[niches/online-marketplaces/search-and-discovery/profile|Search & Discovery]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Information retrieval has fifty years of evaluation methodology and web search two decades of click modelling, and marketplace search is evaluated on conversion.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #gradient-boosting #probability-distributions #descriptive-statistics #cross-validation #logistic-regression
**Contested on:** Not terminal — the contest differs by whether a catalogue exists, and the decomposition is recorded in the profile.

## The Problem
Evaluating a ranking properly — graded relevance, rank-aware metrics, significance testing over query sets, and click models that correct for position and presentation bias before inferring anything about relevance — is a mature discipline. Marketplace search is largely evaluated on conversion and revenue per search, which are business outcomes confounded by price, inventory and presentation, and which reward showing the cheapest popular item regardless of whether it was what the buyer wanted.

## What Already Exists
Graded relevance judgement methodology; rank-aware evaluation metrics; click models correcting for position and examination bias; interleaving for sensitive online comparison; counterfactual evaluation from logged interactions; and diversity and novelty metrics for result sets.

## The Customization Gap
The adaptation is to a ranking whose items are for sale and whose supply is the platform's own asset. It requires: (1) relevance judged separately from commercial outcome, since conversion conflates whether the result was right with whether it was cheap — separating them is the measurement change that would most alter what these teams optimise; (2) click models accounting for price and image prominence as well as position, because in a marketplace the presentation biases are commercial and the standard models do not include them; (3) coverage and exposure metrics over the inventory, since a marketplace has an interest in listings being seen that a web search engine does not have in documents; (4) interleaving as the standard online comparison, which is far more sensitive than the conversion tests these teams run and is unused; and (5) diversity objectives with a stated purpose, since showing ten near-identical results is both a poor buyer experience and a liquidity failure, and the retrieval literature has the machinery to trade it off explicitly.

## Target Customer
Marketplace search teams, their leadership, and the information retrieval community for whom marketplace ranking is a rich and under-studied application.

## Impact If Solved
Conversion conflates relevance with price and rewards showing the cheapest popular item. Separating relevance from commercial outcome is the measurement change that would most alter what search teams optimise, and interleaving is a far more sensitive online test than the ones they run.
