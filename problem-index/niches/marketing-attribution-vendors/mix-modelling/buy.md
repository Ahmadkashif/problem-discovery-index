# Econometric Identification Practice

**Niche:** [[niches/marketing-attribution-vendors/mix-modelling/profile|Mix Modelling]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Applied econometrics has spent decades on identification, specification testing and robustness, and marketing mix modelling reports one specification and a fit statistic.
**Tags:** #causal-inference #bayesian-inference #hypothesis-testing #confidence-intervals #time-series-forecasting #monte-carlo-methods #regularization #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to separate channels whose spends move together, from a series that is too short to do it — and whoever handles that identification problem honestly replaces answers that are mostly priors.

## The Problem
Applied econometrics treats identification as the central question: what variation in the data identifies the parameter of interest, what would confound it, and how robust is the answer to specification. The field developed specification testing, robustness reporting across alternative models, instrumental variables for endogenous regressors, and a professional norm that a result presented without robustness checks is not taken seriously. Marketing mix modelling uses the same regression machinery and skips the discipline that surrounds it.

## What Already Exists
Identification analysis and endogeneity treatment; specification testing and model selection; robustness reporting across alternative specifications; instrumental variable and control function methods; and structural break and stability testing.

## The Customization Gap
The adaptation is to short series, planned regressors and a commercial audience. It requires: (1) regressors that are chosen by the client's own planning process, making them endogenous in a specific and knowable way — the spend was set in response to expected revenue, which is the textbook endogeneity problem and is almost never addressed here; (2) series of a hundred or so weekly observations against a dozen channels with transformations, which is far shorter relative to parameters than most econometric applications and makes regularisation and priors necessary rather than optional; (3) experimental variation available on request, which econometrics rarely has and which should be used deliberately to identify what the observational data cannot; (4) results presented to non-economists who will act on a point estimate, so robustness must be communicated as a decision range; and (5) continuous refitting rather than a published paper, which changes the practice from a study to an operation.

## Target Customer
Measurement vendors, client measurement functions, and applied econometricians for whom marketing mix is an underserved and well-funded domain.

## Impact If Solved
Econometrics treats identification as the central question and mix modelling uses the same regression machinery without the discipline. Spend set in response to expected revenue is textbook endogeneity that is almost never addressed, and available experimental variation is the lever econometrics rarely has.
