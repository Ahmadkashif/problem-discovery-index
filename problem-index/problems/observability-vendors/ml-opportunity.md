# Machine Learning Opportunities — Observability Vendors

**Industry:** [[observability-vendors|Observability Vendors]]
**Derived from:** [[problems/observability-vendors/high-impact|High Impact]], [[problems/observability-vendors/low-impact-1|Low Impact 1]], [[problems/observability-vendors/low-impact-2|Low Impact 2]], [[problems/observability-vendors/worker-life-1|Worker Life 1]], [[problems/observability-vendors/worker-life-2|Worker Life 2]]

---

## 1. Incident Hypothesis Ranking from Signature and Structure
#graph-neural-networks #causal-inference #change-point-detection #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #time-series-forecasting

**Problem statement:** During an incident everything correlates, and the engineer must separate cause from consequence under time pressure at whatever hour it is. The vendor holds a corpus of how production software fails across thousands of organisations, in which failure modes repeat far more than any individual engineer can see.

**ML task:** Ranking candidate explanations using temporal precedence over a service dependency graph, change correlation, and matching against a corpus of abstracted failure signatures
**Input data:** Metric, trace and log telemetry at incident-relevant resolution; service dependency graphs derived from tracing; deployment, configuration, feature flag and infrastructure change events; historical incidents with their confirmed root causes and resolutions; abstracted cross-customer failure signatures.
**Target:** The root cause as recorded in the post-incident review.
**Evaluation metric:** Top-3 hypothesis accuracy is the right target rather than top-1, because an engineer evaluates hypotheses quickly and cannot evaluate a verdict. Calibration is essential — a confidently wrong diagnosis costs time at the most expensive possible moment and destroys trust in the feature permanently. Report time-to-diagnosis improvement against a matched baseline of similar past incidents.
**Scope:** Temporal precedence at fine resolution plus dependency structure is the closest thing to causal evidence available and requires tracing coverage that many customers do not have. Cross-customer learning is where the leverage is and is contractually awkward — the workable form abstracts signatures away from customer service names and semantics, and demonstrating that convincingly is as much a legal and communications project as a technical one. 4 ML engineers plus an SRE domain expert, 9-12 months.
**Data availability:** Telemetry is enormous. Confirmed root causes come from post-incident reviews, which are written inconsistently, sometimes not at all, and rarely in a structured form — this is the binding labelling constraint.

---

## 2. Telemetry Value Attribution and Retention Policy
#gradient-boosting #k-means-clustering #logistic-regression #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Observability spend rivals the infrastructure being observed and customers cut by volume because volume is the only attribute they can see. Value is invisible: nobody knows which signals have been queried, which appeared in an incident investigation, or which underpin an alert that has ever fired usefully.

**ML task:** Value scoring per telemetry stream from query, alert and incident participation, combined with cost attribution, driving retention and sampling policy
**Input data:** Query logs with the streams touched, by user and context; alert definitions and their firing history with outcomes; incident investigation traces showing which data was examined; ingestion volume and cost per stream; stream metadata and ownership.
**Target:** Whether a stream was materially used within a window, and whether its removal would have degraded an actual investigation.
**Evaluation metric:** The honest test is retrospective: for streams the model would have dropped, how many appear in subsequent incident investigations. That is directly measurable and is the number a customer will ask for. Cost reduction achieved at a fixed regret rate is the summary metric.
**Scope:** The commercial conflict is unavoidable — telling customers what to stop paying for reduces revenue, which is why no vendor has surfaced this. It is also why a third party or an OpenTelemetry-based collector layer is a natural home for it. Intelligent sampling that preserves the unusual rather than the representative is a separable component and matters because rare requests are what incidents are made of. 2 ML engineers, 4-5 months.
**Data availability:** Query, alert and ingestion data are all complete inside the platform. Incident investigation traces — which data an engineer actually looked at — are collected by some platforms and not surfaced.

---

## 3. Alert Threshold Backtesting and Quality Measurement
#change-point-detection #time-series-forecasting #gaussian-mixture-models #hypothesis-testing #confidence-intervals #evaluation-metrics #automation

**Problem statement:** Thresholds are numbers an engineer guessed when a monitor was created and never revisited, on services whose behaviour changes underneath them. The result is alerts that fire constantly and get muted, or never fire and are mistaken for health. No platform reports which alerts have ever led to action.

**ML task:** Structural modelling of service metric behaviour with seasonality, regime changes and multi-modality; plus backtesting candidate thresholds against historical incidents
**Input data:** Historical metric series per service; deployment and scaling events; incident records with start and end times; alert firing history with acknowledgement, escalation and resolution outcomes; on-call routing and response data.
**Target:** Whether an alert firing corresponded to a genuine incident requiring action, and whether an incident had an alert that fired in time.
**Evaluation metric:** For recommended thresholds, precision and recall against the incident record under backtest — would this threshold have caught the real events without firing on ordinary variation. For quality measurement, the deliverable is descriptive: an alert inventory classified into fired-and-actioned, fired-and-ignored, never-fired, and missed-the-incident. That inventory alone lets a team prune in an afternoon.
**Scope:** Real service metrics have strong daily and weekly seasonality, deploy-related step changes and genuinely multi-modal regimes, and generic anomaly detection that flags every Monday morning is worse than a static threshold — modelling the structure properly is the whole task. Symptom-level rather than cause-level alerting is a design principle the tooling should encourage and does not. 2 ML engineers, 4 months.
**Data availability:** Metric history and alert firing history are complete. Incident records exist in incident management tools and linking them to the metrics that moved is inconsistent.

---

## 4. Cardinality Explosion Prediction and Instrumentation Health
#change-point-detection #gradient-boosting #k-means-clustering #time-series-forecasting #confidence-intervals #evaluation-metrics #automation

**Problem statement:** A label with unbounded values added to a metric multiplies the time series count, and the customer discovers it through the bill or through query slowness. Support explains the concept repeatedly, and the explosion was detectable at the moment the label first appeared.

**ML task:** Early prediction of unbounded cardinality from a new label's value distribution in its first minutes, plus instrumentation completeness checking
**Input data:** Metric label value distributions over time from first appearance; historical cardinality trajectories with their eventual outcomes; service and agent inventory with versions; expected signal coverage per service; trace context propagation success across boundaries; query performance by pattern.
**Target:** Whether a newly observed label reaches problematic cardinality within a window.
**Evaluation metric:** Detection lead time in minutes from first appearance to the warning, and precision, since a false cardinality warning on a legitimately high-cardinality label is an annoyance the customer will remember. The financial metric is cost avoided, which is directly computable from the trajectory that did not happen.
**Scope:** Value distribution in the first few minutes is highly predictive — identifiers look nothing like enums — which makes this unusually tractable for the value delivered. Capping with an alert rather than silently ingesting is a product decision the category has avoided because ingestion is revenue. Instrumentation health checking is a separable, mechanical capability that would remove a large share of the support queue. 1-2 ML engineers, 3 months.
**Data availability:** Complete and immediate. This is among the best-posed problems in the vault and its absence is a product choice rather than a technical limitation.
