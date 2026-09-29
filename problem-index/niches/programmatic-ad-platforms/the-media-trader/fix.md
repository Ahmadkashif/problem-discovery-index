# The Campaign That Underdelivered on a Friday

**Niche:** [[niches/programmatic-ad-platforms/the-media-trader/profile|The Media Trader]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The trader finds out on the last day of the month that a campaign will miss its delivery, and spends the weekend buying whatever inventory will clear.
**Tags:** #time-series-forecasting #change-point-detection #evaluation-metrics #confidence-intervals #worker-facing #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to take the slider-dragging off the trader so they can do the judgement work they were hired for — and whoever does that changes what a trading desk is worth.

## The Problem
Delivery has been slipping for eleven days. The pacing report shows a percentage against a linear target, which looked acceptable each day because the shortfall accumulated slowly. On the twenty-eighth it becomes obvious that the campaign will land short. The trader now has three days to spend a quarter of the budget, so they raise bids and loosen targeting, buy the cheapest inventory that will clear, hit the delivery number, and deliver terrible results. The client sees a fulfilled contract and poor performance, and the trader knew it was coming for a week and a half without being able to prove it in time.

## Why It's Still Broken
Pacing is reported against a straight line, which is the wrong model for delivery that depends on inventory availability, competition and seasonality — the linear assumption is what hides the shortfall. Reports show position rather than projection, so a trend that is obviously heading to a miss looks like a small current gap. Alerts fire at thresholds that are crossed too late to act well. And the end-of-period scramble is normalised as part of the job.

## What a Fix Looks Like
Forecast the landing, not the position. Project end-of-flight delivery daily with an interval, using the campaign's own observed rate, inventory availability and seasonality, which is the fix and turns an invisible slow slippage into a visible projected miss — a trader who sees a projected shortfall on day nine has options that a trader on day twenty-eight does not. Alert on the projection rather than on the current gap, since the current gap is by construction the least informative number available. Model delivery capacity properly, because a campaign whose targeting simply cannot deliver the budget should be identified in week one and renegotiated rather than rescued in week four. Show the quality cost of catching up, so the trade-off between hitting delivery and destroying performance is an explicit decision rather than a default. Automate gradual correction early, which is far cheaper than a late intervention and is exactly the mechanical work the build note removes. Distinguish a pacing problem from a targeting problem from a market problem, as the three have different remedies and are indistinguishable in a pacing percentage. Give the client an early conversation instead of a late surprise, which is what preserves the relationship. Track the end-of-period quality collapse as a measured phenomenon, since it is systematic across the industry and nobody quantifies it. Learn each account's delivery patterns, because the same campaign structure behaves consistently across flights. And report forecast accuracy, so the trader knows how much to trust the projection.

## Who Feels the Pain
Traders spending the last weekend of every month rescuing delivery; clients receiving fulfilled contracts and poor outcomes; and the market absorbing a systematic end-of-period surge of indiscriminate buying.

## Impact If Fixed
Linear pacing hides a slow shortfall until it is unrescuable, and the report shows position rather than projection. A daily landing forecast with an interval gives the trader options on day nine instead of a weekend of indiscriminate buying on day twenty-eight.
