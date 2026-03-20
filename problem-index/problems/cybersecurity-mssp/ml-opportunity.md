# Machine Learning Opportunities — Cybersecurity MSSPs

**Industry:** [[cybersecurity-mssp|Cybersecurity MSSPs]]
**Derived from:** [[problems/cybersecurity-mssp/high-impact|High Impact]], [[problems/cybersecurity-mssp/low-impact-1|Low Impact 1]], [[problems/cybersecurity-mssp/low-impact-2|Low Impact 2]], [[problems/cybersecurity-mssp/worker-life-1|Worker Life 1]], [[problems/cybersecurity-mssp/worker-life-2|Worker Life 2]]

---

## 1. Alert True-Positive Scoring from Analyst Tacit Knowledge
#gradient-boosting #bert #transformers #feature-engineering #cross-validation #evaluation-metrics #word-embeddings #transfer-learning #entropy-cross-entropy-kl-divergence #tacit-knowledge-ml #revenue-impact

**Problem statement:** Senior SOC analysts can glance at an alert — its source, severity, MITRE mapping, timing, payload snippet, and client context — and classify it as true or false positive in seconds. This expert judgment integrates 15-20 signals simultaneously and is never documented. When that analyst leaves, their pattern recognition leaves too, and the MSSP's false positive rate spikes until a replacement builds the same intuition over 6-12 months.

**ML task:** Binary Classification (true positive vs. false positive) with natural language feature extraction from alert payloads
**Input data:** Structured alert metadata (source tool, rule ID, severity, MITRE ATT&CK technique, source/destination IP, port, user, asset criticality tag, client ID, timestamp, day-of-week, hour-of-day) concatenated with unstructured fields (alert description, raw log payload snippet, rule name). Historical analyst dispositions with timestamps. Per-client baselines (normal traffic patterns, known-good IPs, standard user behavior).
**Target:** Binary label — true positive (requires investigation) vs. false positive (noise). Ground truth refined by downstream investigation outcomes where available.
**Evaluation metric:** Recall at 99.5% for true positives (cannot miss real threats) with precision as secondary optimization. AUPRC preferred over AUROC due to extreme class imbalance (~5% positive rate). Per-client calibration required.
**Scope:** Requires 6-12 months of labeled disposition data across 20+ client environments to train a generalizable base model with per-client fine-tuning heads. A team of 2 ML engineers + 1 security domain expert over 4-6 months for MVP. The data pipeline (ingesting dispositions from ticketing systems like ServiceNow or Jira) is 40% of the work. BERT or similar encoder handles the unstructured payload; gradient-boosted trees handle the structured features; late fusion combines them.
**Data availability:** Disposition labels exist in every MSSP's ticketing system but are noisy — analysts use inconsistent close codes, and "false positive" often includes "true positive we chose not to escalate." Requires a labeling cleanup pass with senior analyst review. Alert metadata is abundant (thousands per day). The main gap is ground-truth confirmation: for most closed alerts, no one ever verified whether the dismissal was correct.

---

## 2. Threat Hunting Anomaly Detection Across Client Environments
#autoencoders #activation-functions #loss-functions #backpropagation #gradient-descent #descriptive-statistics #probability-distributions #feature-engineering

**Problem statement:** Threat hunters at MSSPs proactively search for signs of compromise that rule-based detection missed. They manually query SIEM data looking for unusual patterns — lateral movement, data exfiltration staging, living-off-the-land binary usage — across dozens of client environments. An automated anomaly detection system could surface the most suspicious behavioral deviations for human review, expanding threat hunting coverage from 2-3 clients per hunter per week to all clients continuously.

**ML task:** Anomaly Detection (unsupervised/semi-supervised) on behavioral telemetry time series
**Input data:** Aggregated behavioral features per entity (user, host, service account) per time window: authentication event counts, process execution profiles, network connection volume/destination diversity, file access patterns, privilege escalation events. Computed from SIEM and EDR telemetry. Per-client, per-entity baseline models.
**Target:** Anomaly score per entity per time window, ranked for human review. No explicit labels for training (unsupervised), but feedback loop from hunter investigations provides weak supervision over time.
**Evaluation metric:** Precision@k (of the top 50 anomalies surfaced daily, what fraction lead to a real investigation?) and time-to-detection for confirmed incidents that were first flagged by the system vs. discovered by other means.
**Scope:** Isolation forest or autoencoder per entity type, trained per client on 30-60 days of baseline data. Feature engineering is the hard part — defining meaningful behavioral features from raw SIEM logs requires security domain expertise. 2 ML engineers + 1 threat hunter over 3-4 months. Deploy as a daily digest to the threat hunting team, not an alerting system (to avoid creating more alert fatigue).
**Data availability:** Raw telemetry is abundant but noisy. Feature engineering from raw logs to behavioral profiles requires a well-maintained data pipeline. Ground truth is sparse — most anomalies will never be confirmed as malicious or benign, requiring the system to earn trust through demonstrated utility over months.

