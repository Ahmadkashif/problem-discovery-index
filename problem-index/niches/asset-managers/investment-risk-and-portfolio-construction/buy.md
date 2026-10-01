# Forecast Verification From Meteorology

**Niche:** [[niches/asset-managers/investment-risk-and-portfolio-construction/profile|Investment Risk & Portfolio Construction]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Weather services verify probabilistic forecasts routinely and publish their skill; investment risk forecasts are back-tested occasionally and quietly.
**Tags:** #evaluation-metrics #probability-distributions #confidence-intervals #hypothesis-testing #monte-carlo-methods #compliance
**Contested on:** Every serious competitor in this niche is fighting to make the ex-ante risk forecast something a portfolio manager believes — explaining why realised tracking error and drawdowns differed from the model — and whoever does that becomes the risk system PMs actually consult before trading.

## The Problem
Value-at-risk and tracking error are probabilistic forecasts. Banks back-test VaR because regulators require it; asset managers mostly do not systematically verify the calibration of their tracking error and drawdown forecasts.

## What Already Exists
Forecast verification is a mature discipline in meteorology: calibration diagrams, proper scoring rules, skill relative to a naive baseline, and routine publication of verification statistics. Bank market-risk back-testing frameworks exist alongside.

## The Customization Gap
The adaptation needs: (1) relative-risk forecasts against a benchmark, which bank VaR frameworks do not cover; (2) few independent observations per portfolio, so verification must pool across portfolios and be honest about uncertainty; (3) overlapping horizons and serial correlation in returns; (4) a naive baseline that is meaningful to PMs, such as trailing realised volatility; and (5) reporting that a board or a fund's derivatives risk manager under Rule 18f-4 can read.

## Target Customer
Investment risk teams, fund boards and derivatives risk managers.

## Impact If Solved
The firm knows whether its risk forecasts are calibrated, and can show it.
