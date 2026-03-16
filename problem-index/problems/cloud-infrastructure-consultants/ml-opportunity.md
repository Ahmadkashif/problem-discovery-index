# Machine Learning Opportunities — Cloud Infrastructure Consultants

**Industry:** [[cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Derived from:** [[problems/cloud-infrastructure-consultants/high-impact|High Impact]], [[problems/cloud-infrastructure-consultants/low-impact-1|Low Impact 1]], [[problems/cloud-infrastructure-consultants/low-impact-2|Low Impact 2]], [[problems/cloud-infrastructure-consultants/worker-life-1|Worker Life 1]], [[problems/cloud-infrastructure-consultants/worker-life-2|Worker Life 2]]

---

## 1. Cloud Spend Anomaly & Waste Detection (Tacit Knowledge Capture)
#gradient-boosting #anomaly-detection #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

**Problem statement:** Senior cloud architects can scan a cloud bill and immediately identify misconfigured, oversized, or redundant resources — a skill that takes 3-5 years of hands-on experience to develop and cannot be fully articulated as rules. The goal is to capture this expert pattern recognition into a model that flags waste and recommends right-sizing actions with the same contextual awareness as the best human reviewers.

**ML task:** Anomaly Detection + Regression (predicting optimal resource size) + Ranking (prioritizing recommendations by savings impact)
**Input data:** Cloud billing line items (service, resource type, usage quantity, cost), CloudWatch/Azure Monitor/GCP Monitoring time-series metrics (CPU, memory, disk, network I/O at 5-minute granularity), resource metadata (tags, creation date, last-modified date, VPC/subnet placement), architecture context (security group rules indicating service dependencies, Auto Scaling group configurations, Reserved Instance/Savings Plan coverage). Typically 50-200 features per resource after engineering.
**Target:** For anomaly detection: binary label (waste / not-waste) with sub-labels (unattached volume, oversized instance, idle resource, missing Savings Plan coverage, suboptimal data transfer path). For right-sizing: predicted optimal instance type/size given the workload profile. Labels derived from senior architect review logs — what they recommended, what the client accepted, and the measured savings 30 days post-implementation.
**Evaluation metric:** Precision@10 for the ranked recommendation list (the top 10 recommendations should have >90% acceptance rate by architects), plus total dollar savings captured vs. missed (recall weighted by dollar value). False positives are costly — recommending a downsize on a disaster recovery standby instance that then fails to handle a failover erodes client trust.
**Scope:** Requires 6-12 months of labeled architect reviews across 30+ client environments to build a robust training set. A team of 2 ML engineers + 1 cloud architect (for labeling and validation) can build an MVP in 4-6 months, starting with AWS-only and a single resource type (EC2 right-sizing) before expanding. The feature engineering is the hard part — translating raw CloudWatch metrics and billing data into the same "view" an architect mentally constructs.
**Data availability:** Billing data is readily available via AWS Cost and Usage Reports, Azure Cost Management exports, and GCP billing exports. Utilization metrics require CloudWatch/Monitor agent deployment (often already in place for managed clients). The bottleneck is labeled architect decisions — firms must instrument their review process to capture what architects recommend and why, which most firms do not currently track systematically.

---

## 2. Cloud Capacity Forecasting & Auto-Scaling Optimization
#lstm #time-series-forecasting #tabular-ml #revenue-impact

**Problem statement:** Cloud consultants set auto-scaling policies and capacity reservations based on historical patterns and client-provided growth estimates, but workload patterns are non-stationary — seasonal traffic, marketing campaigns, product launches, and organic growth create demand curves that static scaling rules handle poorly, leading to either over-provisioning (waste) or under-provisioning (outages).

**ML task:** Time-Series Forecasting (multi-step ahead prediction of resource demand)
**Input data:** Historical CloudWatch/Monitor metrics at 1-hour granularity (CPU, memory, request count, queue depth) for 6-12 months per workload. External signals: client-provided event calendars (marketing campaigns, product launches), day-of-week/holiday patterns, and historical scaling events (when auto-scaling triggered and whether it was sufficient). Typically 10-30 input series per workload cluster.
**Target:** Predicted resource demand (number of instances, vCPU hours, memory GB) at 1-hour, 1-day, and 1-week horizons. The model outputs a demand distribution (p50, p90, p99) so that scaling policies can be tuned to the client's risk tolerance.
**Evaluation metric:** Weighted Absolute Percentage Error (WAPE) at the p90 level — under-prediction is penalized 3x vs. over-prediction because outages cost more than over-provisioning. Secondary metric: percentage of scaling events where the model's forecast would have triggered pre-scaling before demand hit.
**Scope:** Each client workload is essentially a separate forecasting problem. A single ML engineer can build the pipeline in 2-3 months, starting with a generic LSTM architecture fine-tuned per workload. The main challenge is handling regime changes (client migrates from monolith to microservices, fundamentally altering the demand profile). Requires integration with auto-scaling APIs for closed-loop deployment.
**Data availability:** CloudWatch and equivalent metrics are readily available with 15-month retention. The challenge is correlating demand patterns with external events — most clients do not systematically log marketing campaigns or product launches in a machine-readable format.

---

## 3. Security Misconfiguration Detection & Prioritization
#gradient-boosting #binary-classification #tabular-ml #compliance

**Problem statement:** Cloud environments accumulate security misconfigurations over time — overly permissive IAM policies, unencrypted data stores, public-facing resources that should be private, stale access keys. CSPM tools flag all of them equally, producing alert fatigue. The actual risk of a misconfiguration depends on context: a public S3 bucket containing static website assets is benign; one containing customer PII is critical.

**ML task:** Binary Classification (exploitable risk vs. low-risk finding) + Ranking (prioritizing by blast radius)
**Input data:** CSPM findings (resource type, rule violated, severity label from tool), resource metadata (tags, data classification labels if available, network exposure via security group analysis), IAM policy analysis (who/what can access the resource, whether access is cross-account), historical remediation data (was this finding type previously remediated or accepted as exception). Approximately 30-50 features per finding after engineering.
**Target:** Binary label: requires-remediation vs. acceptable-risk, derived from the consulting firm's historical triage decisions across client environments. Secondary target: estimated blast radius score (1-10) based on data sensitivity, network exposure, and access scope.
**Evaluation metric:** Recall at 95% for the requires-remediation class (missing a true security risk is unacceptable). Precision is secondary but must exceed 60% to avoid recreating the alert fatigue problem. F2-score as the primary combined metric.
**Scope:** 2 ML engineers + 1 security architect, 3-4 months for MVP. Requires historical triage data from at least 20 client environments over 6+ months. Feature engineering around IAM policy analysis is non-trivial — parsing JSON policy documents into features that capture effective permissions requires a dedicated preprocessing pipeline.
**Data availability:** CSPM tools export findings via API. Historical triage decisions are the bottleneck — most firms track these in Jira tickets or spreadsheets without structured labels. A data collection phase of 2-3 months (instrumenting the triage workflow) is likely needed before model training can begin.

---

## 4. Client Infrastructure Health Scoring
#random-forest #regression #tabular-ml #data-integration

**Problem statement:** Cloud consultants need a single, defensible "health score" for each client environment to prioritize engineering attention, justify engagements to client leadership, and track improvement over time. Today, this assessment is subjective — a senior architect's gut feeling based on their last interaction with the environment — and inconsistent across the firm.

**ML task:** Regression (predicting a composite health score) with feature importance for explainability
**Input data:** Aggregated metrics per client environment: cost efficiency ratio (actual spend vs. optimized spend), compliance posture (percentage of findings remediated), operational metrics (mean time to recovery, alert-to-resolution time, deployment frequency), architecture quality indicators (percentage of resources managed by IaC, drift detection results, unused resource count), and security posture (critical/high findings count, mean age of unresolved findings). Approximately 40-60 features per environment.
**Target:** A continuous health score (0-100) calibrated against architect assessments. Training labels come from quarterly business reviews where senior architects rate each client environment on a standardized rubric. The model must produce feature-importance explanations so that the score is actionable ("Your score dropped 12 points this month primarily because IaC drift increased by 30% and three critical security findings are unresolved for >60 days").
**Evaluation metric:** Mean Absolute Error (MAE) between predicted and architect-rated scores, with a target MAE < 5 points on a 100-point scale. Spearman rank correlation > 0.85 (the ranking of environments by score must match architect intuition even if absolute values differ).
**Scope:** 1 ML engineer + 1 data engineer, 3-4 months. The hardest part is not the model (a random forest or gradient boosting model will suffice) but the data integration — pulling metrics from 5-10 different tools per client (billing, monitoring, CSPM, IaC state, ticketing) into a unified feature set. Requires buy-in from senior architects to provide calibration labels during quarterly reviews.
**Data availability:** All input data exists in the firm's toolchain but is siloed. The data engineering effort to build the feature pipeline is 60-70% of the total project effort. Calibration labels require structured architect input, which must be designed into the quarterly review process.
