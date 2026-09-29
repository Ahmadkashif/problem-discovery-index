# Entitlement & Price Resolution

**Parent Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to resolve one customer's correct price and entitlement for any product at any quantity in milliseconds — and whoever does that takes the account, because that resolution is what a B2B storefront is and everything else in the category is built on it.

## Profile
**Market Size:** ~$3.2B US attributable to pricing and entitlement
**Share of Parent Industry:** ~23% of category revenue
**Digital Adoption:** Low — handled by extension, not by design
**Target Buyer:** Every distributor and manufacturer selling business to business
**Automation Potential:** High — it is a computation and caching problem

## What Makes This a Distinct Niche
Every business customer has their own price for every product at every quantity on every date, and resolving that surface in milliseconds is the requirement B2B platforms inherited an architecture unsuited to. Contract pricing, volume breaks, customer-specific catalogues and exclusions, entitlements that vary by contracting entity and delivery location, rebate structures and negotiated terms combine into a function of customer, product, quantity and date. A consumer platform holds a price on a product and applies promotions; a B2B platform must evaluate a rule set per customer per line, at page load, across a catalogue of hundreds of thousands. This is the architectural difference between the two kinds of commerce, it is handled by extension almost everywhere, and it is why these storefronts are slow and why buyers still call for a price.

## Current Tools & Gaps
Price list hierarchies, customer group pricing, external pricing service calls and caching layers. The gaps: resolution cost forces platforms to show list prices on listing pages and customer prices only in the cart, which breaks the buyer's experience; entitlement filtering is applied after retrieval rather than within it; the rule set is not expressible, so complex agreements become custom code; pricing correctness is not verified against the contract; and no platform can explain to a buyer why they are seeing a price.

## Problems
- [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/build|🔨 Build: A Price Surface the Architecture Was Not Built For]]
- [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/buy|🛒 Buy: Rules Engines and Query Optimisation]]
- [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/fix|🔧 Fix: List Prices on the Listing Page]]
