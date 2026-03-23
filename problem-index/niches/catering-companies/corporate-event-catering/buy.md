# Proposal-Stage Profitability Prediction

**Niche:** [[niches/catering-companies/corporate-event-catering/profile|Corporate Event Catering]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CaterTrax and Better Cater generate proposals with estimated costs, but their cost estimates are static templates — not ML-driven predictions calibrated to actual post-event P&L data.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A corporate catering sales manager quotes 20-40 events per month. Each quote estimates food cost, labor, rentals, and logistics based on templates and experience. The experienced manager adjusts for venue complexity, client history, and seasonal pricing — but these adjustments are tacit. New sales managers quote using templates without adjustments, resulting in 15-25% cost estimation errors that compound across a season into six-figure profit leakage.

## What Already Exists
CaterTrax, Better Cater, and Caterease generate proposals with cost estimates based on per-head templates (e.g., "$35/person for buffet lunch"). These templates can be customized manually but do not learn from actual event outcomes. They do not adjust for venue-specific labor requirements, seasonal ingredient price shifts, or the systematic cost differences between service styles.

## The Customization Gap
The tool must train on historical event data — linking proposal parameters to actual post-event costs — and output a predicted margin with confidence intervals for each new proposal. Key adjustments that templates miss: venue-specific labor multipliers (outdoor events require 20% more service staff), guest-count-to-actual-attendance ratios (corporate events average 8-12% no-show, but it varies by event type), and cross-item dependencies (heavy appetizer menus reduce per-head entree consumption).

## Target Customer
Catering sales managers who generate 20+ proposals per month and currently rely on static per-head cost templates that do not reflect actual event-level profitability.

## Impact If Solved
Reducing cost estimation error from 20% to 5% on a $5M corporate catering operation recovers $300K-$750K in annual margin through accurate pricing.
