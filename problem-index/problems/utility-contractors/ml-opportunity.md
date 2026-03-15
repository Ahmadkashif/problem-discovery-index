# Machine Learning Opportunities — Utility Contractors

**Industry:** [[utility-contractors|Utility Contractors]]
**Derived from:** [[problems/utility-contractors/high-impact|High Impact]], [[problems/utility-contractors/low-impact-1|Low Impact 1]], [[problems/utility-contractors/low-impact-2|Low Impact 2]], [[problems/utility-contractors/worker-life-1|Worker Life 1]], [[problems/utility-contractors/worker-life-2|Worker Life 2]]

---

## 1. Underground Utility Detection from GPR B-Scan Imagery
#cnn #object-detection #regression #signal-processing #tacit-knowledge-ml

**Problem statement:** GPR B-scan interpretation — identifying buried utility hyperbolic reflections and estimating depth — requires 2-3 years of supervised training to perform reliably. A CNN trained on labeled GPR B-scan data can identify and classify subsurface reflections to reduce utility strikes during excavation.

**ML task:** Object detection (hyperbola identification in B-scan imagery); regression (depth estimation from hyperbola geometry); classification (utility type from reflection characteristics: metal pipe, plastic pipe, cable, void)
**Input data:** GPR B-scan images with labeled hyperbolic reflections and confirmed utility identifications from excavation. GSSI, Mala, and large utility contractor GPR archives with ground-truth verification from subsequent excavation.
**Target:** Real-time overlay on GPR display showing detected utilities with depth estimates and confidence; flagged ambiguous areas requiring additional investigation
**Evaluation metric:** Recall on confirmed utility locations (strike prevention metric — must be high); precision on detections (false alarms require re-investigation); depth estimation accuracy vs. confirmed depths at excavation
**Scope:** GPR B-scan interpretation has active academic research and some existing commercial work. GSSI has a GPR AI product in development (as of 2025). The commercial opportunity is in integration with existing GPR hardware and utility contractor workflows. 12-18 months for production-quality model. Dataset assembly (GPR scans matched to excavation-confirmed utility locations) is the primary challenge — requires a utility contractor data partnership.
**Data availability:** Large utility contractors (Quanta, MYR Group) run thousands of GPR surveys per year. Excavation confirmation provides ground truth. Dataset assembly requires linking GPR scan files to excavation logs at the same location — tractable with systematic field documentation.

---

## 2. Gas Leak Indicator Detection from Patrol Photos
#cnn #binary-classification #computer-vision #tacit-knowledge-ml #quick-win

**Problem statement:** Detect above-grade gas migration visual indicators (dead vegetation patterns, surface anomalies) from patrol photos to guide combustible gas indicator deployment during leak detection surveys.

**ML task:** Binary classification — gas migration indicator present (yes/no) per patrol photo section
**Input data:** Patrol photos from leak locations (positive — gas migration patterns confirmed by subsequent leak detection) and patrol photos from clean sections (negative). Labeled by experienced gas distribution technicians.
**Target:** Photo flag indicating potential gas migration indicator with bounding box; patrol location for instrument follow-up
**Evaluation metric:** Recall on photos taken at confirmed leak locations (did we flag the visual indicator?); false positive rate on clean patrol sections; improvement in instrument deployment targeting for technicians using photo screening vs. unaided patrol
**Scope:** Quick win relative to GPR — the classification is binary, patrol photos are easily captured, and the visual patterns (dead vegetation, soil disturbance) are discernible in standard phone photos. A CNN fine-tuned on labeled patrol photos: 8-12 week project with sufficient labeled data (500-1,000 positive examples per indicator type). Data collection requires systematic photo capture at confirmed leak locations — a prospective program.
**Data availability:** Gas distribution contractors performing PHMSA-required leak detection surveys have patrol routes and leak location records. Positive training examples come from confirmed leak locations with associated patrol photos. Collection requires a 6-12 month prospective data gathering program.

---

## 3. CCTV Pipe Inspection Defect Coding (PACP/MACP Automation)
#cnn #object-detection #semantic-segmentation #computer-vision

