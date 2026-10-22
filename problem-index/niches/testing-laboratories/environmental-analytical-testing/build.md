# Predicting Matrix Trouble Before the Sample Hits the Instrument

**Niche:** [[niches/testing-laboratories/environmental-analytical-testing/profile|Environmental Analytical Testing]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** One heavily contaminated sample run undiluted can contaminate an instrument for a day, and the lab usually learns which sample it was only after the damage.
**Tags:** #gradient-boosting #random-forests #feature-engineering #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to return a defensible, accreditation-compliant result inside each method's holding time at a per-sample price consultants and utilities will accept, and whoever runs the densest automated lines — PFAS above all — takes the monitoring contracts.

## The Problem
An environmental lab receives samples from sites it has seen many times and sites it has never seen. Some arrive with concentrations orders of magnitude above the calibration range, or with oils, surfactants and sediment that suppress signals and clog columns. Run undiluted, a hot sample causes carryover into the next several samples, forces reruns, and can take a GC-MS or LC-MS/MS out of service for cleaning. PFAS methods are particularly exposed, because the instrument and the extraction both fight background contamination. Analysts screen some samples, but screening every sample costs instrument time the lab doesn't have.

## Why Nobody Has Built This
LIMS vendors track samples, not what happened to them on the instrument. The information needed — the site's history, the client's field notes, the sample's appearance at receipt, results from earlier events at the same well — sits in different systems, and nobody owns the cross-system question "which of today's samples will hurt us?"

## What to Build
A risk score for every logged sample that predicts the probability it exceeds the calibration range or needs cleanup, using the lab's own history for that client, site and location; prior results at the same sampling point; matrix and field observations recorded at receipt; and the project's expected contaminants. High-risk samples are routed to screening or a pre-planned dilution; low-risk samples go straight to the batch. Every outcome — carryover, rerun, dilution — feeds back as a label.

## Target Customer
VPs of operations and section supervisors at environmental lab networks running high-volume volatiles, semivolatiles and PFAS.

## Impact If Built
Fewer reruns and instrument outages translate directly into capacity on the scarcest lines and into turnaround the lab can promise, which is what environmental accounts are won on.
