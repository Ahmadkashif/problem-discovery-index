# Auction Theory and Bid Optimisation

**Niche:** [[niches/d2c-brand-operators/paid-acquisition/profile|Paid Acquisition]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Auction theory and bidding optimisation are extensively developed on the platform side, and the advertiser's side of the same auction is operated by intuition.
**Tags:** #convex-optimization #markov-decision-processes #probability-distributions #confidence-intervals #revenue-impact #evaluation-metrics #optimization-fundamentals #bayesian-inference
**Contested on:** Every serious competitor in this sub-niche is fighting to buy an incremental new customer for less than the next brand bidding on the same impression — and whoever does that survives, because the auction price rises structurally and the margin between cost and value is the whole business.

## The Problem
The economics of repeated auctions with budget constraints are well studied, and the platforms have invested heavily in the seller's side of them. The advertiser's side — how to value an impression, how to pace a budget, how to behave when competitors change their bids, when to bid on incremental value rather than on attributed value — has the same theory available and is mostly operated by adjusting a target return figure and watching what happens.

## What Already Exists
Auction theory with results on optimal bidding under budget constraints; budget pacing and throttling algorithms; bid shading in programmatic buying; value-based bidding frameworks; sequential decision methods for repeated auctions; and the programmatic industry's toolkit for the buy side.

## The Customization Gap
The adaptation is to an auction where the platform runs the optimisation and the advertiser supplies only the objective. It requires: (1) the value signal as the primary lever, since the advertiser no longer sets bids and the one thing they control is what they tell the platform an outcome is worth — recognising this is the strategic reframing, and it makes the signal work in the build note the main event rather than plumbing; (2) incremental rather than attributed value as the objective, which requires the incrementality measurement and is the correction that stops a brand bidding up customers it would have got anyway; (3) budget pacing across channels with different response latencies, which the pacing literature handles and brands do by eye; (4) competitive response modelled, since a brand raising its bids raises everyone's costs and the auction's structural price trend is partly self-inflicted at a category level; and (5) planning for a rising clearing price rather than treating each quarter's cost increase as an anomaly.

## Target Customer
Performance marketing teams, agencies, brand finance functions planning against rising costs, and the auction theory community whose advertiser-side work is under-applied.

## Impact If Solved
The platform runs the optimisation and the advertiser controls only the objective, which makes the value signal the strategic lever rather than a plumbing detail. Bidding on incremental rather than attributed value is what stops a brand paying up for customers it already had.
