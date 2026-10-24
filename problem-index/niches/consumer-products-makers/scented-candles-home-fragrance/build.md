# A Burn Bench That Measures and Recommends

**Niche:** [[niches/consumer-products-makers/scented-candles-home-fragrance/profile|Scented Candles & Home Fragrance]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decision that limits how many new scents a candle maker can ship each season is a chandler watching test candles burn, and nobody films, measures or learns from those burns.
**Tags:** #tacit-knowledge-ml #cnns #semantic-segmentation #bayesian-optimization #gaussian-processes #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each season's fragrance brief into candles that pass burn testing before the retailer's holiday set ships, and whoever puts the most passing new scents on the holiday shelf takes the account.

## The Problem
For every new fragrance and vessel, the lab pours candles with two or three candidate wicks, cures them for days and burns them in cycles of about four hours (estimate), reading melt pool, flame height, soot and glass heat by eye. A wrong first guess costs a week. Experienced chandlers guess well; new ones do not, and the knowledge sits in notebooks.

## Why Nobody Has Built This
The market looks small and fragmented, makers treat recipes as secrets, and the data does not exist until someone films the burns. Wick suppliers hold the deepest test archives but use them for customer service, not software.

## What to Build
A bench rig of cameras and temperature probes with software that segments flame and melt pool frame by frame, logs the burn metrics against a structured recipe record, and lets the chandler confirm the read in a click. On top, a recommender that proposes the first wicks for a new recipe with uncertainty, and the next test that would narrow it. Production lots can be burn-sampled and compared with the approved standard.

## Target Customer
Heads of lab and quality at candle makers launching dozens of scents a year, and the application labs of wick and wax suppliers.

## Impact If Built
Cutting the average from ~3 test rounds per scent to ~2 (estimate) saves about a week per fragrance; at a maker launching ~40 scents a year that frees ~40 lab-weeks, enough for ~5–10 more scents in a holiday programme (estimate). A filmed burn archive also answers a retailer or CPSC question about a recalled lot in hours rather than days.
