# Machine Learning Opportunities — HVAC Contractors

**Industry:** [[hvac-contractors|HVAC Contractors]]
**Derived from:** [[problems/hvac-contractors/high-impact|High Impact]], [[problems/hvac-contractors/low-impact-1|Low Impact 1]], [[problems/hvac-contractors/low-impact-2|Low Impact 2]], [[problems/hvac-contractors/worker-life-1|Worker Life 1]], [[problems/hvac-contractors/worker-life-2|Worker Life 2]]

---

## 1. Refrigerant System Fault Diagnosis from Gauge Readings
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #conditional-probability-and-bayes-theorem #probability-distributions #tacit-knowledge-ml

**Problem statement:** Experienced HVAC technicians diagnose refrigerant circuit faults by interpreting the joint state of suction pressure, discharge pressure, superheat, and subcooling — a multi-variable pattern recognition skill that takes 5-8 years to internalize. A classification model trained on labeled diagnostic service calls can replicate this reasoning, enabling junior technicians to reach correct diagnosis on the first visit.

**ML task:** Multiclass classification — fault type from gauge readings + system parameters. Classes: normal operation, low refrigerant charge, compressor valve failure, TXV/metering device restriction, dirty condenser/reduced airflow, dirty evaporator/reduced airflow, refrigerant overcharge, liquid line restriction, compressor capacitor fault (electrical, not refrigerant-circuit)
**Input data:** Service call records with gauge readings (suction pressure, discharge pressure) + technician-measured temperatures (suction line, liquid line, indoor return, outdoor ambient) + confirmed repair code (what was actually wrong). Feature engineering: compute superheat, subcooling, pressure ratio, delta-T across evaporator.
**Target:** Ranked differential diagnosis (top-3 fault conditions with probability scores); next diagnostic step recommendation; parts estimate per diagnosis
**Evaluation metric:** Top-1 accuracy on held-out diagnostic calls; recall on high-cost misdiagnosis (compressor condemnation vs. capacitor fault, refrigerant addition vs. TXV restriction); callback rate for firms using vs. not using the model
**Scope:** Large HVAC service companies running ServiceTitan with consistent diagnostic coding have 10,000-50,000 labeled calls available. Gradient boosting on the 8-12 engineered features: 6-10 week modeling project once data is structured. A partnership with a ServiceTitan integration partner or a large DSO (dealer service organization) provides training data and distribution simultaneously.
**Data availability:** ServiceTitan logs repair codes per service call. Gauge readings are currently not digitally captured in most firms — they're recorded on paper manifold worksheets. Adding digital gauge data capture (Testo, Fieldpiece Bluetooth manifolds) to the workflow is the data collection step that unlocks this model.

---

## 2. Predictive Equipment Failure from Runtime and Temperature Data
#lstms-and-grus #time-series-forecasting #change-point-detection #loss-functions #backpropagation #gradient-descent #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Smart thermostats (ecobee, Sensi, Nest) collect continuous runtime and temperature data that encodes early equipment degradation: a system running longer to meet setpoint, reduced cooling capacity in high-load conditions, refrigerant loss reducing efficiency over time. These patterns appear in the data weeks before the customer calls about a comfort complaint. Detect them proactively.

