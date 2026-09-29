# The Promotion That Applies in One Place

**Niche:** [[niches/headless-commerce-vendors/catalogue-price-consistency/profile|Catalogue & Price Consistency]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A promotion is evaluated by the pricing engine at checkout and approximated by every other service that needs to show a price, so the discount shown on the listing is a different calculation from the one applied to the order.
**Tags:** #data-integration #evaluation-metrics #compliance #confidence-intervals #automation #descriptive-statistics #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to make every service's copy of the catalogue agree about the price a customer will be charged — and whoever does that removes the category's most visible failure, because the copies disagree and the customer notices.

## The Problem
A promotion offers twenty percent off when two items from a category are bought together. The pricing engine evaluates this correctly at checkout. The search index cannot evaluate a cart-dependent rule, so it shows the base price. The product page's personalisation layer applies a simplified version and shows twenty percent off unconditionally. The customer adds one item, sees a discounted price on the page, reaches checkout at full price, and complains. Nothing is broken; three services answered a question only one of them can answer, and nobody defined which of them is allowed to.

## Why It's Still Broken
Promotion logic is stateful and cart-dependent, which makes it genuinely unavailable to a stateless index, and the pragmatic response was for each service to approximate. Nobody designated an authority for the displayed price, so every service does its best. The approximations were written separately and diverge in ways no single team can see. And the resulting complaint is handled as a pricing error rather than as an architectural decision that was never made.

## What a Fix Looks Like
Designate the authority and make everybody ask it. Route every customer-visible price through the pricing engine rather than letting services approximate, which is the fix and which the performance objection has prevented — the objection is answerable with caching and batching and has mostly not been tested. Where an approximation is genuinely necessary, make it explicit and label it, so a listing price that cannot account for a cart rule says from rather than a definite figure. Publish the rules each service can and cannot evaluate, since the divergence originates in an unstated capability difference. Test promotions across every surface before activation, which is a pre-flight check on a change that currently ships untested to five services with different logic. Detect display-versus-charge divergence continuously in production, which is the verification work applied to the most common case. Simplify the promotion design where the complexity cannot be represented consistently, since a rule that only one service can evaluate is a rule that will be shown wrongly. Give merchandisers visibility into how a promotion will render on each surface, since they design rules without knowing the constraint. And treat a displayed price that differs from the charged price as an incident, because in several jurisdictions it is also a consumer protection matter.

## Who Feels the Pain
Customers charged more than they were shown; support teams handling complaints about a promotion that worked correctly; and merchandisers whose promotions render differently in five places.

## Impact If Fixed
Three services answer a question only one can answer because nobody designated an authority. Routing every customer-visible price through the pricing engine is the fix, and the performance objection that prevents it is answerable with caching and has mostly not been tested.
