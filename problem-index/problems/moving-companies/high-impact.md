# Move Estimation Accuracy from Walkthrough Intelligence

**Industry:** [[moving-companies|Moving Companies]]
**Type:** High Impact
**One-liner:** Every move gets a quote within 5% of actual cost before the truck leaves the warehouse, eliminating profit-destroying underestimates and customer-losing overestimates.
**Tags:** #gradient-boosting #cnns #object-detection #feature-engineering #cross-validation #evaluation-metrics #transfer-learning #backpropagation #gradient-descent #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced estimator walks through a 3-bedroom house and, within 15 minutes, produces a quote covering cubic footage, crew size, truck allocation, and total hours — accurate to within 10% — using pattern recognition they cannot fully articulate. They notice the solid oak dresser that will need four people, the narrow L-shaped staircase that adds 45 minutes, the garage full of awkwardly shaped items that won't stack. New estimators take 2-3 years to develop this intuition, and during that ramp-up period their estimates miss by 20-40%, directly eroding margins on binding quotes or triggering disputes on non-binding ones. The industry loses an estimated 8-12% of gross revenue annually to estimation error.

## Why It's Unsolved
The core data collection challenge is that you must capture the expert estimator performing the walkthrough — their gaze patterns, the items they linger on, the mental adjustments they make for access difficulty, fragility, and disassembly requirements. No structured dataset of "walkthrough video + actual move outcome" exists at scale. Labeling is equally hard: two veteran estimators looking at the same room may agree on the total but disagree on why — one weights staircase difficulty higher, another focuses on item density. Virtual survey tools like Yembo capture video but reduce it to a flat inventory list, discarding the spatial and contextual reasoning that makes expert estimates accurate. Deployment requires the model to be faster and more consistent than the expert to justify adoption; estimators will reject a tool that second-guesses them unless it demonstrably catches what they miss.

## What a Solution Looks Like
A mobile app captures a walkthrough video of the home. A computer vision pipeline identifies and classifies items (furniture type, approximate weight/volume, fragility indicators), maps the spatial layout (room dimensions, staircase geometry, doorway clearances, elevator access), and flags complicating factors (tight turns, long carries, items requiring disassembly). A gradient-boosted regression model takes these extracted features alongside structured inputs (origin floor, destination floor, drive distance, season, day of week) and outputs a predicted cubic footage, crew size, truck count, and labor hours with confidence intervals. The estimator reviews and adjusts the output rather than building the estimate from scratch.

## Impact If Solved
Estimation accuracy improves from +/-15-20% (industry average including junior estimators) to +/-5%, recovering 5-8% of gross margin on mispriced jobs. New estimators reach effective accuracy in weeks instead of years, dramatically reducing the hiring bottleneck that constrains growth for every independent mover.
