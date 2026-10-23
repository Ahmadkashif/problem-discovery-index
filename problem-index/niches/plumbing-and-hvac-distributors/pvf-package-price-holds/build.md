# Margin-at-Release Simulation Before the Hold Is Promised

**Niche:** [[niches/plumbing-and-hvac-distributors/pvf-package-price-holds/profile|PVF Package Pricing & Price Holds]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A PVF manager promising a six-month hold is selling an option on copper and PVC without pricing it.
**Tags:** #monte-carlo-methods #exponential-smoothing #change-point-detection #linear-regression #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to hold a firm price on a mechanical contractor's pipe, valve and fitting package across a release schedule that runs for months while copper and PVC move, and whoever quotes the lowest price held firm through the job's last release takes the account.

## The Problem
A contractor wants the copper, cast-iron and PVC package for a school held through next summer. The PVF manager decides the price and hold by feel, knowing that COMEX copper set a record settlement of ~$6.9/lb in September 2026 (search summary) and that PVC sheets can move by double digits in a quarter (estimate). When the market moves the wrong way, the late releases ship below cost.

## Why Nobody Has Built This
Pricing tools optimise today's price for today's order; nobody models a release schedule as a series of future purchases against two commodity references and manufacturers' price-sheet habits.

## What to Build
A simulator that takes a package's lines, the expected release schedule and the hold terms, models copper from COMEX volatility and PVC from the house's own price-sheet history and resin assessments, and returns the distribution of margin at each release, the hold length that keeps margin above floor at a chosen confidence, and the price premium a longer hold should carry. A demo needs public copper data and a synthetic release schedule.

## Target Customer
PVF and pricing managers at commercial plumbing and mechanical distributors.

## Impact If Built
If ~5–15% of held PVF lines now ship below margin floor in a rising market (estimate), pricing the hold before promising it recovers ~1–2 margin points on the package, or lets the house offer the longest hold it can afford and win on terms.
