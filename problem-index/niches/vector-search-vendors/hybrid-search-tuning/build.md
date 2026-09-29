# The Weight From the Documentation Example

**Niche:** [[niches/vector-search-vendors/hybrid-search-tuning/profile|Hybrid Search Tuning]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every vendor supports combining lexical and dense retrieval because it reliably beats either alone, and the weighting between them is set to whatever the documentation example used.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #bayesian-optimization #cross-validation #hypothesis-testing #confidence-intervals #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to set the balance between lexical and dense retrieval from the customer's own evidence rather than from a documentation default — and whoever does that takes the account, because the setting is free to change and nobody knows what theirs should be.

## The Problem
An industrial parts catalogue runs hybrid search with the weights from the quickstart. Users search by part number, and part numbers are exactly the tokens dense embeddings represent worst — they are rare, arbitrary and carry no distributional meaning. The lexical side would find them instantly and is weighted at a third. Retrieval quality is poor for the most common query type in the deployment, the team assumes the embedding model is unsuitable and starts evaluating alternatives, and the actual fix is one number that nobody has ever questioned because it came with the example.

## Why Nobody Has Built This
Fitting the weight needs relevance labels, which customers do not have and vendors do not ask for — even though a few hundred judgements would settle it and the downstream acceptance signal would settle it for free. The parameter is exposed rather than owned, which makes it the customer's problem by construction. Vendors avoid opinions about retrieval quality as a positioning choice. And a single constant does not look like it warrants engineering effort, which is exactly why it has had none.

## What to Build
Fit the weight instead of copying it. Derive relevance signal from what the deployment already produces — accepted answers, clicked results, escalations, retries, and a small set of human judgements to anchor it — which is the input the fitting needs and is currently discarded everywhere. Fit the combination on that signal and report the improvement against the default, which quantifies for the first time what the copied constant was costing. Make the weight query-dependent, since query type is the strongest available predictor: exact identifiers, quoted phrases and rare tokens want lexical dominance, while conversational and paraphrased questions want dense — and a lightweight classifier over query features captures most of the available gain. Report what each mode contributed per query, so an engineer can see why a result was returned and whether the balance is sensible. Re-fit automatically when the corpus or the embedding model changes, because both invalidate the fit and nothing prompts a revisit. Extend the fit to the reranker's contribution, since a second stage is now standard and its budget is set by the same guesswork. Detect when one mode is contributing nothing, which is a common and silently wasteful state. And publish the fitted weights across corpus types, which gives every customer a better starting point than the quickstart.

## Target Customer
Retrieval and search engineering teams, application teams whose product quality depends on this setting, and the vendors who ship it as a documented default.

## Impact If Built
A copied constant is deciding retrieval quality in most deployments and nobody has questioned it. The acceptance signal needed to fit it is already produced and discarded, and making the weight query-dependent captures most of the remaining gain with a lightweight classifier.
