# Vegetation and Right-of-Way Encroachment Detection from Aerial Imagery

**Niche:** [[niches/utility-contractors/electric-transmission-distribution/profile|Electric Transmission & Distribution]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A computer vision system that analyzes satellite, drone, or aerial imagery of power line corridors to detect vegetation encroachment, unauthorized structures, and right-of-way violations — replacing the manual line patrol process that is expensive, inconsistent, and produces point-in-time snapshots rather than continuous monitoring.
**Tags:** #object-detection #semantic-segmentation #time-series-forecasting #automation #compliance #revenue-impact #cnns

## The Problem
Utilities spend $10B+ annually on vegetation management — trimming or removing trees that grow too close to power lines. Vegetation contact is the #1 cause of power outages and a leading cause of utility-caused wildfires (the 2018 Camp Fire that destroyed Paradise, California was caused by a PG&E transmission line contacting a tree). Current vegetation assessment: utility crews drive or fly distribution circuits (typically 3-year trim cycles), visually identify trees approaching minimum clearance distances, and schedule trim crews. This manual patrol is expensive ($50-100 per mile), subjective (one patroller flags a tree, another misses it), and produces a static assessment that's immediately outdated as trees continue growing. Between patrols, a fast-growing tree or storm-damaged limb can encroach into the minimum clearance zone undetected. The assessment doesn't predict which trees will grow into the clearance zone before the next patrol, leading to reactive rather than proactive vegetation management.

## Why Nobody Has Built This
Three challenges. First, imagery resolution: detecting a tree branch within 10 feet of a conductor from satellite imagery requires sub-meter resolution, which is available (Planet Labs, Maxar) but expensive at scale across thousands of miles of distribution circuits. Drone imagery provides centimeter resolution but is expensive to collect at scale. Second, 3D assessment: determining clearance between a tree canopy and a conductor requires height estimation from 2D imagery (or LiDAR point clouds), which is technically challenging. Third, growth prediction: estimating when a tree will encroach based on species, growth rate, and current clearance requires botanical knowledge combined with spatial analysis that no existing CV system integrates.

## What to Build
A vegetation intelligence platform with three capabilities. First, encroachment detection: analyze aerial/satellite imagery along utility corridors using CNN-based segmentation to identify vegetation approaching minimum clearance distances, prioritized by proximity, conductor voltage (higher voltage requires greater clearance), and circuit criticality. Second, growth prediction: using historical imagery sequences (annual satellite imagery compared year-over-year), model vegetation growth rates by species and location, predicting when specific trees will reach encroachment thresholds. Third, trim prioritization: rank vegetation management work orders by risk (species, growth rate, current clearance, circuit criticality, wildfire risk zone) rather than fixed-cycle patrol schedules, allocating trim crews to highest-risk sites first.

## Target Customer
Electric utilities with vegetation management budgets exceeding $10M annually (the top 100 US utilities). Vegetation management contractors (Davey Tree, Asplundh) seeking to provide analytics-enhanced services to their utility clients. Utility regulators requiring enhanced vegetation monitoring following wildfire events.

## Impact If Built
Shifts vegetation management from fixed-cycle patrol ($50-100/mile every 3 years) to continuous risk-based monitoring, reducing outage-causing vegetation contacts by 30-50%. Reduces vegetation management costs by 15-25% through targeted trim prioritization rather than full-circuit patrol. Provides regulatory documentation of continuous monitoring compliance, reducing wildfire liability exposure. Worth $1.5-2.5B in annual savings across the US utility industry.
