# The Mechanism: What Scanner Data Made Computable

**Origin:** [[origins/supermarket-chains/profile|Supermarket Chains]]
**Tags:** #descriptive-statistics #time-series-forecasting #linear-regression #feature-engineering #evaluation-metrics #revenue-impact

## The Data Model — and why it is the whole story

The UPC did one thing: it gave every product a **primary key**.

That sentence is the mechanism. Before it, a store's sales were a single scalar per day. After it, sales were a table:

> `(store, item, timestamp, quantity, price, promotion_flag)`

Everything the industry built for the next fifty years is a query over that table. An FDE should sit with this, because it is the most compressed illustration in the vault of a general truth: **the schema is the capability.** Nobody had to invent a new algorithm to do category management. They had to be able to name the row.

## What Became Computable

**Velocity.** Units per SKU per store per week. Trivial arithmetic, previously impossible, and immediately decision-grade: this product earns its facings, that one does not.

**Price elasticity.** With enough price variation across stores and weeks, regress quantity on price and recover a demand curve — per item, per market. Grocers were estimating elasticities from observational data decades before anyone called it that.

**Promotional lift and its ugly cousin.** Compare promoted weeks to baseline and you get lift. But the same data exposes what the promotion *cost*: **forward-buying** (customers stockpiling, so next month's sales are borrowed, not new) and **cannibalisation** (the promoted item stealing from its own category). The honest promotional ROI is usually far worse than the headline lift, and the data to compute it has existed since the 1980s.

> Note that shape carefully. The measurement is possible, the data is present, and the honest number is smaller than the reported one. That is the **declined join** — appearing here in 1985, two decades before the platform era the vault associates it with.

**Basket affinity.** Which items co-occur in a transaction. This is the origin of association-rule mining, and of the "beer and nappies" anecdote — which is almost certainly apocryphal and should not be repeated as fact.

**Automatic replenishment.** Forecast demand per item per store, net against measured on-hand, generate the order. Continuous rather than periodic.

## What It Could Not See — the load-bearing limitation

**The scanner saw the sale. It never saw the shopper.**

The transaction had no identity attached. The store could tell you that 400 units moved on Tuesday and nothing whatsoever about whether that was 400 people buying one or 40 buying ten, whether they were new or loyal, or whether the promotion converted anyone or merely discounted people who would have bought anyway.

**This is the missing join, and it defined the next thirty years of retail.** Loyalty cards in the 1990s were built to close it — the entire value proposition of a loyalty scheme, from the retailer's side, is attaching an identity to a basket. Retail media today is the same join, closed a third time and sold at a much higher price.

## The Trade-Offs Taken

**Measurement favoured the measurable.** Fast-moving packaged goods produced clean data. Fresh, variable-weight and long-tail items produced worse data and lost shelf space accordingly — not because they were less profitable, but because they were less legible.

**Optimising per category broke the store.** Each category, managed as its own business unit against its own targets, produces a locally optimal assortment and a globally worse shop. The shopper does not experience categories.

**The baseline became a negotiation.** Promotional lift is measured against a counterfactual baseline that nobody observes and both parties have an interest in. Retailer and brand argue about the baseline, not the outcome.

## The Transferable Pattern

> **Give something a primary key and you have not just enabled measurement — you have decided what will be optimised and what will be neglected. The schema is a statement about what matters.**

**Sources:** Wikipedia, *Category management*, *Association rule learning*; standard retail-analytics literature on promotional lift, forward-buying and cannibalisation.
