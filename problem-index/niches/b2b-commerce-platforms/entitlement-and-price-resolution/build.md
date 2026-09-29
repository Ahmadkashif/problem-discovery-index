# A Price Surface the Architecture Was Not Built For

**Niche:** [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/profile|Entitlement & Price Resolution]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every business customer has their own price for every product at every quantity on every date, and resolving that surface in milliseconds is the requirement B2B platforms inherited an architecture unsuited to.
**Tags:** #convex-optimization #data-integration #evaluation-metrics #graph-theory #automation #confidence-intervals #compliance #dynamic-programming
**Contested on:** Every serious competitor in this niche is fighting to resolve one customer's correct price and entitlement for any product at any quantity in milliseconds — and whoever does that takes the account, because that resolution is what a B2B storefront is and everything else in the category is built on it.

## The Problem
A buyer opens a category page with forty products. Their correct price for each depends on their contract, their volume tier for the current period, their contracting entity, their delivery location's tax and freight terms, a rebate accrual and an expiry date on one of the agreements. Resolving forty of those takes too long, so the page shows list prices and the buyer discovers their real price in the cart — or, more often, phones their rep. The platform's answer to a pricing model with four dimensions was to extend a model with one, and the consequence is that the storefront cannot do the thing the buyer came for.

## Why Nobody Has Built This
The platforms grew from consumer commerce, where a product has a price, and B2B pricing was added as customer group overrides and then as external service calls. Rebuilding the data model around a resolution function is a foundational change no established platform will make. External pricing services solved correctness and made performance worse. And the buyer's workaround — calling a rep — masks the failure as a preference for personal service.

## What to Build
Make resolution the primitive rather than an extension. Model price and entitlement as a function of customer, product, quantity and date from the ground up, precomputed and indexed where the rules permit and evaluated where they do not, which is the architectural decision that everything else follows from and which no incumbent will make. Precompute the resolved surface per customer for their entitled catalogue, since a customer's agreement changes rarely and their catalogue is a fraction of the whole, which converts a per-request evaluation into a lookup for the overwhelming majority of cases. Apply entitlement within retrieval rather than after it, so a customer never sees an item they cannot buy and the search index does not return results that get filtered away. Make the rule set expressible — tiers, breaks, effective dates, entity scoping, exclusions, rebates — so that a complex agreement is configuration rather than custom code, which is where these implementations become unmaintainable. Invalidate precisely on agreement change, since the correctness depends on it and a blunt invalidation destroys the performance gain. Verify resolved prices against the contract continuously, which the buyer currently does by complaining. Explain the price to the buyer, showing which agreement and which tier produced it, which builds trust and reduces the calls. And measure resolution latency at the page rather than at the service, because the buyer's experience is the page.

## Target Customer
Distributors and manufacturers selling business to business, the platform vendors serving them, and the buyers who currently phone for a price.

## Impact If Built
The platforms extended a single-price model to answer a four-dimensional question and the storefront consequently cannot do the thing the buyer came for. Precomputing the resolved surface per customer over their entitled catalogue turns a per-request evaluation into a lookup for almost every case.
