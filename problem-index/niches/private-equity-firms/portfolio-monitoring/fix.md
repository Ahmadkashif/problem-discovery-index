# The Board Hears It Before the Dashboard Shows It

**Niche:** [[niches/private-equity-firms/portfolio-monitoring/profile|Portfolio Monitoring & KPI Reporting]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Problems at portfolio companies reach the deal partner through a CEO's phone call, weeks after they were visible in the monthly numbers.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn a dozen portfolio companies' differently-defined monthly packages into comparable, on-time KPIs — and whoever does that is the system the deal partner opens when something starts going wrong.

## The Problem
The monitoring dashboard compares actuals to budget once the month is mapped, typically several weeks after month end. Trajectory changes — slowing bookings, stretching receivables, rising overtime — show in the data earlier but are not flagged until they breach a variance threshold.

## Why It's Still Broken
Mapping latency consumes the lead time. Variance-to-budget alerts are the only rule anyone has written. And a false alarm to a deal partner costs credibility.

## What a Fix Looks Like
Shorten mapping latency first. Then flag trajectory breaks on leading indicators, pooled across the portfolio so small series are usable, and rank alerts by estimated EBITDA and covenant impact. Track the lead time of each alert against when the issue was formally raised, and tune to it.

## Who Feels the Pain
Deal and operating partners managing problems late; portfolio CFOs who could have been helped earlier; LPs whose marks absorb the surprise.

## Impact If Fixed
Weeks of lead time on deterioration are worth more than any dashboard redesign, and most of it comes from data the sponsor already collects.
