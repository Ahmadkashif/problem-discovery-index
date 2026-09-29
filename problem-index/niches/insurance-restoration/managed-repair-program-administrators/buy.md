# Contractor Scoring Adapted to Jobs That Are Not Comparable

**Niche:** [[niches/insurance-restoration/managed-repair-program-administrators/profile|Managed Repair Programme Administrators]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The scorecard that decides 60-80% of a restoration company's revenue ranks them on metrics that mostly measure which jobs they were assigned.
**Tags:** #causal-inference #tabular-ml #evaluation-metrics #hypothesis-testing #data-integration

## The Problem
Network contractors are scored on cycle time, estimate accuracy, customer satisfaction, reopen rate, and documentation completeness, and the score drives assignment volume — which Pass 1 says can be most of a restoration company's revenue.

The scores are largely uncontrolled comparisons. A contractor working large fire losses in a dense metro has a longer cycle time than one working small water losses in a suburb, and the scorecard reads that as worse performance. A contractor assigned the difficult jobs in a catastrophe zone gets worse satisfaction scores because the claims were harder, not because the work was worse. A contractor whose estimates are adjusted more often may be scoping correctly against auditors who are wrong.

So the ranking partly measures job mix, and job mix is determined by assignment, which is determined by the ranking. The loop reinforces itself and nobody has broken it open.

## What Already Exists
Vendor performance management, supplier scorecarding, and business intelligence platforms are mature and widely deployed, with SLA tracking, weighted scoring, and benchmarking as standard features.

## The Customization Gap
Generic vendor scorecards assume comparable work. Restoration jobs are not comparable in any dimension that matters.

**Case-mix adjustment is the whole problem.** Cycle time, cost, and satisfaction all need adjusting for loss type, severity, property characteristics, occupancy, geography, and catastrophe conditions before any contractor comparison means anything. This is standard practice in clinical outcome measurement and entirely absent from vendor scorecards.

**Assignment is not random, and it is the administrator's own doing.** Selection into a contractor's book is driven by prior scores, which makes the comparison confounded by construction. Estimating a contractor effect requires acknowledging the assignment mechanism — the administrator knows it exactly, because it runs it.

**Satisfaction is a claim outcome as much as a service outcome.** Policyholders whose claim was underpaid rate the contractor badly. Separating dissatisfaction with the settlement from dissatisfaction with the work is essential and no generic tool attempts it.

**Small denominators need shrinkage.** A contractor with eleven jobs in a quarter has a noisy score, and treating it as comparable to one with four hundred produces rankings driven by luck. Hierarchical estimation is the standard answer and scorecards almost never use it.

**The score has to be explainable to the contractor.** It determines their revenue, and they will challenge it. Adjusted metrics must be defensible in plain terms — which constrains the method and is worth the constraint.

## Target Customer
VP of Network Performance or Chief Analytics Officer at a managed repair administrator, where the scorecard is the primary control mechanism over the network and its fairness is challenged constantly.

## Impact If Solved
Assignment goes to contractors who are genuinely better rather than to those who happened to draw easier work, which improves outcomes for carriers and policyholders. And a scorecard a contractor can understand and contest on the merits removes the largest source of friction between administrators and the operator layer, where the current metric quietly punishes anyone doing the hard jobs.
