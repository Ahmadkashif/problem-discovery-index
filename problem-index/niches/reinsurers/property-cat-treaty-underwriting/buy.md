# Portfolio Pricing Engines That Record Why

**Niche:** [[niches/reinsurers/property-cat-treaty-underwriting/profile|Property Catastrophe Treaty Underwriting]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reinsurers already run every programme through a pricing and portfolio engine that computes layer loss costs and marginal capital, and that engine stores the answer but not the underwriter's reasons for departing from it.
**Tags:** #monte-carlo-methods #bayesian-inference #evaluation-metrics #feature-engineering #workflow-orchestration #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn a cedent's submission into a quoted own view of risk, with every load against the vendor model explained, before the broker's firm-order deadline, and whoever's loads still look right after the next large event takes the account.

## The Problem
The pricing engine produces modelled loss cost, standard deviation and marginal impact on the portfolio's tail for each layer. The underwriter then quotes a different number, and the engine has no field for why.

## What Already Exists
Vendor financial modules in Verisk Touchstone Re and Moody's RMS, portfolio roll-up platforms such as Analyze Re (recalled), and in-house Python pricing frameworks at the larger reinsurers. They simulate layer losses across event sets and aggregate the portfolio well.

## The Customization Gap
The adaptation needs: (1) a structured adjustment schema (insured-value adequacy, data quality, claims culture and litigation, non-modelled perils, trend, portfolio fit) attached to every quote; (2) prompts that draft each component from the referral memo; (3) a link from each programme to the cedent's later event notifications and bordereaux; (4) a market benchmark from industry loss indices for each event; and (5) a review screen that shows a lead underwriter the loads applied to similar cedents and how they performed.

## Target Customer
Heads of cat pricing at reinsurers already licensing a portfolio engine who want to extend it rather than add another vendor.

## Impact If Solved
The engine already at the centre of the workflow becomes the place where the own view of risk is recorded and tested, at almost no extra cost in underwriter time.
