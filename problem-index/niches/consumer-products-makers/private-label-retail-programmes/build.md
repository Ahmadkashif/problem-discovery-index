# Return Reasons Joined to the Lot That Caused Them

**Niche:** [[niches/consumer-products-makers/private-label-retail-programmes/profile|Private-Label Programmes for Mass Retailers]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retailer decides a private-label re-bid on return and defect rates the maker sees only as monthly totals, never traced back to the shift, lot or component that caused them.
**Tags:** #large-language-models #bert #gradient-boosting #causal-inference #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep a retailer's own-brand programme through its annual re-bid, and whoever ships the retailer's specification with the lowest defect-and-return rate takes the account.

## The Problem
The retailer's quality scorecard shows a return rate and a few complaint categories. Customer comments ("wick drowned", "pen dried out", "mop head fell off") sit in the retailer's review and returns systems. The maker cannot tell whether the problem is one bad wax lot, one vessel supplier or a design flaw.

## Why Nobody Has Built This
Returns data belongs to the retailer and arrives as summaries; makers lack lot-level traceability on shipments; and no vendor sells to private-label makers specifically.

## What to Build
A system that ingests whatever return and review data the retailer shares, classifies free-text reasons into defect types with a language model, matches item and date codes to production lots and component batches, and estimates which causes drive the return rate. It produces a corrective-action file for the next quality review.

## Target Customer
Quality directors and private-label account leads at makers supplying three or more retailer own-brand programmes.

## Impact If Built
Cutting a programme's return rate from ~3% to ~2% (estimate) on $10M of own-brand sales saves ~$100K a year in returns and defective allowances, and gives the maker measured evidence to carry into the re-bid.
