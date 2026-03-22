# Estimating Tools That Account for Prep Complexity

**Niche:** [[niches/painting-contractors/residential-exterior/profile|Residential Exterior Painting]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PaintScout and other estimating tools calculate material and labor from square footage, but exterior painting profitability depends on prep intensity — which no estimating tool models as a variable, forcing experienced painters to mentally adjust bids based on surface condition while junior estimators bid blind.
**Tags:** #gradient-boosting #data-integration #revenue-impact

## The Problem
Exterior painting estimating tools treat prep as a flat percentage of labor or a fixed line item. PaintScout lets the user select "light prep," "medium prep," or "heavy prep" as a multiplier, but the definition of these categories is left to the estimator's judgment. The gap between light prep (pressure wash and spot-prime) and heavy prep (full scrape, sand, caulk removal and replacement, wood repair, chemical strip, and multi-coat primer) can be a 3-4x labor difference on the same square footage. No tool captures the variables that drive prep intensity: paint age, number of existing paint layers, substrate type, sun exposure direction, proximity to moisture sources, presence of lead paint (pre-1978 homes requiring RRP compliance), and previous paint quality.

## What Already Exists
PaintScout provides square footage-based estimating with configurable labor rates and material markups. Hover generates exterior measurements from smartphone photos but outputs only dimensions, not surface conditions. EagleView provides aerial measurements for roofing contractors but doesn't assess siding condition. ProPainter and Estimate Rocket offer painting-specific estimating but also treat prep as a manual adjustment.

## The Customization Gap
A prep complexity scoring model needs to sit between measurement (square footage) and pricing (labor rate). The model inputs: substrate type per elevation (selected from dropdown or auto-detected from photo), estimated paint age, compass orientation (south/west = more UV damage), climate zone (moisture, salt, UV intensity), home age (pre-1978 triggers lead paint protocol), and visual condition indicators (the estimator answers 5-6 structured questions per elevation about peeling, chalking, caulk condition, and wood integrity). A gradient-boosted regression model trained on historical exterior projects maps these inputs to actual prep labor hours, replacing the subjective "light/medium/heavy" toggle with a data-driven prediction. The model calibrates to each contractor's labor efficiency using their completed project data, so a faster crew gets tighter estimates while a detail-oriented crew gets appropriately padded ones.

## Target Customer
Exterior painting companies and full-service residential painters already using PaintScout or similar estimating tools, frustrated by the prep estimation gap that causes either margin erosion (underestimate prep) or lost bids (overestimate prep). Companies doing 50+ exterior jobs per year with enough historical data to calibrate the model.

## Impact If Solved
Reduces exterior bid variance from 25-40% to 10-15% by replacing subjective prep assessment with structured, data-driven prediction. Eliminates the $2,000-4,000 average overrun on heavy-prep exteriors that currently erodes margins. Gives junior estimators the prep assessment accuracy that currently takes 5+ years of exterior experience to develop.
