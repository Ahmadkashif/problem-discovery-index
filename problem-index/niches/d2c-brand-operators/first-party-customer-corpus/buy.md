# Customer Analytics and Buy-Till-You-Die Models

**Niche:** [[niches/d2c-brand-operators/first-party-customer-corpus/profile|First-Party Customer Corpus]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Academic marketing produced well-validated models for exactly this data shape — purchase histories with no contract — with open implementations, and the category uses recency and frequency buckets.
**Tags:** #bayesian-inference #survival-analysis #probability-distributions #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn the one dataset the advertising platforms do not have into predictions the brand can act on — and whoever does that takes the advantage, because it is the only asymmetry a small brand holds against a platform.

## The Problem
Predicting future purchasing from a history of past purchases, in a setting with no subscription or contract, is a problem academic marketing science solved with a family of well-validated probability models. They estimate, per customer, the probability of still being an active customer and the expected number of future transactions, from three numbers per customer and nothing else. They have open implementations, published validation across many datasets, and are directly applicable to every brand in this category. Almost none use them.

## What Already Exists
Buy-till-you-die probability models for non-contractual settings; customer lifetime value models combining transaction frequency with monetary value; hierarchical Bayesian extensions borrowing strength across customers; open implementations in common statistical libraries; and the validation literature comparing them against heuristics.

## The Customization Gap
The adaptation is to a brand with covariates and interventions the classical models exclude. It requires: (1) covariates — acquisition channel, first product, discount level, returns — incorporated into the model, since the classical form uses transaction history alone and the brand's richest signals are excluded; (2) the effect of marketing contact modelled, because the classical models assume purchasing is independent of the brand's actions and the entire point of the prediction is to inform those actions; (3) product-level rather than only customer-level prediction, since knowing somebody will buy is less useful than knowing what; (4) delivery as an operational service rather than as an analysis, since the output has to reach the messaging platform and the ad platform to be worth anything; and (5) packaging for a brand with no analyst, which is the practical barrier — the models are free and the person who would run them does not exist.

## Target Customer
Brands, retention platform vendors who could embed this, and the marketing science community whose models are freely available and largely unused in the market they were built for.

## Impact If Solved
Validated models for exactly this data shape exist with open implementations and are not used. Adding covariates and modelling the effect of marketing contact are the two extensions that make them decision-useful, and packaging for a brand with no analyst is the practical barrier.
