# Soil Sampling Design From Geostatistics

**Niche:** [[niches/agtech-platforms/retail-agronomy-prescriptions/profile|Retail Agronomy — Prescriptions With a Conflict Attached]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Variable rate prescriptions are built on soil test values interpolated across a field, geostatistics has a mature literature on how to sample and interpolate spatial data with known uncertainty, and sampling in practice is a grid somebody chose.
**Tags:** #gaussian-processes #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #optimization-fundamentals #numerical-methods #feature-engineering
**Contested on:** Every serious competitor in retail agronomy software is fighting to make a recommendation credible when the adviser's employer sells the product — and whoever can evidence that a prescription paid for the grower takes the relationship.

## The Problem
A field is sampled on a grid, the samples are analysed, the values are interpolated across the field, and a prescription is written from the interpolated surface. Whether the sampling density was adequate for the variability actually present, how much uncertainty the interpolated surface carries, and whether the prescription's zone boundaries are distinguishable from noise are all unasked. The grid spacing is a convention. The prescription is presented as precise.

## What Already Exists
Geostatistics — kriging, variogram estimation, spatial sampling design, uncertainty quantification on interpolated surfaces — is a mature discipline developed substantially for exactly this class of problem, with free implementations and a substantial soil science literature applying it. Optimal sampling design methods are well developed. Gaussian process regression provides both the interpolation and the uncertainty in one framework. All of it is available and taught.

## The Customization Gap
The adaptation is to sampling that costs money per point and prescriptions that must be actionable. It requires: (1) sampling design driven by the field's actual variability structure, estimated from prior samples, imagery and topography, rather than by a uniform grid — which typically means more samples where variation is high and fewer where it is not, at the same total cost and much better information; (2) uncertainty carried through to the prescription, so zone boundaries that are not distinguishable from noise are not drawn, which is the honest treatment and the one that would change several current prescriptions; (3) sampling value analysis — telling a grower what an additional round of sampling would be worth in prescription improvement, which is the question they actually ask when quoted for it; (4) multi-source integration, since imagery, topography, electrical conductivity and yield history all inform the surface and using samples alone discards most of the available information; and (5) presentation that keeps the agronomic interpretation with the agronomist, since a statistically better surface is an input to judgement rather than a replacement for it.

## Target Customer
Retail agronomy organisations and soil sampling service providers, prescription platform vendors, and the independent consultants advising on sampling programmes.

## Impact If Solved
Better sampling design produces better prescriptions at the same cost, which is a direct improvement available by importing a mature method. The uncertainty propagation is the more uncomfortable and more valuable half: some current prescriptions draw distinctions the data does not support, and knowing which is the beginning of the credibility this sub-niche is contested on.
