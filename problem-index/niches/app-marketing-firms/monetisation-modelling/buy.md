# Customer Equity Practice

**Niche:** [[niches/app-marketing-firms/monetisation-modelling/profile|Monetisation Modelling]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Marketing science formalised customer lifetime value with probabilistic models decades ago, and app analytics extends a cohort curve to the right.
**Tags:** #survival-analysis #bayesian-inference #probability-distributions #confidence-intervals #maximum-likelihood-estimation #evaluation-metrics #time-series-forecasting #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to establish what a user is actually worth over their life, across purchases, subscriptions and advertising revenue — and whoever does that correctly sets the number every acquisition decision divides by.

## The Problem
Customer lifetime value has a formal academic and commercial literature. Probabilistic models of purchasing and dropout, separate treatment of transaction frequency and monetary value, heterogeneity across customers modelled explicitly, and validation against holdout periods are all established practice with open implementations. Subscription businesses have their own well-developed retention and cohort methods. App analytics platforms largely offer a cohort revenue curve and an extrapolation, which is the simplest possible approach to a problem with a substantial literature behind it.

## What Already Exists
Probabilistic buy-till-you-die models; separate frequency and monetary value modelling; customer heterogeneity through mixing distributions; subscription retention and cohort analysis; and holdout validation of lifetime value predictions.

## The Customization Gap
The adaptation is to three revenue streams and a decision made in the first hours. It requires: (1) advertising revenue as a component, which no customer lifetime value model contains and which depends on session counts and fluctuating rates rather than on purchase behaviour — adding it properly is the substantive extension; (2) a prediction needed within days of acquisition rather than after a purchase history, so the models must run on almost no individual data and lean on cohort and source priors; (3) extreme skew in in-app purchasing, where a handful of users dominate and the standard models' assumptions about the monetary distribution need care; (4) a coarsened early signal on one platform, connecting this to the prediction niche and constraining the input; and (5) consumption by a bidding system, which needs a distribution rather than an expected value.

## Target Customer
Product and monetisation teams, user acquisition data science, and marketing science practitioners for whom mobile monetisation is an unserved application.

## Impact If Solved
A substantial literature exists and app analytics extends a curve to the right. Adding advertising revenue as a component, and predicting within days rather than after a purchase history, are the two extensions the established models do not cover.
