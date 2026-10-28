# An Adjustment Offer the Buyer Accepts

**Niche:** [[niches/wholesale-auto-auctions/arbitration-post-sale-claims/profile|Arbitration & Post-Sale Claims]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Arbitration desks propose adjustments from experience and a repair estimate the buyer's own shop wrote, so offers are rejected and cars come back.
**Tags:** #k-nearest-neighbors #linear-regression #regularization #large-language-models #evaluation-metrics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to settle buyers' post-sale claims under the NAAA guidelines without taking the car back, and whoever settles the largest share of granted claims by price adjustment rather than unwinding the sale takes the account.

## The Problem
When a claim is granted, the desk offers the buyer an amount to keep the car. The buyer's shop estimate is the anchor, and it is often padded. The seller wants the lowest figure. The admin splits the difference by feel, the buyer refuses, and the car is unwound with transport back, a relisting and a rerun.

## Why Nobody Has Built This
Settled-claim histories sit inside each auction and have never been modelled as a pricing problem. Repair estimates arrive as PDFs in a dozen shop formats. And the categories changed on 1 June 2026, so rules-of-thumb from before are out of date.

## What to Build
An adjustment engine. It extracts line items from the buyer's estimate with an LLM, retrieves the most similar settled claims by defect category, vehicle, price band and region, and fits a regularised model of the amount buyers accepted. The admin sees a proposed figure, a range, the comparable cases and the probability the buyer accepts. The engine learns from every accept or reject.

## Target Customer
Arbitration directors at the national auctions; independent auctions through their auction-management software.

## Impact If Built
If 60% of granted claims settle by adjustment today and better offers lift that to 70% (estimates), each avoided unwind saves ~$500–1,500 in transport, relisting and depreciation. At 10,000 granted claims a year that is $0.5–1.5M saved at one national auction.
