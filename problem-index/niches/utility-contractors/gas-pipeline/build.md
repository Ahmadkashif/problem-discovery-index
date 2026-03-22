# Pipeline Leak Probability Predictor

**Niche:** [[niches/utility-contractors/gas-pipeline/profile|Gas Pipeline]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A predictive model that estimates the leak probability for every gas distribution pipe segment based on material, age, soil type, cathodic protection status, operating pressure, temperature cycling, proximity to trees (root intrusion), and historical break data — enabling utilities to prioritize replacement based on actual risk rather than age-based rules.
**Tags:** #gradient-boosting #time-series-forecasting #compliance #revenue-impact #bayesian-inference #logistic-regression

## The Problem
US gas utilities spend $10B+ annually replacing aging distribution mains, prioritized primarily by pipe material and age — cast iron first, then bare steel, then protected steel, with age as a tiebreaker within material categories. This age-based approach is crude: a 90-year-old cast iron main in sandy, well-drained soil with proper cathodic protection may have decades of remaining life, while a 40-year-old steel main in acidic, saturated clay soil with failed cathodic protection may be actively corroding and near failure. The consequence of age-based prioritization: utilities replace pipe that would have lasted another 30 years while leaving at-risk pipe in the ground. Given capital budgets of $100M-500M per year for replacement programs, misallocation wastes 15-25% of the annual budget on lower-risk replacements while higher-risk segments remain in service.

## Why Nobody Has Built This
The feature set for leak prediction is available but distributed across multiple databases: GIS (pipe material, diameter, age, location), SCADA (operating pressure, pressure transients), leak records (historical leak locations, causes, repair types), soil surveys (USDA soil type, corrosivity, moisture), cathodic protection records (test point readings, rectifier output), and third-party data (tree canopy maps for root intrusion risk, frost depth maps for thermal stress). Joining these datasets into a per-segment feature matrix requires significant data engineering. The training data (actual leak events) is imbalanced — leaks occur on 0.1-1% of pipe segments per year — requiring careful handling of class imbalance. And the stakes are high: a false negative (predicting low risk on a segment that subsequently fails) has catastrophic consequences, demanding very high recall for the positive class.

## What to Build
A pipe segment risk scoring platform that: (1) ingests data from multiple utility sources — GIS (pipe attributes), SCADA (operating conditions), leak database (historical failures), cathodic protection records (corrosion protection status), and external sources (USDA soil data, FEMA flood maps, tree canopy data); (2) builds a per-segment feature matrix including material, age, diameter, soil corrosivity, cathodic protection effectiveness, operating pressure, historical leak density in the area, proximity to trees, proximity to heavy vehicle crossings, and seasonal temperature range; (3) trains a gradient-boosted classifier predicting annual leak probability per segment, optimized for high recall on the positive class; and (4) produces a risk-ranked replacement priority list that reallocates the utility's capital budget from age-based to risk-based prioritization, quantifying the risk reduction per dollar spent on each candidate replacement segment.

## Target Customer
Gas distribution utilities with $50M+ annual pipe replacement programs (top 50 US gas utilities). Pipeline integrity management consultants. State PUC staff evaluating utility replacement program effectiveness.

## Impact If Built
Improves capital allocation efficiency by 20-35% by replacing the highest-risk segments first rather than the oldest. Reduces leak incidents by 15-25% per dollar of replacement spending through risk-based prioritization. Provides defensible, data-driven replacement prioritization for PHMSA regulatory filings. Worth $50M-200M in risk-adjusted savings annually across the US gas utility industry.
