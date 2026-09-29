# Machine Learning Opportunities — Data Platform Integrators

**Industry:** [[data-platform-integrators|Data Platform Integrators]]
**Derived from:** [[problems/data-platform-integrators/high-impact|High Impact]], [[problems/data-platform-integrators/low-impact-1|Low Impact 1]], [[problems/data-platform-integrators/low-impact-2|Low Impact 2]], [[problems/data-platform-integrators/worker-life-1|Worker Life 1]], [[problems/data-platform-integrators/worker-life-2|Worker Life 2]]

---

## 1. Purpose-Aware Asset Value and Safe Pruning
#graph-neural-networks #gradient-boosting #k-means-clustering #confidence-intervals #causal-inference #evaluation-metrics #data-integration #revenue-impact

**Problem statement:** Every data platform carries an estate whose majority is unused, its owners cannot identify which part, and naive pruning by query count deletes the rare-but-essential while keeping the automatically-refreshed-and-unread.

**ML task:** Classify each asset by realised purpose and value using access frequency, lineage position, downstream consumer type and seasonality, joined to attributed compute cost
**Input data:** Query and dashboard access logs with consumer identity and type; lineage graph across models, marts, dashboards and reverse ETL syncs; compute cost attributed per model run; refresh schedules; asset metadata and delivery records from the integrator.
**Target:** Whether an asset is genuinely needed, adjudicated by owner review on a sampled set — there is no natural label and the labelling design is most of the honesty here.
**Evaluation metric:** Precision on deletion candidates must be extremely high, because the action is irreversible and the objection that has killed previous attempts is exactly the false positive: a model queried twice a year for a regulatory extract looks identical to dead inventory on a count. Report the rare-but-essential class separately and measure recall on it as a safety metric. Value-per-dollar ranking is the output that actually gets deletion approved.
**Scope:** Consumer type is the discriminating feature — a human dashboard, a machine sync, a regulatory extract and an unopened scheduled refresh have completely different implications for the same access count. Requires a post-go-live data access clause the industry does not currently write. 1-2 data scientists, 4-6 months.
**Data availability:** Complete inside the client platform and inaccessible to the integrator after handover. This is a contract problem.

---

## 2. Semantic Drift Detection With Consumption-Weighted Alerting
#change-point-detection #time-series-forecasting #hypothesis-testing #gradient-boosting #dbscan #confidence-intervals #evaluation-metrics #data-integration

**Problem statement:** Observability watches freshness, volume and schema, and the expensive failures are semantic — a categorical distribution shifting, a numeric scale changing, a join relationship becoming one-to-many — which pass every structural test while corrupting decisions.

**ML task:** Learn per-column distributional baselines and detect meaningful departures, then propagate the impact through lineage and query history to identify affected downstream reporting and its consumers
**Input data:** Column-level value distributions, cardinalities and null rates over time; join relationship cardinality; schema and upstream release history; lineage graph; query and access logs for consumption weighting; historical incidents with confirmed causes.
**Target:** Whether an observed distributional change corresponds to a genuine upstream semantic change, as confirmed by investigation.
**Evaluation metric:** Alert precision is the governing constraint, because a monitor that fires on ordinary variation gets muted within a fortnight and is then worse than nothing. Weight evaluation by downstream consumption — a missed change in a table feeding the board report and one in an unqueried staging model are not comparable errors, and an aggregate precision figure treats them as if they were. Measure detection lead time against the current mechanism, which is someone noticing a wrong number weeks later.
**Scope:** Baselines must be per-column and per-table; generic thresholds cannot work across columns with different natural variability. The propagation step — which reports were affected and who consumed them in the interim — is what determines whether anyone has to be told, and no observability product offers it. 2 engineers, 6 months.
**Data availability:** Excellent. Distributions are computable from the data itself, lineage from the transformation framework, consumption from query logs.

---

## 3. Legacy Estate Census and Behaviourally Risky Translation
#bert #transformers #large-language-models #graph-neural-networks #gradient-boosting #k-means-clustering #evaluation-metrics #automation

**Problem statement:** Migrations translate everything because nobody establishes what is used, and validation spreads evenly across thousands of translated queries when the risk concentrates in a handful of dialect behaviours.

**ML task:** Census the legacy estate for usage and dependency, classify code constructs by behavioural translation risk, cluster reconciliation differences by cause, and group reports by semantic equivalence for consolidation
**Input data:** Legacy platform query and report access logs; stored procedure, view and report definitions; dependency structure; dialect-specific construct inventory — implicit casts, null-sensitive aggregates, date arithmetic, ordering-dependent logic; legacy-versus-migrated output comparisons.
**Target:** For risk classification, whether a translated construct produced a numerical difference. For consolidation, whether two reports answer the same question, judged by analyst review.
**Evaluation metric:** Recall on constructs that actually produced differences is what matters for the risk classifier, since a missed behavioural difference ships a wrong number onto the new platform. For reconciliation clustering, the measure is reduction in human adjudication time at unchanged decision quality — thousands of row-level differences usually reduce to a handful of causes, and the win is presenting them that way.
**Scope:** The usage census should run first and typically cuts scope substantially, which is the reason it is not run first by firms billing on scope — a conflict worth naming rather than engineering around. Semantic report consolidation is the highest-value and least-attempted piece: four thousand reports usually represent a few hundred distinct questions. 2 engineers, 6-9 months.
**Data availability:** Legacy usage logs exist and are frequently disabled or unexamined; enabling them is step one.

---

## 4. Model Discovery, Intent Reconstruction and Discrepancy Explanation
#bert #contrastive-learning #large-language-models #graph-neural-networks #k-nearest-neighbors #word-embeddings #evaluation-metrics #worker-facing

**Problem statement:** An analytics engineer's day begins with working out which of four similarly-named models is the right one, why it exists, and whether two disagreeing numbers indicate a defect or a definition — and none of those answers are recorded anywhere.

**ML task:** Semantic retrieval over models, columns and metrics weighted by actual usage; intent linkage from models to the tickets and discussions that created them; automated explanation of numerical discrepancies from lineage and definition comparison
**Input data:** Model SQL, column names and descriptions; query logs for usage weighting; lineage; pull requests, tickets and discussion threads; metric definitions and their history; prior discrepancy investigations and their resolutions.
**Target:** For retrieval, whether the returned model is the one the engineer used. For discrepancy explanation, the cause as determined by investigation.
**Evaluation metric:** Retrieval accuracy on realistic queries, weighted by usage so that returning a dead model that matches the name is scored as the failure it is. For discrepancy explanation, top-3 cause accuracy — an engineer can evaluate three hypotheses quickly — and the proportion of investigations resolved without full lineage traversal. Abstention must be treated as correct where no recorded intent exists: inventing a rationale for a model built to satisfy a specific regulatory requirement is considerably worse than saying it is unrecorded.
**Scope:** Recording discrepancy resolutions so the same definitional question is answered before the next person asks is a workflow change with most of the long-run value. Blast-radius reporting on proposed changes, weighting dependencies by whether they are actually queried, converts a nervous change into an assessed one. 2 engineers, 4-6 months.
**Data availability:** Model code, lineage and query logs are complete. Discussion history requires integration and is where intent actually lives.
