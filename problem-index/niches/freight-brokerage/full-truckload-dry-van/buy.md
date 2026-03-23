# TMS-Integrated Lane Pricing Intelligence

**Niche:** [[niches/freight-brokerage/full-truckload-dry-van/profile|Full Truckload Dry Van Brokerages]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** DAT and Truckstop provide market rate benchmarks, but they show the market average — not the rate this specific broker should quote to this specific shipper on this specific lane, given their carrier network depth and the shipper's historical rate sensitivity.
**Tags:** #gradient-boosting #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
A broker quoting a Chicago-to-Dallas dry van load checks DAT's average spot rate ($2.10/mile) and adds their margin to arrive at a shipper quote. But the DAT average doesn't account for: this broker's carrier network on this lane (they have 5 reliable carriers who run it weekly at $1.95/mile), this shipper's rate tolerance (they've accepted quotes 8% above DAT average without pushback), or the current week's capacity signal (carrier-to-load ratio is tightening, rates will be higher by pickup date). The broker leaves margin on the table or loses loads by pricing generically.

## What Already Exists
DAT RateView provides lane-level spot and contract rate averages. FreightWaves SONAR provides market capacity indicators. Greenscreens.ai provides rate intelligence. These tools provide market benchmarks but not broker-specific, shipper-specific pricing recommendations.

## The Customization Gap
A lane pricing tool for mid-market FTL brokers needs: (1) the broker's own transaction history on each lane (their actual carrier costs, not market averages); (2) shipper-specific rate sensitivity modeling (at what price does this shipper switch to a competitor?); (3) carrier network depth signal (how many reliable carriers does this broker have on this lane?); (4) dynamic rate trending that predicts where the market will be on pickup day, not where it is today. The proprietary differentiator is the broker's own transaction data, which no external rate tool has.

## Target Customer
Broker desk leads and pricing managers at mid-market FTL brokerages handling 500+ loads/week. Approximately 1,500 brokerages at this scale.

## Impact If Solved
Reduces pricing research time from 5-8 minutes per quote to 1-2 minutes of model review. Improves margin by 1-3 percentage points on loads where the broker was under-pricing relative to their actual carrier cost advantage.
