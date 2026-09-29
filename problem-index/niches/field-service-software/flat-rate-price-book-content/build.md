# Prices Fitted to a Market From Won and Lost Jobs

**Niche:** [[niches/field-service-software/flat-rate-price-book-content/profile|Flat-Rate Price Book Content]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform records thousands of quoted prices and whether the customer accepted, which is a direct measurement of local price sensitivity per task, and every price book is still a national average with a regional multiplier.
**Tags:** #logistic-regression #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #cross-validation
**Contested on:** Every serious competitor in price book content is fighting to make a task's price right for this trade in this market with this contractor's cost structure — and whoever needs the least customisation on arrival takes the account.

## The Problem
A contractor's book prices a capacitor replacement at a number derived from a national base and a regional multiplier. In their market the job is competitive and the price is high enough that they lose a share of the quotes; on a different task they are leaving money on the table because the local market bears more. They cannot tell which is which, because a close rate of 68% on one task and 81% on another has never been examined against price. The data to answer it — every quote, its price, and whether it was accepted — is in the platform, per contractor and pooled across thousands of them.

## Why Nobody Has Built This
Price book vendors are content businesses, staffed with people who price from labour standards and supplier costs, and fitting prices from demand data is a different discipline entirely. There is also a genuine inference problem that has to be handled honestly: observed acceptance is confounded by which technician quoted, what the customer's situation was, and whether a competitor had already been out, so naive fitting produces a model of the contractor's sales process rather than of the market. And pooling across contractors raises the same corpus governance question that every opportunity in this vault runs into, with an added antitrust sensitivity around price coordination that has to be addressed carefully and can be — the output is an estimate of demand response for a contractor's own decision, not a shared price.

## What to Build
Price response estimated per task per market, fitted to quote acceptance with the confounders modelled rather than ignored. Each task gets an estimated acceptance curve against price, with the contractor's own history as the primary evidence and pooled comparable markets supplying structure where their data is thin — the same borrowing pattern that recurs across vertical SaaS. Output is a recommended price with an expected-margin justification and the uncertainty shown, not an imposed number. Deliberate experimentation is part of the design: small, bounded price variation across comparable jobs is the only way to learn the curve rather than the existing policy, and the product should manage it explicitly rather than leaving the contractor to guess. Recommendations are the contractor's alone, and the system should never surface another contractor's prices.

## Target Customer
Price book content vendors, field service platforms that bundle a book, and the larger contractors who already suspect their pricing is wrong in both directions.

## Impact If Built
A book that arrives approximately right for a market removes the weeks of customisation that are the category's largest implementation friction and its most common reason for switching. For the contractor, correcting prices in both directions on high-volume tasks is a direct margin change that requires no operational effort at all.
