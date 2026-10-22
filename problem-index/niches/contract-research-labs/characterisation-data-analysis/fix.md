# Every Analyst Picks Their Own Threshold

**Niche:** [[niches/contract-research-labs/characterisation-data-analysis/profile|Characterisation & Microscopy Data Analysis]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Fix (Pain Point)
**One-liner:** Two analysts measuring the same micrographs report different size distributions because each set their own threshold and exclusion rules, and nobody wrote either down.
**Tags:** #cnns #semantic-segmentation #evaluation-metrics #hypothesis-testing #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn raw micrographs, spectra and diffraction patterns into a quantified result with stated uncertainty that a sponsor accepts, and whoever does it fastest with a method two analysts would reproduce takes the account.

## The Problem
Thresholds, minimum particle sizes, edge exclusions and how to treat touching particles are judgement calls. They shift between analysts and between days. When a sponsor compares two batches measured by different people, part of the "difference" is the analysts.

## Why It's Still Broken
The choices live in an analyst's ImageJ session and are not saved with the result; methods sections say "ImageJ was used".

## What a Fix Looks Like
A standard per-material analysis protocol saved as a reusable pipeline, with every parameter recorded alongside the result, and a periodic blind re-measurement of a reference image set by each analyst to quantify between-analyst variation and report it with results.

## Who Feels the Pain
Analysts asked to defend numbers; PIs comparing batches; sponsors making qualification decisions on differences that may be noise.

## Impact If Fixed
Measured differences between batches become real differences, and the lab can state its measurement uncertainty instead of hoping nobody asks.
