# Consumption Modelling and Inventory Replenishment Theory

**Niche:** [[niches/subscription-commerce/replenishment-subscriptions/profile|Replenishment Subscriptions]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Inventory theory has solved when to reorder under uncertain demand for a century, and a replenishment subscription is that problem with the household as the stockroom.
**Tags:** #probability-distributions #time-series-forecasting #convex-optimization #confidence-intervals #gradient-boosting #evaluation-metrics #optimization-fundamentals #bayesian-inference
**Contested on:** Every serious competitor in this sub-niche is fighting to have the next delivery arrive as the last one runs out — and whoever does that keeps the subscriber, because the alternative is a customer who simply buys it when they need it and does not need a subscription at all.

## The Problem
Deciding when to reorder so that stock arrives before it runs out, given uncertain consumption and a known lead time, is the reorder point problem — one of the most thoroughly solved questions in operations research, with safety stock formulas, service level targets and periodic review policies. A replenishment subscription is exactly that problem with the customer's cupboard as the stockroom and the company managing it on their behalf, and the category runs it on a dropdown.

## What Already Exists
Reorder point and safety stock models with service level targets; periodic review inventory policies; demand forecasting for slow-moving items; Bayesian updating of consumption estimates from sparse observations; and vendor-managed inventory practice where a supplier manages a customer's stock levels.

## The Customization Gap
The adaptation is to a stockroom the company cannot see. It requires: (1) consumption inferred rather than counted, since the household's stock level is unobserved and must be estimated from behavioural evidence — which is a state estimation problem and is the specific technical work; (2) Bayesian updating from very sparse signals, since a household gives a few informative events a year and pooling across similar households supplies the prior; (3) the cost asymmetry stated explicitly, because running out and over-supplying have different consequences for retention and the service level should reflect that rather than defaulting to the revenue-maximising frequency; (4) vendor-managed inventory as the conceptual model, which is exactly what this is and which supplies the framing the category lacks — the company is managing the customer's stock, not fulfilling a schedule; and (5) the customer as an informant, since unlike a warehouse they can be asked and will answer.

## Target Customer
Replenishment operators, platform vendors, and the inventory theory community for whom the household stockroom is an unclaimed application.

## Impact If Solved
This is the reorder point problem with the household as the stockroom and it is run on a dropdown. Vendor-managed inventory is the right conceptual framing and supplies the reorientation the category needs, and the customer — unlike a warehouse — can simply be asked.
