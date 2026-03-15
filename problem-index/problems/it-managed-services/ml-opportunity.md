# Machine Learning Opportunities — IT Managed Services

**Industry:** [[it-managed-services|IT Managed Services]]
**Derived from:** [[problems/it-managed-services/high-impact|High Impact]], [[problems/it-managed-services/low-impact-1|Low Impact 1]], [[problems/it-managed-services/low-impact-2|Low Impact 2]], [[problems/it-managed-services/worker-life-1|Worker Life 1]], [[problems/it-managed-services/worker-life-2|Worker Life 2]]

---

## 1. Ticket Auto-Classification and Intelligent Routing
#bert #llm #text-classification #nlp #automation #revenue-impact

**Problem statement:** Inbound tickets arrive as unstructured text mixing end-user language with technical jargon, and must be classified by issue category, urgency, affected system, and appropriate technician tier — currently done manually or with brittle keyword rules that misroute 20-30% of tickets.

**ML task:** Multi-label text classification (issue category + urgency + tier assignment)
**Input data:** Ticket subject line, description body, client metadata (industry, agreement tier, device count), historical resolution notes for the same client. Sources: ConnectWise Manage, Autotask, or HaloPSA ticket exports.
**Target:** Issue category (20-30 classes: password reset, printer, VPN, email, backup failure, etc.), urgency level (P1-P4), technician tier (L1/L2/L3), and recommended resolution template ID.
**Evaluation metric:** Macro F1 across issue categories, with weighted penalty for tier misroutes (routing L1 to L3 wastes expensive labor; routing L3 to L1 causes SLA breaches). Aim for >90% accuracy on tier assignment.
**Scope:** Fine-tune a BERT-class model on 50-100K historical tickets from a multi-tenant MSP dataset. 2-3 ML engineers, 8-12 weeks to production MVP. The main challenge is label quality: historical ticket categories in PSA systems are inconsistently applied by technicians.
**Data availability:** High — every MSP has years of ticket history in their PSA. The labeling challenge is that historical categories were applied by humans inconsistently. A relabeling pass using resolution notes (what was actually done) rather than initial categorization improves label quality significantly.

---

## 2. Alert Noise Reduction and Actionability Scoring
#gradient-boosting #binary-classification #tabular-ml #worker-facing

**Problem statement:** RMM monitoring generates 300-800 alerts daily for a mid-size MSP, with 80%+ being non-actionable noise, burying genuine incidents and causing technician alert fatigue.

**ML task:** Binary classification (actionable vs. non-actionable) with calibrated probability output
**Input data:** Alert type, severity level, device class, device age, time of day, day of week, client agreement tier, alert frequency for this device in the last 7/30/90 days, concurrent alerts from the same client, historical resolution (escalated vs. auto-resolved vs. dismissed). Sources: RMM alert logs (Datto, ConnectWise Automate, NinjaRMM).
**Target:** Binary label: was this alert escalated to a ticket and required human intervention (1) or was it dismissed/auto-resolved (0)?
**Evaluation metric:** Recall at 99% for actionable alerts (cannot afford to suppress a real incident); precision on non-actionable is secondary but target >85% to meaningfully reduce noise. Area under precision-recall curve as the aggregate metric.
**Scope:** Gradient-boosted model (XGBoost/LightGBM) on tabular features extracted from RMM alert history. 1-2 ML engineers, 6-8 weeks. Feature engineering is the primary effort: temporal patterns (alert bursts), device-level alert history, and cross-device correlation within a client site. Requires 6-12 months of labeled alert history.
**Data availability:** High — RMM platforms log every alert with timestamp, type, and eventual disposition. The implicit label (was a ticket created?) is already in the PSA. Joining RMM alerts to PSA tickets by timestamp and device is the main data engineering task.

---

## 3. Client Churn Prediction from Ticket and Engagement Patterns
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** MSPs lose 10-15% of clients annually, often with minimal warning — the client simply doesn't renew. Early identification of at-risk clients enables proactive intervention by account managers.

