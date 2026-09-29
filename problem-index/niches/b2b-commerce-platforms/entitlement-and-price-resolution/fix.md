# List Prices on the Listing Page

**Niche:** [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/profile|Entitlement & Price Resolution]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Because resolving customer prices for a page of results is too slow, the listing page shows list prices, which means every browsing surface in the storefront shows a number the customer will not pay.
**Tags:** #evaluation-metrics #revenue-impact #confidence-intervals #descriptive-statistics #convex-optimization #automation #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to resolve one customer's correct price and entitlement for any product at any quantity in milliseconds — and whoever does that takes the account, because that resolution is what a B2B storefront is and everything else in the category is built on it.

## The Problem
A buyer with a thirty percent contract discount browses a category. Every price shown is list. They cannot compare options on the basis that matters to them, cannot assess a budget, and cannot tell whether an alternative part is cheaper for them specifically — which is the entire question a purchasing decision turns on. They add items to the cart one at a time to discover their real prices, or they give up and send the list to their rep. The storefront's core function is defeated by a performance constraint, and the compromise chosen — show a wrong number — is worse for the buyer than showing nothing.

## Why It's Still Broken
Resolving forty customer prices per page was too slow with the architecture available, and showing list was the pragmatic compromise at the time. It has persisted because it is now normal in the category and buyers have adapted by calling. The lost conversion is invisible, since the order eventually arrives through the rep. And the fix appears to require the architectural change rather than a targeted one.

## What a Fix Looks Like
Get customer prices onto the browsing surfaces. Precompute each customer's resolved prices for their entitled catalogue and serve them from that, which is a bounded dataset per customer refreshed on agreement change and makes a listing page a lookup — this is the fix and it does not require rebuilding the platform. Resolve asynchronously and populate the page as the answers arrive, which is a straightforward front-end pattern and is better than showing list. Show the discount relationship rather than the absolute price where full resolution is impossible, since your price is thirty percent below list is more useful than a list price alone. Never show a price the customer will not pay without labelling it, since an unlabelled list price is misleading rather than merely unhelpful. Measure the conversion and call-volume difference between customer-priced and list-priced surfaces, which will make the business case immediately and is a test nobody has run. Prioritise the customer's frequently purchased items for precomputation, since their reorder set is small and covers most of their activity. Let the buyer see quantity break pricing inline, which is a purchasing decision input and is currently in the cart or in a conversation. And report how often buyers add to cart solely to see a price, which is a measurable behaviour and is evidence of the harm.

## Who Feels the Pain
Buyers who cannot compare on the only number that matters to them; reps fielding calls the storefront should have answered; and distributors whose digital channel is bypassed for a reason nobody has measured.

## Impact If Fixed
Showing a number the customer will not pay is worse than showing nothing and is normal in the category. Precomputing each customer's resolved prices over their entitled catalogue is a bounded dataset and turns a listing page into a lookup without rebuilding anything.
