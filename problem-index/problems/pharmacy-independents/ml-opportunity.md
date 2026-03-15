# Machine Learning Opportunities — Independent Pharmacies

**Industry:** [[pharmacy-independents|Independent Pharmacies]]
**Derived from:** [[problems/pharmacy-independents/high-impact|High Impact]], [[problems/pharmacy-independents/low-impact-1|Low Impact 1]], [[problems/pharmacy-independents/low-impact-2|Low Impact 2]], [[problems/pharmacy-independents/worker-life-1|Worker Life 1]], [[problems/pharmacy-independents/worker-life-2|Worker Life 2]]

---

## 1. Prescription Drug-Seeking and Diversion Pattern Detection
#gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #compliance

**Problem statement:** Experienced pharmacists have internalized behavioral and prescription pattern recognition for drug-seeking behavior — specific controlled substance combinations, unusual fill timing, multi-prescriber patterns, cash-only payment, unusual geographic origin of prescriptions — that they use to make accept/refuse decisions. This tacit risk scoring can be formalized as a model that surfaces high-risk prescription presentations systematically, including patterns subtle enough to escape conscious notice.

**ML task:** Binary classification (high drug-seeking risk: yes/no) with ranked feature contributions for pharmacist review
**Input data:** Prescription attributes (controlled substance class, prescriber NPI, patient address, fill timing relative to last fill, days supply, prescriber's geographic distance from pharmacy, payment method), patient history (fill patterns, multi-prescriber indicators, out-of-state prescriptions, prescription presentation patterns), PDMP (Prescription Drug Monitoring Program) data for the patient
**Target:** Risk flag binary, with confidence score and top 3 contributing factors for pharmacist review context
**Evaluation metric:** Recall on confirmed diversion cases in training data; pharmacist acceptance rate (does the pharmacist agree with the flag?); false positive rate (flags that are overridden with no issue)
**Scope:** PDMP data is state-level and requires integration agreements. Pharmacy claims data provides prescription attributes. A gradient boosting model on structured features is achievable in 4-6 weeks; PDMP integration adds 8-12 weeks. Critically: the model outputs a flag for pharmacist review — the pharmacist makes the final decision. This is a decision support tool, not autonomous refusal.
**Data availability:** Pharmacy claims data is available at any pharmacy with 2+ years of controlled substance dispensing history. PDMP data requires state agency data sharing agreements, which are increasingly available through prescription monitoring initiatives.

---

## 2. DIR Fee Exposure Prediction at Claim Level
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** Predict the expected retroactive DIR fee for a new claim at point-of-sale, based on the PBM, plan type, drug class, patient adherence history, and current pharmacy performance metrics — enabling real-time margin calculation and cash-pay alternative counseling when DIR exposure makes a claim unprofitable.

**ML task:** Regression (predicted DIR fee as % of reimbursement) per claim, trained on historical (reimbursement, DIR claw-back, contributing metrics) pairs
**Input data:** Historical claims with matched DIR fee reconciliation data (available in PBM year-end DIR statements), plan type, drug class, patient adherence PDC at time of fill, pharmacy's current star ratings performance metrics
**Target:** Expected DIR fee percentage for a new claim (continuous); secondary binary flag: claim expected to be net-loss after DIR
**Evaluation metric:** Mean Absolute Error of DIR prediction; calibration; net margin prediction accuracy vs. actual post-DIR reimbursement
**Scope:** This model requires the pharmacy to have at least 2 years of DIR reconciliation statements matched to original claims — data that exists but requires manual assembly. A data pipeline to parse DIR statements and match them to PMS claims is the hardest engineering step (2-4 weeks). The model itself is straightforward (LightGBM, 4-6 weeks). Full integration into PMS fill workflow requires PMS API access.
**Data availability:** DIR reconciliation statements are available at every pharmacy on Medicare Part D contracts. Original claim data is in the PMS. The matching step requires pharmacy-side effort — but the resulting dataset is uniquely valuable and exists nowhere else.

---

## 3. Medication Adherence Dropout Survival Analysis
#gradient-boosting #survival-analysis #tabular-ml

**Problem statement:** For each chronic medication patient, predict the probability of missing the next refill (adherence gap) in the next 30/60/90 days — enabling proactive outreach to the highest-risk patients before the gap opens, rather than reactive calls after it already affects PDC scores.

**ML task:** Survival analysis (time-to-next-gap) + binary classification (will miss next expected refill: yes/no) per patient-drug pair
**Input data:** Patient refill history (fill dates, days supply, gaps), drug class (adherence behavior differs significantly between statins, antihypertensives, and diabetes drugs), patient demographics (age), seasonal patterns, whether the patient previously responded to pharmacist outreach
**Target:** 30/60/90-day gap probability per patient-drug pair; ranked list of highest-risk patients for weekly proactive outreach
**Evaluation metric:** AUC-ROC for gap prediction; precision at top-20% risk flag (the pharmacy can only call so many patients — the model must identify the right ones); PDC improvement in patients who receive proactive outreach
**Scope:** Any pharmacy with 3+ years of refill data for chronic medications has sufficient volume. For a pharmacy with 200+ chronic disease patients, a gradient boosting model trains in minutes and needs retraining monthly. 3-4 week project, straightforward data pipeline from PMS.
**Data availability:** PMS systems log every fill with date and days supply. Adherence history is computable from these records. Data is available at every pharmacy; no external data needed.

---

## 4. Drug Interaction Clinical Significance Scoring
#gradient-boosting #ranking #tabular-ml #compliance #worker-facing

**Problem statement:** Re-rank the existing pharmacy DDI alert stream by clinical significance for this specific patient — suppressing low-risk theoretical interactions and elevating alerts where patient-specific risk factors (age, renal function, dose, novel combination) make the interaction genuinely actionable.

**ML task:** Learning-to-rank model that re-scores existing DDI alerts by clinical significance given patient context
**Input data:** DDI alert data (drug pair, severity code from Medi-Span/First DataBank database), patient profile (age, weight if available, renal function markers if in PMS, concurrent drug list, diagnosis codes if available), whether this drug combination has been previously reviewed and accepted for this patient, prescriber awareness indicator (both drugs from same prescriber vs. different prescribers)
**Target:** Clinical significance score (0-10) per alert; binary "requires active review" flag
**Evaluation metric:** Agreement with pharmacist clinical judgment (labeling study with PharmDs); reduction in override-without-reading rate; no increase in missed clinically significant interactions
**Scope:** The scoring model requires a labeled training set: pharmacists evaluating a sample of historical alerts and rating their clinical significance. 500-1,000 labeled alerts from 3-5 pharmacists provides sufficient training signal. Model is a relatively simple gradient boosting classifier. 6-8 week project. Integration requires PMS DDI module API access.
**Data availability:** Historical alert data with override records is available in PMS audit logs. Creating clinical significance labels requires pharmacist annotation time — this is the primary investment. Published clinical significance ratings (Hansten & Horn's Drug Interactions Analysis and Management) can seed the label set.

---

## 5. Pharmacy Revenue Mix Optimization — Cash Pay vs. Insurance
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** For each prescription at fill, determine whether the cash pay price (via GoodRx, Mark Cuban Cost Plus, etc.) yields better net margin than the adjudicated insurance reimbursement after estimated DIR exposure — and surface this comparison to the pharmacist for patient counseling in real time.

**ML task:** Regression (net margin comparison: insurance-adjudicated vs. cash-pay) per prescription, using DIR-adjusted insurance margin prediction as the insurance leg
**Input data:** Drug NDC, quantity, insurance adjudication result (if run), cash-pay pricing from discount card APIs (GoodRx API), pharmacy acquisition cost (from wholesaler), predicted DIR exposure (from model #2)
**Target:** Net margin for each payment path; binary flag (cash pay recommended: insurance margin < cash margin after DIR)
**Evaluation metric:** Margin improvement per counseled prescription; patient acceptance rate of cash-pay alternatives; revenue impact per prescription category
**Scope:** Cash-pay pricing is available via GoodRx API in real time. DIR prediction provides the insurance leg estimate. The comparison calculation is arithmetic once the inputs exist. Integration into PMS fill workflow is the primary engineering challenge. 3-4 week project, straightforward once DIR model is in place.
**Data availability:** GoodRx pricing API is publicly accessible. Pharmacy acquisition cost is in the wholesaler invoice data (linked to drug NDC). Insurance adjudication data is real-time from PMS. This model is lightweight and builds directly on the DIR prediction model.
