# Machine Learning Opportunities — BI & Analytics Platforms

**Industry:** [[bi-analytics-platforms|BI & Analytics Platforms]]
**Derived from:** [[problems/bi-analytics-platforms/high-impact|High Impact]], [[problems/bi-analytics-platforms/low-impact-1|Low Impact 1]], [[problems/bi-analytics-platforms/low-impact-2|Low Impact 2]], [[problems/bi-analytics-platforms/worker-life-1|Worker Life 1]], [[problems/bi-analytics-platforms/worker-life-2|Worker Life 2]]

---

## 1. Metric Definition Fingerprinting and Drift Detection
#bert #word-embeddings #graph-neural-networks #dbscan #large-language-models #hypothesis-testing #feature-engineering #evaluation-metrics

**Problem statement:** Organisations hold several defensible definitions of their most important metrics, discover the divergence only when two numbers meet in a room, and spend the meeting reconciling. The semantic layer solves this where adopted, adoption is always partial, and the ungoverned periphery holds most of the assets and all of the drift.

**ML task:** Semantic fingerprinting of computed fields from query logic, clustering by business term, and divergence detection weighted by usage
**Input data:** Query and dashboard definitions across the asset estate; parsed SQL with tables, joins, filters and aggregations; field names and labels; lineage graphs; asset usage telemetry by viewer and role; semantic layer definitions where present.
**Target:** Pairs of assets computing the same business term with materially different logic, as adjudicated by an analytics engineer.
**Evaluation metric:** Precision on flagged divergences, weighted by combined usage — the four divergences appearing in executive reporting matter and two hundred in unused assets do not. Recall against a manually audited sample of a business domain, since the failure that hurts is the divergence nobody found.
**Scope:** Full query equivalence is undecidable in general and unnecessary here; the target is likely divergence for human adjudication, which is far easier. Lineage-aware comparison catches the subtle case where two dashboards agree at the metric level and diverge upstream. The resolution path — proposed canonical definition, owner, and a migration list showing which numbers would change and by how much — is what makes the finding actionable rather than demoralising. 2-3 ML engineers plus an analytics engineer, 5-6 months.
**Data availability:** Complete within every platform. Query definitions, lineage and usage telemetry all exist and are never joined for this purpose.

---

## 2. Asset Lifecycle Classification for Estate Management
#gradient-boosting #bert #word-embeddings #dbscan #k-means-clustering #evaluation-metrics #automation

**Problem statement:** Mature deployments hold thousands of dashboards, most rarely opened, many near-duplicates, and a significant number silently broken. Nothing is deleted because deleting something in use is a visible failure while keeping it costs nothing visible, so the estate grows monotonically and discovery fails.

**ML task:** Multiclass classification of assets into archive, deduplicate, repair or certify, combined with near-duplicate clustering on query semantics
**Input data:** Asset definitions and query logic; usage telemetry by asset, viewer and role; lineage and downstream dependencies; execution results including zero-row and error outcomes; source table deprecation status; author and last-modified history.
**Target:** The disposition an owner ultimately agrees with, gathered from a governance review of a sampled subset.
**Evaluation metric:** Precision on archive recommendations is the constraint, since archiving something in use is exactly the failure that made everyone stop deleting. Report reversal rate on archived assets — how many were restored — as the operational metric, and make archival reversible so the cost of an error is a click.
**Scope:** Brokenness detection needs no modelling and delivers the most immediate value, because a silently zero-row dashboard is actively harmful. Duplicate detection over query semantics is straightforward. Evidence-based certification — widely used, built on governed sources, consistent with canonical definitions, not broken — replaces a volunteer process that goes stale. 2 ML engineers, 4 months.
**Data availability:** Excellent. Every platform collects the telemetry and none of it drives any action.

---

## 3. Series-Aware Data Quality Monitoring
#change-point-detection #time-series-forecasting #gaussian-mixture-models #hypothesis-testing #confidence-intervals #evaluation-metrics #automation

**Problem statement:** Data quality tests are hand-written with hand-guessed thresholds, so they either fire constantly and get muted or never fire. Real business data has weekly seasonality, month-end spikes and step changes when a large customer onboards, and generic anomaly detection treats all of those as incidents, which is what produces the muting.

**ML task:** Per-series structural modelling with seasonality and regime change, driving anomaly detection on volume, freshness and distribution; plus consequence-weighted alert routing
**Input data:** Historical row counts, freshness timestamps and column distributions per table and partition; calendar structure; known business events such as customer onboardings and product launches; lineage graphs; downstream asset usage; historical incident records with root causes.
**Target:** A genuine data incident as confirmed by the engineer who investigated it.
**Evaluation metric:** Precision is the metric that determines whether anyone reads the alerts — a channel with a low precision rate is muted within a fortnight and then the tool has negative value. Report precision and recall separately for volume, freshness and distributional anomalies, since distributional shift is the silent failure class and is both the hardest and the most valuable.
**Scope:** Modelling seasonality and step changes properly is a modest time-series problem that the existing tooling approximates rather than solves, and it is the difference between a trusted channel and a muted one. Consequence routing — is this table read by the board deck or by nothing — uses lineage and usage the platform already holds. Silent failures that produce plausible-but-wrong output are the remaining hard case and require distributional rather than count-based detection. 2 ML engineers, 4-5 months.
**Data availability:** Warehouse metadata and query history provide the series. Incident labels exist in ticketing systems and are inconsistently linked to the table that failed.

---

## 4. Question-to-Existing-Asset Retrieval
#large-language-models #bert #word-embeddings #k-nearest-neighbors #transfer-learning #evaluation-metrics #workflow-orchestration

**Problem statement:** Analysts spend their day answering questions that a dashboard already answers, frequently by opening that dashboard and copying the number. Self-service failed on discovery and trust rather than on capability, and generating fresh SQL for every question manufactures new definition drift at speed.

**ML task:** Retrieval and ranking of existing assets against a natural language question, with grounded generation only as a fallback and only against canonical definitions
**Input data:** Asset definitions, titles, descriptions and query logic; usage telemetry and certification status; the canonical metric layer; historical analyst request threads with the asset or query that eventually answered them; column and table documentation.
**Target:** The asset that actually answered the question, taken from analyst request history.
**Evaluation metric:** Top-1 and top-3 retrieval accuracy against historical resolved requests, with a separate measure for correctly declining to answer — saying no asset covers this is far better than returning a plausible wrong dashboard. For any generated query, agreement with canonical definitions is a hard gate rather than a metric.
**Scope:** Retrieval over existing assets is both more tractable and considerably safer than text-to-SQL, and it is the version that reduces drift rather than creating it. Repeat request detection — the same question asked four times is a dashboard that should exist — needs no modelling and is the highest-value operational output. Instrumenting the request queue at all is a prerequisite most organisations have not done. 2 ML engineers, 4-5 months.
**Data availability:** Asset metadata is complete. Historical request-to-answer pairs live in Slack threads and ticket systems and must be assembled, which is the main data engineering task.
