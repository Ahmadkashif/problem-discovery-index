# Machine Learning Opportunities — Chiropractic Practices

**Industry:** [[chiropractic-practices|Chiropractic Practices]]
**Derived from:** [[problems/chiropractic-practices/high-impact|High Impact]], [[problems/chiropractic-practices/low-impact-1|Low Impact 1]], [[problems/chiropractic-practices/low-impact-2|Low Impact 2]], [[problems/chiropractic-practices/worker-life-1|Worker Life 1]], [[problems/chiropractic-practices/worker-life-2|Worker Life 2]]

---

## 1. Postural Compensation Pattern Recognition from Standardized Photos
#cnn #gradient-boosting #multiclass-classification #computer-vision #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced chiropractors read compensatory biomechanical chains across the full kinetic chain — seeing how foot pronation drives pelvic tilt drives spinal curvature drives head position. This pattern recognition takes 10-15 years of clinical experience to develop and varies by technique system. Encoding this tacit knowledge into a computer vision model would make expert-level postural assessment available to every DC regardless of experience level.

**ML task:** Multi-label classification — identify primary postural deviations AND their compensatory relationships (which deviations are biomechanically linked as cause-and-effect chains)
**Input data:** Standardized postural photographs (anterior, posterior, left lateral, right lateral) taken with calibrated camera positioning. Patient demographics (age, sex, BMI, occupation). Chief complaint and symptom location. Optional: prior X-rays with measured Cobb angles and sagittal balance metrics.
**Target:** (1) Anatomical landmark positions and deviations from neutral (shoulder height difference, ASIS height difference, head forward translation in mm, thoracic kyphosis angle, lumbar lordosis angle, knee valgus/varus angle, foot pronation/supination degree). (2) Compensatory chain classification — which deviations are biomechanically related (e.g., "right foot pronation → right knee valgus → right pelvic drop → left lumbar lateral flexion → right thoracic lateral flexion → left shoulder elevation"). (3) Primary subluxation level prediction.
**Evaluation metric:** Landmark detection accuracy (mm error vs. expert annotation); compensatory chain agreement with expert panel (F1 score targeting 0.75+); subluxation level agreement with treating DC (top-3 accuracy targeting 0.80+). Note: inter-rater reliability among expert DCs is itself only 0.60-0.70, so the model's target is expert-panel consensus, not individual agreement.
**Scope:** Phase 1 (landmark detection): 500-1,000 patients with expert-annotated photos, 2-3 person team, 4-6 months. Phase 2 (compensatory chains): 2,000-5,000 patients with expert assessments from multiple technique backgrounds, paired with treatment outcomes, 3-4 person team, 6-9 months. Phase 3 (outcome correlation): 5,000+ completed treatment courses with pre/post postural data and validated outcome measures, 12-18 months.
**Data availability:** Postural photos are taken by many practices but not in standardized format. PostureScreen and PostureRay users have some digital postural data. The key challenge is obtaining expert compensatory chain annotations — this requires building a labeling panel of experienced DCs from multiple technique backgrounds and achieving consensus methodology. Existing datasets of postural assessment do not include compensatory chain analysis.

---

## 2. Treatment Outcome Prediction by Condition and Presentation
#gradient-boosting #regression #tabular-ml

**Problem statement:** Chiropractors set treatment plans based on experience and condition type, but cannot predict which patients will respond quickly (6-8 visits), which will require extended care (20+ visits), and which are unlikely to respond to chiropractic care at all. Accurate outcome prediction would reduce over-treatment, enable earlier referral for non-responders, and support insurance medical necessity documentation.

