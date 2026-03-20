# Dynamic Lane Pricing and Margin Optimization

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Type:** High Impact
**One-liner:** Freight brokers who price loads on a lane by gut feel — using last week's rate they saw plus a margin — get a model that prices each load based on current market conditions, carrier capacity in the lane, day-of-week demand patterns, and the shipper's service sensitivity to generate the price that maximizes expected margin without losing the load.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #gradient-descent #bias-variance-tradeoff #entropy-cross-entropy-kl-divergence #revenue-impact

## The Problem

Freight load pricing is a two-sided decision: the shipper price (what to charge the customer) and the carrier cost (what to pay for capacity). The optimal shipper price is the highest rate the shipper will accept before using a competing broker or their own carrier network. The optimal carrier cost is the lowest rate a reliable carrier will accept for this load.

The spread between these two numbers is the broker's margin. In liquid lanes (Chicago-Atlanta dry van, Los Angeles-Dallas reefer), spot rate data from DAT provides a market reference. In thinner lanes or specialized equipment, the market signal is noisier and the broker's judgment determines margin.

An experienced broker prices with implicit knowledge of: how tight capacity is on this lane this week (carrier calls taken vs. declined), the shipper's historical rate sensitivity (do they push back or accept the first quote?), seasonal patterns for this lane, and what competitive brokers are charging. A junior broker often leaves margin on the table by under-pricing to secure the load quickly, or loses loads by over-pricing from rate complacency.

## Why It's High Impact

A 2-3 percentage point improvement in blended margin (from 18% to 20-21%) on a brokerage doing $30M in revenue adds $600,000-$900,000 in gross profit annually. This is achievable through systematic pricing optimization — not rate gouging, but more precisely matching price to market conditions on each transaction.

## What a Solution Looks Like

A TMS-integrated pricing model that: (1) ingests the load details (origin/destination lane, equipment type, weight, pickup date); (2) queries current lane rate data from DAT/Truckstop plus the broker's own recent transaction history; (3) models carrier capacity signal for this lane (how many carriers are posting in this corridor today vs. last week); (4) returns a recommended all-in rate to offer the shipper and a target carrier rate to buy capacity at. The broker reviews the recommendation, adjusts based on relationship-specific knowledge, and presents the quote. Over time the model learns from accepted vs. rejected quotes.

## Implementation Path

DAT rate data API provides the market signal. The broker's own TMS contains historical lane transaction data for training. A gradient boosting regression on lane features + market conditions: 4-6 week modeling project. Any brokerage with 10,000+ annual loads has sufficient training data. McLeod or Mercury Gate TMS integration is the deployment path.
