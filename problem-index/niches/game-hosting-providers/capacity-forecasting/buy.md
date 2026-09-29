# Demand Planning From Utilities and Retail

**Niche:** [[niches/game-hosting-providers/capacity-forecasting/profile|Capacity Forecasting & Allocation]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Utilities forecast peak load regionally with asymmetric reserve margins as a regulated discipline, and game capacity runs on an estimate.
**Tags:** #time-series-forecasting #confidence-intervals #optimization-fundamentals #gradient-boosting #evaluation-metrics #revenue-impact #causal-inference #exponential-smoothing
**Contested on:** Every serious competitor in this niche is fighting to commit capacity in specific regions hours before a demand curve that can multiply within an hour, where being wrong costs either a large bill or the most public failure a multiplayer game can have — and whoever forecasts it takes the account.

## The Problem
Electricity system operators face a structurally identical problem and have solved it to a regulated standard: forecast peak load per region hours to days ahead, hold reserve margins sized against an explicitly asymmetric cost of shortfall, incorporate weather and event signals, and commit capacity in advance because the response time of generation is slower than the demand change. Retail does the same with promotional demand. Game hosting has the same shape, faster dynamics and none of the discipline.

## What Already Exists
Regional peak load forecasting; reserve margin sizing under asymmetric cost; event and weather signal incorporation; capacity commitment scheduling; and forecast accuracy tracking as a managed metric.

## The Customization Gap
The adaptation is to demand driven by cultural events rather than by weather. It requires: (1) demand signals that are social — a streamer's schedule, a content release, a free weekend — rather than meteorological, so the feature set is entirely different and must be assembled from outside the business, which is the substantive difference; (2) spikes measured in minutes rather than hours, compressing the whole commitment cycle; (3) a new title with no historical load curve at all, where utilities always have decades of history; (4) capacity that can be acquired in seconds but not fast enough, giving a middle ground utilities do not have; and (5) a shortfall cost that is reputational and immediate rather than regulated and financial.

## Target Customer
Game hosting providers, studios, cloud capacity teams, and demand forecasting vendors.

## Impact If Solved
Utilities forecast regional peaks with asymmetric reserve margins to a regulated standard. Demand driven by streamer schedules rather than weather, on a title with no load history, is what has to be built new.
