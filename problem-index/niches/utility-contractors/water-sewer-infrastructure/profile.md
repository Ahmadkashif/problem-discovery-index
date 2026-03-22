# Water & Sewer Infrastructure

**Parent Industry:** [[industries/utility-contractors|Utility Contractors]]
**Category:** Low Digitized

## Profile
**Market Size:** $30-35B
**Share of Parent Industry:** ~22%
**Digital Adoption:** Low-Medium — CityWorks and ESRI handle asset management for municipal water/sewer. SCADA monitors treatment plants and pump stations. But pipe condition assessment, break prediction, and as-built documentation for buried infrastructure are manual and error-prone.
**Target Buyer:** Water/sewer utility contractor, municipal water department director, or civil engineering project manager
**Automation Potential:** High — pipe condition prediction is a tabular ML problem, and as-built documentation for buried utilities is a data integrity challenge with well-defined solutions

## What Makes This a Distinct Niche
Water and sewer infrastructure contracting involves installing, maintaining, and replacing underground pipe networks that are invisible once buried. The buried nature of the assets creates a unique documentation challenge: the contractor installs a water main 6 feet underground, records its location on an as-built drawing, and that drawing becomes the only record of the pipe's exact location, depth, and material for the next 50-100 years. If the as-built is inaccurate (and studies show 30-40% of as-built utility locations are off by more than 2 feet), every future excavation in that area risks striking the pipe. The US loses an estimated 6 trillion gallons of treated water annually through leaking pipes — 14-18% of total treated water production. Sewer overflows from aging collection systems cause environmental contamination and EPA consent decree enforcement. The infrastructure is old: the average US water main is 45+ years old, with some systems including pipe from the 1800s.

## Current Tools & Gaps
CityWorks and Cartegraph handle work order management for municipal water/sewer departments. ESRI ArcGIS maps pipe networks. CCTV inspection of sewer pipes produces video records graded by NASSCO's PACP (Pipeline Assessment Certification Program) standards. No tool predicts which pipe segments will fail, integrating pipe material, age, soil conditions, break history, and CCTV inspection grades into a failure probability model.

## Problems
- [[niches/utility-contractors/water-sewer-infrastructure/build|🔨 Build: Pipe Condition Predictor]]
- [[niches/utility-contractors/water-sewer-infrastructure/buy|🛒 Buy: CityWorks/ESRI with Failure Prediction]]
- [[niches/utility-contractors/water-sewer-infrastructure/fix|🔧 Fix: As-Built Documentation Accuracy]]
