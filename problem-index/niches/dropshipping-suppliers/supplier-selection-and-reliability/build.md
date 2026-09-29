# A Star Rating for the Only Thing That Matters

**Niche:** [[niches/dropshipping-suppliers/supplier-selection-and-reliability/profile|Supplier Selection & Reliability Signals]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A merchant commits their storefront and their customer relationship to a supplier they have never met, on the basis of a star rating that measures volume more than performance.
**Tags:** #survival-analysis #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to tell a merchant whether a specific supplier will actually perform on a specific product before they commit their storefront to it — and whoever produces a signal that predicts downstream outcomes replaces the star rating the whole category runs on.

## The Problem
A merchant picks a product, builds a store around it, spends on advertising, and starts taking orders. Everything now depends on a supplier they chose from a list, on the strength of 4.7 stars and eleven thousand orders. Those numbers tell them the supplier has been on the platform a while. They say nothing about whether this product ships in six days or thirty, whether the last two hundred orders to their country arrived, whether returns spiked last month, or whether the supplier has quietly started substituting a cheaper version. The platform knows all of it — it routed every order and recorded every tracking event — and publishes a star.

## Why Nobody Has Built This
Ratings were copied from consumer marketplaces, where the reviewer is the end customer and the purchase is small; here the reviewer is a merchant whose own business depends on the supplier looking good, which corrupts the signal at source. Publishing accurate supplier performance means telling merchants that suppliers earning the platform money are bad. Volume-weighted ratings are self-reinforcing and look healthy. And nobody has been asked for the honest version.

## What to Build
Compute the signal from outcomes rather than from opinions. Score suppliers on what actually happened — fulfilment latency, tracking-confirmed delivery, return rate, dispute rate, chargeback rate, cancellation rate — every one of which the platform observes directly and none of which depend on anyone writing a review; this is the core and it replaces the rating rather than supplementing it. Resolve to the product and the destination, because a supplier excellent on one item to one country and poor on another is the normal case and a single supplier-level number averages away the only useful detail. Report uncertainty honestly, since a supplier with nine orders and a supplier with nine thousand should not display the same way, and the absence of a confidence interval is what makes new suppliers unusable. Separate what the supplier controls from what the carrier and the border do, otherwise the score punishes a destination rather than a supplier. Detect change rather than reporting a lifetime average, which is the fix note's subject and is where most merchant harm comes from. Predict rather than describe — the merchant's question is what will happen to my orders, not what happened to everyone's. Give new suppliers a path by scoring their initial orders with explicit uncertainty rather than leaving them unrated, which is the only way the supply side stays open. Expose the score before commitment, at product selection, which is when the decision is actually made. And publish the method, because a score suppliers cannot understand is a score they will attack rather than improve against.

## Target Customer
Dropshipping platforms and sourcing marketplaces, merchants selecting suppliers, and the aggregators whose entire risk is supplier performance.

## Impact If Built
The platform routed every order and observed every outcome, and publishes a star that mostly encodes tenure. Outcome-based scoring resolved to product and destination, with honest uncertainty, is computable today and is the product the category claims to sell.
