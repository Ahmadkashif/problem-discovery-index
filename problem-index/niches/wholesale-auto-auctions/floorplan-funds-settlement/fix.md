# The Seller Paid Before the Floorplan Funded

**Niche:** [[niches/wholesale-auto-auctions/floorplan-funds-settlement/profile|Floorplan & Funds Settlement]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Fix (Pain Point)
**One-liner:** The auction pays a commercial seller on its standard schedule, and the buyer's floorplan request is declined two days later because the lender had already put the dealer on hold.
**Tags:** #descriptive-statistics #logistic-regression #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to pay sellers and collect from buyers on every sale without the auction carrying an uncollected receivable, and whoever has the lowest settlement write-offs per dollar of gross sales takes the account.

## The Problem
Commercial consignors expect payment on a fixed schedule, and large dealer sellers negotiate fast payouts. The buyer's floorplan request is submitted after the sale, and the lender can decline it if the dealer's line is frozen, past curtailment or under audit. The auction has then paid out money it has not collected, against a dealer who may already be in trouble with every lender it uses.

## Why It's Still Broken
Payout schedules are set by the commercial contract and run on autopilot. Lender holds reach the auction as a declined funding request, not as an advance warning. Different lenders do not tell the auction about each other's holds.

## What a Fix Looks Like
Hold the seller payout for any sale whose floorplan funding has not confirmed, and query the lender's status API at the sale, not after it. Where lenders publish dealer hold status to the auction under their agreements, show it on the buyer's account before the next bid.

## Who Feels the Pain
Auction treasurers carrying the receivable; collections teams chasing a dealer in distress; commercial sellers whose payouts are later clawed back or delayed.

## Impact If Fixed
If a mid-sized auction pays out ~$50,000–150,000 a year on purchases whose funding is later declined (estimate), matching payout to funding confirmation removes most of that exposure for the cost of a one- or two-day payout delay on a small share of sales.
