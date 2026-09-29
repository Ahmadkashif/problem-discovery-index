# Software Analytics and Pattern Mining

**Niche:** [[niches/headless-commerce-vendors/composition-pattern-intelligence/profile|Composition Pattern Intelligence]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software analytics established that architectural and practice choices correlate measurably with outcomes across many projects, and this category has the projects and no analysis.
**Tags:** #causal-inference #gradient-boosting #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #graph-theory #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn hundreds of implementations into an empirical account of which compositions work — and whoever does that advises better than anybody, because every architect in the category is currently designing from anecdote.

## The Problem
Studying many software projects to find which practices and structures correlate with which outcomes is an established research and industry practice. Software analytics mines repositories and delivery data across organisations to produce findings about what actually predicts defect rates, delivery speed and maintainability. Architecture research does the same for structural choices. The methods, the confounding controls and the reporting conventions all exist, and a platform vendor with hundreds of implementations has a better dataset than most of that research used.

## What Already Exists
Software analytics methodology across multi-project datasets; architectural metrics including coupling and change propagation; mining of delivery and incident data for practice correlations; observational study design with confounding control; and the published findings on what predicts software delivery outcomes.

## The Customization Gap
The adaptation is to a composition spanning organisations. It requires: (1) architectural characterisation at the composition level rather than at the code level, since the structure of interest is which services with which boundaries rather than which classes — defining that characterisation is the specific work and no metric set exists for it; (2) retailer complexity as the dominant confounder, since a large complex retailer chooses different compositions and has worse outcomes for reasons unrelated to the choice, and failing to control for it will produce confident nonsense; (3) outcomes drawn from several parties, including the retailer's own conversion data, which requires a data-sharing basis; (4) small sample sizes by research standards, which argues for simple analyses with honest uncertainty rather than elaborate models; and (5) findings expressed as guidance for an architect rather than as coefficients.

## Target Customer
Platform vendors, integrators, and the software analytics research community for whom cross-organisation composed architectures are an unstudied case.

## Impact If Solved
Software analytics established that structural choices correlate measurably with outcomes and this category has a better dataset than most of that research used. Retailer complexity is the dominant confounder and failing to control for it would produce confident nonsense, which is the analysis's central design requirement.
