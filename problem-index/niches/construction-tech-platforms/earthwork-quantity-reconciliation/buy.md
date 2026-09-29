# Drone Survey Adapted to Continuous Quantity Verification

**Niche:** [[niches/construction-tech-platforms/earthwork-quantity-reconciliation/profile|Earthwork & Sitework — Quantity Reconciliation]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Drone survey is a mature, cheap, widely adopted product that earthwork contractors already fly weekly, and its output is used as a progress photo and a monthly volume check rather than as the continuous measurement instrument it is.
**Tags:** #numerical-methods #confidence-intervals #hypothesis-testing #change-point-detection #evaluation-metrics #descriptive-statistics #automation #data-integration
**Contested on:** Every serious competitor in earthwork software is fighting to reconcile the material actually moved against the material paid for, across design surfaces, machine control, survey and truck counts — and whoever makes those four numbers agree takes the account.

## The Problem
A contractor flies the site every week and gets a surface, an orthomosaic and a volume figure against the design. The volume figure is used once a month to check the pay quantity, and the rest is filed. Meanwhile the weekly cadence contains a far richer signal — where material moved between flights, whether a area is tracking to its planned production, where the surface is diverging from design in a way that predicts a quantity overrun — and none of it is extracted, because the product delivers a surface and the contractor has an engineer, not an analyst.

## What Already Exists
DroneDeploy, Propeller, Pix4D and Skydio's mapping products all deliver photogrammetric surfaces at survey-grade accuracy with proper ground control, and volume comparison against a design surface is a standard feature in every one of them. Flight is routine and unremarkable on most sites. Accuracy characteristics are well documented. The technology and the operational practice are both settled.

## The Customization Gap
The adaptation is to treat the weekly flight as a time series rather than as a snapshot. It requires: (1) flight-to-flight differencing to produce weekly moved-volume by area, which is the production measurement the contractor actually manages by and which almost nobody computes; (2) honest uncertainty propagation, because a small difference between two surfaces each carrying centimetre-level error is not a measurement, and a product that reports it as one will be discredited on its first argument; (3) automatic exclusion of the things that corrupt a comparison — stockpiles, equipment, standing water, vegetation — which is ordinary segmentation work and is the difference between a usable number and a noisy one; (4) forecasting remaining quantity from the realised production curve rather than from the plan, so a contractor knows in week four whether the schedule is achievable; and (5) exporting into the reconciliation engine rather than into a report, since the survey's value multiplies when compared with machine and haul data.

## Target Customer
Earthwork contractors already flying regularly, and the drone survey vendors who currently compete on accuracy and could compete on production intelligence instead.

## Impact If Solved
Weekly located production data changes earthwork management from monthly retrospection to weekly control, and forecasting remaining quantity from realised rates is the earliest reliable warning a contractor can get on a quantity-paid job. The flights are already paid for; this is extraction from data currently filed.
