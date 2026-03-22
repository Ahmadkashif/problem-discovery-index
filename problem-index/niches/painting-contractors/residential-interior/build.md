# Room-by-Room Photo Estimating

**Niche:** [[niches/painting-contractors/residential-interior/profile|Residential Interior Painting]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mobile app that calculates paintable square footage from room photos — measuring walls, identifying doors, windows, trim, and closets — eliminating the 15-20 minutes of manual measurement per room that makes accurate estimating the bottleneck of residential interior painting sales.
**Tags:** #object-detection #semantic-segmentation #tacit-knowledge-ml #revenue-impact #automation #cnns

## The Problem
Residential interior painting estimates require room-by-room measurement of every paintable surface. An experienced estimator walks through a 2,500 sq ft home and spends 45-90 minutes measuring walls, counting windows and doors, noting ceiling heights, assessing surface conditions, and calculating total paintable area. This manual process limits estimating capacity to 3-4 estimates per day, creates a bottleneck during peak season (spring and fall), and introduces measurement errors that cause either under-bidding (unprofitable jobs) or over-bidding (lost sales). The experienced estimator also performs a tacit assessment during measurement: they notice that the textured walls will require extra material, that the dark accent wall needs tinted primer, that the crown molding adds 30% to trim time. Junior estimators measure the same rooms but miss these adjustments, producing estimates that are technically correct on square footage but wrong on scope and labor.

## Why Nobody Has Built This
Computer vision for room measurement requires solving multiple problems simultaneously: monocular depth estimation from phone photos (no LiDAR on most phones), semantic segmentation of paintable surfaces vs. non-paintable elements (windows, doors, built-ins, outlets), handling of non-rectangular rooms (alcoves, bay windows, vaulted ceilings), and surface condition classification (smooth drywall vs. textured vs. damaged). LiDAR-equipped iPhones partially solve depth estimation but market penetration is insufficient — most painting contractors use Android or older iPhones. The training data problem is severe: you need thousands of room photos with pixel-level annotations of every surface type and condition, labeled by experienced painting estimators who disagree on difficulty ratings 25-35% of the time. Existing room measurement apps (MagicPlan, RoomScan) measure dimensions but don't calculate paintable surface area or assess surface conditions.

## What to Build
A mobile app where the estimator takes 4-6 photos per room (each wall, ceiling, and any special features) and the system produces a detailed painting scope: total wall square footage (minus windows, doors, and non-paintable surfaces), ceiling square footage, linear feet of trim/baseboard/crown, number of doors, surface condition rating (1-5 scale for prep intensity), and a recommended coat count based on detected surface texture and color-change analysis. The computer vision pipeline uses a CNN for semantic segmentation of room elements, monocular depth estimation for measurements, and a classification head for surface condition. Output feeds directly into pricing calculations using the contractor's per-square-foot rates. For rooms where the model confidence is low (unusual geometry, heavy furniture blocking walls), it flags for manual measurement rather than guessing.

## Target Customer
Interior painting companies doing 150+ estimates per year, with 1-3 dedicated estimators spending 60%+ of their time on site visits. Companies in the $500K-5M revenue range where estimating capacity directly limits growth — they turn away estimate requests during peak season because they can't physically visit enough homes.

## Impact If Built
Reduces per-room estimating time from 15-20 minutes to 3-5 minutes, increasing daily estimate capacity from 3-4 to 6-8 homes. Improves estimate accuracy by standardizing surface condition assessment, reducing the 15-20% bid variance between estimators that causes either lost jobs or lost margin. Worth $100K-300K annually in recovered revenue for a mid-size painting company through higher estimate volume and improved close rates.
