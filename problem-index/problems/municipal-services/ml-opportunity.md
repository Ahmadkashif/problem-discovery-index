# Machine Learning Opportunities — Municipal Services

**Industry:** [[municipal-services|Municipal Services]]
**Derived from:** [[problems/municipal-services/high-impact|High Impact]], [[problems/municipal-services/low-impact-1|Low Impact 1]], [[problems/municipal-services/low-impact-2|Low Impact 2]], [[problems/municipal-services/worker-life-1|Worker Life 1]], [[problems/municipal-services/worker-life-2|Worker Life 2]]

---

## 1. Infrastructure Failure Prediction from Tacit Expert Knowledge
#cnn #gradient-boosting #anomaly-detection #computer-vision #tabular-ml #tacit-knowledge-ml

**Problem statement:** Senior public works supervisors have internalized 20-30 years of pattern recognition — they can visually assess pavement crack morphology, audibly evaluate hydrant flow rates, and visually predict tree failure risk in ways they cannot fully articulate or transfer to new hires. This tacit knowledge must be captured as training signal for models that fuse street-level imagery with asset management data to predict infrastructure failure timelines.

**ML task:** Multi-modal prediction — CNN-based image scoring (pavement distress index, vegetation risk, drainage condition) combined with gradient-boosted tabular regression for time-to-failure prediction across asset classes (roads, water mains, sewer lines, trees, sidewalks).

**Input data:** (1) Street-level imagery from vehicle-mounted cameras during routine supervisor drives — continuous video segmented into geo-tagged frames every 5 meters. (2) Tabular asset data: pipe material, installation year, diameter, soil type, traffic count, utility cut count, last repair date, freeze-thaw cycles per year, water pressure readings, complaint history. (3) Expert labels: supervisors annotate a ride-along dataset by flagging assets they would prioritize and rating severity on a 1-5 scale.

**Target:** Per-asset failure probability over 6, 12, and 24-month horizons. Secondary target: predicted repair cost category (routine maintenance, structural repair, full replacement) to support budget prioritization.

**Evaluation metric:** Precision@K for the top-K assets recommended for maintenance (K = budget-constrained list size). Secondary: Spearman rank correlation between model priority ranking and expert consensus ranking on a held-out district. Recall matters more than precision for safety-critical assets (water mains, bridges) — a missed failure is catastrophic, a false alarm is just an unnecessary inspection.

**Scope:** 12-18 month build. Phase 1 (months 1-6): instrument 5-10 supervisor vehicles with dashcams, build annotation tool, collect 10,000+ labeled image segments across pavement, drainage, and vegetation. Phase 2 (months 6-12): train CNN feature extractor on image data, build tabular model on asset database, fuse into ensemble. Phase 3 (months 12-18): deploy as tablet overlay for field use, validate against one winter cycle of actual failures. Requires 2-3 ML engineers, 1 data engineer, and dedicated time from 3-5 senior supervisors for labeling. The labeling challenge is the hardest part: experts disagree with each other (inter-annotator agreement is typically 70-80% on severity ratings) and even with themselves on re-evaluation (intra-annotator agreement ~85%). Consensus protocols (majority vote of 3+ experts, calibration sessions) are essential. Deployment must be faster than the expert's own windshield survey to achieve adoption — if the tablet slows down the drive-through, supervisors will ignore it.

**Data availability:** Imagery must be collected fresh (no public dataset matches the resolution, angle, and asset diversity needed). Tabular asset data exists in CityWorks/Tyler/GIS but is often incomplete — pipe age may be "pre-1950" for 30% of the network. Historical work order data (5-10 years) is available in most municipalities and provides ground-truth failure events. The expert labeling is the bottleneck: budget 200-300 hours of senior supervisor time across the project.

---

## 2. 311 Request Classification and Priority Scoring
#bert #text-classification #nlp #workflow-orchestration

**Problem statement:** Citizen service requests arrive as unstructured text (call transcripts, web form narratives, emails) with unreliable self-categorization. Requests must be classified into the correct department and assigned a priority score that reflects urgency, safety risk, and operational efficiency.

**ML task:** Hierarchical text classification (department → sub-category → priority) with a safety-critical escalation detector.

**Input data:** Historical 311 records with free-text descriptions, assigned department, resolution code, and response time. Typical municipality has 50,000-200,000 records over 5 years. Supplementary: GIS coordinates, repeat-request flags, time-of-year patterns.

**Target:** (1) Department assignment (10-20 classes depending on municipality). (2) Sub-category within department (50-100 classes). (3) Priority score (1-5). (4) Binary safety escalation flag (gas leak, water main break, downed power line, sinkhole).

**Evaluation metric:** Macro F1 for department classification (must perform well on rare but critical categories like gas leaks, not just high-volume categories like potholes). Precision on safety escalation flag must exceed 95% — false negatives are unacceptable. Priority score: mean absolute error against reviewer-assigned priority.

