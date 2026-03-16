# Machine Learning Opportunities — Oil & Gas Field Services

**Industry:** [[oil-gas-field-services|Oil & Gas Field Services]]
**Derived from:** [[problems/oil-gas-field-services/high-impact|High Impact]], [[problems/oil-gas-field-services/low-impact-1|Low Impact 1]], [[problems/oil-gas-field-services/low-impact-2|Low Impact 2]], [[problems/oil-gas-field-services/worker-life-1|Worker Life 1]], [[problems/oil-gas-field-services/worker-life-2|Worker Life 2]]

---

## 1. Equipment Condition Classification from Multi-Modal Field Observations
#lstm #cnn #anomaly-detection #signal-processing #computer-vision #tacit-knowledge-ml #revenue-impact

**Problem statement:** Veteran field technicians diagnose wellsite equipment health through integrated sensory observation — the sound of a rod pump gearbox, the color of produced fluid at the separator, the vibration feel of a wellhead, the smell near a casing vent — and make go/no-go decisions that prevent catastrophic failures. This tacit expertise must be encoded into a model that replicates multi-modal diagnosis at scale.

**ML task:** Multi-modal anomaly detection and multiclass classification (healthy / degraded / imminent failure, with sub-classification of failure mode: rod part, ESP burnout, gearbox failure, stuffing box leak, separator internals fouling, compressor valve wear).

**Input data:** Time-series accelerometer data (vibration spectra, 1-10 kHz sampling), audio recordings from wellsite microphones (ambient + contact microphones on equipment housings), images/video of produced fluid at separator sight glass and equipment visual condition, plus contextual metadata (well age, last workover date, pump type, run time hours, current production rate from SCADA).

**Target:** Equipment health state label (3-class: healthy / degraded / imminent failure) with failure mode sub-label (8-10 failure types). Secondary target: estimated days to failure (regression). Ground truth is established retrospectively from workover reports confirming what actually failed and when.

**Evaluation metric:** Recall at 90%+ for imminent failure class (missing a failure is far more costly than a false alarm). Secondary: mean absolute error on days-to-failure regression, targeting +/- 3 days. False alarm rate must stay below 15% to maintain tech trust.

**Scope:** This is a 12-18 month build for a team of 3-4 ML engineers plus 1-2 oilfield domain experts. The first 4-6 months are dominated by data collection: instrumenting 50-100 wellsites with sensor arrays while simultaneously having veteran techs annotate their observations in real time using a structured mobile app. Model development begins with single-modality baselines (vibration-only, audio-only, vision-only) before fusing into a multi-modal architecture. Edge deployment on solar-powered compute (NVIDIA Jetson class) with satellite uplink requires aggressive model compression. Initial deployment targets a single basin (e.g., Permian) with expansion after validation.

**Data availability:** Vibration and SCADA data are abundant (most operators already collect this, though not at the sampling rates needed for ML). Audio data is almost nonexistent — must be collected from scratch. Visual fluid data is new — no existing datasets of separator sight glass images labeled with water cut or condition. The critical bottleneck is expert annotation: you need experienced techs willing to verbalize and label their observations over months of normal operations. Workover records (ground truth) exist in operator databases but are often unstructured text requiring NER extraction. Expect 6+ months of data collection before training begins.

---

## 2. Production Decline Curve Forecasting with Equipment Health Integration
#gradient-boosting #lstm #time-series-forecasting #tabular-ml

**Problem statement:** Standard decline curve analysis (DCA) treats production decline as a purely geological phenomenon, but in practice 20-40% of production shortfall is caused by equipment degradation (pump wear, scale buildup, paraffin accumulation) that is correctable with timely intervention. A model that separates equipment-driven decline from reservoir-driven decline would identify which wells have recoverable production.

**ML task:** Time-series forecasting with causal attribution — predict daily production rate and decompose forecast into geological component vs. equipment component.

**Input data:** Daily production data (oil, gas, water volumes), SCADA telemetry (casing pressure, tubing pressure, pump speed, motor amps), workover history, chemical treatment logs, completion design parameters, and equipment health scores from Opportunity #1 if available.

**Target:** Next-30-day production trajectory (regression). Secondary: binary flag for "equipment intervention would recover >10% production" with estimated recovery volume.

**Evaluation metric:** MAPE (mean absolute percentage error) on 30-day production forecast, targeting <8%. For the intervention flag: precision >80% (operators will not pull equipment on false positives that cost $50K+ each).

**Scope:** 6-9 month build for 2-3 ML engineers with petroleum engineering consultation. Training data is relatively accessible from production accounting databases. The main challenge is separating equipment effects from reservoir effects, which requires wells where equipment was replaced and production recovered as positive examples. A gradient boosting model on tabular features is the likely starting point, with LSTM for the temporal component.

**Data availability:** Production data is universally available (operators are required to report it). SCADA telemetry is available for ~60% of wells. Workover records are available but often unstructured. The key gap is labeled examples of "equipment-driven decline" vs. "reservoir-driven decline" — this requires retrospective analysis of wells where a workover restored production, providing implicit labels.

---

## 3. Chemical Treatment Optimization for Well Maintenance
#gaussian-process #bayesian-network #regression #tabular-ml

**Problem statement:** Field service companies apply chemical treatments (corrosion inhibitors, scale inhibitors, paraffin solvents, biocides, demulsifiers) to wells on fixed schedules or in response to visible problems. Treatment dosages and frequencies are set by chemical vendor recommendations and field tech judgment, but the actual optimal regime depends on well-specific conditions (water chemistry, temperature, flow rate, bacterial load) that change over time. Over-treatment wastes $2,000-$10,000/well/year in chemicals; under-treatment causes equipment failures and production loss.