**ML task:** Anomaly detection on time-series runtime data; binary classification (failure within 30/60/90 days: yes/no) from runtime trend features; change-point detection for efficiency degradation onset
**Input data:** Thermostat runtime records (time series of compressor-on minutes per hour), indoor/outdoor temperature differential, equipment model and age. Supervision signal: service calls documenting system failure or major repair — the runtime anomaly should precede the service call by days to weeks.
**Target:** Anomaly alert when runtime pattern deviates from equipment's established baseline; proactive maintenance recommendation to customer (90-day failure probability with recommended service action)
**Evaluation metric:** Recall on service calls preceded by detectable runtime anomalies; lead time between first anomaly alert and confirmed failure; false positive rate (alerts that didn't result in required service)
**Scope:** Thermostat manufacturers (ecobee, Sensi/Emerson) have the continuous runtime data. A data partnership with an ecobee or Sensi for access to runtime history matched to HVAC contractor service records (via address matching) provides the training dataset. LSTM or transformer on time-series runtime features + gradient boosting for the classification step: 3-4 month project.
**Data availability:** Smart thermostat penetration in US homes is approximately 30% and growing. The runtime data exists — the gap is joining it to service outcomes for supervision.

---

## 3. Maintenance Agreement Churn Prediction
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #conditional-probability-and-bayes-theorem #revenue-impact

**Problem statement:** Predict which maintenance agreement customers are at risk of cancellation at their next renewal, 60-90 days in advance, to trigger targeted retention outreach before the renewal date.

**ML task:** Binary classification (cancel at next renewal: yes/no) using ServiceTitan customer history features
**Input data:** Customer features: equipment age, maintenance visit completion rate, appointment reschedule/cancel count (last 24 months), repair call frequency, discount redemption rate, time since last contact, agreement tier (basic vs. premium), customer tenure
**Target:** Churn probability per customer at 90-day renewal horizon; churn reason prediction (engagement lapse, equipment age, price sensitivity) for outreach message customization
**Evaluation metric:** AUC-ROC on held-out renewal cohort; precision at top-quintile churn flag; revenue retained from proactive outreach to flagged customers vs. control group
**Scope:** Any HVAC firm with 1,500+ maintenance agreement customers and 3+ years of ServiceTitan data has training data. Gradient boosting on ~15 customer features: 3-4 week project. High business value, low modeling complexity — the impact is in the feature engineering (understanding which ServiceTitan fields encode the signals) and the outreach automation.
**Data availability:** ServiceTitan logs all customer interactions, visit history, and agreement status. Agreement cancellation dates provide the supervision label. Firms with disciplined service code usage have clean training data.

---

## 4. Capacitor and Contactor Failure Prediction from Electrical Measurements
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #descriptive-statistics #tacit-knowledge-ml #quick-win

**Problem statement:** Experienced HVAC technicians measure capacitor microfarad ratings and contactor resistance during maintenance visits and assess proximity to failure from the reading — a capacitor at 85% of nameplate rating is at risk; one at 70% should be replaced. Codify this tacit decision rule into a model that flags borderline components for proactive replacement during maintenance visits rather than waiting for emergency failure.

**ML task:** Binary classification (component will fail before next annual maintenance visit: yes/no) from electrical measurement inputs
**Input data:** Capacitor microfarad reading vs. nameplate rating (% of spec remaining), component age, system runtime hours (if available), ambient temperature conditions. Supervision signal: component failures between maintenance visits in the service history.
**Target:** Replace-now vs. monitor classification per component at each maintenance visit; probability of failure before next scheduled maintenance
**Evaluation metric:** Recall on components that failed before next maintenance (did we flag them?); precision on replace-now flags (did flagged components actually need replacement?); revenue from proactive component replacement on maintenance visits vs. emergency failure calls
**Scope:** This is a quick win because the decision boundary is relatively simple (% of nameplate + age), the measurement data is collected at every maintenance visit already, and proactive component replacement is a well-accepted upsell on maintenance visits. Adding the probabilistic framing to what technicians already do subjectively. 2-3 week project with ServiceTitan maintenance visit data.
**Data availability:** ServiceTitan logs parts installed per service call, which captures component replacement events. Capacitor readings are recorded in some firms' maintenance checklists — others require adding this to the standard maintenance workflow.

---

## 5. Duct Leakage Estimation from System Performance Measurements
#gaussian-processes #linear-regression #kernel-methods #feature-engineering #evaluation-metrics #probability-distributions #bayesian-inference #tacit-knowledge-ml

**Problem statement:** Experienced HVAC technicians can estimate duct leakage severity from system performance indicators — significantly low static pressure, higher-than-expected runtime for setpoint, temperature differential below spec at registers — without performing a full blower door test. A regression model can provide a duct leakage probability estimate from easily-measured system performance inputs, flagging homes that warrant a full duct sealing evaluation.

**ML task:** Regression (estimated duct leakage rate as % of system flow) from system performance measurements; binary classification (duct leakage severity: moderate/severe requiring remediation)
**Input data:** Static pressure measurements (supply and return), supply register airflow estimates, temperature differential across coil, return air temperature, equipment tonnage, home size. Supervision signal: blower door and duct blaster test results matched to the performance measurements from the same service calls.
**Target:** Duct leakage severity estimate; recommendation for full duct testing (cost-benefit framing for customer)
**Evaluation metric:** Correlation between model estimate and blower door test result on homes where both measurements exist; recall on severe leakage cases (> 20% leakage) vs. model flag
**Scope:** Requires prospective data collection — service calls where both performance measurements and duct blaster results are recorded for the same system. Energy audit firms and weatherization contractors who routinely perform both would be the training data source. Moderate scope: 1,500-3,000 matched records, 8-12 week modeling project.
**Data availability:** Energy audit firms have duct blaster and blower door test data. Matching this to HVAC service performance measurements from the same homes requires a data partnership or prospective collection program.
