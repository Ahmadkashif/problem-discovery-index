# A Disposition Policy per Lot

**Niche:** [[niches/grocery-stores/fresh-markdown-expiry-pricing/profile|Fresh Markdown & Expiry Pricing]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every aging lot has five possible endings (mark down, transfer, surplus app, donate, cull), and no system chooses among them with the lot's own sales rate and the store's prices in view.
**Tags:** #markov-decision-processes #dynamic-programming #causal-inference #bayesian-inference #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to price or divert short-dated fresh product before it is culled, and whoever recovers the most margin per marked-down lot net of cannibalised full-price sales takes the account.

## The Problem
A store has 14 packs of ground beef dated tomorrow, 30 pounds of ripe bananas and six bakery cakes past their best. The clerk applies the chain's rule: 30% off on the date. Some items would have sold at full price by evening; others needed 50% off two days earlier; the bananas would have been worth more as smoothie fruit in the deli. Each ending is managed by a different tool or none.

## Why Nobody Has Built This
Markdown vendors price, surplus apps list, donation programmes collect, and the deli runs its own production. None owns the choice between them. Measuring cannibalisation needs randomised markdown tests that chains rarely run.

## What to Build
A daily policy per lot that estimates the sales rate at each markdown depth and days-to-expiry, the cannibalised full-price sales, the transfer value to the deli, and the surplus-app and donation outcomes. It then recommends the ending that maximises recovered value under the chain's waste and donation targets. It prints or pushes the label, lists the item on the surplus app, or schedules the donation, and runs small randomised depth tests to keep its elasticity estimates honest.

## Target Customer
Fresh merchandising and sustainability leaders at chains with food-waste commitments and electronic shelf labels in at least some stores.

## Impact If Built
For a store marking down ~$4,000 of fresh a week, recovering 10 more cents per marked-down dollar is ~$20,000 a year (estimate), with less sent to the dumpster.