**ML task:** Regression — predict optimal chemical treatment type, dosage, and frequency for each well given its current operating conditions.

**Input data:** Historical chemical treatment logs (product, volume, frequency), water analysis results (pH, TDS, chlorides, iron, bacteria counts), production data trends, corrosion coupon readings, equipment failure history, well temperature and pressure profiles.

**Target:** Recommended treatment regime (chemical type, dosage in gallons, frequency in days) that minimizes combined cost of chemicals + equipment failures + production loss over a 90-day horizon.

**Evaluation metric:** Total cost reduction vs. current practice, measured in $/well/quarter. Target: 15-25% cost reduction. Secondary: corrosion rate and scale deposition rate must not increase.

**Scope:** 6-8 month build for 2 ML engineers plus a production chemist. Gaussian process regression handles the small-data-per-well challenge (typically 12-50 treatment events per well per year) with uncertainty quantification that is critical for avoiding under-treatment. Bayesian network models the causal relationships between treatment, water chemistry, and failure modes. Pilot on a 50-well cluster before scaling.

**Data availability:** Chemical treatment logs are maintained by service companies and chemical vendors. Water analysis data is collected quarterly for most wells but may not be digitized. Corrosion coupon data is sparse. The main gap is connecting treatment history to outcomes — this requires joining treatment logs with production data and failure records across different databases that are rarely linked.

---

## 4. Environmental Compliance Anomaly Detection from Field Data Streams
#isolation-forest #gradient-boosting #anomaly-detection #tabular-ml #compliance

**Problem statement:** Regulatory violations in oilfield operations — unreported spills, excessive flaring, methane emissions above permit limits, produced water disposal irregularities — often originate from field-level events that are visible in operational data but not flagged by current threshold-based monitoring. By the time a violation is discovered during an inspection, penalties have compounded and remediation costs have escalated.

**ML task:** Anomaly detection — identify operational patterns that precede or indicate a regulatory violation, ranked by severity and urgency of required response.

**Input data:** SCADA telemetry (tank levels, flow rates, flare volumes, casing pressures), field ticket narratives (NLP-extracted events), weather data (rainfall triggering spill risk, wind affecting emissions dispersion), satellite methane detection data (where available), truck ticket volumes for produced water disposal, and historical violation records from state commission databases.

**Target:** Anomaly score per wellsite per day, with classification into violation type (spill, emissions, disposal, mechanical integrity). Ground truth from historical inspection results and self-reported violations.

**Evaluation metric:** Recall >85% for violations that resulted in fines >$10,000 (must not miss serious violations). Precision >60% to keep alert volume manageable. Lead time: anomaly should be detectable >48 hours before it would be discovered by conventional means.

**Scope:** 8-10 month build for 2-3 ML engineers plus a regulatory specialist. Isolation forest for unsupervised anomaly detection on telemetry data, gradient boosting for supervised classification where historical violation data exists. Requires access to state commission violation databases (public records) and operator SCADA historians. The NLP component for extracting events from field ticket narratives adds complexity but is critical for detecting human-observed anomalies that do not appear in telemetry.

**Data availability:** SCADA data is abundant. State commission violation records are public but require scraping and normalization across different state systems. Satellite methane data is becoming available through EPA's GHGRP and commercial providers (Kairos, GHGSat). The main challenge is the low base rate of violations — even a large operator may have only 50-100 recordable violations per year, requiring careful handling of class imbalance.

---

## 5. Crew Route and Dispatch Optimization with Dynamic Re-Routing
#gradient-boosting #reinforcement-learning #regression #tabular-ml

**Problem statement:** Dispatchers assign field crews to wellsites using manual judgment, resulting in 30-40% excess driving miles, chronic schedule unpredictability for techs, and suboptimal allocation of specialized skills to the jobs that need them. When emergency calls come in mid-day, the entire schedule is disrupted because re-optimization is done by gut feel.

**ML task:** Sequential decision optimization — given a queue of jobs with varying priority, location, skill requirements, and time windows, assign techs to jobs and sequence routes to minimize total travel time while meeting all service deadlines. Re-optimize in real time as new jobs arrive.

**Input data:** Job queue (location, estimated duration, required certifications, priority, deadline), tech roster (current location via GPS, certifications, remaining hours in shift, fatigue score based on hours driven), road network and travel times (accounting for lease road conditions and seasonal access), historical job duration data by type and tech experience level.

**Target:** Optimized assignment and route sequence for each tech, updated every 15 minutes as conditions change. Secondary: predicted job completion time for customer communication.

**Evaluation metric:** Total fleet miles driven per day (target: 25-35% reduction). Schedule adherence (% of jobs completed within promised window, target: >85%). Tech workload variance (standard deviation of daily hours across techs, target: reduce by 40%). Customer-facing: predicted vs. actual arrival time MAE <20 minutes.

**Scope:** 6-9 month build for 2 ML engineers plus an operations researcher. The core is a vehicle routing problem (VRP) variant with time windows and skill constraints, solvable with gradient boosting for travel time prediction + reinforcement learning for dynamic re-routing as emergency jobs arrive. Requires integration with fleet GPS systems and the dispatch platform. Pilot with a single district (20-30 trucks) before scaling. The reinforcement learning component for dynamic re-routing is the most technically challenging piece and may require 3-4 months of simulation-based training.

**Data availability:** GPS tracking data is available from fleet management systems (most service companies already run Samsara, Geotab, or similar). Historical job data with durations and locations is in dispatch systems. Road network data is available via mapping APIs but must be supplemented with lease road conditions that are not in standard maps. The main data gap is lease road accessibility — some roads are impassable after rain, and this is currently tracked only in tech's heads.
