# Wholesale Order and Inventory Matching for Ornamental Growers

**Industry:** [[greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic inventory management cannot track live plants at varying growth stages, predict bloom timing, or match future-state inventory to wholesale orders placed weeks in advance.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #data-integration

## The Problem
Ornamental greenhouse operations (bedding plants, potted flowering, foliage) sell primarily through wholesale channels — big box retailers (Home Depot, Lowe's), garden centers, and landscapers — with orders placed 2-8 weeks before ship date. The grower must commit to fulfilling an order for "5,000 4.5" red geraniums, in flower, ship week 18" based on their assessment of current crop status. If the crop runs late (cold snap, cloudy weeks), they ship substandard product or short the order; if it runs early, they hold finished plants that consume bench space and labor. Current systems track what was planted and when, but cannot forecast what will be shippable and when.

## What Already Exists
Greenhouse ERP platforms like BloomMaster, Picas, and GrowerExpert handle order entry, invoicing, and basic inventory counts. Retail supply chain tools (EDI-based) manage purchase orders and ASNs. None model the biological state of inventory — a flat of petunias planted last Monday is not the same as one planted three weeks ago, even though both are "petunia flats" in the system. Generic demand forecasting tools (e.g., built into NetSuite or SAP) assume fixed lead times and deterministic supply.

## The Customisation Gap
The system needs to: (1) track each crop lot with planting date, current growth stage, and zone assignment, (2) predict finish date and bloom timing using accumulated growing degree days, light integral, and cultivar-specific response curves, (3) model the probability distribution of ship-readiness for each lot (not a point estimate), (4) match incoming orders against predicted-available inventory with confidence intervals, and (5) flag order commitments that have >20% risk of not being met in time for the grower to adjust (e.g., apply growth regulators, increase temperature). A gradient-boosting model trained on historical lot-level data (planting → actual ship date, with climate data as features) provides the predictive core.

## Impact If Solved
Ornamental growers report 5-12% of revenue lost to order shortfalls, substitutions, and distressed-price sales of mis-timed crops. For a $10M/year operation, that is $500K-$1.2M in recoverable revenue. Buyers benefit from higher fill rates, reducing the grower's risk of losing shelf space allocations at major retailers.
