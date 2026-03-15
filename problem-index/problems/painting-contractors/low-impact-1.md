# Surface Area Measurement and Material Estimation from Photos

**Industry:** [[painting-contractors|Painting Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic area measurement tools exist but don't handle the painting-specific deductions (windows, doors, trim vs. field), substrate-specific spread rate adjustments, and two-coat vs. one-coat calculations that determine accurate material quantities for a residential painting quote.
**Tags:** #computer-vision #regression #multimodal #automation

## The Problem

Painting material estimation requires: measuring wall area (height × width minus door and window openings), adjusting for the specific paint's spread rate on the substrate (smooth drywall vs. textured, masonry vs. wood), accounting for number of coats specified, and adding waste factor for brush work and cut-in. An experienced estimator performs this calculation accurately in 20-30 minutes for a typical interior job. A junior estimator makes errors — over-ordering (higher material cost, disposal liability) or under-ordering (mid-job supply run disrupting the crew).

The measurement task is also a field estimation problem: measuring room dimensions with a tape measure takes time and is often done imprecisely; customers expect quotes quickly and estimators skip thorough measurement.

## What Already Exists

PaintScout has surface area calculation tools. Laser measurement devices (Bosch GLM, Leica Disto) speed up room measurement. No tool estimates surface area from photos — the estimator still measures manually.

## The Customisation Gap

A painting-specific area estimation tool needs: (1) room dimension estimation from photos using depth estimation or ArUco marker-based scaling; (2) automatic deduction for door and window openings detected in the photos; (3) substrate classification (smooth vs. orange peel vs. knockdown texture) to apply the correct spread rate; (4) coat count specification to adjust material quantity. The substrate classification and spread rate adjustment are painting-specific and not in general estimating tools. A monocular depth estimation model (DPT, ZoeDepth) adapted for room measurement would reduce field measurement time significantly.

## Impact If Solved

Reduces site measurement time from 20-30 minutes to 5-8 minutes. Reduces material over-ordering (waste cost and disposal liability). Enables faster quote delivery — same-day quotes close at higher rates than next-day quotes.
