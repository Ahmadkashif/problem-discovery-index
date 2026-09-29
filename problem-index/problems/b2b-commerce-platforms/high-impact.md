# Customer-Specific Pricing and Entitlements at Scale

**Industry:** [[b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** High Impact
**One-liner:** Every business customer has their own price for every product at every quantity on every date, and resolving that surface in milliseconds is the requirement B2B platforms inherited an architecture unsuited to.
**Tags:** #optimization-fundamentals #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #graph-theory #data-integration #revenue-impact

## The Problem
In consumer commerce a product has a price. In B2B it has a price per customer, and the rules producing it are layered: a contract rate negotiated with this account, volume tier breaks, a customer-specific catalogue that excludes some items, promotional pricing that may or may not stack with contract terms, entitlements that differ by contracting entity, location or cost centre, and pricing agreements with expiry dates.

The resolution must happen at page load for every item on a category page, for a customer with a specific contract, at their specific quantity. It is not a lookup; it is an evaluation of a rule hierarchy where precedence matters and errors are commercially serious in both directions.

Systems built for a list price with promotions handle this by extension. The result is that customer-specific pricing is the most common performance problem in B2B storefronts — pages that take seconds because each item's price is being resolved — and the most common correctness problem, where a customer is quoted one price online and invoiced another from the ERP.

The consequence is that large customers do not trust the storefront and route their orders through inside sales, which is precisely the cost the platform was bought to remove.

## Why It's Unsolved
The rule hierarchy is genuinely complex and is genuinely necessary — it encodes commercial agreements that took years to negotiate and cannot be simplified away.

Pricing usually lives in the ERP, which is the system of record for contracts and which was not built to answer thousands of pricing questions per second. The platform either calls it, which is slow, or caches, which risks staleness on a number that must be exactly right.

Precomputation is defeated by dimensionality. Customers times products times quantity breaks times dates is a very large space, and materialising it is impractical for a distributor with tens of thousands of customers and hundreds of thousands of items.

Entitlement adds another dimension. Which products a customer may see and buy is itself contractual, and it interacts with pricing in ways that make caching harder.

And correctness is unverified. Whether the price shown matches the price the ERP will invoice is checkable and is generally checked by customers noticing discrepancies on invoices.

## What a Solution Looks Like
Selective precomputation guided by prediction. Most customers buy a small, stable set of products repeatedly, and precomputing prices for the combinations a customer is actually likely to view covers the overwhelming majority of requests cheaply. Predicting that set from purchase history is straightforward and turns an intractable materialisation into a manageable one.

Continuous reconciliation between the storefront price and the ERP price. Sampling and comparing, systematically, converts a class of silent commercial error into a monitored one, and it is the check nobody runs.

Rule hierarchy analysis. Which pricing rules actually fire, which are dead, which conflict and which are shadowed by higher-precedence rules is answerable from evaluation logs and would let an administrator simplify a hierarchy that has accreted for a decade.

Entitlement resolution treated as a first-class access problem rather than as a catalogue filter, so that what a customer may buy is evaluated consistently across search, browse, reorder and punchout.

Expiry management, since agreements lapse and a lapsed contract silently reverting to list price is a common and damaging failure.

## Impact If Solved
Customer-specific pricing is the defining requirement of B2B commerce and the reason large customers bypass the storefront for inside sales. Making it fast through predictive precomputation and correct through continuous ERP reconciliation addresses the two failures that determine whether self-service adoption actually happens.
