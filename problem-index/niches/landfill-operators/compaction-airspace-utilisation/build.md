# Density by Lift and Shift

**Niche:** [[niches/landfill-operators/compaction-airspace-utilisation/profile|Compaction & Airspace Utilisation]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Landfills measure density for the whole site a few times a year; nobody measures it where it is decided — on each lift, by each operator, on each shift.
**Tags:** #semantic-segmentation #bayesian-linear-regression #gaussian-processes #feature-engineering #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to pack more waste into each cubic yard of permitted airspace, and whoever achieves the highest measured in-place density between airspace surveys takes the account.

## The Problem
Managers know some operators and some practices compact better, but the only density number is site-wide and weeks old, so no lever can be tested.

## Why Nobody Has Built This
The data sits in three places — compactor GNSS, scale tickets and drone surveys — owned by operations, finance and engineering, and allocating volume to periods and areas needs modelling, not a dashboard. Equipment makers sell machines and survey firms sell flights.

## What to Build
A fused model: compactor tracks give pass counts and elevation change per grid cell; scale tickets give tons tipped per face and hour; drone surveys every week or two segment waste from cover and anchor the volume. A hierarchical model estimates density per area and shift with uncertainty and attributes it to lift thickness, passes, waste mix and weather. Operators see their numbers in the cab; managers see which practices move density.

## Target Customer
Landfill managers and engineering directors at sites taking more than ~500 tons a day.

## Impact If Built
Lifting average density by ~5% (estimate) at a site with 15 years of remaining capacity adds ~9 months of life, worth ~$12M at 400,000 tons a year and ~$40 net per ton (estimate).
