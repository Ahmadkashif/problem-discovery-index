# Real-Time Margin Optimization Dashboard

**Niche:** [[niches/freight-brokerage/full-truckload-dry-van/profile|Full Truckload Dry Van Brokerages]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool shows a broker their real-time blended margin across all active loads, highlights which lanes are under-priced relative to current market conditions, and recommends rate adjustments on pending quotes before they're sent to shippers.
**Tags:** #gradient-boosting #time-series-forecasting #tacit-knowledge-ml #revenue-impact

## The Problem
Mid-market FTL brokers price each load individually — a broker checks DAT, looks at their recent history on the lane, and quotes a rate. There is no portfolio-level view showing which shipper accounts are generating healthy margins and which are eroding, or which pending quotes are priced below current market conditions. By the time a broker realizes a lane's market has tightened, they've already quoted and booked loads at stale rates, compressing margin for the entire week.

## Why Nobody Has Built This
Building a margin optimization dashboard requires integrating TMS transaction data (shipper rates, carrier costs per load) with real-time market rate feeds (DAT API, FreightWaves SONAR) and computing the gap on a per-load, per-lane basis. The data integration between TMS platforms and market data APIs is bespoke — McLeod's data model differs from Mercury Gate's. No vendor has invested in the mid-market integration work because the large brokerages built this internally.

## What to Build
A TMS-integrated dashboard that: (1) shows real-time blended margin by shipper account and lane; (2) highlights pending quotes where the quoted shipper rate is below the current market rate plus target margin; (3) recommends rate adjustments on pending quotes with expected win probability at each price point; (4) alerts when a contracted shipper lane's margin has dropped below threshold due to carrier cost increases.

## Target Customer
Operations managers and brokerage owners at mid-market FTL brokerages ($10-100M revenue) using McLeod or Mercury Gate TMS. Approximately 3,000 brokerages fit this profile. Average contract value: $12-24K/year.

## Impact If Built
A 2-point margin improvement on a $30M brokerage generates $600K in additional annual gross profit. Even a 1-point improvement from avoiding under-priced quotes on tightening lanes pays for the tool 25x over.
