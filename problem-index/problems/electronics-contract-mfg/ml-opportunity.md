# Machine Learning Opportunities — Electronics Contract Manufacturing

**Industry:** [[electronics-contract-mfg|Electronics Contract Manufacturing]]
**Derived from:** [[problems/electronics-contract-mfg/high-impact|High Impact]], [[problems/electronics-contract-mfg/low-impact-1|Low Impact 1]], [[problems/electronics-contract-mfg/low-impact-2|Low Impact 2]], [[problems/electronics-contract-mfg/worker-life-1|Worker Life 1]], [[problems/electronics-contract-mfg/worker-life-2|Worker Life 2]]

---

## 1. Solder Joint Quality Classification from AOI Images
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** AOI (Automated Optical Inspection) systems flag solder joints as potential defects, but experienced AOI operators know that 30-60% of flags are false calls — the system triggers on joints that an experienced inspector recognizes as acceptable based on visual patterns the AOI algorithm doesn't understand. These operators develop a calibrated eye for the visual signatures of acceptable vs. genuinely defective joints that reduces false call rate and prevents unnecessary rework on boards that are actually good.

**ML task:** Multiclass classification of solder joint images (classes: acceptable, insufficient solder, excess solder, bridging, cold joint, tombstone, head-in-pillow, voiding, misalignment)
**Input data:** High-resolution AOI images of solder joints flagged by the primary AOI system; operator disposition labels (accept/reject with defect type); 3D SPI (Solder Paste Inspection) data from Koh Young or equivalent for solder volume correlation; component package type and pad geometry metadata
**Target:** Defect type classification with confidence score; binary accept/reject recommendation for each flagged joint; false call identification (joints flagged by AOI but classified as acceptable by the model)
**Evaluation metric:** Recall on genuinely defective joints (miss rate); false call reduction rate (percentage of AOI false flags correctly identified as acceptable); agreement rate with experienced AOI operators on borderline cases
**Scope:** Per-facility model training using AOI operator disposition history. Requires 5,000-10,000 labeled AOI images per defect category. 8-12 week project. Integration with existing AOI review workflow — model recommendation displayed alongside AOI image for operator verification.
**Data availability:** AOI systems generate and store flagged images with operator dispositions — this data exists at every ECM running AOI. The labeling is already done by operators during production. Key challenge: operator labeling quality varies; a calibration exercise with experienced operators is needed to establish ground truth labels.

---

## 2. Reflow Profile Optimization for New BOMs
#gaussian-process #regression #tabular-ml

**Problem statement:** Selecting the optimal reflow profile for a new PCBA requires understanding how the BOM's thermal mass distribution, component thermal sensitivities, and board characteristics interact with the reflow oven's zone temperatures. Experienced process engineers estimate starting profiles from intuition; a model trained on historical BOM-to-profile mappings can predict optimal starting parameters with uncertainty estimates.

**ML task:** Regression (predict zone temperatures, ramp rates, soak time, peak temperature, and time above liquidus for each reflow zone) given BOM and board characteristics
**Input data:** BOM characteristics (component count by package type, thermal mass estimates by board zone, moisture sensitivity levels, maximum reflow temperature ratings); board specifications (dimensions, layer count, copper weight, thickness); historical programs' final stable reflow profiles correlated with their BOM characteristics and yield outcomes
**Target:** Recommended reflow profile (zone-by-zone temperature setpoints) with uncertainty bands per zone; predicted first-pass yield at recommended profile
**Evaluation metric:** Profile prediction accuracy (MAE per zone vs. final empirically tuned profile); first-pass yield improvement vs. engineer-estimated starting profile; reduction in tuning iterations to reach stable yield
**Scope:** Requires 50-100 historical NPI programs with complete BOM characteristics and final stable reflow profiles. Gaussian process model for uncertainty quantification (critical: the engineer needs to know where the prediction is confident vs. uncertain). 8-10 week project. Facility-specific model (different ovens, different thermal behavior).
**Data availability:** Historical reflow profiles are logged in MES. BOM data is in ERP. The challenge is correlating BOM thermal characteristics with reflow outcomes — this mapping is rarely captured explicitly and must be derived from BOM component data and thermal simulation or empirical measurement.

---

