# Machine Learning Opportunities — Insurance Restoration

**Industry:** [[insurance-restoration|Insurance Restoration]]
**Derived from:** [[problems/insurance-restoration/high-impact|High Impact]], [[problems/insurance-restoration/low-impact-1|Low Impact 1]], [[problems/insurance-restoration/low-impact-2|Low Impact 2]], [[problems/insurance-restoration/worker-life-1|Worker Life 1]], [[problems/insurance-restoration/worker-life-2|Worker Life 2]]

---

## 1. Moisture Migration Prediction from Visible Damage and Construction Type
#cnns #gradient-boosting #transfer-learning #feature-engineering #evaluation-metrics #loss-functions #backpropagation #gradient-descent #cross-validation #bias-variance-tradeoff #tacit-knowledge-ml

**Problem statement:** Experienced restoration technicians predict where water has migrated behind walls and under floors based on visible damage patterns, construction type, elapsed time, and environmental conditions. This tacit knowledge — reading visible cues to predict invisible moisture extent — determines scope accuracy, which directly controls job profitability. Technicians without this skill underscope (causing mold and re-mobilization) or overscope (triggering carrier audits).

**ML task:** Regression — predict moisture migration distance and direction from loss origin point, producing a 2D probability map of affected areas
**Input data:** Photos of visible damage (water staining, material deformation, standing water), construction type (frame type, floor type, wall materials), loss characteristics (water source, category, elapsed hours/days), initial moisture readings on a spatial grid, ambient temperature and humidity, property age and square footage
**Target:** Spatial moisture migration map — predicted moisture content levels at grid points beyond visible damage, validated against actual moisture readings taken during selective demolition
**Evaluation metric:** MAE on moisture content prediction at each grid point; percentage of affected areas correctly identified (recall > 0.85 to avoid missed wet areas that develop mold); false positive rate below 20% to avoid unnecessary demolition
**Scope:** Requires 1,000-2,000 water loss jobs with paired initial-inspection and post-demo documentation. A large restoration company (100+ losses/month) can accumulate this in 12-18 months with structured data collection. 3-person team (ML engineer, data engineer, domain expert), 9-12 months for model development after data collection. Multi-modal model combining CNN for photo analysis with gradient-boosted regression for tabular construction/environmental features.
**Data availability:** Initial inspection photos exist in job management systems. Post-demo moisture maps exist on paper grid sheets but are rarely digitized. The key bottleneck is pairing pre-demo predictions with post-demo ground truth in a structured format. Requires a purpose-built data collection protocol layered onto existing inspection workflows.

---

## 2. Drying Time Prediction by Job Configuration
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #linear-regression #time-series-forecasting #probability-distributions #bias-variance-tradeoff

**Problem statement:** Knowing when a water-damaged structure will reach target dryness determines equipment rental duration, job timeline, and clearance testing scheduling. Currently estimated by experience, with 30-40% of jobs requiring extended drying beyond initial estimates.

**ML task:** Regression — predict days to reach target moisture content given current conditions and equipment deployment
**Input data:** Initial moisture readings (grid), materials affected (drywall, hardwood, carpet, concrete), equipment deployed (dehumidifier count/capacity, air mover count/placement), ambient conditions (temperature, humidity, season), structure characteristics (ventilation, HVAC availability, crawlspace vs. slab), water category and volume
**Target:** Days to clearance-level dryness (typically <15% moisture content for wood, <1% for concrete)
**Evaluation metric:** MAE in days; percentage of predictions within ±1 day of actual
**Scope:** 2,000-5,000 completed water loss jobs with daily moisture logs. 1-2 person team, 4-6 months. Relatively straightforward tabular ML problem once data is structured.
**Data availability:** Daily moisture readings exist in paper logs and some digital systems. Equipment deployment records exist in job management platforms. Main challenge is digitizing paper moisture logs from historical jobs.

---

## 3. Job Cost Estimation Accuracy
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #linear-regression #regularization #expectation-variance-covariance #bias-variance-tradeoff

