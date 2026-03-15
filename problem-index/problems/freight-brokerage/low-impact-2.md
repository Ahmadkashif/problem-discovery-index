# Shipper Demand Forecasting for Capacity Pre-Procurement

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic demand forecasting tools project volume but don't understand freight-specific demand drivers — shipper inventory cycles, seasonal produce patterns, retail inventory push ahead of holiday seasons — that allow a broker to pre-position carrier capacity before a demand spike.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact

## The Problem

Freight demand is predictable at the macro level — spot rates spike before major holidays, during harvest season for produce, and during retail inventory build cycles. Brokers who know their shippers' demand patterns 3-4 weeks in advance can pre-commit carrier capacity at rates before the market tightens, then fulfill shipper demand at the lower pre-committed rate, earning a higher margin than brokers who are buying capacity reactively when the market is tight.

Experienced brokers who manage major shipper accounts internalize these seasonal patterns. They know that the mid-October produce surge from Florida's citrus harvest hits their shipper's northbound lanes, and they pre-committed capacity in September at flat rates. Junior brokers or new account managers react to demand after it arrives, buying capacity at peak prices.

## What Already Exists

DAT and Truckstop provide rate trend data and seasonal analysis. Freight market analysts (Morgan Stanley freight indices, FreightWaves SONAR) provide macro demand forecasts. No tool builds shipper-specific demand forecasts from the broker's own transaction history with each shipper account.

## The Customisation Gap

A shipper demand forecasting tool needs: (1) shipper-specific historical demand data from the broker's TMS (loads tendered by lane by week over the past 2-3 years); (2) external demand signal integration (retail sales indices, agricultural USDA crop reports, weather patterns affecting produce lanes); (3) a per-shipper, per-lane demand forecast for the next 4-8 weeks; (4) actionable capacity pre-procurement recommendations with the estimated margin improvement from pre-committing vs. spot buying. The shipper-specific demand model is proprietary to the broker's own data.

## Impact If Solved

Pre-committed capacity during peak demand generates 3-5 percentage points of additional margin vs. reactive spot buying. On a $5M shipper account, this is $150,000-$250,000 in incremental gross profit annually.
