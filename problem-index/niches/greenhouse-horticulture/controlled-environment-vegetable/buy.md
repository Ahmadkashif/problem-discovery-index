# Fertigation Controller with Crop-Response Feedback Loop

**Niche:** [[niches/greenhouse-horticulture/controlled-environment-vegetable/profile|Controlled-Environment Vegetable Production]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fertigation controllers (Priva Nutri-line, Ridder HortiMaX) deliver precise nutrient recipes to the plant but operate open-loop — they do not adjust recipes based on how the plant actually responds, requiring the grower to manually interpret drain EC, substrate moisture, and plant symptoms.
**Tags:** #lstm #time-series-forecasting #signal-processing #data-integration #automation

## The Problem
A greenhouse vegetable crop receives 4-8 irrigation events per day, each delivering a precise nutrient solution (nitrogen, potassium, phosphorus, calcium, magnesium, micronutrients at specified concentrations and EC). The fertigation controller executes the recipe flawlessly. But the optimal recipe changes as the plant grows (more potassium needed during fruiting), as seasons shift (higher EC in summer to control vegetative growth), and as substrate conditions evolve (salt accumulation requiring leaching events). The grower adjusts recipes weekly based on drain analysis (EC and nutrient ratios in the water draining from pots), substrate sensor readings, and plant visual assessment. This adjustment process is the core of the grower's irrigation expertise — and it is entirely manual.

## What Already Exists
Priva Nutri-line, Ridder HortiMaX, and Dosatron fertigation systems deliver nutrient solutions with precision (EC +/- 0.1 mS/cm, pH +/- 0.1). Grodan GroSens and Meter TEROS substrate sensors measure moisture, EC, and temperature in the root zone. These systems collect the data needed for a feedback loop but do not close it — the grower is the controller, reviewing sensor data and drain analysis to decide recipe adjustments.

## The Customization Gap
A closed-loop fertigation system needs: (1) continuous substrate sensor monitoring integrated with drain analysis data, (2) a crop-specific model of optimal root zone conditions at each growth stage (vegetative establishment, first truss set, peak production, end-of-season drain-down), (3) automatic recipe adjustments within grower-defined bounds (e.g., EC can vary +/- 0.5 mS/cm from base recipe without grower approval), and (4) a learning component that refines the crop-stage model based on this facility's specific substrate, water quality, and cultivar response. The system must operate within the grower's risk tolerance — conservative adjustments with clear explanation of why the change is recommended.

## Target Customer
Head growers and irrigation managers at CEA vegetable facilities with computerized fertigation systems. Approximately 800-1,200 US facilities with the prerequisite infrastructure.

## Impact If Solved
Recipe optimization reduces nutrient waste by 10-15% ($5-$15K/year in fertilizer savings on a 10-acre facility). More precise root zone management reduces water-related crop stress events by 30-50%, worth 3-5% in yield improvement. Grower time on irrigation management reduced from 5-8 hours/week to 1-2 hours of review.
