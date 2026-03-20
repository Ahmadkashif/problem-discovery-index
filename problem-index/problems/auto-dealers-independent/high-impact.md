# Vehicle Acquisition Pricing and Turn Rate Optimization

**Industry:** [[auto-dealers-independent|Independent Auto Dealers]]
**Type:** High Impact
**One-liner:** Dealers stop overpaying at auction and stop sitting on cars that won't move, reclaiming $500-1,500 per unit in margin that currently bleeds out through bad buys and slow turns.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #probability-distributions #revenue-impact

## The Problem
Independent dealers acquire 80% or more of their inventory through wholesale auctions (Manheim, ADESA, local lanes, online simulcast). A dealer principal with a 200-unit lot makes 400-600 buy decisions per year, each one a bet on what a specific VIN will retail for in their local market and how many days it will take. Overpaying by $500 per car — easily done when auction energy runs high and comparable data is stale — destroys $100K+ in annual gross profit. Equally damaging is buying cars with 60+ day market supplies that sit on the lot accruing $35-50/day in floorplan interest while depreciating. The best dealers develop an intuition for local demand patterns, but that intuition doesn't scale and disappears when the owner steps away.

## Why It's Unsolved
Auction pricing data exists (Manheim Market Report, Black Book, NADA guides) but reflects national or regional averages, not the hyperlocal demand at a specific dealer's zip code with their specific buyer demographics. A 2018 Honda Accord might move in 20 days at a suburban Dallas lot but sit for 60 days at a rural Oklahoma lot — guide prices don't capture that. Additionally, condition-adjusted pricing requires interpreting auction condition reports (CR scores, announcements like "frame damage" or "check engine light") that vary in reliability across auction houses. No tool currently combines local retail velocity, acquisition cost, reconditioning cost estimate, and floorplan carrying cost into a single buy/no-buy decision at auction speed.

## What a Solution Looks Like
A mobile-first tool that a dealer uses during auction preview or simulcast: scan or enter VIN, get a localized retail price prediction, estimated days-to-turn at that price, projected reconditioning cost band, and a maximum bid recommendation that preserves target gross margin after floorplan and recon. The model trains on the dealer's own historical sales (price, days on lot, acquisition cost) augmented with regional wholesale and retail transaction data. Output is a simple dashboard: green/yellow/red buy signal, recommended max bid, projected ROI per unit.

## Impact If Solved
A 200-unit dealer improving acquisition accuracy by $500/car reclaims $100K-200K annually in gross profit. Reducing average days-to-turn from 50 to 35 cuts floorplan interest expense by 30%. Across the 38,000 independent dealers in the US, even modest adoption represents billions in recovered margin industry-wide.
