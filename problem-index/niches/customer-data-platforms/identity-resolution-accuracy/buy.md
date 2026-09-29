# Record Linkage Practice

**Niche:** [[niches/customer-data-platforms/identity-resolution-accuracy/profile|Identity Resolution Accuracy]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical agencies have matched records to people for seventy years with published error rates and clerical review, and identity graphs ship a threshold.
**Tags:** #bayesian-inference #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #expectation-maximization #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to measure how often the identity graph merges two people or splits one — and whoever makes that measurable turns the category's central function from a threshold into an engineering discipline.

## The Problem
Record linkage is an old and rigorous discipline. Statistical agencies, health systems and census operations have matched records to individuals for decades using formal probabilistic frameworks with estimated match probabilities, defined clerical review regions for uncertain pairs, measured false match and false non-match rates, and published methodology. The error rates are known and reported because decisions depend on them. Commercial identity graphs perform the same operation at far greater scale with a configurable threshold and no error measurement.

## What Already Exists
Probabilistic record linkage frameworks with estimated match weights; clerical review of the uncertain middle; false match and false non-match rate estimation; blocking and indexing for scale; and published linkage quality methodology.

## The Customization Gap
The adaptation is to real-time commercial scale with no clerical reviewer. It requires: (1) no human review of uncertain pairs, since the volume is billions and the practice's key quality mechanism is a clerk examining the middle band — replacing that with automated adjudication and sampled review is the central adaptation; (2) identifiers that are devices and cookies rather than names and addresses, which have entirely different error structures and no established weight estimates; (3) real-time resolution at activation, where the statistical practice is batch; (4) the graph being used for consequential personal decisions including privacy fulfilment, which raises the stakes on a false match beyond what a statistical estimate carries; and (5) continuous change in identifier availability as privacy mechanisms evolve, which makes the linkage model non-stationary in a way census matching is not.

## Target Customer
Customer data platform vendors, identity providers, enterprise data governance teams, and record linkage practitioners for whom commercial identity graphs are an unserved application.

## Impact If Solved
Seventy years of linkage practice reports error rates because decisions depend on them, and commercial graphs report a match rate. Replacing clerical review with automated adjudication plus sampled verification is the adaptation that makes the quality mechanism work at billions of records.
