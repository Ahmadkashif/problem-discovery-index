# Allocating Through Intermediaries

**Niche:** [[niches/game-user-acquisition-firms/bidding-and-media-buying/profile|Bidding & Media Buying]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The buyer sets a target, the network optimises for itself, and what arrives is the product of both.
**Tags:** #optimization-fundamentals #bayesian-optimization #confidence-intervals #evaluation-metrics #time-series-forecasting #revenue-impact #causal-inference #markov-decision-processes
**Contested on:** Every serious competitor in this niche is fighting to allocate spend across networks whose own optimisers they cannot see, against a predicted value they do not trust — and whoever buys better takes the account.

## The Problem
A UA team allocates budget across several networks, each of which runs its own optimisation against the signals the team sends it. The team cannot see how that optimisation works, cannot verify what it delivers, and receives outcome feedback days later with substantial uncertainty attached. The result is a control problem with an opaque plant, delayed noisy feedback, and a target that is itself a prediction.

## Why Nobody Has Built This
The networks' opacity is deliberate and unlikely to change. Cross-network comparison is hard because each measures differently. The feedback delay makes rapid iteration impossible. And the current practice of manual allocation with frequent adjustment works well enough that the harder framing has not been forced.

## What to Build
Treat it as allocation under delayed uncertain feedback, not as campaign management. Allocate across networks as a portfolio under uncertainty rather than campaign by campaign, which is the core — the decision is how to divide a budget and it is made as a series of local adjustments. Model each source's saturation curve, since spending more on a good source eventually buys worse users and nobody knows where the knee is. Handle the delayed feedback explicitly with sequential decision methods rather than reacting to yesterday's incomplete data. Account for network-side optimisation by treating the network as a system with its own objective rather than as a delivery mechanism. Normalise measurement across networks so comparison is honest, which is a data problem more than a modelling one. Hold spend on uncertain sources to keep learning about them, as a purely exploitative allocation stops learning and then decays. Propagate the value model's uncertainty into the bid rather than bidding the point estimate. Detect when a source's delivered quality changes, which happens constantly and is noticed late. Simulate allocation changes before making them where the history supports it. And report allocation decisions and their outcomes so the team's own judgement can be calibrated.

## Target Customer
UA teams and agencies, mobile publishers, bid management platforms, and marketing optimisation vendors.

## Impact If Built
The decision is how to divide a budget under delayed uncertain feedback and it is made as a series of local adjustments. Portfolio allocation with saturation curves and sequential methods is the framing the problem actually has.
