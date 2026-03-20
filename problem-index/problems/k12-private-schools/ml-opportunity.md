# Machine Learning Opportunities — K-12 Private Schools

**Industry:** [[k12-private-schools|K-12 Private Schools]]
**Derived from:** [[problems/k12-private-schools/high-impact|High Impact]], [[problems/k12-private-schools/low-impact-1|Low Impact 1]], [[problems/k12-private-schools/low-impact-2|Low Impact 2]], [[problems/k12-private-schools/worker-life-1|Worker Life 1]], [[problems/k12-private-schools/worker-life-2|Worker Life 2]]

---

## 1. Student Engagement Risk Detection (Tacit Knowledge ML)
#gradient-boosting #lstms-and-grus #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #backpropagation #loss-functions #tacit-knowledge-ml

**Problem statement:** Experienced teachers can "read a room" and identify which students are disengaging — showing up but mentally checked out, socially withdrawing, losing curiosity — weeks or months before grades decline. This perceptual judgment, built over years of observing thousands of students, is the earliest and most actionable signal of academic or emotional trouble. It cannot currently be captured, scaled, or transferred to less experienced teachers.

**ML task:** Anomaly detection on multivariate student behavior time series, followed by binary classification (at-risk vs. on-track)
**Input data:** Daily attendance records, assignment submission timestamps and completion rates, LMS login frequency and session duration, grade trajectory (not absolute grades — the slope matters), library system checkouts, extracurricular participation logs, counselor visit frequency, and optional teacher micro-observations (a lightweight "pulse check" rating entered weekly). Data sourced from SIS (FACTS/Veracross), LMS (Canvas/Google Classroom), and a purpose-built teacher observation interface.
**Target:** Binary label: "teacher would flag this student for intervention" vs. "teacher considers this student on-track." Ground truth collected by having experienced teachers label their own students monthly, then validating against subsequent outcomes (grade drops, counselor referrals, family-initiated withdrawals).
**Evaluation metric:** Recall at 90%+ (missing an at-risk student is far worse than a false alarm), with precision tracked to avoid alert fatigue. F2-score as the primary optimization target. Time-to-detection compared against the teacher's own flagging timeline.
**Scope:** Requires partnership with 10-20 schools to collect sufficient labeled data across grade levels and school cultures. Initial model is per-division (lower/middle/upper school) because engagement signals differ by age. A 2-person ML team can build an MVP in 6 months if data pipelines from SIS/LMS are established. The hardest part is the labeling protocol — teachers must be trained to provide consistent micro-observations without it feeling like surveillance.
**Data availability:** Behavioral data (attendance, grades, LMS usage) is already captured digitally at most private schools. The critical missing piece is the teacher's expert judgment labels — these must be collected prospectively through a lightweight observation tool. Cross-school data sharing requires anonymization and parent consent, which is achievable but adds 2-3 months of compliance work.

---

## 2. Enrollment Yield Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff #revenue-impact

**Problem statement:** After admissions decisions are sent, schools cannot accurately predict which accepted families will enroll, leading to over-acceptance (overcrowded classrooms) or under-acceptance (empty seats and revenue shortfalls).

**ML task:** Binary classification — will this accepted family enroll (yes/no)?
**Input data:** Application metadata (submission date, completeness speed, financial aid request amount, sibling status), campus visit behavior (number of visits, events attended, questions asked — logged in admissions CRM), geographic distance, feeder school, communication responsiveness (email open rates, response times from Finalsite/FACTS), and historical yield data for similar family profiles. Sourced from admissions CRM, FACTS, and Finalsite analytics.
**Target:** Binary label: enrolled vs. did not enroll, collected at the enrollment contract deadline each year.
**Evaluation metric:** AUC-ROC with calibrated probabilities — the school needs reliable probability estimates, not just rankings, to set acceptance numbers. Brier score as secondary metric for calibration quality.
**Scope:** Each school has only 3-10 years of historical admissions data (200-800 families per year), so the model must be lightweight (gradient-boosted trees, not deep learning) and benefit from cross-school transfer learning. A solo ML engineer can build a school-specific model in 2-3 months if data export from admissions CRM is clean. Multi-school models require a data consortium, adding 4-6 months for agreements and normalization.
**Data availability:** Most data is already in admissions CRMs (Ravenna, SchoolAdmin, FACTS). The main gap is behavioral signals from campus visits, which are inconsistently logged. Schools that adopt structured visit tracking will have significantly better models.

