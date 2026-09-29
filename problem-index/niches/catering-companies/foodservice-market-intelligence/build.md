# Menu Coding as a Learned System With Measured Consistency

**Niche:** [[niches/catering-companies/foodservice-market-intelligence/profile|Foodservice Market Intelligence Firms]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The whole product is a menu database coded by hand against a proprietary taxonomy, and nobody has ever measured whether two coders reading the same dish description assign it the same way.
**Tags:** #bert #transformers #transfer-learning #contrastive-learning #word-embeddings #random-forests #evaluation-metrics #cross-validation #tacit-knowledge-ml #automation #revenue-impact

## The Problem
Every trend claim the firm sells rests on one operation: reading a menu item — a dish name, a description, sometimes a price and nothing else — and coding it into ingredients, preparation methods, flavour profiles, dietary attributes, and category. The work is done by analysts at volume, the taxonomy has thousands of nodes, and the judgments are frequently genuinely hard: whether a described preparation counts as one technique or another, whether a regional term implies a specific ingredient, whether a garnish mentioned in passing should be coded at all. Consistency across coders and across years has never been measured, because measuring it requires double-coding a sample and nobody has built the process. That matters more here than in most coding operations, because the product is change over time — and a drift in coding convention is indistinguishable, in the output, from a real trend.

## Why Nobody Has Built This
The taxonomy is the moat and has always been treated as expert craft. As with every classification operation of this kind, the decisions were stored as outcomes rather than as labelled examples: the database records that this item carries these tags, not what the coder was reading or why they hesitated. The failure mode also discourages automation — a coder that is right most of the time introduces systematic error into precisely the categories clients scrutinize, and a wrong trend line is worse commercially than a slow one. So the operation has stayed manual and unmeasured together.

## What to Build
A coding engine that treats the taxonomy as a calibrated model and consistency as a measured property. Menu items are coded automatically with confidence, and only genuinely uncertain items route to analysts, which reverses where expert time is spent. Every analyst decision from that point is captured with its full input context, building the labelled corpus that was previously discarded. A standing double-coding sample runs continuously, so inter-coder agreement becomes a reported number rather than an assumption, and coding drift over time becomes detectable — which is what separates a real flavour trend from a change in how the house codes it. Retrospective consistency checking runs over the historical database, surfacing items whose coding disagrees with current convention, which is how years of accumulated drift become visible for the first time. Taxonomy changes are versioned, so a trend series can state which convention it was coded under and back-corrections can be applied deliberately rather than by quietly recoding history.

## Target Customer
VPs of insights and heads of data operations at foodservice intelligence firms running 100-400 analysts, and the client-facing research leads who defend trend claims they have no consistency evidence for.

## Impact If Built
Removes the constraint that caps coverage — more menus, more attributes, faster refresh, without proportional headcount — and simultaneously addresses the quiet liability underneath the flagship product, which is that nobody knows how much of a published trend is coding drift. Measured consistency is also a claim no competitor in this segment can currently make, and it is exactly the question a sophisticated buyer asks.