**ML task:** Binary classification (churn within 90 days: yes/no)
**Input data:** Monthly ticket volume and trend, SLA breach count and trend, average first-response time, technician satisfaction survey scores (if collected), QBR attendance, contract renewal date proximity, client growth metrics (endpoint count change over time), billing dispute history, executive sponsor engagement (email/meeting frequency from CRM). Sources: PSA, RMM, CRM (HubSpot/ConnectWise Sell).
**Target:** Binary label: did this client churn (non-renew or cancel) within 90 days of the observation date?
**Evaluation metric:** Recall at 80%+ (catch most at-risk clients) with precision >50% (account managers can handle some false positives). AUC-ROC as aggregate metric. The cost of a false negative (missed churn) is $5-15K/month in lost recurring revenue; the cost of a false positive (unnecessary outreach) is 2 hours of account manager time.
**Scope:** Tabular model on aggregated monthly client-level features. 1-2 ML engineers, 6-8 weeks. The main challenge is small dataset size: an MSP with 200 clients may see only 20-30 churns per year, requiring either multi-MSP data pooling or careful regularization and cross-validation.
**Data availability:** Medium — ticket and SLA data is readily available, but CRM engagement data and survey scores are spottier. Multi-MSP data pooling (through a vendor platform) would significantly improve model quality but requires data sharing agreements.

---

## 4. Endpoint Failure Prediction from RMM Telemetry
#random-forest #gradient-boosting #binary-classification #time-series-forecasting #tabular-ml

**Problem statement:** MSPs are reactive to hardware failures — a server disk fails, a workstation blue-screens — causing emergency tickets, SLA breaches, and client frustration. RMM agents already collect the telemetry that could predict failures before they happen.

**ML task:** Binary classification (device failure within 30 days: yes/no) with time-series feature extraction
**Input data:** Daily RMM telemetry: CPU utilization patterns, disk I/O latency trends, disk SMART attributes, memory usage, event log error frequency, uptime/reboot frequency, ambient temperature (where available), device age, device model, firmware version. Sources: Datto RMM, ConnectWise Automate, NinjaRMM agent telemetry databases.
**Target:** Binary label: did this device experience a hardware failure (disk, PSU, motherboard, RAM) requiring replacement within 30 days?
**Evaluation metric:** Recall >85% for true failures (early warning must catch most events), precision >40% (some false alarms are acceptable if they prompt proactive checks). The cost asymmetry is extreme: a predicted failure caught early costs $200 in proactive replacement labor; a missed failure costs $2,000-5,000 in emergency response and client downtime.
**Scope:** Feature engineering over time-series RMM telemetry (rolling statistics, trend slopes, anomaly indicators) fed into gradient-boosted or random forest models. 2-3 ML engineers, 10-14 weeks. Requires at least 12 months of telemetry with labeled failure events. The primary challenge is label availability: "hardware failure" must be extracted from ticket resolution notes, which requires NLP-based label extraction as a preprocessing step.
**Data availability:** Medium — RMM platforms collect telemetry but retention periods vary (30-90 days by default; extended retention requires configuration). Failure labels must be inferred from ticket data. MSPs that have extended their telemetry retention to 12+ months and maintain clean asset records are best positioned.

---

## 5. Technician Utilization Optimization and Scheduling
#linear-regression #gradient-boosting #regression #tabular-ml #workflow-orchestration

**Problem statement:** MSP dispatchers assign tickets to technicians based on availability and rough skill match, but suboptimal scheduling leaves some technicians over-utilized (causing burnout and quality drops) while others are under-utilized, and on-site visits are not batched geographically.

**ML task:** Regression (predicted resolution time per ticket-technician pair) feeding a constrained optimization scheduler
**Input data:** Ticket category, complexity indicators (number of affected devices, client environment size), technician skill profile (certifications, historical resolution time by category), technician current queue depth, client site location (for on-site dispatch), technician location, time-of-day preferences. Sources: PSA ticket data, HR/skill matrices, GPS or address data for on-site scheduling.
**Target:** Predicted resolution time in minutes for each ticket-technician pair, used as input to a scheduling optimizer that minimizes total queue time while balancing utilization across the team.
**Evaluation metric:** Mean absolute error on resolution time prediction (target <15 minutes MAE). Downstream metric: standard deviation of daily utilization across technicians (lower is better, indicating balanced workload) and average ticket wait time.
**Scope:** Two-stage system: a regression model predicting resolution time, and an optimization layer (constraint programming or greedy heuristic) for assignment. 2 ML engineers + 1 backend engineer, 10-12 weeks. Resolution time prediction benefits from per-technician historical data, so cold-start for new technicians requires fallback heuristics.
**Data availability:** High — PSA systems record ticket assignment, start time, and resolution time. Skill matrices are often informal (in the service manager's head) and would need to be formalized. Geographic data for on-site optimization requires client site addresses, which are in the PSA but may not be clean.