---

## 3. Client Security Risk Scoring & Gap Prioritization
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #descriptive-statistics #compliance

**Problem statement:** MSSPs assess each client's security posture periodically, but the scoring is subjective and inconsistent across analysts. A model that ingests each client's actual telemetry — patch cadence, endpoint coverage percentage, mean-time-to-respond, alert volume trends, vulnerability scan results, compliance control status — and outputs a calibrated risk score with prioritized gap recommendations would standardize assessments and enable continuous monitoring.

**ML task:** Multiclass Classification (risk tier: critical / high / medium / low) per control domain, with feature importance for gap explanation
**Input data:** Per-client feature vector: percentage of endpoints with EDR agent, mean patch latency (days), open critical vulnerability count, SIEM rule coverage percentage by MITRE technique, mean-time-to-acknowledge alerts, mean-time-to-resolve incidents, compliance control pass/fail status per framework, number of security incidents in trailing 90 days, industry vertical (for threat model weighting).
**Target:** Risk tier per control domain (endpoint, network, identity, data, compliance) and overall composite score. Labels derived from vCISO assessments on historical clients, calibrated against actual incident occurrence rates.
**Evaluation metric:** Weighted F1 across risk tiers, with heavier penalty for underestimating risk (classifying a critical-risk client as low). Calibration curve to ensure predicted probabilities match observed incident rates.
**Scope:** Requires structured feature extraction from 50+ client environments with at least 12 months of telemetry history. Gradient-boosted trees with SHAP explanations for each score. 1 ML engineer + 1 vCISO for feature definition over 2-3 months. The model is relatively simple; the data engineering to normalize features across heterogeneous client tool stacks is 60% of the work.
**Data availability:** Most features are already computed in SIEM/EDR dashboards but not aggregated into a single feature store. Historical vCISO assessments exist in slide decks and spreadsheets, requiring manual extraction for training labels. The dataset is small (50-200 clients) so regularization and cross-validation are critical.

---

## 4. Incident Response Time Prediction & SLA Risk Scoring
#gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #confidence-intervals #probability-distributions #revenue-impact

**Problem statement:** MSSPs operate under SLA commitments — typically 15-minute acknowledgment and 1-4 hour containment windows depending on severity. When multiple incidents occur simultaneously or during off-hours with reduced staffing, SLA breaches happen and trigger contractual penalties. A model that predicts expected resolution time for each incoming incident, given current SOC workload and analyst availability, would let shift leads proactively redistribute work and escalate before an SLA breach occurs rather than after.

**ML task:** Regression (predicted time-to-acknowledge and time-to-contain in minutes) with SLA breach probability as a derived binary output
**Input data:** Incident attributes at creation time (severity, incident type, client SLA tier, affected asset count, MITRE techniques involved), SOC state features (current queue depth, analyst count on shift, concurrent active incidents, time-of-day, day-of-week), historical performance features (analyst's average handle time for this incident type, client's historical complexity multiplier).
**Target:** Time-to-acknowledge (minutes) and time-to-contain (minutes). SLA breach probability derived by comparing predicted time to contractual threshold.
**Evaluation metric:** MAE in minutes for time predictions; AUROC for SLA breach probability. Business metric: reduction in SLA breaches per quarter.
**Scope:** Training data comes from ticketing system timestamps (incident created, acknowledged, contained, resolved). 6-12 months of incident history across all clients provides 5,000-20,000 training examples. Gradient-boosted regression with quantile outputs for uncertainty. 1 ML engineer over 2 months. The main challenge is capturing SOC state features in real-time — current queue depth and analyst availability may not be systematically logged.
**Data availability:** Incident timestamps are reliably recorded in ticketing systems. SOC staffing data may require integration with scheduling tools. The prediction is most valuable during high-load periods (overnight, weekends, concurrent incidents), which are also the periods with the least training data — requiring careful handling of distributional shift.
