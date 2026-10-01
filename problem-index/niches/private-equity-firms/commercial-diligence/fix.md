# Market Forecasts Never Checked Against the Market

**Niche:** [[niches/private-equity-firms/commercial-diligence/profile|Commercial Diligence]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every CDD report contains a five-year market growth forecast, and neither the sponsor nor the provider ever checks it five years later.
**Tags:** #time-series-forecasting #evaluation-metrics #confidence-intervals #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to say, from evidence gathered in four weeks, whether the target's revenue will still be there and growing in five years — because that judgement is the exit multiple.

## The Problem
The market model is the spine of the commercial case: a growth rate, a share trajectory, a pricing assumption. The sponsor underwrites to it and the exit thesis depends on it. At exit, the company's realised growth is known and the market's is often observable too. The forecast is never compared with the outcome.

## Why It's Still Broken
The provider would rather not be graded; the sponsor's deal team has moved on; and the forecast lives in a slide rather than a dataset.

## What a Fix Looks Like
Store every CDD forecast as structured data at close — market, metric, horizon, base and range. At each annual review and at exit, record the realised value. Report forecast error by provider, market type and horizon, and apply the measured bias as an adjustment in future underwriting.

## Who Feels the Pain
Deal partners underwriting to optimistic market views; LPs whose returns depend on them; and good CDD providers whose accuracy cannot be demonstrated.

## Impact If Fixed
A few years of structured forecasts gives the sponsor a calibrated view of how far to trust any CDD growth number — a cheap, compounding improvement to every future underwriting.
