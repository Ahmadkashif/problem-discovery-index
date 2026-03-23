# Photo-Based Post-Construction Scope Estimator

**Niche:** [[niches/cleaning-companies/post-construction/profile|Post-Construction Cleanup]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool lets a cleaning operator photograph a construction site and receive an automated labor estimate, supply list, and quote.
**Tags:** #cnn #object-detection #computer-vision #automation

## The Problem
Post-construction cleaning estimates are generated during site walkthroughs where the estimator mentally catalogs debris types, surface conditions, and square footage, then builds a quote from memory and experience. This process takes 1-3 hours per site, is inconsistent across estimators, and often misses hidden work (HVAC duct contamination, paint overspray on high windows). Under-estimating means losing money; over-estimating means losing the bid.

## Why Nobody Has Built This
The visual assessment requires identifying construction-specific debris types (drywall dust vs. concrete dust vs. sawdust), surface conditions (sealed vs. unsealed floors, painted vs. unpainted trim), and spatial reasoning (ceiling height, window count). No labeled dataset of post-construction site conditions exists. The output isn't a simple classification — it's a multi-variable estimate combining debris type, surface area, and labor intensity.

## What to Build
A mobile app where the estimator walks through the site taking photos and short videos. Computer vision identifies debris types, surface conditions, and room dimensions. The system generates a phase-by-phase cleaning plan (rough clean, detail clean, final touch) with labor hours, supply needs, and a quote range. Each completed job's actual hours feed back to calibrate the model.

## Target Customer
Post-construction cleaning operators bidding on 5+ projects per month who currently spend 10-15 hours per week on site walkthroughs and manual estimating.

## Impact If Built
Cuts estimate preparation time by 60-70% and improves quote accuracy by 15-25%, reducing both lost bids and money-losing jobs.
