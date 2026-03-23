# Sourcing Decision Fatigue and Scan-to-Decision Latency

**Niche:** [[niches/ecommerce-sellers/reseller-arbitrage-ops/profile|Reseller & Arbitrage Operators]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Fix (Pain Point)
**One-liner:** Resellers scan 200-500 barcodes per sourcing trip but spend 30-60 seconds evaluating each product because current scanning tools don't provide an instant buy/skip decision with full cost analysis.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #worker-facing #quick-win

## The Problem
A retail arbitrage reseller walks through Walmart or Target scanning barcodes with the Amazon Seller App. For each scan, they must evaluate: current Amazon price, sales rank (velocity proxy), FBA fees, their target margin, competitive seller count, and whether the product has restrictions or IP complaints. This evaluation takes 30-60 seconds per item, and during a 3-hour sourcing trip scanning 300 items, mental fatigue sets in after the first hour — leading to bad decisions (buying marginal products or passing on good ones) and physical exhaustion from the repetitive evaluate-decide-scan cycle.

## Why It's Still Broken
The Amazon Seller App shows raw data (price, rank, fees) but doesn't compute a clear buy/skip recommendation. Scoutify (from Inventory Lab) and ScanPower add profitability estimates but still require mental evaluation of velocity, competition, and restrictions. No tool provides a single "buy at this price or below / skip" output that accounts for the reseller's personal criteria (target ROI, category preferences, storage constraints, historical performance on similar products). The reseller must mentally process 5-7 data points per scan, hundreds of times per trip.

## What a Fix Looks Like
A scan-and-decide tool that processes a barcode scan and within 2 seconds displays a single green/yellow/red signal with the maximum purchase price to hit the reseller's target margin. Behind the signal: automated checks for FBA restrictions, IP complaints, competitive saturation (too many sellers), and velocity thresholds. Yellow items show the specific concern ("slow sales rank — expect 45 days to sell" or "3 competitors at this price — margin pressure likely"). Personal criteria (minimum ROI, excluded categories, maximum inventory value per item) are preconfigured so the decision requires zero mental math.

## Who Feels the Pain
Full-time retail arbitrage resellers who do 3-5 sourcing trips per week and scan 200-500 products per trip, experiencing decision fatigue that reduces sourcing quality in the second half of every trip.

## Impact If Fixed
Reduces scan-to-decision time from 30-60 seconds to 2-5 seconds, increasing products evaluated per trip by 2-3x. Eliminates decision fatigue errors that account for an estimated 15-20% of unprofitable purchases. Recovers 5-8 hours/week of sourcing time through faster evaluation.
