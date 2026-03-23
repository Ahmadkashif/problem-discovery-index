# Hail Storm Job Tracking Across Hundreds of Vehicles

**Niche:** [[niches/auto-body-shops/paintless-dent-repair/profile|Paintless Dent Repair Operators]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Fix (Pain Point)
**One-liner:** After a major hail storm, a PDR team processes 200-500 vehicles at a dealership lot over 4-8 weeks with no system to track which vehicles are assessed, repaired, invoiced, and paid.
**Tags:** #workflow-orchestration #automation #data-integration #worker-facing

## The Problem
Hail storms are the highest-revenue events for PDR operators — a single storm can generate $500K-$2M in work across multiple dealership lots. A PDR team sets up at a dealership and processes 20-40 vehicles per day for weeks. Each vehicle needs: initial assessment (dent count and pricing), insurance authorization, repair, quality check, and invoicing. With 200+ vehicles in various stages, tracked on paper clipboards and spreadsheet printouts, vehicles get missed, double-assessed, repaired without authorization, or invoiced incorrectly. A single lost vehicle in the tracking system means $500-$2,000 in unrecovered revenue.

## Why It's Still Broken
Hail work is episodic — a PDR operator might do 3-4 hail events per year, each lasting 4-8 weeks. No one invests in building a tracking system for something that happens quarterly. During the event, the pace is too fast to set up new software — teams resort to whatever is fastest (paper, spreadsheets, texts). Between events, the operator forgets about the tracking problem until the next storm hits.

## What a Fix Looks Like
A lot-management tool designed specifically for hail PDR work: the team scans VINs (or enters plate numbers) as vehicles are assessed, assigns a status (assessed/authorized/in-progress/QC/complete/invoiced/paid), and moves vehicles through the pipeline with tap-based status updates. A map view shows vehicle location on the lot. Daily reports show productivity per technician and revenue per vehicle. At the end of the event, the system generates consolidated invoicing for the dealership or insurer.

## Who Feels the Pain
PDR team leads managing 5-15 technicians across 200-500 vehicles on a dealership lot, who currently track everything on paper and lose 3-5% of revenue to tracking errors.

## Impact If Fixed
Recovers 3-5% of hail event revenue lost to tracking errors ($15K-$100K per major hail event). Reduces daily lot-management overhead from 2-3 hours to 30 minutes. Enables accurate technician productivity tracking for fair compensation on team jobs.
