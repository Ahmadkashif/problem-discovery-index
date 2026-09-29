# Ranking Under Competing Objectives

**Industry:** [[retail-media-networks|Retail Media Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every network licenses the same auction technology and ranks on bid times predicted click, while the retailer's actual objective is a mix of relevance, margin, inventory, private label and long-run basket that no vendor platform expresses.
**Tags:** #gradient-boosting #convex-optimization #evaluation-metrics #feature-engineering #bayesian-optimization #k-nearest-neighbors #revenue-impact #transfer-learning

## The Problem
A sponsored placement is chosen by ranking advertisers on expected revenue per impression — bid multiplied by predicted click-through, sometimes with a relevance floor. That objective is correct for a pure advertising business and wrong for a retailer, whose economics involve several things the auction cannot see.

Margin differs enormously by product, and the highest-bidding advertiser is frequently not the highest-margin sale. Inventory is finite and local: promoting an item that is out of stock in the shopper's fulfilment region converts an ad impression into a poor experience and a lost basket. Private label competes directly with the advertisers funding the network. Some categories are basket-builders whose value is what gets bought alongside them. And the relevance floor, where it exists, is a threshold rather than a trade-off, so a marginally relevant high bid wins over a strongly relevant low one.

## What Already Exists
The serving layer is a solved and commoditised product. Criteo Retail Media, Epsilon's CitrusAd, Topsort, Moloco and Pentaleap all provide auction, ranking, pacing and reporting, and most networks outside the top tier run on one of them. They ship click prediction, bid shading, budget pacing and category-level relevance controls out of the box. Amazon's internal system is the outlier and is not for sale. Onsite search ranking itself is served by Algolia, Bloomreach, Constructor, Lucidworks and the retailer's own systems, usually as a separate stack from the ad ranker — which is itself part of the problem.

## The Customisation Gap
The vendor platforms optimise ad revenue because that is the product they sell; the retailer's objective function is a weighted combination that only the retailer knows, changes by category and season, and is not expressible in the licensed system. A network running someone else's ranker is structurally unable to express its own economics.

The specific gaps are concrete. Margin-aware ranking needs unit economics per SKU per fulfilment path, which sits in the merchandising system and never reaches the ad platform. Inventory-aware ranking needs live regional availability, which exists and is not wired in. Private label treatment is a policy decision with a number attached that no vendor will make on a retailer's behalf. Joint ranking of organic and sponsored results — the only way to price displacement correctly — requires the two stacks to be one, and they are two.

The transferable part is the machinery: a constrained ranking formulation where relevance, margin, availability and ad revenue are explicit terms with retailer-set weights, fit to that retailer's own outcomes. The non-transferable part is every weight in it, which is exactly why a licensed platform cannot supply this and why it is worth a retailer building.

## Impact If Solved
The ranking decision is made millions of times a day and currently optimises one term of a four-term objective. Bringing margin and availability into it changes the profit per impression rather than the revenue per impression — a different and larger number — and joining the organic and sponsored rankers is the prerequisite for measuring displacement at all. For mid-tier networks it is also the only available differentiation, since everyone below the top runs the same licensed auction against the same brands.
