# Burial Likelihood Maps With Stated Uncertainty

**Niche:** [[niches/geophysical-survey-firms/burial-cemetery-archaeological-gpr/profile|Burial, Cemetery & Archaeological GPR]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every grave-search report sorts anomalies into "probable," "possible" and "unlikely" by one interpreter's judgement, with no calibrated basis anyone can check against the excavations and records that exist from other sites.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #bayesian-inference #confidence-intervals #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to produce a map of probable burials that families, tribes and regulators accept as honest — neither overclaiming anomalies as graves nor missing them — and whoever's confidence language holds up when ground-truthing happens is hired for the next search.

## The Problem
Experienced cemetery interpreters recognise grave shafts by size, orientation, alignment in rows, depth and the reflection pattern of disturbed backfill, and distinguish them from roots, animal burrows and utility trenches. Their categories are qualitative and differ between practitioners, and the public reads any category as a count of graves.

## Why Nobody Has Built This
Ground truth is rare and sensitive: many communities choose not to excavate. Where it exists — cemetery relocations for development, archaeological excavation, known-burial test grids — it is scattered across reports and firms. And no one wants to be first to publish a probability for something this painful.

## What to Build
A consortium dataset of GPR grids from sites with verified burials (relocation projects, excavated archaeological cemeteries, marked graves in active cemeteries), used to train detectors and calibrate likelihoods by soil, age of burial and survey parameters. Reports would map each feature with a stated probability band and the basis for it, plus the share of likely burials the survey could have missed given soil attenuation and coverage.

## Target Customer
Cultural resource management firms, university geophysics groups doing community searches, and tribal governments commissioning them.

## Impact If Built
Findings that communities can act on and defend — fewer overstated numbers and fewer graves missed under a development.
