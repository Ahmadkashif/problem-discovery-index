# Card-Network Payment Risk Scoring Adapted to Dealer Settlements

**Niche:** [[niches/wholesale-auto-auctions/floorplan-funds-settlement/profile|Floorplan & Funds Settlement]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payment processors score every card and ACH transaction for return risk in milliseconds; auctions accept a dealer's draft on reputation.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to pay sellers and collect from buyers on every sale without the auction carrying an uncollected receivable, and whoever has the lowest settlement write-offs per dollar of gross sales takes the account.

## The Problem
Dealers pay by floorplan draw, ACH, wire, draft or check. Non-floorplan payments are accepted and the car is often released before they clear. Returns surface days later.

## What Already Exists
Payment risk platforms used by processors and banks score ACH and card transactions for return and fraud risk from account history, velocity and network data. Bank-account verification services confirm balances and ownership.

## The Customization Gap
Auction settlement needs:
- dealer-level rather than consumer-level features: licence status, floorplan headroom, purchase velocity across channels, prior returns and arbitration behaviour;
- large, lumpy tickets averaging ~$13,800 a car, often several a day;
- decision points that match the auction workflow, at bid acceptance, gate pass and seller payout;
- links to floorplan lender APIs for the share of purchases they fund.

## Target Customer
Auction treasurers and controllers; payment-operations teams at digital marketplaces.

## Impact If Solved
Scoring non-floorplan payments at gate-pass time could halve returned-payment losses (estimate). At an auction absorbing ~$200,000 a year in uncollected receivables, that saves ~$100,000.
