# Machine Learning Opportunities — Agtech Platforms

**Industry:** [[agtech-platforms|Agtech Platforms]]
**Derived from:** [[problems/agtech-platforms/high-impact|High Impact]], [[problems/agtech-platforms/low-impact-1|Low Impact 1]], [[problems/agtech-platforms/low-impact-2|Low Impact 2]], [[problems/agtech-platforms/worker-life-1|Worker Life 1]], [[problems/agtech-platforms/worker-life-2|Worker Life 2]]

---

## 1. On-Farm Randomised Trials and Pooled Treatment Effect Estimation
#causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Growers commit large input budgets annually against evidence from manufacturer plots, retailer trials and neighbours. The machinery in the field can execute a randomised, replicated, geographically blinded experiment without anyone leaving the cab, and the prescription file that would specify it is written on a computer before every pass.

**ML task:** Experimental design (randomised strip allocation blocked on within-field variation) followed by treatment effect estimation, with hierarchical pooling across farms and seasons
**Input data:** As-applied machine records with position; yield monitor data at sub-metre resolution; soil survey and electrical conductivity maps; elevation and drainage; historical yield by zone; weather at field level; crop, variety and management; input and grain prices for the return calculation.
**Target:** Yield difference between treatment and control strips, converted to return per acre at realised prices.
**Evaluation metric:** Interval coverage on synthetic treatments with known zero effect is the honest first test — a method that finds significant effects in null trials is worse than no method. Report minimum detectable effect size per farm-season and how it shrinks with pooling, since that is the number that tells a grower whether their trial can answer their question.
**Scope:** Yield data cleaning dominates the work and determines whether the result is real: flow delay through the combine, header width errors, headland passes, moisture calibration drift and operator behaviour all produce artefacts that swamp a few per cent treatment effect. Within-field soil variation frequently exceeds the effect being measured, which is precisely why blocking and randomisation are non-negotiable and why casual side-by-side comparisons mislead. 3-4 ML engineers plus an agricultural statistician, 8-12 months across at least two seasons.
**Data availability:** Machine and yield data is abundant. Randomised treatment assignment does not currently exist and must be created prospectively, which makes this a multi-season programme rather than a retrospective analysis. Historical data supports observational estimates only, with all the confounding that implies.

---

## 2. Field, Product and Operation Entity Resolution Across Brands
#bert #word-embeddings #k-nearest-neighbors #dbscan #k-means-clustering #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** A mixed-fleet farm cannot assemble a coherent field record. Standards translate file formats and do not resolve semantics — that "Home 80" and "Home Farm 80" are one field, that a retailer's product abbreviation is the plan's trade name, or which of two overlapping boundary polygons is correct.

**ML task:** Multi-type entity resolution — fields by geometry, products by chemistry and rate, operations by timing and overlap — plus systematic correction of known machine data artefacts
**Input data:** Machine task data across brands with boundaries, names, products, rates and timestamps; input invoices and applicator tickets; crop plans; historical resolved records as labels where available; product registration databases for chemistry normalisation.
**Target:** A canonical field, product and operation identity per record, and a corrected as-applied and yield surface.
**Evaluation metric:** Resolution accuracy against grower-confirmed records, with false merges weighted heavily — combining two fields or two products silently corrupts every downstream analysis and is far worse than leaving a record unresolved. For artefact correction, agreement between corrected yield totals and elevator delivery records, which is an independent ground truth the industry rarely uses.
**Scope:** Geometry does most of the field resolution work and is reliable. Product resolution is the harder half because names are abbreviated, retailer-specific and drift, though chemistry and rate constrain it strongly. Yield artefact correction is well-characterised engineering rather than research and should ship first, since every analysis depends on it. 2-3 ML engineers plus an agronomy data specialist, 6 months.
**Data availability:** Excellent volume across platform customer bases. Labels come from records growers have already reconciled by hand, which exist but sit in individual farm accounts rather than as a curated set.

---

## 3. Practice Inference from Remote Sensing for Programme Baselines
#cnns #semantic-segmentation #time-series-forecasting #gradient-boosting #confidence-intervals #evaluation-metrics #transfer-learning #compliance

**Problem statement:** Sustainability and conservation programmes require documented practice history over a baseline period that most growers hold in a filing cabinet, in a format each programme defines differently. The administrative burden deters exactly the growers whose practices would qualify.

**ML task:** Temporal classification of management practices — tillage intensity, cover crop presence and termination timing, residue cover, crop identity — from satellite image time series
**Input data:** Multi-spectral satellite time series (Sentinel-2, Landsat, commercial constellations); field boundaries; ground truth from as-applied machine records where growers permit; crop insurance and USDA layers; local weather.
**Target:** Practice labels per field per season, validated against machine records.
**Evaluation metric:** Per-practice accuracy with explicit calibration, because programme payments depend on the claim and an over-confident classification is a verification failure with financial consequences. Report accuracy separately by region and by cloud cover conditions, since coverage gaps are where the method quietly degrades.
**Scope:** Machine records from participating growers provide the labels, which makes this an unusually well-supervised remote sensing problem compared to most agricultural imagery work. Cover crop detection is hardest in short windows and under cloud, and tillage intensity classification is genuinely difficult at the margins between reduced and conventional. Uncertainty should be carried through to the grower's expected payment rather than hidden behind a point estimate. 3 ML engineers plus a remote sensing specialist, 6-8 months.
**Data availability:** Imagery is free, global and continuous. Labels require grower consent to use as-applied records, which platforms can obtain but must obtain explicitly. Soil carbon outcomes — what programmes actually pay for — are modelled with wide error bars and are not directly observable, which limits what any of this can honestly claim.

---

## 4. Scouting Observation Capture and Pest Identification
#cnns #object-detection #semantic-segmentation #large-language-models #transformers #transfer-learning #evaluation-metrics #worker-facing

**Problem statement:** Agronomists write scouting reports in the evening from notes and photographs taken hours earlier across a dozen fields. Reports become short under time pressure, and the accumulated scouting record — potentially the most valuable dataset an agronomy operation owns — is a series of brief notes.

**ML task:** Image classification and detection for weed, disease and insect identification with severity estimation, plus report generation grounded in the captured observations
**Input data:** Geotagged field photographs; spoken observation notes; crop, variety and growth stage; planting date; local weather; historical scouting records for the territory; regional pest and disease pressure reports.
**Target:** Confirmed species identification and severity as the agronomist recorded them, and the final report text they sent.
**Evaluation metric:** Top-1 and top-3 identification accuracy by species, reported separately for common and rare species since the aggregate hides the failures that matter. Precision must dominate for anything that triggers a spray recommendation. For reports, the proportion of sections sent with minor or no editing, and adherence to the individual agronomist's established style.
**Scope:** Common species identification is a solved problem class; the value is in the workflow — capture at the point of observation, confirmation rather than typing, and a report that assembles itself. Growth stage inference from imagery adds useful context and is more reliable than it sounds given the planting date. The territory-level view of pest movement is a straightforward aggregation once observations are structured and located, and is the part that compounds. 2-3 ML engineers, 5 months, using public agricultural image datasets as a base and fine-tuning on the operation's own photographs.
**Data availability:** Public labelled datasets exist for major crop pests and diseases and are a strong starting point. Agronomist photographs are abundant and unlabelled; confirmed identifications from the reports provide weak labels once capture is instrumented.
