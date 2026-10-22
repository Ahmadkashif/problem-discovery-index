# A Bid Model Graded Against What the Portfolio Did

**Niche:** [[niches/credit-card-issuers/co-brand-partnership-bidding/profile|Co-Brand Partnership Bidding & Renewal]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Issuers bid on co-brand portfolios with spreadsheet forecasts and almost never go back to see how far the winning bid's assumptions were from what the portfolio then did.
**Tags:** #survival-analysis #bayesian-inference #time-series-forecasting #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to price a partner's portfolio — remuneration per mile or point, the spend and revolve the partner's customers will generate, acquisition through the partner's own channels, and the balances that move at contract expiry — closer to its true lifetime value than the rival bidder, and whoever prices it best takes the account.

## The Problem
A bid assumes spend per active account, revolve rates, credit losses, new accounts per year through the partner's channels, attrition, and the partner's cost per mile. Each assumption is a forecast; together they decide a ten-year contract. After signing, the deal team moves on and the assumptions are never graded.

## Why Nobody Has Built This
Each bid is treated as a one-off, the data rooms are confidential to each process, and the issuer's own history of bids — won and lost — sits in deal folders rather than a database.

## What to Build
An issuer-side valuation model that takes a data room's portfolio tapes and produces lifetime value with uncertainty bands, calibrated on the issuer's own past co-brand portfolios and their actual performance; and a bid ledger that records every assumption in every bid and grades it annually against the portfolio's results, so the next bid starts from known biases.

## Target Customer
Heads of partnerships and card CFOs at issuers that compete for co-brand and private-label programmes.

## Impact If Built
Bids priced from evidence about the issuer's own forecasting error, which on a portfolio of tens of billions of dollars in balances is worth more than any single assumption.