**Problem statement:** Initial Xactimate estimates frequently deviate 20-40% from final job cost due to scope changes, supplements, and unforeseen conditions. Predicting the likely final cost from initial scope would improve cash flow planning and carrier negotiation.

**ML task:** Regression — predict final job cost from initial Xactimate estimate and job characteristics
**Input data:** Initial Xactimate line items and total, loss type, property size and construction, water category, number of rooms affected, carrier identity, historical supplement approval rates for this carrier, property age
**Target:** Final invoiced amount (after all supplements and change orders)
**Evaluation metric:** MAE as percentage of initial estimate; percentage of predictions within ±10% of final cost
**Scope:** 5,000-10,000 completed jobs with initial and final Xactimate files. 1-person team, 3-4 months. Data is well-structured within Xactimate exports.
**Data availability:** Xactimate files (initial and final) are stored digitally by every restoration company. This is one of the most data-rich ML opportunities in the industry — the main challenge is normalizing across different Xactimate pricing databases and regional cost variations.

---

## 4. Equipment Utilization Optimization
#gradient-boosting #feature-engineering #evaluation-metrics #optimization-fundamentals #markov-decision-processes #dynamic-programming #cross-validation #probability-distributions #expectation-variance-covariance

**Problem statement:** Restoration companies manage 200-500 pieces of drying equipment across 15-40 concurrent jobs, making constant allocation trade-offs without real-time drying progress data. Optimal equipment allocation would reduce idle time and prevent both premature removal (causing drying failures) and over-deployment (wasting capacity).

**ML task:** Multi-objective optimization — recommend equipment allocation across concurrent jobs that minimizes total drying time while maximizing equipment utilization
**Input data:** Current equipment deployment (type, capacity, location, runtime hours), drying progress per job (moisture readings, trend), new job requirements (loss type, estimated equipment needs), equipment availability in warehouse, crew schedules, job priorities (carrier SLAs, customer satisfaction risks)
**Target:** Recommended equipment moves: which units to redeploy, from which jobs, to which jobs, and when
**Evaluation metric:** Average equipment utilization rate (target >80%); drying failure rate (target <5%); average days-to-dry improvement vs. baseline
**Scope:** Requires integration with moisture monitoring and equipment tracking systems. Reinforcement learning approach needs simulation environment built from historical job data. 2-3 person team, 6-9 months. Real-time data feeds are the integration challenge.
**Data availability:** Equipment location data exists in asset tracking systems. Moisture reading data exists but is often on paper. Building a real-time data pipeline from field devices to optimization model is the primary engineering challenge.

---

## 5. Carrier Compliance Score Prediction
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #descriptive-statistics #expectation-variance-covariance #compliance

**Problem statement:** Carrier preferred vendor programs evaluate restoration companies on quarterly scorecards with metrics including response time, documentation quality, estimate accuracy, and customer satisfaction. Predicting end-of-quarter scores mid-quarter would enable proactive remediation before thresholds are breached.

**ML task:** Regression — predict end-of-quarter carrier compliance scores from current-quarter job performance data
**Input data:** Current quarter job-level metrics (response times, documentation completeness, estimate accuracy, customer satisfaction ratings), historical quarterly scores, number of jobs remaining in quarter (estimated), carrier-specific scoring methodology and weights, current active jobs with in-progress metrics
**Target:** Predicted end-of-quarter scores for each carrier program metric
**Evaluation metric:** MAE on each predicted metric; binary accuracy on threshold breach prediction (will score fall below minimum?)
**Scope:** 2-3 years of quarterly scorecard data across 5-8 carrier programs. 1-person team, 2-3 months. Relatively small dataset but high business value — each program is worth $200K-$500K annually.
**Data availability:** Carrier scorecards are provided quarterly in PDF or portal format. Job-level performance data exists in job management systems. The challenge is extracting and standardizing scorecard data across different carrier reporting formats.
