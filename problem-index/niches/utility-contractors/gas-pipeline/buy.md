# GIS Platform with Integrity Prediction

**Niche:** [[niches/utility-contractors/gas-pipeline/profile|Gas Pipeline]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ESRI ArcGIS maps every gas pipeline segment with material, age, and diameter — but doesn't predict which segments will fail, forcing utilities to maintain separate Excel-based risk models that are disconnected from the spatial data and updated annually rather than continuously.
**Tags:** #gradient-boosting #data-integration #compliance #automation #logistic-regression

## The Problem
Gas utilities maintain comprehensive GIS databases of their pipeline network — every main, service line, valve, and regulator is mapped with installation date, material, diameter, and operating pressure. Separately, they maintain integrity management databases that track leak history, cathodic protection readings, and inline inspection results. These databases are disconnected: the GIS shows where the pipe is and what it's made of; the integrity database shows how it's performing and where it's failing. Risk assessment is done offline in Excel or specialty software (DNV GL MAOP Suite, Piramid), producing risk scores that are mapped back to GIS segments annually. The annual refresh means the risk model doesn't incorporate recent leak events, cathodic protection changes, or soil condition updates until the next model run.

## What Already Exists
ESRI ArcGIS stores and visualizes pipeline spatial data with rich attribute tables. ESRI supports spatial analysis (proximity to trees, soil type overlays, flood zone intersections). ArcGIS has Python and R integration for advanced analytics. What's missing is a continuously updated risk prediction model running within the GIS platform rather than in offline Excel models.

## The Customization Gap
A pipeline integrity prediction module within ArcGIS that: (1) continuously integrates data from the utility's leak database, cathodic protection monitoring, SCADA operating data, and external sources (soil, weather, construction activity); (2) runs a gradient-boosted risk model within ArcGIS, updating risk scores for every pipe segment as new data arrives (not annually); (3) visualizes risk scores on the map with color-coded overlays — red for high-risk segments, yellow for moderate, green for low — enabling spatial analysis of risk patterns; and (4) generates risk-prioritized replacement lists that feed directly into the utility's capital planning process. This brings integrity prediction inside the GIS platform where field planners and engineers already work, rather than requiring a separate analytics workflow.

## Target Customer
Gas utilities already using ESRI ArcGIS for pipeline asset management who maintain separate offline risk models. ESRI seeking to offer utility-specific AI capabilities within the ArcGIS ecosystem.

## Impact If Solved
Eliminates the 2-4 month lag between new data and risk model updates by continuously recalculating risk scores. Reduces the risk assessment labor from 200-500 hours per annual model refresh to continuous automated updates. Puts risk scores in the hands of field planners on the same map they use for daily operations. Enables ESRI to offer a premium pipeline integrity tier at $100K-500K per utility per year.
