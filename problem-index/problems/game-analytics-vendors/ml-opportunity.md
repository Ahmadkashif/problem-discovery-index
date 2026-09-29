# Machine Learning Opportunities — Game Analytics Vendors

**Industry:** [[game-analytics-vendors|Game Analytics Vendors]]
**Derived from:** [[problems/game-analytics-vendors/high-impact|High Impact]], [[problems/game-analytics-vendors/low-impact-1|Low Impact 1]], [[problems/game-analytics-vendors/low-impact-2|Low Impact 2]], [[problems/game-analytics-vendors/worker-life-1|Worker Life 1]], [[problems/game-analytics-vendors/worker-life-2|Worker Life 2]]

---

## 1. Genre-Conditioned Market Baselines From the Cross-Studio Corpus
#bayesian-inference #confidence-intervals #time-series-forecasting #k-means-clustering #hypothesis-testing #evaluation-metrics #probability-distributions #descriptive-statistics

**Problem statement:** The first question any analyst asks when a metric moves is whether comparable games moved the same way, and it is unanswerable from inside one game and a query away from the vendor's position — which holds event data from thousands of titles and sells each studio a view of its own funnel.

**ML task:** Construct genre, platform and monetisation-conditioned distributions of key metrics over time, and locate a customer's game within them
**Input data:** Event and metric time series across the vendor's customer base; game metadata — genre, monetisation model, platform, audience, age since launch; seasonal and platform-level events; cohort size for anonymity thresholds.
**Target:** The distribution of each metric for comparable games in each period, and this game's position within it.
**Evaluation metric:** The practical test is how many metric movements resolve to a market event once the comparison is available — that share is the product's value and is currently unknown to everyone. Comparability is the modelling question: genre labels are coarse and a learned similarity over behavioural signatures will define peer sets better than a taxonomy. Validate peer sets by whether their metrics actually co-move, which is checkable.
**Scope:** The obstacle is commercial and legal rather than technical. Customer agreements vary in what aggregate use they permit, and some customers will object to their data informing a competitor's benchmark even anonymised — so cohort-size thresholds, aggregation guarantees and an opt-in structure are as much of the project as the modelling. Doing it properly is a communications exercise with a query attached. 1-2 ML engineers plus legal and customer-facing work, 6-9 months.
**Data availability:** Already held. This is the clearest case in the industry of an asset sitting unused.

---

## 2. Metric Movement Decomposition and Cause Attribution
#causal-inference #change-point-detection #time-series-forecasting #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #data-integration

**Problem statement:** Build changes, content updates, configuration changes, acquisition mix shifts, price changes, competitor launches and seasonality all move retention and routinely happen in the same week, and half of them are not in the analytics system at all.

**ML task:** Decompose a metric movement into observable components and attribute the remainder to timestamped cause events integrated from build, configuration and acquisition systems
**Input data:** Metric series with full segmentation; cohort, acquisition source, version and platform mix over time; build release metadata and contents; live operations configuration change logs; acquisition spend and source mix from measurement partners; content release calendar; seasonality baselines; the cross-studio market comparison from item 1.
**Target:** The decomposition itself — points of movement attributable to each component — with the residual reported rather than allocated.
**Evaluation metric:** Reconstruction error against the actual total, and the size of the unexplained residual, which should be prominent rather than smoothed away. For cause attribution, agreement with post-hoc analyst conclusions on a labelled set of historical incidents, and specifically the ability to say "several things changed and this data cannot separate them" — which is frequently the true answer and is currently unsayable in a leadership review.
**Scope:** Most of this is careful accounting rather than sophisticated modelling, which is why it is achievable quickly. The three integrations — build metadata, configuration logs, acquisition data — are the real work and every customer already has all three in systems with APIs. Building for causal inference going forward, with staged rollout support and default holdout cohorts, is what makes future attribution possible rather than reconstructed. 2 ML engineers, 6-9 months.
**Data availability:** Metrics are complete. The causes sit in three other systems and are the gap.

---

## 3. Per-Game Prediction With Cross-Studio Priors and Reported Calibration
#gradient-boosting #survival-analysis #transfer-learning #bayesian-inference #confidence-intervals #cross-validation #probability-distributions #evaluation-metrics

**Problem statement:** Churn scores and lifetime value estimates ship as generic features fitted across a heterogeneous customer base, are used to set acquisition bids and target offers, and their calibration for any particular game has typically never been checked.

**ML task:** Fit predictions per game, using the cross-studio corpus as a prior for small and new titles, with calibration reported in the interface and drift-triggered retraining
**Input data:** Each customer's own event history; the cross-studio corpus for transfer priors; game genre and structural metadata; realised churn and spend outcomes; evidence volume per player — session count and tenure.
**Target:** Churn within a defined window and lifetime value over a defined horizon, as calibrated probabilities and distributions.
**Evaluation metric:** Calibration is the headline and must be displayed, not assumed: a churn score of 0.8 is used as though it means eighty percent and typically nobody has verified that for this game. Report reliability per game and monitor it, alerting on degradation. Evaluate the transfer prior specifically on small and new titles, which is where the generic model is worst and where a well-constructed prior should be best — an aggregate metric will be dominated by large customers and will hide exactly the case this is for.
**Scope:** Uncertainty must reach the interface: a prediction from two sessions and one from two hundred currently look identical, and the downstream uses — bid setting, offer targeting — are precisely where acting on a confident-looking uninformative number costs money. Drift detection with automatic refitting and a visible record of when the model changed is standard practice elsewhere and absent here. 2 ML engineers, 6-9 months.
**Data availability:** Complete. This is a product architecture decision more than a data problem.

---

## 4. Instrumentation Drift, Version Reconciliation and Coverage Assessment
#change-point-detection #bert #word-embeddings #time-series-forecasting #gradient-boosting #evaluation-metrics #data-integration #workflow-orchestration

**Problem statement:** Event schemas drift as games change, several client versions are live simultaneously each sending a different schema, and the gaps are discovered when a metric looks wrong — or when a question turns out to be unanswerable because the event was never sent.

**ML task:** Forecast per-event arrival rates and parameter distributions to detect drift with version attribution; infer mappings between schema versions; and assess coverage against what games of this genre typically need
**Input data:** Event arrival volumes and parameter distributions by client version; release timing and version adoption curves; event names, structures and their session position; dashboard, alert and model dependencies; the cross-studio corpus of event taxonomies by genre.
**Target:** Whether an observed stream departs from its own history; whether two differently-named events across versions denote the same concept; and which events a given game is missing relative to comparable titles.
**Evaluation metric:** Detection lead time against when the drift was actually noticed, which today is when a number looks wrong — typically weeks. False alarm rate must be low enough that alerts are read, which means modelling version adoption curves properly, since a legitimate version rollout produces exactly the pattern a naive detector flags. For coverage, the measure is how often a studio's question turns out to be unanswerable for want of instrumentation, before and after.
**Scope:** Multiple long-lived client versions are a structural feature of games that general analytics tooling ignores entirely, and declarative version mapping applied at query time is the fix. Coverage assessment during development — telling a studio which events it will wish it had — is the highest-value piece because instrumentation lead times in games are weeks and the vendor's corpus is the only source for the answer. 2 ML engineers, 6-9 months.
**Data availability:** Complete within the vendor across all customers.
