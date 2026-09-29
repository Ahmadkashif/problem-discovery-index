# Pricing the Risk Rather Than Absorbing It

**Niche:** [[niches/game-porting-studios/effort-model-and-pricing/profile|Effort Model & Bid Pricing]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The studio carries all the uncertainty and prices none of it.
**Tags:** #gradient-boosting #confidence-intervals #revenue-impact #evaluation-metrics #bayesian-linear-regression #hypothesis-testing #optimization-fundamentals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn measured codebase properties and a history of past projects into a price with stated risk — and whoever prices it correctly takes the account.

## The Problem
A fixed-price bid transfers all the uncertainty to the studio, and the studio prices it with a margin assumption rather than with a risk model. When the codebase turns out to be worse than assumed, the difference comes out of profit. When it turns out easier, the studio has usually bid low to win. The corpus of past projects that would let it price this properly exists as invoices and memories.

## Why Nobody Has Built This
The project history has never been structured, so there is nothing to model. Risk pricing makes a bid look more expensive than a competitor's optimistic one. Service businesses of this size have no analytics function. And the losses are absorbed as margin variation rather than surfacing as a pricing failure.

## What to Build
Model the distribution of outcomes and price against it. Relate realised effort to assessed codebase properties across the studio's own project history, which is the core and turns an inherited judgement into a checkable relationship. Produce a distribution of likely effort rather than a single figure, since the right price depends on the spread and not only the centre. Price contingency from the historical variance for projects of that profile rather than from a round percentage. Identify which uncertainties should be excluded or made conditional in the contract instead of being priced, which is frequently the better commercial answer. Model the moving-target risk separately, as client-side development is a distinct and separately manageable exposure. Support a paid assessment phase in the commercial structure, which is how the information asymmetry is properly resolved. Track win rate against estimate accuracy together, because optimising either alone destroys the business in a different way. Report margin variance attributable to estimation, which is the number that makes the case internally. Let commercial leadership see the model's reasoning rather than a price, since they must defend it in a negotiation. And keep the expert in the loop as a reviewer, which is both better and the only way it gets adopted.

## Target Customer
Porting and co-development studios, commercial leadership, publishers commissioning ports, and services pricing vendors.

## Impact If Built
The studio carries all the uncertainty and prices it with a margin assumption. Modelling the effort distribution from its own project history lets contingency be priced rather than absorbed.
