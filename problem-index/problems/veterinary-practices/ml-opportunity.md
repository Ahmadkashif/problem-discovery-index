# Machine Learning Opportunities — Veterinary Practices

**Industry:** [[veterinary-practices|Veterinary Practices]]
**Derived from:** [[problems/veterinary-practices/high-impact|High Impact]], [[problems/veterinary-practices/low-impact-1|Low Impact 1]], [[problems/veterinary-practices/low-impact-2|Low Impact 2]], [[problems/veterinary-practices/worker-life-1|Worker Life 1]], [[problems/veterinary-practices/worker-life-2|Worker Life 2]]

---

## 1. Veterinary Radiograph Abnormality Detection
#cnn #object-detection #semantic-segmentation #computer-vision #tacit-knowledge-ml

**Problem statement:** Given a canine or feline radiograph (DICOM), detect and localize pathological findings across musculoskeletal, thoracic, and abdominal regions — replicating the pattern recognition of an experienced veterinary radiologist for the most common abnormality categories seen in general practice.

**ML task:** Multi-label object detection + localization on veterinary radiograph images; output: list of findings with bounding regions, confidence scores, and recommended action tier (routine / recommend specialist / urgent)
**Input data:** DICOM radiograph images (VD/DV and lateral projections) with radiologist interpretation labels — pathology type, location, severity. Need separate models for species (canine vs. feline; exotic requires a different dataset entirely).
**Target:** Abnormality present/absent per category (pulmonary, cardiac silhouette, hepatic, renal, orthopedic, spinal) with bounding box annotations
**Evaluation metric:** AUC-ROC per finding category; sensitivity > 0.90 for high-risk findings (pulmonary nodules, cardiac silhouette enlargement, spinal compression); specificity > 0.85 to maintain clinical utility without alert fatigue
**Scope:** The hardest part is data — veterinary radiograph datasets with expert radiologist labels are 10-100x smaller than human medical imaging datasets. IDEXX has the largest private dataset; academic veterinary schools (Cornell, UC Davis, Colorado State) maintain labeled research datasets. A model trained on 50,000+ labeled canine chest and abdominal radiographs is achievable. Plan for 12-18 months from dataset assembly to production-ready model. A collaboration with one or two veterinary schools accelerates dramatically.
**Data availability:** Veterinary teaching hospitals have the largest labeled radiograph archives. Commercial teleradiology services have scale but may not share. The dataset scarcity is the primary bottleneck — not the modeling approach.

---

## 2. Feline Pain and Distress Assessment from Facial Imagery
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced vets assess feline pain level through subtle behavioral cues — ear position, orbital tightening, whisker position, muzzle tension, head position — captured in the Feline Grimace Scale (FGS). Automate FGS scoring from a still image or video frame, enabling real-time pain assessment by technicians without specialized training.