## 3. Component Placement Defect Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** Certain component/pad/feeder combinations produce higher defect rates than others due to interactions between component packaging (tape pocket shape, cover tape peel characteristics), placement machine nozzle selection, feeder condition, and pad geometry. Predicting which placements on a new program are high-risk enables targeted AOI attention and proactive process parameter adjustment.

**ML task:** Binary classification (placement defect probability above threshold: yes/no) per component placement on a BOM
**Input data:** Component package type, feeder type and age, nozzle type, placement speed, pad geometry (from Gerber data), historical defect rates for the same component/feeder/nozzle combination across programs
**Target:** Per-placement defect probability; ranked list of high-risk placements for a new program
**Evaluation metric:** AUC-ROC on placement-level defect prediction; top-20 high-risk accuracy (do the model's top-20 flagged placements match the actual highest-defect placements during NPI?)
**Scope:** Requires placement-level defect data correlated with component/feeder/nozzle metadata. Many MES platforms capture this at the board level but not the individual placement level — data granularity is the constraint. 6-8 week project if placement-level data is available.
**Data availability:** AOI systems can provide defect-by-component data. Placement machine logs contain feeder/nozzle assignments. The join between AOI defect location and placement machine assignment is the data engineering challenge.

---

## 4. Incoming Component Counterfeit Detection
#cnn #binary-classification #computer-vision #compliance

**Problem statement:** Counterfeit electronic components — remarked, recycled, or cloned parts — enter the supply chain through unauthorized distributors and brokers. Visual and dimensional inspection by trained receiving inspectors can detect many counterfeits, but the assessment requires experience with the visual characteristics of genuine components from each manufacturer. A vision model trained on known-genuine reference images can flag suspect incoming components before they enter production.

**ML task:** Binary classification (genuine vs. suspect) from component package images; anomaly detection for novel counterfeit types not in training set
**Input data:** High-resolution images of component packages (top marking, lead/ball appearance, package dimensions, surface finish); reference images of known-genuine components from authorized distributors; dimensional measurements (package size, lead pitch, ball diameter); X-ray images for BGA ball patterns (if available)
**Target:** Genuine/suspect classification with confidence score; for suspect parts, which visual features triggered the flag (marking inconsistency, surface finish anomaly, dimensional deviation)
**Evaluation metric:** Recall on known counterfeits (miss rate must approach zero — a single counterfeit in a medical or aerospace product is catastrophic); false positive rate (target <5% to avoid excessive holds on genuine components from unfamiliar packaging runs)
**Scope:** Requires reference image library of genuine components from major manufacturers. SAE AS6171 provides the testing framework. 10-14 week project. Most critical for ECMs serving aerospace, defense, and medical customers where counterfeit risk has regulatory and safety implications.
**Data availability:** Known-counterfeit sample libraries exist at testing labs (e.g., SMT Corp, Integra Technologies) and industry consortia (GIDEP, ERAI). Genuine reference images can be built from authorized distributor inventory. Data access for counterfeit samples may require industry consortium participation.

---

## 5. Test Yield Root Cause Attribution
#gradient-boosting #multiclass-classification #tabular-ml

**Problem statement:** When ICT or FCT yield drops on a production program, the test engineer must identify whether the root cause is a component issue (specific lot), a process issue (reflow, placement, solder paste), or a test fixture/program issue (intermittent contact, marginal test limit). Attributing yield loss to the correct root cause currently requires manual cross-referencing of test failure patterns with process and component lot data.

**ML task:** Multiclass classification (failure root cause category: component defect, process defect, test artifact) per test failure type
**Input data:** Test failure logs (test step, measured value, limit, pass/fail); component lot traceability per board; SMT process parameters (SPI solder volume, AOI results, reflow profile adherence); test fixture maintenance history; historical failure patterns for the same test step across production runs
**Target:** Root cause category per failure type; for component-attributed failures, identified suspect component lot; for process-attributed failures, identified suspect process parameter
**Evaluation metric:** Root cause attribution accuracy vs. test engineer determination; time from yield drop detection to root cause identification (model should beat manual investigation time by 5-10x)
**Scope:** Requires test failure data with board-level traceability to component lots and process parameters. 8-10 week project. Most impactful on high-volume programs where yield issues accumulate quickly.
**Data availability:** Test failure data is logged by ICT/FCT systems. Component traceability is in MES/ERP. Process parameter data is in MES. The data exists; the challenge is building the board-level linkage between test failure, component lots, and process parameters.