**ML task:** Regression — predict expected outcome score (ODI/NDI/PROMIS) at visits 6, 12, and 24
**Input data:** Patient demographics, condition type and chronicity, baseline outcome scores (ODI, NDI, PROMIS-29), initial postural assessment findings, comorbidities, prior treatment history, psychosocial factors (fear-avoidance beliefs, catastrophizing scores), treatment approach (technique, adjustment frequency)
**Target:** Predicted outcome scores at defined milestones; probability of clinically meaningful improvement (MCID achievement)
**Evaluation metric:** MAE on predicted outcome scores; AUC-ROC on MCID achievement prediction (targeting 0.78+)
**Scope:** Requires 3,000-5,000 completed treatment courses with baseline and milestone outcome measures. 1-2 person team, 4-6 months after data collection. The data collection challenge is administering validated outcome measures consistently — most practices don't currently do this.
**Data availability:** Practices using outcome tracking systems (PatientIQ, FOTO) have this data. Most chiropractic practices do not systematically collect validated outcome measures. Building the model requires first deploying outcome collection infrastructure.

---

## 3. Visit Count Estimation for Treatment Planning
#gradient-boosting #regression #tabular-ml

**Problem statement:** DCs estimate treatment plan length at the initial exam, but these estimates are often standardized by condition type rather than individualized. Accurate per-patient visit estimates improve case acceptance, insurance pre-authorization, and patient expectation management.

**ML task:** Regression — predict total visits to maximum medical improvement (MMI)
**Input data:** Condition type and duration, baseline severity scores, patient age, prior chiropractic treatment history, imaging findings, number of involved spinal regions, comorbidities, insurance type (visit limits), treatment approach
**Target:** Total visits to MMI or discharge, defined as the visit at which the last clinically meaningful improvement is documented
**Evaluation metric:** MAE on visit count; percentage within ±3 visits of actual
**Scope:** 2,000-5,000 completed cases with clear discharge documentation. 1-person team, 3-4 months. Requires consistent discharge criteria across the training dataset.
**Data availability:** EHR systems contain visit counts and discharge dates. The challenge is defining "treatment completion" consistently — many patients stop treatment without formal discharge, and distinguishing completed care from dropouts requires clinical review.

---

## 4. Insurance Denial Risk Prediction
#gradient-boosting #binary-classification #tabular-ml #compliance

**Problem statement:** Chiropractic claims are denied at 2-3x the rate of general medical claims. Predicting which claims are likely to be denied before submission would enable proactive documentation improvement, saving both the denied revenue and the appeal time.

**ML task:** Binary classification — will this claim be denied?
**Input data:** CPT codes, diagnosis codes (ICD-10), visit number in current treatment plan, carrier identity, patient's remaining visit allocation, documentation word count and keyword presence, prior denial history for this patient/carrier combination, time since initial exam, outcome measure trends
**Target:** Binary: claim paid / claim denied
**Evaluation metric:** AUC-ROC targeting 0.82+; recall at 0.80 (catch 80% of denials with acceptable false positive rate for documentation enhancement)
**Scope:** 10,000-50,000 claim records with outcomes. 1-person team, 2-3 months. Data is well-structured in practice management systems.
**Data availability:** Every practice has claims data with payment/denial outcomes in their billing system. Aggregating across practices requires data normalization across different EHR systems. Carrier-specific models may be more accurate than a universal model given different denial patterns by carrier.

---

## 5. Patient Compliance and Dropout Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** 30-40% of chiropractic patients drop out of their treatment plan before completion. Predicting which patients are at risk of dropping out would enable proactive engagement (schedule flexibility, financial arrangements, education on expected timeline) before the patient disappears.

**ML task:** Binary classification — will this patient complete their treatment plan?
**Input data:** Patient demographics, insurance type and copay amount, treatment plan length, visit frequency, distance from practice, appointment adherence pattern (cancellations, reschedules, no-shows), outcome measure trends, visit-over-visit symptom change, payment history
**Target:** Binary: completes treatment plan / drops out before completion
**Evaluation metric:** AUC-ROC targeting 0.75+; recall at 0.70 for dropout prediction with 2-3 visit advance warning
**Scope:** 3,000-5,000 patient treatment courses with completion/dropout labels. 1-person team, 2-3 months. Straightforward tabular classification.
**Data availability:** Scheduling and billing data captures attendance patterns. Defining "dropout" requires a threshold (e.g., no visit within 30 days of last scheduled appointment without formal discharge). Data exists in practice management systems but requires extraction and labeling.
