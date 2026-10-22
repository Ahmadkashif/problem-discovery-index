# Mini-Bid Triggers From Live Acceptance Data

**Niche:** [[niches/logistics-consultants/truckload-bid-routing-guide/profile|Truckload Bid Design & Routing Guide Performance]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Shippers re-bid a failing lane months after its routing guide broke, because nobody forecasts which lanes are about to fail.
**Tags:** #gradient-boosting #survival-analysis #change-point-detection #time-series-forecasting #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to design truckload awards that carriers keep accepting when the spot market turns, and whoever's routing guides hold the highest primary tender acceptance through the contract year takes the account.

## The Problem
Between annual bids, the transportation team watches acceptance reports. A lane whose primary carrier starts rejecting is noticed when spot spend on it shows up in the monthly report, and a mini-bid is organised weeks later. By then the shipper has paid spot premiums on that lane for a quarter, and carriers in the mini-bid price in the tight market.

## Why Nobody Has Built This
Acceptance is reported backwards, as a percentage per carrier per month. Forecasting it needs the lane's contract rate against the live spot market, carrier-level rejection history, seasonality and the carrier's network balance — data split between the TMS, a benchmark subscription and the consultant's spreadsheet, and owned by nobody whose job is prediction.

## What to Build
A lane-level model that estimates, weekly, the probability that the primary carrier's acceptance will fall below a threshold in the next four to eight weeks, from the contract-to-spot spread, recent rejections, carrier behaviour on similar lanes and season. Lanes above a risk threshold are queued for a mini-bid, with a draft lane package and the carriers most likely to hold the lane at a stated rate. Distinct from measuring decay after the fact — this decides when to act.

## Target Customer
Shippers with several hundred or more contracted truckload lanes, and consultants offering managed procurement between annual bids.

## Impact If Built
Mini-bids run before the spot premium accumulates; recovering even a few points of primary acceptance on high-volume lanes saves material spot spend (estimate).
