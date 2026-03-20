# ML Opportunities — Metal Fabrication

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Tags:** #cnns #gradient-boosting #gaussian-processes #object-detection #transfer-learning #linear-regression #loss-functions #backpropagation #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact #compliance

---

## 1. Weld Quality Visual Inspection (Primary Opportunity — Tacit Knowledge ML)

**ML Task:** Object detection + multiclass classification (defect type: porosity / undercut / overlap / crack / lack-of-fusion / acceptable)
**Input data:** Weld surface images captured under controlled LED illumination; CWI-annotated labels with defect type, bounding box, and accept/reject disposition per AWS D1.1 or applicable standard; reference images of known-acceptable welds per joint type
**Target:** Binary accept/reject per weld + defect type multiclass for rejects; dimensional severity estimate relative to acceptance threshold
**Model:** Fine-tuned CNN (EfficientDet for detection, EfficientNet for classification); PatchCore anomaly detection for initial deployment on new joint types with limited labeled data
**Evaluation:** Recall on rejectable defects vs. CWI ground truth (miss rate); false reject rate; agreement rate with CWI on borderline indications; comparison to inspector-to-inspector agreement rate on the same samples
**Scope:** Inspection station with controlled illumination; real-time inference per weld pass (under 5 seconds); borderline cases queued for CWI review
**Data availability:** Requires structured image capture program at inspection station; 2,000-5,000 labeled images per defect category for fine-tuning; CWI annotation time is the primary data cost

---

## 2. Fabrication Quote Labor Estimation

**ML Task:** Regression (labor hours by operation: setup / fit-up / weld / post-weld / inspection)
**Input data:** Historical job records — drawing features extracted from DXF/DWG files (linear weld length by joint type, material thickness, part count, joint count, tight-tolerance feature count), actual vs. quoted labor hours per operation
**Target:** Actual labor hours per operation type (separate models for setup, fit-up, weld-out, distortion correction, inspection)
**Model:** Gradient boosting regression; drawing feature extraction from DXF geometry analysis
**Evaluation:** MAE of labor hour prediction vs. actuals on held-out jobs; reduction in systematic quote error rate by job type
**Scope:** Quote workflow integration; one estimate per quote with itemized operation breakdown
**Data availability:** Job shop ERP (JobBOSS, Prodsmart) actuals; requires 2+ years of job history with actual vs. quoted labor tracking; DXF file library for training feature extraction

---

## 3. Weld Distortion Prediction and Pre-Compensation

**ML Task:** Regression (distortion magnitude and direction per assembly zone)
**Input data:** Assembly geometric features (plate thickness, joint type distribution, weld sequence, restraint configuration), material properties (modulus, yield strength by material grade), welding parameters (heat input per pass, preheat temperature, interpass temperature); historical distortion measurement records or FEA simulation outputs
**Target:** Distortion magnitude (angular and linear) per assembly zone after welding sequence
**Model:** Gradient boosting on assembly feature set; Gaussian process for uncertainty quantification and pre-compensation angle recommendation
**Evaluation:** MAE between predicted and measured distortion; reduction in post-weld straightening rework rate
**Scope:** Pre-job planning tool; one prediction per new assembly type with recommended pre-compensation setup
**Data availability:** FEA simulation outputs (Simufact, ANSYS) across assembly parameter space as surrogate training data; supplemented by production distortion measurement records

---

## 4. Press Brake Springback Compensation

**ML Task:** Regression (overbend angle for target achieved angle)
**Input data:** Historical press brake setup records — material grade, temper, thickness, die opening width, punch radius, target angle, overbend angle used, actual achieved angle measured; mill cert properties where available
**Target:** Overbend angle that achieves target angle within ±0.5° after springback
**Model:** Gradient boosting regression; Gaussian process for uncertainty quantification (critical: operator needs to know confidence range, not just point estimate)
**Evaluation:** Prediction error (predicted overbend vs. overbend that achieves target); reduction in test pieces required per setup
**Scope:** Press brake workstation tool; operator-facing app with material selection and target angle input
**Data availability:** Setup log records from press brake operators; requires systematic logging of actual achieved angles (currently done manually or not at all)

---

## 5. Remnant Inventory Matching and Material Procurement Optimization

**ML Task:** Ranking (remnant-to-job matching) + regression (material waste prediction for quote)
**Input data:** Nesting software output files (part dimensions, material spec, sheet utilization, offcut dimensions); job schedule (upcoming jobs with material requirements); historical remnant reuse records
**Target:** Ranked list of remnant-job matches by material savings; material waste prediction per job type for quote material cost estimation
**Model:** Rule-based matching with gradient boosting ranking for prioritization; regression for waste prediction
**Evaluation:** Percentage of remnant material reused vs. scrapped; quote material cost accuracy vs. actuals
**Scope:** Daily batch matching run for remnant inventory vs. upcoming job queue; integrated with ProNest/Sigmanest workflow
**Data availability:** Nesting software output files; ERP job records; remnant inventory log (may require new data capture process)