**Problem statement:** Automate NASSCO PACP/MACP condition coding from CCTV footage to reduce the labor intensity of large utility pipe inspection programs.

**ML task:** Multi-label object detection per video frame — PACP defect code classification (root intrusion grade, crack type/severity, deformation, infiltration, deposits) with per-frame and per-footage-position output
**Input data:** CCTV inspection footage with PACP codes assigned by certified technicians. WinCan and Envirosight have labeled datasets from their existing AI products for municipal pipe diameters (6"-24"+).
**Target:** Per-frame PACP code assignment with confidence; aggregated condition report by footage position; comparison to NASSCO PACP report format
**Evaluation metric:** Code agreement rate with certified human coder on held-out footage; false negative rate on structural defects requiring repair; PACP agreement rate between model and certified reviewer
**Scope:** WinCan AI and Envirosight AI Assist already provide commercial versions of this product for municipal pipe diameters. The opportunity for utility contractors is in asset management integration and report customization (the gap identified in low-impact-1). Custom integration development: 4-8 weeks per utility owner's system requirements.
**Data availability:** WinCan and Envirosight have large labeled datasets and existing models. The integration and customization layer is the remaining work, not the model development.

---

## 4. Project Ground Condition Risk Assessment
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Predict which utility construction projects are at elevated risk of encountering unforeseen ground conditions (rock, unexpected utility congestion, groundwater) that will require scope changes and erode fixed-price contract margin.

**ML task:** Binary classification (significant unforeseen ground condition encountered: yes/no) from project pre-bid features; regression (magnitude of scope change cost)
**Input data:** Project records with bid type, location geology (from geologic survey maps by county), soil boring data (if available in the project specs), utility congestion estimate (from 811 locate ticket density), pipeline material (affects trench difficulty), and actual scope change costs per project
**Target:** Risk score per project at bid time; specific risk factor flags (high rock probability from geology, congested corridor from locate density, high water table from drainage features)
**Evaluation metric:** AUC on projects with significant scope changes vs. clean projects; recall on high-cost scope changes; improvement in bid margin for projects using risk-adjusted bidding vs. standard approach
**Scope:** Any utility contractor with 100+ completed project records with scope change cost tracking has training data. Gradient boosting on 8-12 project features: 3-4 week modeling project. The feature engineering (geology data integration, locate ticket density by corridor) is the primary technical work.
**Data availability:** Geologic survey data is publicly available (USGS). Locate ticket density can be estimated from 811 call center data (available in some states). Project scope change costs are in the contractor's ERP system.

---

## 5. Cathodic Protection System Anomaly Detection
#isolation-forest #anomaly-detection #time-series-forecasting #signal-processing

**Problem statement:** Cathodic protection (CP) systems on buried metal pipelines require periodic voltage and current measurement surveys. Detecting when a CP system's readings indicate inadequate protection — before the pipeline segment corrodes through — is a safety and regulatory compliance requirement.

**ML task:** Anomaly detection on cathodic protection measurement time series; binary classification (CP system providing adequate protection: yes/no based on PHMSA protection criteria)
**Input data:** CP survey measurement records (pipe-to-soil potential readings by measurement station) with timestamps, measurement equipment, and weather conditions. PHMSA protection criterion (typically -850 mV vs. Cu/CuSO4 reference) provides the classification threshold.
**Target:** Anomaly flag when a measurement station reading falls below protection criterion; trend alert when readings show degrading trajectory before the threshold is breached; rectifier fault identification from measurement pattern
**Evaluation metric:** Recall on CP failures that resulted in pipeline defects (did the model flag the location before the defect was found?); lead time between anomaly flag and confirmed protection failure; false positive rate
**Scope:** Cathodic protection records exist for every regulated natural gas distribution system. PHMSA requires documentation of CP survey records. Any gas distribution utility or contractor with 3+ years of CP survey records has sufficient data. Statistical anomaly detection on time-series measurement data: 3-4 week project.
**Data availability:** PHMSA-regulated operators maintain CP survey records by regulation. These records are in the operator's O&M records — available but often in paper or PDF format requiring digitization.
