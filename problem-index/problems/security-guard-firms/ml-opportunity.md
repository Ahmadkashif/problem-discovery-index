# Machine Learning Opportunities — Security Guard Firms

**Industry:** [[security-guard-firms|Security Guard Firms]]
**Derived from:** [[problems/security-guard-firms/high-impact|High Impact]], [[problems/security-guard-firms/low-impact-1|Low Impact 1]], [[problems/security-guard-firms/low-impact-2|Low Impact 2]], [[problems/security-guard-firms/worker-life-1|Worker Life 1]], [[problems/security-guard-firms/worker-life-2|Worker Life 2]]

---

## 1. Site Security Assessment from Walkthrough Evaluation
#gradient-boosting #cnns #linear-regression #transfer-learning #feature-engineering #evaluation-metrics #loss-functions #tacit-knowledge-ml

**Problem statement:** Experienced operations managers walk a new client site and intuitively assess security requirements — identifying coverage gaps, vulnerable entry points, sight-line limitations, patrol route needs, and optimal guard post positions. This tacit assessment determines staffing proposals and pricing. Junior account managers lack this skill and either under-staff (creating security gaps) or over-staff (pricing themselves out of the contract). The experienced ops manager reads a site the way an architect reads a building — understanding how people flow through the space and where control points and vulnerabilities exist.

**ML task:** Multi-output regression (predict staffing requirements, patrol route timing, and guard post positions from site characteristics)
**Input data:** Site layout data (photos, floor plans if available, square footage, building type), operating hours, threat profile (asset value, neighborhood crime data, historical incidents), access point count and type, parking areas, lighting conditions, tenant/occupant data
**Target:** Recommended staffing level by shift, patrol route specifications (checkpoints, timing), guard post positions, and coverage assessment score
**Evaluation metric:** MAE on recommended staffing vs. experienced manager assessment; client satisfaction scores post-deployment as downstream metric
**Scope:** Requires 500-2,000 site assessments with experienced manager recommendations and deployment outcomes. 2-3 person team, 9-12 months. Challenge: site assessments are high-value institutional knowledge rarely documented in structured form.
**Data availability:** Site proposals and staffing plans exist in account management files but unstructured. Photos from initial site visits available. Crime data from public sources. Structured data collection requires standardized assessment protocol.

---

## 2. Guard No-Show Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff

**Problem statement:** 10-20% of shifts experience no-shows, but the risk isn't uniformly distributed. Certain combinations of guard, shift type, day, site, and conditions predict no-shows with significant accuracy.

**ML task:** Binary classification (will this guard show up for this specific shift?)
**Input data:** Guard profile (tenure, reliability history, commute distance, full-time/part-time), shift characteristics (day/night, hours, site, armed/unarmed), contextual factors (weather, day of week, holiday proximity, payday timing), recent behavior (late arrivals, shift swap requests, complaint frequency)
**Target:** Binary: no-show / attended
**Evaluation metric:** AUC-ROC targeting 0.80+; precision-recall optimized for top-decile risk (identify the 10% of shifts most likely to experience no-shows)
**Scope:** Trainable on 50,000-200,000 historical shift records. 1-2 person team, 3-4 months. Challenge: class imbalance (80-90% attendance). Guard behavior changes over time — model needs regular retraining.
**Data availability:** Scheduling and attendance data in guard management platforms. GPS check-in data for ground truth. Contextual features (weather, calendar) from public APIs.

---

## 3. Incident Pattern Analysis and Risk Prediction
#bert #transformers #attention-mechanisms #word-embeddings #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics

**Problem statement:** Incident reports contain valuable intelligence about security risks, but the unstructured text and inconsistent quality make pattern detection impossible at scale.

**ML task:** Multi-task: (1) Text classification — categorize and extract structured data from incident narratives; (2) Time-series forecasting — predict incident frequency and type by site by week
**Input data:** Incident report text, time, location within site, type codes, weather, special events calendar, historical incident data
**Target:** Structured incident classification (type, severity, suspect description, root cause), plus weekly incident probability by site and type
**Evaluation metric:** Accuracy on incident classification; MAPE on weekly incident forecasting; entity extraction precision for suspect descriptions and locations
**Scope:** BERT fine-tuning for text extraction on 5,000-10,000 labeled reports. Time-series model on 2+ years of incident data per site. 2-person team, 4-6 months.
**Data availability:** Incident reports in guard management platforms. Historical data available per site. Labeling for text extraction requires security professional review.

---

## 4. Guard-Site Match Optimization
#gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #expectation-variance-covariance

**Problem statement:** Some guards perform well at certain types of sites but poorly at others — a guard excellent at corporate lobby work may struggle at construction site security. Matching guards to sites based on performance patterns, not just availability, improves quality and reduces turnover.

**ML task:** Regression / recommendation (predict guard performance score at a given site type)
**Input data:** Guard profile (experience, certifications, physical fitness, communication skills), site characteristics (type, environment, client expectations, threat level), historical guard-site performance data (client feedback, incident handling, attendance, supervisor ratings)
**Target:** Predicted performance score for each guard-site combination
**Evaluation metric:** Correlation between predicted and actual performance scores; reduction in client complaints post-deployment
**Scope:** Requires 5,000+ guard-assignment records with performance outcomes. 1-2 person team, 3-4 months. Challenge: performance data is sparse and subjective (client feedback, supervisor assessments).
**Data availability:** Scheduling data links guards to sites. Performance data scattered across client feedback, supervisor reports, and incident records. Requires aggregation and normalization across subjective rating sources.

---

## 5. Guard Attrition and Retention Prediction
#gradient-boosting #survival-analysis #feature-engineering #maximum-likelihood-estimation #evaluation-metrics #probability-distributions #conditional-probability-and-bayes-theorem

**Problem statement:** With 100-300% annual turnover, predicting which guards are at risk of leaving — and when — enables targeted retention interventions for the highest-value guards.

**ML task:** Survival analysis (predict time to separation) + binary classification (will this guard leave within 90 days?)
**Input data:** Guard tenure, pay rate, shift patterns (proportion overnight, weekend), commute distance, attendance patterns, training completion, performance scores, site assignments, overtime hours, comparable pay rates in the market
**Target:** 90-day attrition probability; predicted tenure
**Evaluation metric:** C-index for survival model; AUC-ROC for 90-day classification. Focus on identifying at-risk guards among the top performance quartile (highest-value retention targets).
**Scope:** Trainable on 5,000-20,000 guard employment records with separation data. 1-person team, 2-3 months. HR data integration required.
**Data availability:** Employment records in HRIS. Scheduling and attendance data in guard management platforms. Pay and benefits data from payroll systems. Exit interview data (when available) provides ground truth on attrition drivers.
