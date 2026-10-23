# The Daily Sweep of Every Open Lumber Quote

**Niche:** [[niches/building-material-dealers/commodity-lumber-panel-pricing/profile|Commodity Lumber & Panel Pricing]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every dealer has hundreds of open lumber quotes priced at different moments; none of them knows, each morning, which ones are now underwater.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #gradient-boosting #feature-engineering #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to reprice every open quote, builder price sheet and counter price to the latest lumber and panel market before the material ships, and whoever lets the fewest packages ship below replacement cost without losing bids to stale prices takes the account.

## The Problem
A quote written three weeks ago at last month's OSB price ships next week. The salesperson remembers some of them; the buyer warns about big moves; most open quotes are never revisited.

## Why Nobody Has Built This
ERPs store quotes and expiry dates, not replacement cost; price optimisers set list prices, not quote-level exposure; and market references are licensed separately.

## What to Build
A nightly job that costs every open quote, unreleased package and builder price sheet at current replacement cost (licensed assessments or the dealer's latest buys, plus freight and duty), adds a short-horizon cost forecast with intervals, ranks quotes by margin at risk and likely ship date, and drafts repricing notes for the salesperson within the hold terms. A two-week demo works on synthetic quotes and a public futures series.

## Target Customer
Pricing managers and commodity buyers at mid-size and large dealers.

## Impact If Built
Margin held through market swings on a category worth ~$10–30M a year at a mid-size dealer (estimate).
