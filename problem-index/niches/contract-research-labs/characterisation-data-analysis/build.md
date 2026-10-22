# Segmentation With a Review Loop and a Method Record

**Niche:** [[niches/contract-research-labs/characterisation-data-analysis/profile|Characterisation & Microscopy Data Analysis]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Research labs have models that can segment particles, and still trace them by hand, because nothing wraps the model in a review step and a record a sponsor will accept.
**Tags:** #cnns #semantic-segmentation #object-detection #transfer-learning #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn raw micrographs, spectra and diffraction patterns into a quantified result with stated uncertainty that a sponsor accepts, and whoever does it fastest with a method two analysts would reproduce takes the account.

## The Problem
Open-source segmentation models exist and papers show they work, but a lab adopting one must annotate its own images, retrain per material, decide when to trust the output, and explain the method in a report. Most labs try once, find the model wrong on their hardest images, and go back to tracing.

## Why Nobody Has Built This
Microscope vendors sell per-instrument software and treat AI segmentation as a feature; academic tools stop at the model; and the review-and-traceability layer that makes the output usable in a contract deliverable is nobody's product.

## What to Build
A lab-hosted pipeline that segments every incoming micrograph, flags low-confidence regions and unsplittable agglomerates for review, captures corrections as new training labels, retrains per material class, and writes a method record — model version, training set, review statistics, uncertainty in the reported distribution — into the deliverable.

## Target Customer
Characterisation group leads at materials and nanotech research firms and institutes processing hundreds of micrographs a month.

## Impact If Built
A multi-hour manual count becomes a twenty-minute review (estimate), results stop depending on who traced them, and the sponsor gets a number with a traceable method behind it.
