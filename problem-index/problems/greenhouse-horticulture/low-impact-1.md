# Crop Scheduling and Space Planning for Multi-Crop Greenhouses

**Industry:** [[greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic project management tools cannot model greenhouse-specific constraints like bench space allocation, light zone requirements, propagation-to-finish transitions, and temperature compartment sharing.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #optimization-fundamentals #combinatorics-and-counting #workflow-orchestration

## The Problem
A multi-crop ornamental greenhouse may run 50-200 different SKUs (cultivars x pot sizes) simultaneously, each with different space requirements at different growth stages — a 4" poinsettia takes 0.5 sq ft in propagation but 1.2 sq ft at finish. Crops must be assigned to specific zones based on temperature and light requirements (high-light warm zone vs. cool-growing shade zone). The scheduling goal is to maximize revenue per square foot per week while meeting shipping dates for pre-booked wholesale orders. Most operations manage this with spreadsheets or whiteboards, and head growers report spending 8-12 hours per week on manual scheduling that still leaves 10-15% of bench space idle between crop turns.

## What Already Exists
Project management tools like Monday.com or Asana have been tried by larger operations, along with greenhouse-specific ERP modules in BloomMaster and Picas. Microsoft Excel remains the dominant tool. None of these understand the biological constraints: a crop cannot be moved mid-cycle without stress, propagation benches have different spacing than finish benches, and crop duration varies by 1-3 weeks depending on actual growing conditions (light accumulation, temperature).

## The Customisation Gap
The scheduling engine needs to model: (1) variable space-over-time curves for each crop type, (2) zone assignment constraints (temperature compartments, supplemental light availability, bench height for hanging baskets vs. floor crops), (3) propagation-to-finish transition rules including hardening-off periods, (4) dynamic crop duration adjustments based on actual growing degree day accumulation rather than fixed calendar dates, and (5) integration with order management to prioritize high-margin or committed orders. A gradient-boosting model trained on historical crop-turn data can predict actual finish dates, which feeds a constraint-based scheduling optimizer.

## Impact If Solved
Reducing dead bench time from 15% to 5% in a 200,000 sq ft greenhouse generating $40/sq ft/year represents ~$800K in recovered annual revenue. Head growers reclaim 8-12 hours per week of scheduling time for higher-value crop management decisions.
