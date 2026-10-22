# Machine Learning Opportunities — Geophysical Survey Firms

**Industry:** [[geophysical-survey-firms|Geophysical Survey Firms]]
**Derived from:** [[problems/geophysical-survey-firms/high-impact|High Impact]], [[problems/geophysical-survey-firms/low-impact-1|Low Impact 1]], [[problems/geophysical-survey-firms/low-impact-2|Low Impact 2]], [[problems/geophysical-survey-firms/worker-life-1|Worker Life 1]], [[problems/geophysical-survey-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Interpreter's Anomaly Call From Verified Digs
#tacit-knowledge-ml #cnns #object-detection #transfer-learning #evaluation-metrics #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Senior near-surface interpreters look at a radargram or an EM/magnetic grid and "know" which hyperbolas are utilities and which are cobbles, which anomalies are intact munitions and which are fragments — a judgement built over years that they cannot specify. The ML problem is to learn that call from features whose outcome was later verified by excavation, coring or a test hole, and present it with its track record to whoever interprets the next site.

**ML task:** Object detection of candidate targets in GPR B-scans and gridded EM/magnetic maps, followed by multi-class classification (utility / non-utility debris / geology; or munition class / clutter) with a calibrated probability, conditioned on site-condition features
**Input data:** GPR profiles and depth slices; EM61, magnetometer or advanced-sensor grids; the interpreter's historical picks with class and depth; site features (soil velocity and attenuation estimated from the data, clutter density, method settings); and verification records — QL-A test-hole sheets with measured offsets, munitions dig results with item identification, core logs, drill logs.
**Target:** Verified class of each candidate and, for utilities, horizontal and vertical offset between the pick and the exposed position; secondary target: agreement with the senior interpreter.
**Evaluation metric:** Recall on verified hazardous classes (utilities in a designated corridor, munitions items) at a fixed false-positive budget, because a missed gas line or projectile is a safety event while a false call costs an excavation; calibration of the probability by site-condition bucket, measured on held-out sites, never held-out patches from the same site. Report against interpreter test-retest agreement on a re-shown sample as the realistic ceiling.
**Scope:** The data collection challenge is the hardest part: the interpreter's picks exist but their confidence and reasons do not, and verification records must be recovered from clients project by project and spatially matched to picks — a test hole six feet from a pick may be a miss or a different line. The labeling challenge is that only selected anomalies are dug, so negatives are under-sampled and biased toward easy calls, and interpreters disagree with themselves on marginal features, so a repeated-annotation sample is needed to estimate intra-rater reliability. The deployment challenge is speed and liability: the model must rank candidates on a field tablet faster than the interpreter scans the data, and must explain itself, because the signer owns any miss. A firm or platform with 2 ML engineers and 1 senior geophysicist, 9–12 months, starting with retrieval of similar verified examples before any classifier is trusted; transfer learning from synthetic GPR (gprMax-style forward models) helps with scarce classes.
**Data availability:** Raw data and picks sit on each firm's servers. Verification is richest where rules require it: munitions response digs every item above threshold and logs it, SERDP/ESTCP demonstration reports publish some labelled sites, and SUE projects record QL-A results. Utility and concrete outcomes elsewhere must be collected prospectively.

---

## 2. Live Coverage and Sensor-Quality Monitoring
#change-point-detection #gaussian-processes #evaluation-metrics #feature-engineering #automation #quick-win

**Problem statement:** Detect, while the crew is on site, the coverage gaps, positioning failures and sensor drift that would fail the project's quality plan, instead of finding them during overnight processing.

**ML task:** Streaming change-point and anomaly detection on sensor and GNSS time series, plus spatial coverage estimation with uncertainty
**Input data:** Raw sensor streams (EM channels, magnetometer readings, GPR trace energy), GNSS fix quality and positions, sensor geometry, the planned grid and the quality plan's tolerances; historical surveys with the QC geophysicist's accept/reject decisions.
**Target:** Per-segment flags for drift, spikes, dropouts and lift-off; a coverage map with confidence; a predicted pass/fail against each quality objective.
**Evaluation metric:** Recall on segments the QC geophysicist later rejected, at a false-alarm rate low enough that crews do not mute alerts — measured in alerts per field hour. Time-to-flag after the defect begins is the operational metric.
**Scope:** Mostly signal processing and rules, with learned components for drift and lift-off. 1–2 engineers, 4–6 months per instrument family; the hard part is reading proprietary logger formats in real time.
**Data availability:** Every firm holds years of raw streams and its QC rejections in processing notes; instrument vendors hold format specifications.

---

## 3. Landowner Permit Outcome Prediction
#gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #revenue-impact #workflow-orchestration

**Problem statement:** Before a seismic survey is laid out, predict which tracts are likely to refuse access, attach costly conditions or generate damage claims, so the design and the permit effort start where the risk is.

**ML task:** Tract-level multi-class classification (grant / conditional / refuse) and a damage-claim probability
**Input data:** Historical permit outcomes and conditions by tract from prior programs; parcel attributes (ownership type, size, absentee owner, land use, improvements near lines); prior seismic activity in the area; permit fee offered; agent visit logs.
**Target:** Permit outcome and condition class per tract; claim/no-claim after recording.
**Evaluation metric:** AUC and calibration of refusal probability, judged by how much of the eventual no-permit area falls in the top risk decile; precision matters less than early warning, because a late refusal forces redesign after the crew is mobilised.
**Scope:** Modest modelling on small, messy tables. 1 data scientist, 3 months, once two or three programs of permit records are digitised; transfer between basins is weak.
**Data availability:** Permit records exist in spreadsheets at permit-agent firms and seismic contractors; parcel data is public through county records and commercial parcel layers.

---

## 4. Lane-Exposure Planning and Work-Zone Intrusion Warning
#cnns #object-detection #gradient-boosting #optimization-fundamentals #evaluation-metrics #worker-facing

**Problem statement:** Cut the hours utility designating technicians spend on foot in live lanes by predicting, before mobilisation, which corridor segments can be designated from the shoulder, which need a crossing and which justify a closure — and warn a technician when a vehicle enters the moving work zone.

**ML task:** Segment-level multi-class classification (shoulder / crossing / closure needed) feeding a schedule optimisation over permitted closure windows; plus real-time object detection and trajectory classification of vehicles from a truck-mounted camera
**Input data:** Utility records and QL-D/QL-C layers, corridor geometry (lanes, medians, intersections), traffic volumes and speed limits, aerial imagery, and past projects' field logs of where crews actually had to enter lanes; for intrusion, video from truck-mounted cameras with labelled intrusion events and near-misses.
**Target:** Access class and planned exposure hours per segment; per-frame intrusion probability with estimated time to contact.
**Evaluation metric:** For planning, predicted versus actual lane-exposure hours per corridor. For intrusion, recall on true intrusions at a false-alarm rate low enough that technicians do not learn to ignore the wearable — measured in false alerts per shift — with latency that leaves several seconds of warning. A missed intrusion is the costly error; a false alert costs attention, which is why the false-alarm budget is set with the crews.
**Scope:** The planning model is modest: 1 data scientist, 3–4 months once a firm's field logs record lane entries. Intrusion detection adapts existing vehicle-detection models; the hard part is false alarms from ordinary passing traffic on curved shoulders and at night, which needs field pilots. 1–2 engineers, about 6 months. Work-zone intrusion alarms exist for fixed highway construction zones (estimate); the gap is a two-person zone that moves every few minutes.
**Data availability:** Records and corridor geometry are available from DOTs and the project's own QL-D/QL-C work; lane-entry logs must be captured prospectively; intrusion video must be collected on working crews, and true intrusions are rare, so near-misses and staged events supplement them.

---

## 5. Report Drafting From Project Records
#large-language-models #transformers #feature-engineering #evaluation-metrics #worker-facing #automation

**Problem statement:** Draft the methods, QC, results and limitations sections of a geophysical report, plus the anomaly table, from the project's own logs, settings, QC results and picks.

**ML task:** Retrieval-grounded text generation with structured-data-to-text for tables, and claim-level citation to source records
**Input data:** Field logs, instrument settings, QC outputs, processed grids and picks, prior signed reports as style and content examples, the client's report template.
**Target:** Draft sections and tables with every factual statement linked to a source record.
**Evaluation metric:** Edit distance between draft and signed version, and zero unsupported statements — a fabricated depth or method in a signed report is worse than a blank paragraph. Hours from data freeze to signed report.
**Scope:** 1–2 engineers, 3–4 months for one firm's report family; the value depends on clean project records, which items 1 and 2 also build.
**Data availability:** Each firm has hundreds of prior reports and their source files; no external data needed.
