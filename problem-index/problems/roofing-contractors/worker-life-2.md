# Storm Event Lead Prioritization and Coverage Area Routing

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Type:** Worker Life Changing
**One-liner:** Roofing sales reps who canvas neighborhoods after a hail event — knocking doors without knowing which streets had hail damage severe enough to warrant a claim, or which neighborhoods have homes aged enough to be replacement candidates — get a ranked canvas route generated from weather hail data, aerial imagery condition scoring, and property age data before they leave the office.
**Tags:** #gradient-boosting #ranking #tabular-ml #automation #worker-facing

## The Problem

Door-to-door canvasing after hail storms is the primary lead generation method for insurance restoration roofing firms. Sales reps drive through affected neighborhoods targeting homes that show visible damage from the street. The problem: not all neighborhoods in a hail event receive the same hail size; homes with newer roofs installed after the last major event are not claimable; and canvasing time is limited — a rep can knock 30-50 doors in a half-day canvas. Without routing intelligence, reps canvas randomly within the general storm area, wasting time on streets with sub-threshold hail or recently replaced roofs.

## Why It Matters to the Worker

Sales reps' income is commission-based. A better canvas route directly increases their income by putting them in front of higher-probability claim candidates. Reps who operate in firms with no data-driven routing spend 40-50% of their canvas time on low-probability targets.

## What a Solution Looks Like

A pre-canvas routing tool that ingests: (1) storm path and hail size data by zip code (NOAA storm data + commercial hail verification services like CoreLogic or Verisk); (2) aerial imagery condition scores for the affected area (EagleView, Nearmap property condition data); (3) property age data from county assessor records (homes with roofs > 12 years old are higher claim probability). Output: a ranked map of streets within the storm footprint, sorted by composite claim probability score, with a suggested canvas route for the day's team. The rep opens the app, sees their assigned zone ranked by priority, and knocks in order.

## Impact If Solved

Increases close-per-canvas-hour rate. A rep knocking 40 doors in a high-probability zone versus 40 doors in a mixed zone sees 20-30% more signed contracts per canvas day. For a firm running 10 reps during a storm surge, data-driven routing adds meaningful revenue per storm event.
