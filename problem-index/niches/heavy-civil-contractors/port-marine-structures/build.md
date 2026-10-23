# Pile Records That Predict Refusal

**Niche:** [[niches/heavy-civil-contractors/port-marine-structures/profile|Port, Wharf & Marine Structures]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every pile driven leaves a blow-count record and a dynamic test; marine contractors don't use those records to predict refusal, splices and production on the next pile, or the next job.
**Tags:** #gradient-boosting #gaussian-processes #time-series-forecasting #feature-engineering #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to drive, cap and deck wharves, piers and bulkheads while the port keeps ships working at the neighbouring berths, and whoever hands back each berth with the fewest days of closure takes the account.

## The Problem
A pile that refuses early or runs long breaks the day's sequence, the berth schedule and the budget. Experienced pile foremen read the blow counts and sense a refusal coming; the records sit in binders.

## Why Nobody Has Built This
Pile logs and PDA tests belong to the geotechnical engineer of record and the contractor's field staff, in different formats. Boring logs are PDFs, and no vendor serves the marine pile niche.

## What to Build
A model trained on pile logs, dynamic test results and nearby borings that predicts penetration, final set and splice need for each remaining pile. It updates spatially as piles go in, and it feeds a daily production forecast to the berth schedule. A demo can be built on published pile-load-test datasets.

## Target Customer
Marine superintendents and estimators at contractors driving ~1,000+ piles a year (estimate).

## Impact If Built
If unplanned splices and refusals drop by a quarter (estimate), a 300-pile wharf (illustrative) saves several crane-barge days and keeps its berth handover dates.