**Scope:** 3-4 month build for a single municipality. Fine-tune a pre-trained BERT model on the municipality's historical 311 data. Requires 1 ML engineer and 1 domain expert (311 supervisor) for label validation. The model must be retrained or fine-tuned for each municipality due to local taxonomy differences — this is a deployment-per-city model, not a universal one. Multilingual support (Spanish minimum, additional languages depending on demographics) adds 1-2 months.

**Data availability:** Excellent. Most municipalities with digital 311 systems have 5+ years of labeled data. The labels (department assignment, resolution code) are operational byproducts — no additional annotation needed. Quality varies: some records have sparse descriptions ("pothole"), others are paragraphs. A 90/10 train/test split on historical data with temporal validation (train on years 1-4, test on year 5) is the right setup.

---

## 3. Water Main Break Prediction
#gradient-boosting #time-series-forecasting #anomaly-detection #tabular-ml

**Problem statement:** Water main breaks cost US municipalities $2.6B annually in emergency repairs and cause cascading damage (road collapse, property flooding, boil-water advisories). Most municipalities replace mains reactively after failure rather than proactively based on risk, because the failure models that exist (age-based, material-based) are too coarse to prioritize the 5% of pipes that will actually fail next year out of a network where 30% are past nominal lifespan.

**ML task:** Binary classification (will this pipe segment fail within 12 months?) with calibrated probability outputs for ranking.

**Input data:** Pipe attributes (material, diameter, installation year, joint type, lining), soil characteristics (corrosivity, moisture, frost depth), operational data (pressure zone, flow velocity, transient events), historical break records (location, date, failure mode), nearby construction activity (utility cuts within 50 feet in past 5 years), climate data (freeze-thaw cycles, drought index, rainfall extremes), and complaint data (discolored water, low pressure reports near the segment).

**Target:** Probability of failure for each pipe segment within the next 12 months. Secondary: predicted failure mode (circumferential crack, longitudinal split, joint failure, corrosion hole) to inform repair vs. replace decisions.

**Evaluation metric:** AUC-ROC for the binary classifier. Operationally: precision@100 (of the top 100 pipes flagged, how many actually fail?) because municipalities can only proactively replace 50-200 segments per year. Cost-weighted recall is the true objective — missing a 24-inch transmission main break is 100x more consequential than missing a 6-inch distribution line crack.

**Scope:** 6-9 month build. Requires integration with the municipality's GIS and asset management system (CityWorks, ESRI, or equivalent). Historical break data going back 10+ years is essential — municipalities with fewer than 200 recorded breaks will have insufficient positive examples. Team: 2 ML engineers, 1 GIS/data engineer. The biggest risk is data quality: pipe age is unknown for 20-40% of segments in most systems, and failure records before digital adoption (pre-2005) may be incomplete.

**Data availability:** Moderate. Pipe attribute data exists in GIS but has gaps. Break records are available but may require cleaning (merging maintenance logs, emergency dispatch records, and insurance claims). Soil data is available from USDA SSURGO. Climate data is available from NOAA. The integration work — joining 6-8 data sources on spatial keys — is the real engineering challenge, not the modeling.

---

## 4. Proactive Code Violation Prediction
#gradient-boosting #binary-classification #tabular-ml #data-integration

**Problem statement:** Code enforcement is entirely complaint-driven in most municipalities — violations are discovered only when a neighbor calls. By the time a complaint triggers an inspection, a property may have accumulated $50,000+ in remediation needs (structural, environmental, health). Predicting which properties are likely to develop code violations before complaints arrive enables proactive outreach and early intervention.

**ML task:** Binary classification — will this property receive a code violation within the next 12 months?

**Input data:** Property attributes (age, assessed value, owner-occupied vs. rental, square footage), permit history (has the owner pulled permits for work, or is unpermitted work likely?), utility data (water shutoffs, abnormal consumption patterns suggesting vacancy or overcrowding), tax payment history (delinquency as a proxy for financial distress), previous violation history, 311 complaint density in the surrounding block, ownership transfer recency, and rental registration status.

**Target:** Probability of code violation within 12 months. Secondary: predicted violation type (structural, property maintenance, zoning, environmental) to route the right inspector.

**Evaluation metric:** AUC-ROC overall. Operationally: precision@200 (the number of proactive inspections a code enforcement team can add per quarter). Fairness constraint is critical — the model must not systematically over-target low-income or minority neighborhoods, which requires demographic parity auditing and potentially constrained optimization. This is a model where deployment without a fairness audit would be irresponsible.

**Scope:** 4-6 month build. Requires data integration across assessor records, permit system, utility billing, tax records, and violation history — typically 5 different databases with no shared key except parcel number (which may be formatted differently in each system). Team: 1 ML engineer, 1 data engineer, 1 policy advisor (for fairness review). Must include a bias audit before deployment and ongoing monitoring. The model should generate explanations (SHAP values) for each prediction so inspectors can justify proactive visits.

**Data availability:** All input data exists within municipal systems but is siloed. The data engineering to join assessor, utility, tax, and violation databases is 60% of the project effort. Violation records are typically available for 5-10 years. The positive class (violation) is relatively rare (~5% of parcels per year), so class imbalance handling is needed. Some municipalities may have privacy concerns about linking utility data to property data — legal review is required.
