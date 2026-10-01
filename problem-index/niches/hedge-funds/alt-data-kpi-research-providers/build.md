# Every Estimate Ever Published, Graded Against the Print

**Niche:** [[niches/hedge-funds/alt-data-kpi-research-providers/profile|Alternative Data KPI Research Providers]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A KPI research vendor publishes thousands of estimates a year, each one followed weeks later by the company's reported number, and has no standing, honest record of its own accuracy by ticker, metric and panel condition.
**Tags:** #bayesian-inference #time-series-forecasting #confidence-intervals #evaluation-metrics #hypothesis-testing #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to put the most accurate pre-earnings KPI estimate in front of a fund on the most tickers — and whoever can show a graded, calibrated track record per ticker takes the renewal.

## The Problem
The product of an alternative-data research firm is a forecast with a perfect, fast label. Every estimate of a company's quarterly revenue, units or subscribers is followed by the reported figure on a known date. Funds renew subscriptions on whether the estimates helped, and every client builds its own private scorecard to decide.

The vendor itself typically holds the complete history — every estimate, every revision, every methodology change — and reports accuracy selectively: headline hit rates on the tickers where the panel works, marketing decks on the best calls. There is rarely a standing, internally trusted record that says, for each ticker and metric, how accurate the estimate has been, how that varies with panel size and seasonality, and when a mapping started to drift.

## Why Nobody Has Built This
Publishing honest accuracy invites clients to drop the weak tickers. Internally, accuracy is tracked by individual analysts in their own spreadsheets, and methodology changes break comparability over time. The estimate archive is often stored as current state rather than as dated vintages.

## What to Build
A forecast ledger: every estimate stored with its vintage, panel composition, methodology version and analyst; graded automatically against the reported figure on the print date; and summarised per ticker and metric with intervals. Use it internally to allocate analyst effort, retire tickers where the panel no longer tracks, and detect drift between quarters. Use it externally as a calibrated confidence on every estimate, which turns a number into a decision input a PM can size against.

## Target Customer
Chief research officers and heads of research product at alternative-data research vendors.

## Impact If Built
Calibrated confidence per estimate is a product feature competitors without the archive cannot copy, and internal grading points analyst time at the tickers where accuracy can still be improved.
