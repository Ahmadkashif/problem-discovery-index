# Store Assortment Set Without the Local Vehicle Parc

**Industry:** [[auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Retail demand-forecasting tools are mature; they forecast from past sales, and a parts store's long tail sells once a year, so the real driver, the vehicles registered around the store and their age, never enters the model.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #bayesian-inference #feature-engineering #data-integration #revenue-impact

## The Problem
A parts store holds ~20,000–25,000 SKUs (AutoZone's 10-K figure for a standard store) out of hundreds of thousands it could stock, and the inventory planner or store owner must decide which. Most of those SKUs sell a handful of times a year at any one store, so last year's sales are a noisy guide: a part that sold zero times may be exactly what the few hundred local crossovers of one model year are about to need as they pass 100,000 miles. Get it wrong and the store either carries dead stock, or sends the shop's call to a hub or a competitor. The chains spend heavily on this (AutoZone's inventory per store reached $963K in fiscal 2026), but a jobber store typically takes the programme group's or supplier's recommended "core assortment" and adjusts by feel, and a supplier's recommendation is shaped by its interest in shelf coverage.

## What Already Exists
General retail forecasting and assortment platforms such as Blue Yonder and RELEX forecast item demand from point-of-sale history, promotions and seasonality, and they are proven in grocery and general merchandise. Vehicle-in-operation data by ZIP code is sold by S&P Global Mobility and Experian, the vendors profiled at [[niches/auto-dealers-independent/registration-market-intelligence/profile|Vehicle Registration & Market Intelligence Data]], and distributor business systems offer min/max replenishment.

## The Customisation Gap
Auto parts demand is driven by the local vehicle parc, not by last year's sales: how many of each vehicle configuration are registered nearby, how old they are, and when each part type tends to fail on that configuration. A useful assortment model has to join licensed VIO counts to the catalog's ACES applications (which part fits which configuration), apply failure-age curves by part type, net out what the nearest hub can deliver within the hour, and learn from lost sales: lookups that found no stock, which the point of sale never records as demand. It also needs to separate shop and do-it-yourself demand, which follow different parts, and to treat cores and returns as reverse flows rather than sales.

## Impact If Solved
If a store reallocated ~10% of its inventory dollars from dead stock to parts its parc is about to need (estimate), its first-call fill rate on shop orders could rise by a few points and its inventory turns by ~0.3–0.5 a year (estimate), without adding a dollar of stock.