---

## 3. Family Attrition Prediction
#gradient-boosting #survival-analysis #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #maximum-likelihood-estimation #revenue-impact

**Problem statement:** Schools discover families are leaving when re-enrollment contracts are not returned in March — too late to intervene or backfill the seat. Predicting attrition 4-6 months in advance enables targeted retention outreach.

**ML task:** Survival analysis (time-to-attrition) with binary classification at fixed horizons (will this family re-enroll next year?)
**Input data:** Tuition payment timeliness (days late per payment over the year), parent engagement metrics (volunteer hours, event attendance, parent-teacher conference attendance, fundraising participation), student academic trajectory (GPA trend, not level), family communication patterns (email frequency with teachers, complaint tickets), financial aid dependency (percentage of tuition covered by aid, year-over-year aid increases requested), sibling enrollment pipeline, and external signals where available (local competitor school expansion, real estate listings in the family's zip code). Sourced from SIS, billing system, development/advancement CRM, and optionally public data APIs.
**Target:** Binary label: family re-enrolled vs. did not re-enroll. For survival analysis, the event is "submitted withdrawal notice" with right-censoring for families still enrolled.
**Evaluation metric:** Concordance index (C-index) for survival model; recall at the top-20% risk tier (the school can realistically intervene with 20% of families). False negative cost is high — missing a family that leaves costs $25-50K in lost tuition.
**Scope:** Requires merging SIS, billing, and advancement data — typically a 1-2 month data engineering effort per school. Model training needs 5+ years of historical data to capture attrition patterns across economic cycles. A 2-person team (1 ML engineer, 1 data engineer) can deliver an MVP in 4 months. The biggest risk is that attrition drivers are often external (job relocation, divorce) and unpredictable.
**Data availability:** Payment and enrollment history is well-captured in billing systems. Parent engagement data is patchily recorded — many schools track volunteer hours in spreadsheets, not databases. A structured data collection protocol for engagement signals adds significant predictive power but requires school buy-in.

---

## 4. Financial Aid Optimization
#gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #optimization-fundamentals #expectation-variance-covariance #data-integration

**Problem statement:** Schools allocate $2-10M in annual financial aid using committee judgment and static formulas (e.g., "families below $X income get Y% discount"). This approach either over-awards (reducing net tuition revenue) or under-awards (losing price-sensitive families to competitors), but schools have no model to optimize the tradeoff.

**ML task:** Regression (predict the minimum aid award that retains a family) combined with constrained optimization (maximize enrollment yield subject to a total aid budget)
**Input data:** Historical aid applications (family income, assets, household size, number of children in tuition-charging schools), the aid award offered, whether the family enrolled, retention duration after enrollment, competitor school tuition rates, and local cost-of-living indices. Sourced from financial aid management systems (SSS by NAIS, FACTS, Clarity), admissions CRM, and public economic data.
**Target:** For the regression: the enrollment/retention outcome as a function of aid amount. For the optimization: the aid allocation vector across all applicant families that maximizes expected net tuition revenue.
**Evaluation metric:** Net tuition revenue per cohort (total tuition collected minus total aid awarded) compared against the prior year's committee-based allocation. Secondary metric: enrollment yield among aided families.
**Scope:** Highly sensitive data requiring strict access controls and possibly on-premise deployment. Requires 5-10 years of aid-award-to-outcome data per school. The optimization layer is non-trivial — it must respect constraints (minimum aid floors, maximum percentages, board-mandated diversity targets). A 2-person team can build the regression in 3 months; the optimization layer adds 2-3 months. Requires close collaboration with the business office to validate assumptions.
**Data availability:** Financial aid applications contain detailed family financial data, but access is restricted to a small number of staff. Historical aid-to-outcome linkage requires joining aid records with enrollment and retention records across systems — doable but rarely done. Schools using SSS by NAIS have the most standardized data.
