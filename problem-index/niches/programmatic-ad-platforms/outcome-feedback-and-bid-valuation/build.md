# Trained on a Click, Sold on a Sale

**Niche:** [[niches/programmatic-ad-platforms/outcome-feedback-and-bid-valuation/profile|Outcome Feedback & Bid Valuation]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bid is priced in ten milliseconds against a click, because the sale it was supposed to cause is observed by the advertiser a month later and never joined back to the impression.
**Tags:** #survival-analysis #causal-inference #gradient-boosting #loss-functions #confidence-intervals #evaluation-metrics #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to join the sale back to the impression that caused it and price the bid against that rather than against a click — and whoever closes that loop changes what every impression in the market is worth.

## The Problem
A bidder values an impression at four-tenths of a cent because a model says this user, on this page, at this moment, is likely to click. Thirty days later some of those users bought something, in a system the bidder will never see, recorded against a campaign rather than an impression. The model that set the price is never told which of its bids were right. The industry has built the most sophisticated real-time infrastructure in commercial computing and pointed it at a label it openly describes as a proxy, because the real label arrives late, aggregated, and in someone else's hands.

## Why Nobody Has Built This
The outcome belongs to the advertiser and the impression belongs to the platform, and neither will hand its asset to the other — this is a data-ownership standoff rather than a technical limit, and it has held for fifteen years. Clicks are immediate, abundant and sufficient to demonstrate optimisation. Delayed and censored labels require modelling most bidding teams have not built. And every participant benefits from a metric they can report today.

## What to Build
Make the outcome the training signal. Build a return path for advertiser outcome data that is privacy-preserving and commercially acceptable — clean rooms, aggregate joins, or advertiser-side models returning gradients rather than rows — which is the prerequisite and is a commercial design problem at least as much as a technical one. Handle delayed and censored labels properly, since most conversions have not happened yet when the model trains and treating them as negatives is the specific error that makes the naive approach worse than clicks. Predict conversion value rather than conversion probability, because bidding on a probability of a purchase of unknown size discards the information that matters most to the advertiser. Model the delay distribution itself, as an impression that converts in three days and one that converts in twenty-eight are worth different amounts to a business with a cost of capital. Price the bid on incremental rather than total expected outcome, which connects to the incrementality niche and is the difference between buying sales and buying credit for sales. Support advertisers who will return only aggregate data, since that is most of them and a system requiring row-level returns serves nobody. Fall back gracefully to proxies where outcome data is thin, with the model knowing which regime it is in. Report to advertisers what their returned data bought them, because the return path only persists if its value is demonstrable. Handle the cold start for new advertisers with transfer from similar ones, which is where the platform's cross-advertiser position is a genuine advantage. And evaluate on outcome lift against a proxy-trained baseline, since that comparison is the whole argument.

## Target Customer
Demand-side platforms and bidders, large advertisers with outcome data and no way to use it, and the measurement vendors sitting between them.

## Impact If Built
The industry points extraordinary infrastructure at a label it describes as a proxy because the real one is late and in someone else's hands. A commercially acceptable return path plus proper delayed-label handling changes what every impression is worth rather than making the auction faster.
