# Anomaly Detection Adapted to Thin Cash Bid Networks

**Niche:** [[niches/crop-farming/ag-market-intelligence-providers/profile|Agricultural Market Intelligence Providers]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data quality monitoring learns what normal looks like from history; a rural elevator that posts a bid twice a week during three months of the year has no history to learn from.
**Tags:** #gaussian-mixture-models #probability-distributions #confidence-intervals #change-point-detection #random-forests #evaluation-metrics #hypothesis-testing #automation #data-integration #workflow-orchestration

## The Problem
The cash bid network is the firm's most distinctive asset and its most fragile. Bids are collected from thousands of elevators by scraping, feeds, and phone, with wildly uneven frequency — major terminals post continuously, small rural elevators post irregularly and seasonally. A bad bid propagates directly into basis calculations that farmers use to decide whether to sell, and the thin locations where errors are hardest to detect are exactly the ones a local farmer relies on most, because no alternative source exists for them. Detection today is threshold rules and analyst spot checks, which work on the busy locations and fail on the sparse ones.

## What Already Exists
Data observability is mature and inexpensive. Monte Carlo, Bigeye, Soda, and Great Expectations all provide freshness, volume, and distribution monitoring with learned thresholds and lineage-aware alerting; time series anomaly detection is a commodity capability in every cloud platform.

## The Customization Gap
All of them define anomalies against an entity's own history, which requires the entity to have one. A location posting a few dozen bids a year provides no usable baseline, so these tools either alert constantly or, once tuned to be usable, never alert at all. The information that would catch a bad thin-location bid is structural: its relationship to nearby elevators, to the futures market, to freight economics, and to the seasonal basis pattern for that crop and region. The adaptation is anomaly detection over a spatial and economic relationship graph rather than over independent series — a bid evaluated against what its neighbours, the board, and freight imply it should be, with the strength of the inference scaled to how much support the location actually has. Alerting must be weighted by reliance rather than uniformly: an error at a location that is the only reference for a farming area matters far more than the same error where three alternatives exist. And the same relationship model that catches errors is the right basis for estimating a bid where none was posted, which the firm currently handles by carrying the last value forward.

## Target Customer
Heads of data operations and market data leads at agricultural intelligence providers, and the analysts who currently catch bad bids by spot check and by subscriber call.

## Impact If Solved
Fixes the failure that most damages a market data subscription — the customer finding the bad number first — in the part of the network where it is most likely and where the customer has no alternative source. Structural estimation also fills gaps that are currently carried forward silently, which is a quiet quality problem nobody is measuring.
