# A Clearing-Price Model From the Firm's Own Deals

**Niche:** [[niches/film-distributors/library-licence-pricing/profile|Library Licence Pricing]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A library seller negotiates hundreds of licences a year and keeps no structured record of offers, counters and clearing prices that could tell the next negotiation where to anchor.
**Tags:** #tacit-knowledge-ml #gradient-boosting #bayesian-inference #confidence-intervals #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a library title or package for a specific buyer, territory and window close to what that buyer will actually pay, and whoever knows the clearing price best closes the deal without leaving money on the table.

## The Problem
The senior salesperson knows that one platform always opens at half what it will pay, that a broadcaster pays a premium for titles with a recent theatrical run, and that package discounts beyond a certain size are a mistake. That knowledge is personal, and leaves when they do.

## Why Nobody Has Built This
Prices are confidential, deal counts per firm are modest, and the variables (title, buyer, territory, term, exclusivity, package composition) are many. Demand vendors estimate value from audience signals without seeing realised prices.

## What to Build
A deal ledger capturing every offer, counter and final price with its terms, drafted from emails and deal memos. On top of it, a hierarchical model of clearing price by buyer, territory, window and title features, with demand-vendor signals as inputs. It proposes an opening ask and a walk-away range with the comparables shown.

## Target Customer
Heads of library sales and television distribution at library holders and independent distributors.

## Impact If Built
More consistent pricing across the sales team, fewer deals closed far below what the buyer would have paid, and a pricing memory that survives staff turnover.
