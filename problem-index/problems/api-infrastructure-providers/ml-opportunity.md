# Machine Learning Opportunities — API Infrastructure Providers

**Industry:** [[api-infrastructure-providers|API Infrastructure Providers]]
**Derived from:** [[problems/api-infrastructure-providers/high-impact|High Impact]], [[problems/api-infrastructure-providers/low-impact-1|Low Impact 1]], [[problems/api-infrastructure-providers/low-impact-2|Low Impact 2]], [[problems/api-infrastructure-providers/worker-life-1|Worker Life 1]], [[problems/api-infrastructure-providers/worker-life-2|Worker Life 2]]

---

## 1. Consumer Dependency Graph and Breaking Change Impact
#graph-neural-networks #gradient-boosting #dbscan #survival-analysis #confidence-intervals #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** Providers cannot enumerate who depends on an API, so nothing is ever removed and surfaces grow monotonically. The gateway carries every request and computes rate limits from it while answering none of the dependency questions.

**ML task:** Graph construction over consumers, operations and fields from observed traffic, plus classification of which consumers would break under a proposed change
**Input data:** Request logs with consumer identity, operation, parameters and frequency over time; response payloads where inspectable; client library telemetry where the provider ships the library; historical breaking changes with the incidents and support tickets that followed; consumer registration metadata.
**Target:** Consumers who actually broke following a historical change, taken from incident and support records.
**Evaluation metric:** Recall on consumers that broke is the binding constraint, since a missed dependency is an outage for someone else. Report precision too, because over-predicting breakage recreates the paralysis the system exists to remove. Field-level usage inference should be evaluated separately against client instrumentation ground truth where it exists.
**Scope:** Field-level usage is the high-value extension and the hard one — knowing a field is returned to eleven consumers and parsed by none makes removal a decision rather than a risk. Where the provider ships client libraries, instrumenting them is the cleanest path; otherwise inference from consumer request patterns and selection parameters is partial and should be reported as such. Consumer criticality and human reachability are metadata problems rather than modelling ones and are equally blocking. 2-3 ML engineers, 5-6 months.
**Data availability:** Traffic logs are complete and voluminous. Response body inspection raises retention and privacy questions that must be settled before it is sampled. Historical breakage labels are sparse and come from incident records that were not written for this purpose.

---

## 2. Continuous Specification Conformance from Live Traffic
#hypothesis-testing #bert #large-language-models #change-point-detection #confidence-intervals #evaluation-metrics #data-integration

**Problem statement:** Specifications describe intent and consumers integrate against behaviour, so behaviour is the real contract and it is unverified. Contract testing checks a specification in a test environment; the divergences live in production, where nothing compares the two.

**ML task:** Conformance checking of observed requests and responses against the specification, plus specification induction where none exists and behavioural change detection across deployments
**Input data:** Live request and response payloads sampled from the gateway; the current OpenAPI or equivalent specification; deployment and release history; historical specification versions.
**Target:** Divergences between specification and behaviour — undocumented fields, unlisted enum values, nullability violations, unexpected status codes — and behavioural changes coinciding with a deployment.
**Evaluation metric:** Precision on reported divergences, since a conformance report full of sampling artefacts is ignored immediately. For change detection, lead time from deployment to alert, and false positive rate per deployment, which determines whether the check can gate a release.
**Scope:** Most of this is deterministic comparison rather than learning; the modelling is in distinguishing a genuine contract change from normal variation in a sampled stream, which is a statistical question about rare values. Specification induction from traffic is most valuable for internal APIs that were never specified, where the generated document is strictly better than nothing. Sampling strategy matters enormously — rare enum values appear rarely by definition. 2 ML engineers, 4 months.
**Data availability:** Complete at the gateway, subject to payload retention policy. Specifications exist for most external APIs and for a minority of internal ones.

---

## 3. Usage Segmentation and Bill Shock Prediction
#k-means-clustering #gradient-boosting #time-series-forecasting #logistic-regression #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Pricing design determines the economics of an API business, is set by intuition and competitor copying, and is very hard to change afterwards. Meanwhile the provider holds complete usage data for every customer and uses it only to compute invoices.

**ML task:** Clustering customers by usage shape, forecasting period-end usage per customer, and predicting bills materially exceeding customer expectation
**Input data:** Per-customer usage event streams by operation and resource; billing history and plan structure; customer attributes and tenure; support tickets and credits related to billing; historical churn and usage caps applied by customers; infrastructure cost attribution per operation where available.
**Target:** Period-end usage and charge; and separately, billing disputes, credits or defensive usage caps as evidence of bill shock.
**Evaluation metric:** For forecasting, quantile accuracy on period-end charge with enough lead time to warn — a prediction on the last day is useless. For bill shock, precision on customers who subsequently disputed or capped, since the intervention is an outbound conversation that costs goodwill if unnecessary.
**Scope:** Bill shock prediction is the highest-value component and the easiest, and telling a customer before the invoice is both better service and cheaper than a credit. Cost-to-serve alignment — whether the billable unit correlates with what serving actually costs — requires infrastructure cost attribution that most providers have not built and that reveals structurally unprofitable customers. Elasticity estimation is possible only where price variation exists, including across grandfathered cohorts, and should not be attempted otherwise. 2 ML engineers plus a pricing analyst, 4-5 months.
**Data availability:** Usage and billing data are complete. Cost attribution per operation is the gap and is an infrastructure accounting project rather than a modelling one.

---

## 4. Error Attribution and Consumer Failure Clustering
#gradient-boosting #bert #word-embeddings #k-means-clustering #change-point-detection #evaluation-metrics #automation #worker-facing

**Problem statement:** Integration support spends most of every ticket establishing whose fault a failure is, in an interaction that is adversarial by construction, when the gateway logged both the request and the response at the time. The same consumer misunderstandings recur endlessly and are handled as individual tickets rather than as design findings.

**ML task:** Classification of failure cause from the logged request and response, plus clustering of consumer error patterns and change detection on per-consumer error rates
**Input data:** Request and response pairs with status codes and error bodies; consumer identity, client library and version; authentication state; rate limit state; historical tickets with their resolved cause; parameter values and their validity.
**Target:** The fault attribution a support engineer ultimately reached — consumer error, provider error, third party, or expected behaviour misunderstood.
**Evaluation metric:** Attribution accuracy against resolved tickets, with provider-error recall weighted heavily because incorrectly telling a customer the fault is theirs when it is not is the failure that damages the relationship. For proactive detection, lead time on a consumer's error rate jump relative to when they reported it.
**Scope:** Self-service request inspection removes most of the volume and all of the blame dynamic without any modelling — the consumer looks up their own request and sees what was wrong. The clustering output is the durable value: a parameter that a hundred consumers misuse is a naming problem, and that finding never currently reaches the API design conversation. 2 ML engineers, 4 months.
**Data availability:** Gateway logs are complete. Ticket resolutions provide labels of moderate quality, since engineers record the fix rather than the attribution.