**ML task:** Regression or ordinal classification (FGS score 0-10) from standardized feline facial photographs
**Input data:** Standardized feline facial photographs (direct frontal) with veterinary clinician FGS scores as labels. The Montreal FGS research group has published labeled datasets.
**Target:** Continuous FGS score (0-10) or ordinal class (0-2: no/mild pain; 3-6: moderate pain; 7-10: severe pain) with confidence
**Evaluation metric:** Mean Absolute Error vs. clinician-assigned score; inter-rater agreement (Cohen's kappa) between model and multiple clinician raters
**Scope:** Published FGS datasets exist (Evangelista et al., Univ of Montreal) — approximately 2,500+ labeled images available for transfer learning. A CNN fine-tuned from a general face recognition backbone can achieve clinician-level agreement in 6-8 weeks with this data. Extension to dogs (CGPS — Canine Grimace Pain Scale) follows the same approach with different training data.
**Data availability:** FGS research datasets are public or available via collaboration. A production system would benefit from additional data collection at veterinary practices — adding tens of thousands of labeled images from routine clinical use.

---

## 3. Patient Mortality and Anesthetic Risk Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** Predict anesthetic complication risk for individual patients before a procedure, using patient history, species, breed, age, weight, and pre-anesthetic lab values — to guide anesthetic protocol selection and client counseling.

**ML task:** Binary classification (anesthetic complication: yes/no) + severity regression for high-risk patients
**Input data:** Patient demographics (species, breed, age, weight, sex/reproductive status), ASA classification, procedure type, pre-anesthetic bloodwork values (PCV, BUN, creatinine, glucose, liver enzymes), concurrent medications
**Target:** Complication probability (intra-operative or within 24 hours) + predicted complication type (respiratory, cardiac, recovery)
**Evaluation metric:** AUC-ROC; calibration plot (predicted probabilities must be well-calibrated for clinical use); sensitivity > 0.85 for severe complications
**Scope:** Veterinary anesthetic complication databases exist (CEPSAF study, published dataset ~98,000 procedures across UK practices). A gradient boosting model on structured features is achievable in 4-6 weeks. The key challenge is the heterogeneity of procedures — a dental cleaning in a young healthy dog has a very different risk profile than a splenectomy in a geriatric patient, requiring procedure-stratified models.
**Data availability:** The CEPSAF dataset (companion animal anesthetic safety study) is the best public source. Practices with 2,000+ anesthetic procedures per year can build a reasonable practice-specific model, though multi-practice pooled data is preferred.

---

## 4. Drug Interaction and Contraindication Classification for Multi-Species Prescriptions
#gradient-boosting #binary-classification #tabular-ml #compliance

**Problem statement:** Given a veterinary patient's species, breed, weight, age, concurrent medications, and a newly prescribed drug, flag contraindications, species-specific toxicity risks, and drug-drug interactions — returning a safety score with specific warnings.

**ML task:** Rule-based + ML hybrid: structured drug safety knowledge base (species contraindications, metabolic pathways, known interactions) combined with a classifier trained on historical adverse drug event reports
**Input data:** FDA Adverse Event Reporting System (FAERS) veterinary data, published veterinary pharmacology references, AVMA drug interaction databases, patient profile (species, breed, weight, age, concurrent meds)
**Target:** Binary flag (interaction/contraindication present: yes/no) per drug pair, with severity classification (caution / avoid / absolute contraindication) and specific warning text
**Evaluation metric:** Recall on known contraindications > 0.99 (false negatives are unacceptable); precision > 0.70 (some alert fatigue acceptable but not excessive)
**Scope:** The knowledge base component is straightforward — codifying Plumb's and AVMA resources into a queryable structure. The ML component adds adverse event signal from FAERS and published case reports. 8-12 week project for a robust v1. The species-specificity layer (especially exotic animals) requires specialist consultation for coverage.
**Data availability:** FDA FAERS veterinary section is public. Plumb's content requires licensing. Published pharmacokinetics literature covers major species (dog, cat) well; exotic species coverage requires academic collaboration.

---

## 5. Client Appointment No-Show and Compliance Dropout Prediction
#gradient-boosting #survival-analysis #tabular-ml

**Problem statement:** Predict which patients are at risk of missing their next scheduled appointment or dropping out of a chronic care protocol (dental health plan, senior wellness program, chronic disease management), enabling proactive outreach that prevents care gaps.

**ML task:** Survival analysis (time-to-dropout from care) + binary classification (will miss next appointment: yes/no)
**Input data:** Patient appointment history (scheduled, attended, cancelled, no-show), client demographics, practice-client relationship tenure, time since last visit, appointment type (routine vs. sick vs. specialist), payment history, vaccination/wellness protocol enrollment
**Target:** No-show probability for the next scheduled appointment; dropout risk score over the next 12 months
**Evaluation metric:** AUC-ROC for no-show prediction; calibration; precision at top-20% risk (practices can only proactively call so many clients — the model must identify the right ones)
**Scope:** Any practice with 3+ years of appointment data (5,000+ scheduled appointments) has sufficient volume. A gradient boosting model on structured features runs in milliseconds. The business logic for triggered outreach (text reminder vs. phone call vs. discount offer) is separate from the model but straightforward to implement. 3-4 week project.
**Data availability:** Practice management systems log every appointment status. Data is abundant, clean (structured fields), and already collected as part of normal operations.
