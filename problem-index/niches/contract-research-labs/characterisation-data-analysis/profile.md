# Characterisation & Microscopy Data Analysis

**Parent Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn raw micrographs, spectra and diffraction patterns into a quantified result with stated uncertainty that a sponsor accepts, and whoever does it fastest with a method two analysts would reproduce takes the account.

## Profile
**Market Size:** ~$250M a year in image and spectral analysis software, analysis services and staff time spent on data reduction at materials and nanotech research labs (estimate)
**Share of Parent Industry:** ~12% of contract research labs' tooling and services spend (estimate)
**Digital Adoption:** Medium — instruments are digital; analysis is semi-manual in vendor software, ImageJ and personal scripts
**Target Buyer:** Characterisation group lead or chief scientist
**Automation Potential:** High — segmentation, peak fitting and phase identification are well-defined tasks with abundant data

## What Makes This a Distinct Niche
Materials and nanotechnology research ends in measurement: particle size distributions from electron micrographs, film thickness and composition from spectroscopy, phase from diffraction, defect counts from inspection images. The reduction from raw data to a number is repetitive, often manual where samples are messy, and varies between analysts, which matters when the number goes into a sponsor's qualification decision. Published work shows segmentation models trained on 30–40 annotated TEM images reaching ~85% F1 and agreeing with manual sizing.

## Current Tools & Gaps
Instrument vendor software (Thermo Fisher Velox and Avizo, Gatan DigitalMicrograph, Bruker and Malvern Panalytical analysis suites); ImageJ/Fiji; Python and MATLAB scripts; Excel. Gaps: agglomerated and irregular particles traced by hand; thresholds and fitting choices undocumented; no shared method across analysts or instruments; no record linking a reported number to the exact analysis that produced it.

## Problems
- [[niches/contract-research-labs/characterisation-data-analysis/build|🔨 Build: Segmentation With a Review Loop and a Method Record]]
- [[niches/contract-research-labs/characterisation-data-analysis/buy|🛒 Buy: Instrument Analysis Suites Fitted to Sponsor Reporting]]
- [[niches/contract-research-labs/characterisation-data-analysis/fix|🔧 Fix: Every Analyst Picks Their Own Threshold]]
