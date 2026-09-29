# Optimising Watch Time in a Shop

**Niche:** [[niches/live-commerce-platforms/purchase-intent-matching/profile|Purchase-Intent Matching]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The ranking objective came from short-form video and rewards watching, and live commerce has kept it while calling itself a commerce channel.
**Tags:** #loss-functions #logistic-regression #gradient-boosting #evaluation-metrics #revenue-impact #confidence-intervals #transformers #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to rank streams for what a viewer will buy rather than for how long they will watch — and whoever changes the objective successfully converts an entertainment feed into a commerce channel.

## The Problem
The feed is very good at finding streams a viewer will watch. A viewer who wanted a specific card, a specific size, a specific brand is shown three hours of entertaining shows that sell none of it, enjoys some of them, and buys nothing. The platform records a strong session. Meanwhile a seller with exactly that inventory streamed to an empty room. Both sides of the transaction were present on the platform at the same moment and the ranking objective kept them apart, because it was never asked to bring them together.

## Why Nobody Has Built This
Watch-time optimisation is what the parent platforms are built on and is genuinely hard-won engineering nobody wants to discard. Purchase is a rare, delayed and noisy label, so naive substitution degrades every offline metric and the experiment fails. Entertainment and commerce genuinely coexist here, which makes the objective a product decision rather than a modelling one. And engagement growth is legible to leadership in a way conversion mix is not.

## What to Build
Rank on the transaction. Define the objective as expected purchase value with an explicit horizon, rather than as watch time with a conversion reweighting, since the reweighted version preserves the original system's preferences and is why the half-measure keeps failing. Capture intent as a signal in its own right — searches, saved items, category follows, waitlist entries, a stated want — which most platforms discard and which is the closest thing to a declared demand the system will ever get. Separate browsing sessions from shopping sessions, because a viewer in each state wants opposite things and one ranker serving both serves neither. Handle label sparsity with intermediate targets that genuinely precede purchase — item taps, cart adds, notification sign-ups — chosen for their causal position rather than their density. Model price and category exposure so the objective is not quietly a preference for cheap impulse items, which is the standard failure of naive value optimisation. Match declared want to live inventory across streams, which is the highest-value and most obvious mechanic in the category and is largely absent. Handle the timing: the viewer needs to arrive when the item is up, so the system must interrupt rather than wait to be browsed. And evaluate on purchase rate and on whether the viewer got what they came for, alongside retention — not instead of it, since an entertainment feed that nobody watches sells nothing either.

## Target Customer
Live commerce platforms, marketplaces adding live formats, and commerce leadership at platforms whose discovery is run by a video team.

## Impact If Built
Both sides of the transaction were on the platform at the same moment and the objective kept them apart. Reweighting watch time preserves the original system's preferences, which is why the half-measure keeps failing, and discarded intent signals are the closest thing to declared demand available.
