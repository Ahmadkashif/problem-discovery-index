# Machine Learning Opportunities — Cloud Cost Management

**Industry:** [[cloud-cost-management|Cloud Cost Management]]
**Derived from:** [[problems/cloud-cost-management/high-impact|High Impact]], [[problems/cloud-cost-management/low-impact-1|Low Impact 1]], [[problems/cloud-cost-management/low-impact-2|Low Impact 2]], [[problems/cloud-cost-management/worker-life-1|Worker Life 1]], [[problems/cloud-cost-management/worker-life-2|Worker Life 2]]

---

## 1. Ownership Inference for Untagged Infrastructure
#graph-neural-networks #gradient-boosting #k-means-clustering #dbscan #feature-engineering #confidence-intervals #evaluation-metrics #data-integration

**Problem statement:** Cost attribution depends on tagging, tagging has resisted governance for a decade, and the unallocated remainder is large and concentrated in exactly the shared, cross-cutting resources where the spend is. Reporting therefore reaches finance and never reaches the engineer who could act.

**ML task:** Multiclass classification of owning team for untagged resources, using infrastructure metadata and relationship structure
**Input data:** Resource creation events with creator identity; account, project and subscription structure; naming conventions; network topology and security group relationships; deployment source (infrastructure-as-code repository, pipeline, console); traffic and dependency relationships between resources; correctly tagged resources as labels.
**Target:** The owning team as confirmed when a tag is eventually applied or an owner is identified.
**Evaluation metric:** Accuracy on held-out tagged resources, reported by resource type, since shared services and managed offerings are much harder than compute instances. Confidence calibration matters because an allocation presented as certain and disputed once will be ignored thereafter — the product requirement is a stated confidence per allocation.
**Scope:** Creator identity and deployment source carry most of the signal and are frequently available even when tags are not. Shared service allocation is a different problem requiring dependency-based apportionment from query and traffic telemetry, and it has no correct answer, only defensible conventions — which means the convention must be visible and adjustable rather than hidden. Kubernetes allocation joins node billing to pod-level consumption and is its own project. 2-3 ML engineers, 5 months.
**Data availability:** Metadata is complete in cloud provider APIs. Correctly tagged resources provide abundant labels, though they are a biased sample — teams that tag well may be structurally different from those that do not.

---

## 2. Resource Purpose Classification for Credible Recommendations
#gradient-boosting #k-means-clustering #time-series-forecasting #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics

**Problem statement:** Rightsizing recommendations are computed from utilisation alone, so they confidently propose downsizing standbys, disaster recovery capacity and batch headroom. Two such recommendations are enough to make an engineer stop reading the feature permanently.

**ML task:** Classification of resource purpose — production, standby, disaster recovery, batch, development, canary — from behavioural and structural signals, used to gate and risk-annotate recommendations
**Input data:** Utilisation time series with their temporal shape; naming and tags where present; network position and traffic patterns; peer resources in the same account or cluster; deployment configuration and autoscaling settings; failover and health check configuration; historical recommendation acceptance, rejection and reversion.
**Target:** Resource purpose as confirmed by the owning engineer, gathered from recommendation feedback and a labelling exercise.
**Evaluation metric:** The metric that matters is realised saving per recommendation shipped, not notional saving generated — and the reversion rate, since an accepted recommendation that caused an incident is the failure that ends the programme. Report precision on the specific classes that cause the damage: standby and disaster recovery misclassified as waste.
**Scope:** Utilisation shape is highly diagnostic — a standby has a distinctive flat-then-spike profile, a batch workload is periodic, a canary tracks production at a fraction. Cross-organisational context is the vendor's unique asset: what utilisation is normal for this workload shape across thousands of companies distinguishes genuinely oversized from typical. Acceptance history is a free feedback loop that no platform currently closes. 2 ML engineers, 4 months.
**Data availability:** Utilisation and configuration data are complete. Purpose labels do not exist and must be created, initially through the recommendation feedback loop itself.

---

## 3. Commitment Portfolio Optimisation Under Uncertainty
#time-series-forecasting #monte-carlo-methods #optimization-fundamentals #confidence-intervals #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Commitments are one-to-three-year bets recommended by extrapolating ninety days of usage, on workloads that will be re-architected within eighteen months. Organisations that get burned under-commit defensively and pay full rate, which is itself a large recurring cost.

**ML task:** Probabilistic usage forecasting at commitment horizons, combined with portfolio optimisation over term, coverage and instrument flexibility under simulated scenarios
**Input data:** Historical usage by instance family, region and service; existing commitment portfolio with terms and expiry; architectural change signals — migration plans, roadmap items, deprecation notices where available; seasonality beyond typical lookback windows; contract discount structures; historical forecast error at long horizons.
**Target:** Realised usage over the commitment period and realised waste or shortfall against the position taken.
**Evaluation metric:** Expected saving net of waste under the recommended portfolio, evaluated against what actually happened, with the distribution reported rather than the mean. Calibration of the long-horizon forecast is the honest headline — a one-year forecast with an interval that turns out to be far too narrow is the failure mode that produces the defensive behaviour.
**Scope:** The forecast is genuinely uncertain at these horizons and the product contribution is presenting it as such rather than as a point recommendation with an optimistic saving. Planned architectural change is the most valuable input and is knowable inside the organisation while never reaching the tool — capturing even a coarse signal changes the answer materially. Continuous rebalancing rather than episodic review is the operational fix. 2 ML engineers plus a cloud economist, 5 months.
**Data availability:** Usage and commitment data are complete. Roadmap and migration plans exist in planning tools and have never been connected, which is an integration problem rather than a modelling one.

---

## 4. Spend Variance Decomposition and Anomaly Explanation
#change-point-detection #gradient-boosting #time-series-forecasting #hypothesis-testing #confidence-intervals #evaluation-metrics #automation

**Problem statement:** Spend rose eleven per cent and a FinOps practitioner spends days pivoting the bill and chasing engineers to explain it. Anomaly detection exists everywhere and notifies that a number moved, which is the least useful part of the answer.

**ML task:** Decomposition of spend change into price, quantity and mix components, with attribution of the quantity component to specific resources and the events that created them
**Input data:** Detailed billing records at resource and hourly granularity; rate and discount changes; resource creation, deletion and modification events; deployment and infrastructure-as-code change history; autoscaling events; traffic and workload telemetry; region and service expansions.
**Target:** The explanation a practitioner eventually recorded for a variance, gathered from their own investigation notes.
**Evaluation metric:** Proportion of variances explained without human investigation, and the accuracy of those explanations judged by the practitioner. Detection latency matters too — an explanation delivered when the change happens is worth far more than one at month end.
**Scope:** The decomposition is mostly deterministic arithmetic over billing detail and is not done because the data model in most tools aggregates too early. Attributing a quantity change to the deployment that caused it requires joining billing to change events, which is the integration that makes this work. Anomaly detection without explanation should be considered incomplete rather than a separate feature. 2 ML engineers, 4 months.
**Data availability:** Billing detail is complete and voluminous. Change event streams exist in CI/CD and infrastructure-as-code systems and are rarely joined to cost data.
