# Spatial Statistics the Discipline Already Has

**Niche:** [[niches/agtech-platforms/row-crop-farm-management/profile|Row Crop Farm Management]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Agricultural field experimentation has a century of statistical method behind it — the design of experiments literature began in agriculture — and commercial farm software compares two strips by taking averages.
**Tags:** #hypothesis-testing #bayesian-inference #gaussian-processes #confidence-intervals #evaluation-metrics #causal-inference #monte-carlo-methods #feature-engineering
**Contested on:** Every serious competitor in row crop software is fighting to tell a grower which of their input decisions actually changed the yield on their own ground — and whoever produces credible on-farm effect estimates takes the account.

## The Problem
A grower runs a side-by-side comparison — this half of the field treated, that half not — and compares average yields. The treated half comes out higher. It is also the half with the better drainage, which the grower knows and cannot quantify, so the comparison is uninterpretable and everyone knows it. The methods for handling exactly this were developed in agricultural field trials and are taught in every agronomy programme, and none of them are in the software.

## What Already Exists
The design and analysis of field experiments is the founding application of modern statistics, with a century of literature on blocking, randomisation, spatial adjustment and mixed models. Spatial statistics packages implementing kriging, Gaussian process regression and spatially correlated error structures are mature and free. Agronomic research institutions publish on-farm trial methodology, and several university extension programmes run on-farm research networks using it. The methodology is public, taught, and entirely absent from commercial farm management software.

## The Customization Gap
The adaptation is to the operational realities of a working farm rather than a research plot. It requires: (1) designs constrained by equipment — strip widths set by planter and sprayer geometry, turn rows excluded, headlands handled — since a design the machinery cannot execute is not a design; (2) spatial adjustment as standard rather than optional, because the within-field variation in soil, drainage and topography is the dominant source of yield variation and any analysis that ignores it is measuring geography; (3) yield monitor data cleaning as a prerequisite, since raw combine yield data contains substantial artefacts and analysing it unfiltered produces confident nonsense — this is the fix note's subject and is genuinely load-bearing; (4) power analysis presented before the trial, so a grower knows whether the question they are asking can be answered on the acres they have, which is the honest conversation nobody currently has; and (5) multi-year and multi-farm pooling with the heterogeneity modelled, since most effects worth knowing are too small to resolve in one field-season.

## Target Customer
Farm management platform vendors, independent agronomy firms running trials for clients, and the agricultural research and extension programmes who have the methodology and lack the distribution.

## Impact If Solved
The statistical methodology is the mature part and the operational adaptation is the work, which inverts the usual case and makes this unusually tractable. Power analysis before the trial is the element most likely to change practice immediately, because a great deal of current on-farm comparison is asking questions the acreage cannot answer, and saying so is more useful than another inconclusive result.
