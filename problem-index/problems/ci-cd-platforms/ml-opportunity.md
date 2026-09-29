# Machine Learning Opportunities — CI/CD Platforms

**Industry:** [[ci-cd-platforms|CI/CD Platforms]]
**Derived from:** [[problems/ci-cd-platforms/high-impact|High Impact]], [[problems/ci-cd-platforms/low-impact-1|Low Impact 1]], [[problems/ci-cd-platforms/low-impact-2|Low Impact 2]], [[problems/ci-cd-platforms/worker-life-1|Worker Life 1]], [[problems/ci-cd-platforms/worker-life-2|Worker Life 2]]

---

## 1. Statistical Flakiness Detection and Cause Classification
#logistic-regression #gradient-boosting #hypothesis-testing #change-point-detection #confidence-intervals #causal-inference #feature-engineering #evaluation-metrics

**Problem statement:** Flaky tests train engineers to re-run rather than investigate, and once that habit forms real regressions get re-run too. Detection by re-running is expensive and incomplete, and distinguishing a lying test from one correctly catching a nondeterministic bug is both hard and consequential.

**ML task:** Inference of flakiness from the relationship between failures and the changes preceding them, plus multiclass classification of the underlying cause
**Input data:** Full test execution history with outcomes, durations, runner identity and load, execution order, parallelism level and timestamp; the code changed in each run; retry outcomes; quarantine history; subsequent reverts and production incidents linked to changes.
**Target:** Flakiness as established by re-runs on identical commits where available, extended by statistical inference where not; and cause class as determined by whoever eventually fixed the test.
**Evaluation metric:** Precision on flakiness calls, weighted heavily, because labelling a test flaky that was correctly detecting a race is how a serious bug reaches production — that specific error should be reported as its own class rather than absorbed into a precision number. Detection cost is the second metric: how much of the detection is achieved with zero additional executions.
**Scope:** Statistical inference from existing history is what makes this affordable — a test whose failures show no relationship to the changes preceding them is flaky, and that is testable without re-running anything. Cause classification is what turns a list into a work queue, and the signatures are distinguishable: correlation with runner load, with execution order, with parallelism. The lying-versus-real-race distinction should be surfaced for human judgement rather than automated. 2-3 ML engineers, 5 months.
**Data availability:** Excellent — every CI platform holds enormous, clean, labelled execution history. Links from changes to subsequent production incidents are the weakest join and the most valuable.

---

## 2. Learned Test Relevance with Backtested Miss Rate
#gradient-boosting #graph-theory #k-nearest-neighbors #confidence-intervals #cross-validation #feature-engineering #evaluation-metrics

**Problem statement:** Test impact analysis has existed for years and is used by a minority, because skipping a test that would have caught a regression is a visible failure while running everything is defensible. Nobody has measured how often selection would actually miss something.

**ML task:** Prediction of which tests could fail for a given change, from historical failure-to-change relationships rather than static call graphs; plus ordering by failure likelihood
**Input data:** Historical changes with files touched and the tests that failed; test execution durations; dependency and call graphs where derivable; test-to-code co-change history; module ownership; the change's author and branch context.
**Target:** Tests that actually failed for a given change.
**Evaluation metric:** The number that determines adoption is the backtested miss rate — over the organisation's own history, how many genuine failures would this selection have skipped, at what time saving. Report it as a curve so a team can choose their own risk point. Ordering should be evaluated separately by time-to-first-failure, which is a pure win requiring no risk at all.
**Scope:** Historical relevance beats static analysis for integration tests, which are the longest-running and the ones static analysis handles worst. The confidence statement is the product: selection without a measured error rate is not adoptable, and with one it becomes a normal engineering trade-off. Failure-ordered execution should ship first because it improves the experience immediately and skips nothing. 2 ML engineers, 4-5 months.
**Data availability:** Complete within any CI platform, and the cross-customer version would let a vendor state typical miss rates by codebase shape, which no single organisation can establish.

---

## 3. Build Waste Identification and Right-Sizing
#gradient-boosting #k-means-clustering #optimization-fundamentals #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** CI compute is substantial, unowned and optimised by whoever notices the invoice. Usage dashboards report minutes by repository, which is not a unit anyone can act on, while the waste is structural and visible in the execution data.

**ML task:** Attribution of cost to the pipeline decisions that produced it, plus classification of waste patterns and runner right-sizing from utilisation
**Input data:** Job execution records with duration, runner size and resource utilisation; pipeline configuration including matrix dimensions, triggers and caching; cache hit rates; change contents and whether they could affect each job's outcome; retry counts and their causes; branch activity and abandonment.
**Target:** Cost attributable to each configuration decision, and waste classes — unnecessary triggers, unused matrix combinations, oversized runners, ineffective caches, retry-driven spend.
**Evaluation metric:** Realised saving after applying recommendations, tracked against prediction, which is directly measurable from subsequent invoices. Report false-saving rate too: recommendations that were applied and later reverted because something broke.
**Scope:** Most of this is querying rather than learning — jobs that always pass and have never caught a failure, matrix combinations whose results nobody has examined, caches with near-zero hit rate. Right-sizing from utilisation is a straightforward regression. The genuine contribution is attribution at the level of a decision a team can change, which is what makes showback or chargeback possible. 1-2 ML engineers, 3-4 months.
**Data availability:** Complete. Resource utilisation per job is collected by most platforms and rarely exposed.

---

## 4. Build Failure Classification and Aggregation
#bert #word-embeddings #gradient-boosting #k-means-clustering #large-language-models #evaluation-metrics #automation #worker-facing

**Problem statement:** Build engineers spend their weeks diagnosing other teams' pipeline failures — dependency conflicts, expired secrets, changed base images, misconfigured steps — and the same classes recur across teams with each handled individually because nothing aggregates them.

**ML task:** Classification of build failure cause from logs and configuration, with clustering across teams to produce shared findings and static validation of configuration before execution
**Input data:** Build logs and exit codes; pipeline configuration; dependency manifests and lock files; secret and credential references; base image and toolchain versions; historical failures with their eventual resolutions; cross-team pipeline configurations.
**Target:** The failure cause as resolved, taken from the fix that followed.
**Evaluation metric:** Classification accuracy per cause class, and the proportion of failures that can be self-served — resolved by the developer from the classification without contacting the build team, which is the metric the build engineer experiences. For static validation, the share of failures that could have been caught before the run.
**Scope:** Static pre-run validation catches a meaningful share with no modelling — undefined secrets, invalid step references, versions that do not exist — and should ship first. Cross-team aggregation is where the durable value sits: forty teams hitting one dependency conflict is a shared fix visible only from the platform's vantage point. Configuration drift detection lets a template improvement propagate rather than each team diverging. 2 ML engineers, 4 months.
**Data availability:** Logs and configurations are complete. Resolution labels come from subsequent successful runs and from support conversations, which are noisier.
