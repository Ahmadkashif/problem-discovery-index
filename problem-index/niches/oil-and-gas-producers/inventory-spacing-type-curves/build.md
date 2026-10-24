# Spacing-Aware Type Curves With a Track Record

**Niche:** [[niches/oil-and-gas-producers/inventory-spacing-type-curves/profile|Inventory, Spacing & Type-Curve Planning]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Type curves for infill locations are averages of chosen analogs with a manual spacing haircut, and no operator keeps a running score of how its curves performed.
**Tags:** #gradient-boosting #gaussian-processes #bayesian-inference #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rank an operator's undrilled locations and set their spacing so the wells drilled land on the forecasts that funded them, and whoever's location forecasts come closest to realised 24-month production takes the account.

## The Problem
An infill location's value depends on its neighbours: how far away they are, whether they are in the same bench, and how long they have been draining the rock. Engineers handle this by choosing analogs and cutting the average curve by a percentage they judge from experience. The resulting type curve funds the well, and 24 months later the operator knows whether it was right, but the analog set and haircut were never saved, so the error cannot be traced to its cause.

## Why Nobody Has Built This
Data vendors sell type curves to everyone and avoid publishing their own error, which would hand customers a negotiating tool. Operators build models internally, but asset teams are reorganised by each merger and the work restarts. The label is noisy, mixing geology, completion changes and downtime, which discourages anyone from grading forecasts publicly.

## What to Build
A model that predicts a location's normalised 12- and 24-month production from geology, completion design and the full geometry and timing of its neighbours, with calibrated P10–P90 bands, trained on the public well panel plus the operator's own data. Around it, a ledger that records each approved location's analogs, haircut and reason, and a quarterly calibration report comparing the operator's type curves, the model and realised production at matching months. Parent-well losses after each child completion are tracked as a second label.

## Target Customer
VPs of development and reservoir engineering at operators running two or more rigs, and A&D teams pricing inventory.

## Impact If Built
Removing a systematic 10% optimism from type curves on a 200-well annual programme re-ranks enough locations to move ~$100M+ of capital (estimate). It also gives the operator a calibration record it can show its board, its lenders and a buyer.
