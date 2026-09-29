# Nobody Measures Classification Accuracy

**Niche:** [[niches/procurement-spend-platforms/spend-classification-supplier-master/profile|Spend Classification & Supplier Master]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every spend report in every procurement organisation is built on a classification whose accuracy has never been measured, so nobody can say how much of their own category analysis is right.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #cross-validation #automation #quick-win #compliance
**Contested on:** Every serious competitor in spend analytics is fighting to classify at the line item rather than the supplier and to resolve the supplier master into real entities — and whoever gets those two layers right takes every analysis built on them.

## The Problem
A chief procurement officer presents category spend, savings achieved and consolidation opportunities to a finance committee. Every figure derives from a classification produced by a rules engine and a supplier master maintained by an analyst. Asked how accurate the classification is, nobody knows — not the procurement team, not the platform vendor, not the specialist who supplied the classification service. A sampled audit would settle it in a day and has never been performed, which means an entire function's reporting rests on an assumption nobody has tested.

## Why It's Still Broken
Measurement requires a ground truth, which means someone classifying a sample by hand, which is a day of work nobody has scheduled. The classification vendors have no incentive to publish accuracy in a market where nobody asks, and the same first-mover problem applies as in freight visibility and activity capture. And the finding would be uncomfortable: an accuracy figure below expectation calls into question several years of reported savings, which is the kind of result organisations discover reluctantly.

## What a Fix Looks Like
Sample and measure, then report it alongside the numbers. A stratified sample of transactions — weighted toward high-value lines and toward the categories that drive decisions — classified independently by a category expert, gives an accuracy figure with a confidence interval in a day. Report it per category, since accuracy varies enormously and the categories where it is worst are frequently the ones with the most tail spend and the most consolidation opportunity. Measure supplier resolution the same way: what proportion of supplier records are correctly resolved, and what does correcting them do to measured concentration. Then attach the accuracy to the reporting — a category spend figure presented with a stated classification accuracy is a far more honest artefact than one presented as fact, and it tells the reader how much weight to put on it. Repeat quarterly, since classification quality drifts as new suppliers and items arrive. And use the samples as training data, which makes the measurement exercise also the improvement exercise.

## Who Feels the Pain
Category managers negotiating from figures of unknown quality; finance committees receiving savings claims built on them; and analysts who suspect the classification is poor and have no way to demonstrate it.

## Impact If Fixed
A day of sampling produces the accuracy figure an entire function's reporting has been missing, and the per-category breakdown directs improvement effort to where the decisions are worst informed. Attaching accuracy to reported numbers is the honest change and is what makes the improvement case fundable.
