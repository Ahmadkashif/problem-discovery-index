# A Pre-Bid Exposure Check Across Every Channel

**Niche:** [[niches/wholesale-auto-auctions/floorplan-funds-settlement/profile|Floorplan & Funds Settlement]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A dealer can bid in a physical lane, a simulcast and two digital auctions at once, and the auction learns the dealer cannot pay only after winning all four.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to pay sellers and collect from buyers on every sale without the auction carrying an uncollected receivable, and whoever has the lowest settlement write-offs per dollar of gross sales takes the account.

## The Problem
Bidding limits are set per buyer per channel, if at all. A dealer under stress buys aggressively across channels and lenders, and floorplan headroom is checked only when a purchase is funded. The auction finds the gap when the funding request is declined or the draft is returned.

## Why Nobody Has Built This
Exposure data is split between the auction's channels and the dealer's lenders, and each lender sees only its own line. Auctions fear that declining bids costs sales.

## What to Build
A live exposure service. It sums a buyer's open high bids, unpaid purchases and pending fundings across every channel the auction runs, against the remaining headroom on the buyer's linked floorplan lines (via lender APIs) and the buyer's payment history. A model scores the probability that a purchase will fail to settle. Bids above a threshold are paused for approval or require prepayment, with the reason shown to the buyer.

## Target Customer
Auction controllers and credit managers at chains running physical and digital channels; floorplan lenders integrated with them.

## Impact If Built
If settlement write-offs run at ~0.05% of gross sales (estimate), an auction selling $2B a year loses ~$1M. Catching half of the failing purchases before the bid is accepted saves ~$500,000 a year.
