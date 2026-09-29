# Evaluation Workflow Built for Vertical Wells

**Niche:** [[niches/oil-gas-field-services/reserve-engineering-firms/profile|Reserve Engineering Firms]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The evaluation software the industry runs on was designed for conventional wells that decline predictably, and the assets being evaluated do not.
**Tags:** #ml-time-series #tabular-ml #workflow-orchestration #evaluation-metrics #automation

## The Problem
A reserve evaluation means fitting a decline to every producing well, projecting it to an economic limit, assigning undeveloped locations, applying prices and costs, and discounting — repeated across thousands of wells, twice a year, on immovable deadlines.

The software the industry uses is mature and was designed around conventional production: wells that establish a stable decline and follow it. Unconventional wells do not. They exhibit long transient flow, respond to offset activity, are shut in for adjacent operations, and are frequently refractured — and every one of those breaks a simple decline fit.

So engineers fit curves by hand, well by well, exercising judgment on which portion of history to honour and which to disregard. It is the largest labour item in the engagement and it happens under a deadline that does not move.

## What Already Exists
Reserve evaluation and economics software is mature and universally deployed, with decline analysis, economic modelling, and reporting to the required disclosure formats.

## The Customization Gap
The incumbent tools do the arithmetic. The judgment they were built around no longer matches the assets.

**Decline fitting has to handle interruption.** Shut-ins, offset interference, artificial lift changes, and refracs are events, and a fitting routine that treats them as data produces a wrong forecast. Detecting and classifying them from the production series is a well-posed problem the tools do not attempt.

**Analogue selection is the real judgment.** Undeveloped locations are assigned type curves from analogous wells, and choosing the analogues is where the estimate is actually made. Making that selection evidence-based — nearest neighbours by geology, spacing, and completion, with the resulting dispersion shown — is the highest-value change available and the tools offer a dropdown.

**Uncertainty must be carried through.** The output of a fit is a distribution and the workflow collapses it to a point at the first step, so the final estimate has no uncertainty attached even though the disclosure categories are defined probabilistically.

**Volume with auditability.** Thousands of wells, twice a year, where every fit must be explicable to an auditor months later. Automation is only useful if it leaves a reviewable record of what was decided and why.

**Portfolio review, not just well review.** Engineers see wells; the errors that matter appear as patterns across a property. Surfacing wells whose fits diverge from their peers is a check nobody runs.

## Target Customer
Practice leader or chief engineer at a reserve engineering firm, where deadline pressure and per-well judgment set both the cost and the quality ceiling of every engagement.

## Impact If Solved
Semi-annual redetermination and year-end reporting are hard deadlines across thousands of wells, and the labour goes into curve fitting rather than judgment. Automating the mechanical portion with event detection, and making analogue selection evidence-based, moves engineer time to the decisions that actually determine the estimate.
