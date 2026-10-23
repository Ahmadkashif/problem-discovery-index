# The Fixed Five-Day Lead Time in the ERP

**Niche:** [[niches/aerospace-parts-suppliers/outside-special-processing/profile|Outside Special Processing & Sub-Tier Expediting]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** The ERP plans every heat treatment as five days because someone typed five years ago, and every schedule built on it is wrong by design.
**Tags:** #descriptive-statistics #exponential-smoothing #data-integration #quick-win #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to give production control a trusted completion date for every lot at an outside heat treater, plater or NDT house, and whoever's predicted dates hold best against processors' real turn times takes the account.

## The Problem
Outside operations carry a fixed lead time in the routing. Real turn times vary from two days to three weeks with the processor, the process and the season. Planners know the number is wrong and pad by feel, so the plan and the expediter's list disagree every day.

## Why It's Still Broken
Updating lead times means pulling shipment and receipt dates for hundreds of routings, and nobody owns the job.

## What a Fix Looks Like
A monthly script that computes actual turn times per processor and process from shipment and receipt records, updates routing lead times with a smoothed median and a stated percentile, and reports where the gap was largest.

## Who Feels the Pain
Planners, expediters and the customers who receive dates built on old numbers.

## Impact If Fixed
Realistic lead times could cut schedule misses on outside-processed parts by ~20–30% within a quarter (estimate) for a few days of analyst time a month.
