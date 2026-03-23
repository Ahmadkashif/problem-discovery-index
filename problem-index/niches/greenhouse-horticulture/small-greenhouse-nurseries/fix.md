# Spring Season Demand Forecasting from Pre-Book Orders

**Niche:** [[niches/greenhouse-horticulture/small-greenhouse-nurseries/profile|Small Greenhouse Nurseries]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Fix (Pain Point)
**One-liner:** Small nurseries must commit to plug and liner orders 4-6 months before spring sales, but pre-book orders from landscaper accounts represent only 30-50% of total demand — the rest is walk-in retail that is forecast by the owner's gut feel and consistently missed by 20-40%.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
In October-November, a small nursery owner submits plug and liner orders to wholesale propagators (Ball Horticultural, Syngenta Flowers, Proven Winners) for spring delivery. These orders lock in 60-70% of the spring production plan 5-6 months in advance. The owner bases quantities on: pre-book orders from landscaper accounts (often informally communicated), last year's sales (recalled from memory or basic POS data), and general market trends (from trade publications and supplier sales reps). Walk-in retail demand — which represents 50-70% of revenue at retail nurseries — is the hardest to forecast because it depends on spring weather timing, local housing market activity, competitor pricing, and consumer trends that shift annually. The result: chronic over-ordering of perennial favorites ("we always sell hostas") and under-ordering of trending items ("everyone wanted native plants this year and we ran out in week 2").

## Why It's Still Broken
Small nurseries generate 3-5 months of meaningful sales data per year (the spring rush), making the time series extremely short and seasonal. Year-over-year demand varies by 20-40% based on weather-driven season start dates alone — a late frost delays the entire season by 2-3 weeks, compressing sales into a shorter window. The owner's historical sales data, where it exists, is at the SKU level (did this item sell?) not at the timing level (when did demand peak, how fast did we sell through, when did we stock out?). Without sell-through rate data, the owner cannot distinguish between items that sold well and items that could have sold twice as much if more had been grown.

## What a Fix Looks Like
A demand planning tool that ingests: (1) last year's POS sales data at the daily-item level, (2) pre-book orders from landscape accounts, (3) regional spring weather forecasts and historical season-start dates, (4) local housing permit data (proxy for landscape demand), and (5) trend signals from industry sources (Proven Winners trending items, Pinterest garden trends). The model produces per-item quantity recommendations with confidence intervals for the October ordering window. Key output: "Based on your sales data, landscaper pre-books, and the long-range forecast, order 150 flats of calibrachoa (up 20% from last year) and reduce dianthus to 80 flats (sold through only 60% last spring)."

## Who Feels the Pain
Nursery owners who commit $30K-$100K in plug orders every October with 30-40% forecast error. The financial pain manifests as $5K-$15K in wasted plants (overproduction of slow items) and $10K-$30K in lost sales (stockouts of popular items).

## Impact If Fixed
Ordering accuracy improves from +/- 30% to +/- 15%, reducing combined waste and lost-sale costs by $10K-$25K annually per nursery. Cash flow improves as capital is deployed more efficiently — buying what will sell rather than what the owner hopes will sell.
