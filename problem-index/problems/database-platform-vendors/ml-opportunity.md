# Machine Learning Opportunities — Database Platform Vendors

**Industry:** [[database-platform-vendors|Database Platform Vendors]]
**Derived from:** [[problems/database-platform-vendors/high-impact|High Impact]], [[problems/database-platform-vendors/low-impact-1|Low Impact 1]], [[problems/database-platform-vendors/low-impact-2|Low Impact 2]], [[problems/database-platform-vendors/worker-life-1|Worker Life 1]], [[problems/database-platform-vendors/worker-life-2|Worker Life 2]]

---

## 1. Degradation Forecasting from Fleet-Learned Thresholds
#change-point-detection #time-series-forecasting #gradient-boosting #survival-analysis #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics

**Problem statement:** Databases degrade gradually and fail at peak load. The engines expose every diagnostic needed to see it coming, and interpreting them requires specialists the managed service era removed. Thresholds do not transfer between workloads, which is why generic monitoring on database metrics produces noise.

**ML task:** Per-workload anomaly detection with fleet-derived failure trajectory matching, plus survival modelling of time to a threshold-crossing failure
**Input data:** Engine telemetry — plan statistics, wait events, buffer hit ratios, index usage and selectivity, bloat, lock waits, transaction identifier consumption, replication lag; table and index growth series; workload characteristics (read-write mix, transaction size, concurrency, working set); version and instance configuration; confirmed incidents across the fleet with their causes.
**Target:** A performance incident or availability event within a horizon, with its cause class.
**Evaluation metric:** Lead time on correctly predicted degradations is the value — a warning at the cliff is what already happens. Precision matters because these warnings go to teams without database specialists who cannot evaluate a false alarm, so report precision@k for a small weekly warning budget per database.
**Scope:** Per-workload baselining is essential because a buffer hit ratio that is excellent for one workload is catastrophic for another. Plan stability monitoring requires per-query plan tracking over time, which few systems retain and which is the prerequisite for detecting the most consequential failure class. Growth-driven threshold forecasting converts a cliff into a date and is the most legible output for a non-specialist. 3 ML engineers plus a database internals expert, 6-8 months.
**Data availability:** Telemetry is abundant across managed fleets. Incident labels require joining support records to telemetry and are inconsistently recorded. Plan history is the specific gap and is a product change before it is a modelling one.

---

## 2. Migration Duration, Lock and Blast Radius Prediction
#gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #graph-theory #evaluation-metrics #workflow-orchestration

**Problem statement:** Every substantial schema migration is planned individually by whoever has done one before, because the tools do not answer the questions that determine risk: how long, will it lock, for how long, is there disk headroom, and is anything still using what is being dropped.

**ML task:** Regression on migration duration and lock hold time from schema and workload features, plus dependency analysis for blast radius
**Input data:** Historical migrations across the fleet with statement type, table size, row width, index count, engine version, instance class and concurrent traffic, joined to observed duration and lock behaviour; query logs for column and index usage; query plans affected by the change.
**Target:** Realised migration duration and maximum lock hold time.
**Evaluation metric:** Quantile accuracy rather than mean, because the decision is whether the worst case fits the maintenance window. Under-prediction is the dangerous error and should be reported separately. For blast radius, recall on affected queries, since a missed dependency is a self-inflicted outage.
**Scope:** The fleet corpus is what makes this a regression on a large labelled dataset rather than a guess — the same migration shapes recur across thousands of customers and nobody has assembled them. Column usage verification from query logs needs no modelling and prevents the most common footgun. Automatic rewriting of unsafe statements into their safe multi-step equivalents is the constructive extension that linters stop short of. 2 ML engineers, 4-5 months.
**Data availability:** Managed vendors observe migrations across their fleet and do not currently record them as a labelled dataset. Query logs vary in retention, which limits the confidence of usage verification.

---

## 3. Workload-Aware Configuration Tuning
#bayesian-optimization #gaussian-processes #gradient-boosting #confidence-intervals #time-series-forecasting #evaluation-metrics #automation

**Problem statement:** Engines ship hundreds of parameters with generic defaults, tuning guidance is a decade of blog posts written for different hardware, and the organisations applying it no longer employ database specialists. Connection exhaustion under autoscaling is the most common resulting outage.

**ML task:** Learning the mapping from workload characteristics to good configuration across a fleet, with safe sequential optimisation on individual systems
**Input data:** Workload characterisation (read-write mix, transaction size and duration, concurrency profile, working set relative to memory, access pattern); current configuration; observed performance and stability outcomes; instance class and hardware; application-side connection pool configuration where visible; fleet-wide configuration and outcome pairs.
**Target:** Performance and stability outcomes under a configuration, with regression events as the negative signal.
**Evaluation metric:** Improvement against the vendor's current default for a given workload class, measured on held-out systems. Regression rate under automated tuning is the guardrail and must be very low, since a tuning change that degrades a production database is far worse than a suboptimal default.
**Scope:** Safe sequential tuning — one parameter at a time, observe, revert on regression — is standard adaptive control practice and absent here. Bayesian optimisation is well suited given expensive evaluations. Connection pool sizing deserves its own treatment because the platform can see both sides and it causes more outages than any other configuration mistake. 2-3 ML engineers plus a database engineer, 6 months.
**Data availability:** Fleet configuration and telemetry are complete for managed services. Application-side pool configuration is usually invisible, which is the main gap for the highest-value parameter.

---

## 4. Query Behaviour Prediction at Authoring Time
#gradient-boosting #graph-theory #large-language-models #time-series-forecasting #confidence-intervals #evaluation-metrics #automation #worker-facing

**Problem statement:** Developers write queries against a development dataset a fraction of production size, ship them, and discover the problem months later as an incident. The knowledge required to predict the outcome — plans, selectivity, join strategy — is database expertise most application developers reasonably do not have.

**ML task:** Prediction of production plan and cost from a query plus production statistics, growth projection of that cost, and detection of anti-patterns in ORM-generated SQL
**Input data:** Query text or generated SQL; production table statistics, cardinalities and index definitions; historical plans and execution costs for similar queries across the fleet; table growth trajectories; ORM call sites and the statements they emit in test runs.
**Target:** The plan and execution cost the query actually incurs in production, and whether it later becomes a top-cost query.
**Evaluation metric:** Accuracy of the predicted plan shape and cost order of magnitude, which is what matters for the decision — precise cost prediction is unnecessary and precise plan prediction is what catches sequential scans on large tables. For anti-patterns, recall on query-per-row loops, which are the most common and most damaging ORM failure.
**Scope:** Production statistics are the input that makes this possible and the developer needs no access to the data itself. Growth projection — this is fine now and degrades past a particular table size — converts an invisible cliff into a date and is the most useful output. Attribution back from a slow production query to the ORM call site closes a loop that currently requires a specialist. 2 ML engineers, 5 months.
**Data availability:** Statistics and plan history are held by the platform. ORM call site mapping requires application-side instrumentation, which is available in APM products and not joined to database telemetry.
