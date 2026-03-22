# Pipe Condition Predictor

**Niche:** [[niches/utility-contractors/water-sewer-infrastructure/profile|Water & Sewer Infrastructure]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A predictive model that estimates failure probability for every water main and sewer main segment based on material, age, diameter, soil type, break history, water pressure, proximity to trees, and CCTV inspection grades — enabling municipal utilities to prioritize replacement based on actual condition rather than age-based scheduling.
**Tags:** #gradient-boosting #survival-analysis #data-integration #compliance #revenue-impact #logistic-regression

## The Problem
Municipal water and sewer utilities replace pipe reactively (after it breaks) or on age-based schedules (replace all cast iron over 80 years old). Neither approach is optimal: reactive replacement is 3-5x more expensive than planned replacement (emergency excavation, traffic disruption, water service interruption, property damage), while age-based replacement wastes capital on pipe that could last decades longer. A 100-year-old ductile iron main in stable, non-corrosive soil may have 50+ years of remaining life, while a 40-year-old asbestos cement main in acidic soil may be actively deteriorating. Water main breaks cost US utilities $3B+ annually in emergency repair and associated damage. Sewer failures cost $1B+ in EPA consent decree compliance, environmental remediation, and sanitary sewer overflow penalties.

## Why Nobody Has Built This
Water and sewer utilities have less data maturity than gas or electric utilities. Many operate on paper work orders with no digitized break history. Pipe material records are often incomplete — segments installed before 1940 may have no material documentation. GIS data quality varies: some utilities have GPS-grade mapped networks, others have hand-digitized maps from paper drawings with 10-20 foot positional accuracy. Building a pipe failure prediction model requires joining GIS data, break history, CCTV inspection data, soil surveys, and water quality data — databases that are typically maintained by different departments with different systems. The market is highly fragmented: 50,000+ water and sewer systems in the US, most serving fewer than 10,000 connections.

## What to Build
A failure prediction platform that: (1) ingests available data — GIS (pipe attributes), work order history (break locations, repair types, dates), CCTV inspection grades (PACP scores for sewer), water quality data (chlorine residual, pressure), and external data (USDA soil, tree canopy, traffic loading); (2) handles missing data gracefully — many utilities lack complete material records or break history, so the model must produce useful predictions from partial feature sets; (3) predicts annual failure probability per pipe segment using survival analysis or gradient-boosted classification, calibrated to the utility's historical failure rate; (4) outputs a risk-ranked replacement priority list with cost-benefit analysis — "Segment 456: replacement cost $180K, annual failure cost probability $45K, recommended replacement priority: High."

## Target Customer
Municipal water and sewer utilities with 20,000+ service connections and $5M+ annual capital improvement budgets. Consulting engineering firms (Black & Veatch, AECOM, Arcadis) that advise utilities on capital planning.

## Impact If Built
Shifts 20-40% of pipe replacement spending from age-based to risk-based prioritization, improving risk reduction per capital dollar by 25-40%. Reduces water main break frequency by 15-25% through proactive replacement of highest-risk segments. Provides data-driven capital planning justification for rate case filings, helping utilities secure rate increases for infrastructure investment.
