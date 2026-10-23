# Machine Learning Opportunities — Electric Distribution Utilities

**Industry:** [[electric-utilities|Electric Distribution Utilities]]
**Derived from:** [[problems/electric-utilities/high-impact|High Impact]], [[problems/electric-utilities/low-impact-1|Low Impact 1]], [[problems/electric-utilities/low-impact-2|Low Impact 2]], [[problems/electric-utilities/worker-life-1|Worker Life 1]], [[problems/electric-utilities/worker-life-2|Worker Life 2]]

---

## 1. Learning the Planner's Capacity Read
#tacit-knowledge-ml #gradient-boosting #graph-neural-networks #large-language-models #survival-analysis #evaluation-metrics #revenue-impact

**Problem statement:** A senior distribution planner can glance at a request and a feeder and say whether it fits, what will bind and roughly what the upgrade costs, a judgement built across hundreds of studies that juniors lack and that leaves at retirement. The ML problem is to learn that read from the utility's archive of interconnection and large-load studies, joined to the feeder state at the time, and to predict the study outcome for a new request before the study is run.

**ML task:** Multi-task prediction per request: binary fits-without-upgrade, multi-class binding constraint (thermal, voltage, reverse flow, protection, substation capacity), and quantile regression of upgrade cost. Feeder topology is encoded as a graph, and information extraction from historical study PDFs feeds the labels.
**Input data:** Historical study reports (PDF) parsed by a language model into structured records; feeder and substation models from CYME, Synergi or OpenDSS reconstructed at study date; SCADA and AMI loading history, peak and minimum load; existing DER by location; protection settings; request size, type and location; planners' one-click quick reads captured on new requests. Public features from EIA-861, EIA-860 and published hosting-capacity maps allow a territory-level version.
**Target:** Study outcome labels (fit, binding constraint, upgrade list, estimated cost); where available, actual energised cost and post-energisation violations.
**Evaluation metric:** On fits-without-upgrade, precision at high confidence matters most. A request waved through that later needs a substation bank is a public embarrassment and a cost shift, while a false "needs study" only costs time. Report precision at the confidence threshold used for auto-screening, coverage (share of requests the screen can answer), and pinball loss on cost quantiles. Report agreement with the senior planner's quick read against the planner's own test-retest agreement on repeated cases as the ceiling. Evaluate strictly out of time: train on studies before a date, test after.
**Scope:** The data collection challenge comes first: the expert's read must be captured when the request arrives, through a near-zero-effort labelling step in the intake workflow, and years of study PDFs must be extracted and matched to model snapshots that no longer exist in their original form. The labelling challenge is that planners disagree with each other and with their past selves. Borderline cases need double labelling to measure that, and withdrawn requests must be treated as censored, not as negatives, which is where survival-style handling of outcomes comes in. The deployment challenge is that the screen must answer faster than the planner's glance and give reasons the planner recognises: the binding element and the most similar past studies. It must also run inside the utility, because network models are often protected critical infrastructure information. 2 ML engineers, 1 power systems engineer and part of a senior planner's time, 6–9 months for one utility. The study archive extraction is the long pole.
**Data availability:** Study reports and network models are held by each utility and are not shared across utilities. Public data (EIA-861, EIA-860, FERC Form 1, DOE's hosting-capacity map atlas) supports a coarse screen and an MVP; the decisive labels are internal.

---

## 2. Storm Damage and Outage Prediction for Crew Staging
#gradient-boosting #random-forests #time-series-forecasting #feature-engineering #evaluation-metrics #workflow-orchestration

**Problem statement:** Two to three days before a hurricane, ice storm or derecho, predict outage counts and damage (broken poles, downed spans) per grid cell or feeder, so the utility can request the right number of mutual-assistance crews and pre-stage them, then refine the prediction as the storm arrives.

**ML task:** Count regression (outages and damage locations per cell and time window) with quantile outputs, updated as forecasts change; later, nowcasting from early outage reports
**Input data:** Numerical weather prediction forecasts (gusts, precipitation, ice accretion, soil moisture); vegetation density from LiDAR or satellite; asset attributes (pole age and class, conductor type, overhead versus underground); past storm outage records from the outage management system; ORNL's EAGLE-I public county outage data for cross-utility history.
**Target:** Outage events and damage counts per cell; customers out; total restoration crew-hours needed.
**Evaluation metric:** Interval coverage and pinball loss on the territory total and on regional totals, because staging decisions are made on totals with uncertainty. Under-prediction is costlier than over-prediction: extra crews cost money, but too few crews add days of outage and regulatory scrutiny. Report skill against the storm boss's own pre-storm estimate.
**Scope:** University-utility outage prediction models have shown this is buildable. The hard parts are a small number of major storms per utility, forecast error that dominates model error, and changing grids. 2 data scientists with a meteorologist, 4–6 months to a first operational model, improved storm by storm.
**Data availability:** Outage history is utility-owned and usually clean in the OMS; weather forecasts and EAGLE-I are public; vegetation and asset data vary in quality.

---

## 3. Probabilistic Load Forecasting With a Large-Load Pipeline
#temporal-fusion-transformers #gradient-boosting #survival-analysis #time-series-forecasting #bayesian-inference #evaluation-metrics #revenue-impact

**Problem statement:** Forecast substation and system peak load over one to ten years when a pipeline of large-load requests (data centres, factories, EV depots) of very uncertain realisation sits on top of organic load growth, for use in distribution capital plans, integrated resource plans and rate cases.

**ML task:** Hierarchical probabilistic forecasting of hourly and peak load per substation and system, combined with survival modelling of each large-load request's time to energisation (or withdrawal) and ramp shape
**Input data:** Hourly substation and system load (SCADA; system-level is public through FERC Form 714 and EIA-930); AMI aggregates by class; weather; economic drivers; EV, heat-pump and solar adoption; the large-load request log with stage gates (application, study, agreement signed, collateral posted, construction, first energisation) and requester attributes.
**Target:** Load distribution per substation per year at peak; per-request probability and timing of energisation and ramp.
**Evaluation metric:** Continuous ranked probability score and peak-hour interval coverage, back-tested on past forecast vintages; for the pipeline model, concordance and calibration of energisation probability by stage. Over-forecasting strands capital in rates; under-forecasting leaves loads unserved, so calibration matters more than point accuracy.
**Scope:** Organic load forecasting is mature (Itron and in-house models). The new part is the pipeline model, which needs disciplined stage tracking of requests that most utilities keep in spreadsheets. 2 data scientists, 4–6 months.
**Data availability:** System load and filed forecasts are public; substation loads and the large-load pipeline are internal and commercially sensitive.

---

## 4. Meter-to-Transformer Connectivity From AMI Voltage
#k-means-clustering #pca #graph-theory #feature-engineering #descriptive-statistics #data-integration #quick-win

**Problem statement:** GIS connectivity models are often wrong about which transformer and phase serve each meter, which corrupts outage prediction, transformer loading estimates and hosting capacity. Infer the true meter-to-transformer and phase mapping from correlations in AMI voltage time series, and flag overloaded transformers and suspect meters along the way.

**ML task:** Unsupervised grouping of meters by voltage-profile correlation, with dimensionality reduction and graph-constrained assignment to transformers and phases; anomaly flags for meters whose consumption and voltage do not fit their group
**Input data:** 5–15 minute AMI voltage and consumption series; GIS connectivity and transformer ratings; field-verified corrections as validation labels.
**Target:** Corrected meter-to-transformer and meter-to-phase assignments with confidence; transformer loading estimates; suspect-meter flags.
**Evaluation metric:** Accuracy of assignments against field-verified samples, reported per feeder type; precision of correction suggestions (a wrong correction pushed into GIS is worse than none). Downstream: improvement in outage-prediction accuracy after correction.
**Scope:** Well-studied and quick to show value where AMI collects voltage. 1–2 data scientists, 3 months for a pilot feeder set; scaling needs data engineering against the meter data system.
**Data availability:** AMI data is utility-owned and subject to state customer privacy rules; it stays inside the utility. Voltage collection is not enabled on every AMI deployment.

---

## 5. Rate Case Data Request Triage and Drafting
#bert #large-language-models #transformers #word-embeddings #evaluation-metrics #compliance #automation

**Problem statement:** Classify each intervenor data request by topic, FERC account and responsible witness, retrieve the closest prior answers and workpapers, and draft a response consistent with pre-filed testimony and earlier answers in the same case.

**ML task:** Multi-label text classification for routing; dense retrieval over prior responses, testimony and workpapers; grounded drafting with consistency checking against testimony
**Input data:** Past data requests and served responses (public on commission e-filing systems for most cases, internal drafts for the rest); testimony and exhibits; the minimum filing requirement schedules; the witness list.
**Target:** Topic, account and witness labels; retrieved prior answers; draft responses; inconsistency flags.
**Evaluation metric:** Routing accuracy (top-1 witness); retrieval recall at 5 on requests with a known prior answer; witness edit distance on drafts; and above all zero unflagged contradictions with testimony, since an inconsistency becomes cross-examination material.
**Scope:** A retrieval-first build on public filings is feasible in 3–4 months with 2 engineers and a regulatory analyst; drafting confidence grows with each case.
**Data availability:** Served responses are mostly public on state commission dockets, which makes a cross-utility corpus possible; confidential responses stay internal.
