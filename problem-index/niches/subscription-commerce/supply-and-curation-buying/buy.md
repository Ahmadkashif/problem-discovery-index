# Assortment Planning and Commitment Under Uncertainty

**Niche:** [[niches/subscription-commerce/supply-and-curation-buying/profile|Supply & Curation Buying]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fashion retail solved buying for an uncertain season with option contracts, staged commitments and postponement, and subscription merchandisers commit everything in one order.
**Tags:** #probability-distributions #convex-optimization #time-series-forecasting #confidence-intervals #revenue-impact #optimization-fundamentals #evaluation-metrics #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to buy the right quantity of the right things for a subscriber base whose size and composition at delivery is unknown — and whoever does that protects the margin, because the buy is committed months before the base that receives it is known.

## The Problem
Committing to inventory before demand is known is the defining problem of seasonal retail, and the industry built real answers: quick response and postponement to delay commitment, option and buyback contracts that share the risk with the supplier, staged buys with in-season reorders, and the newsvendor framework for setting the quantity against the costs of being wrong in each direction. Subscription merchandisers place one order at one moment for a demand they will not know for months.

## What Already Exists
Newsvendor and stochastic inventory models for single-period commitments; quick response and postponement strategies; supply contracts that share risk including options, buybacks and revenue sharing; in-season reorder and chase capability; and assortment planning with breadth-versus-depth optimisation.

## The Customization Gap
The adaptation is to demand that is a known subscriber base rather than an anonymous market. It requires: (1) demand modelled as a subscriber count with a churn distribution rather than as a sales forecast, which is a much better-posed problem than retail's and the category does not exploit it — the subscribers are individually known and their survival is estimable; (2) composition as well as quantity, since the assortment must match a preference distribution that is also forecastable from the same base; (3) the absence of a markdown channel, which makes the over-buy cost far higher than in retail and should shift the optimal quantity down substantially; (4) supplier contracts adapted to small operators, where the option and buyback structures assume scale and the equivalent here is a staged commitment or a later cut-off; and (5) postponement applied to the box composition, since deciding the final allocation late is cheap and deciding the purchase late is not.

## Target Customer
Subscription merchandisers, their suppliers, and the retail planning discipline for whom a known subscriber base is a better-posed version of a familiar problem.

## Impact If Solved
Retail's methods assume anonymous demand and this category knows its customers individually, which makes the forecast better-posed and is unexploited. The absence of a markdown channel means the over-buy cost is far higher than retail's and the optimal quantity should be lower than merchandisers assume.
