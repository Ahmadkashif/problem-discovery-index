# Machine Learning Opportunities — Synthetic Data Providers

**Industry:** [[synthetic-data-providers|Synthetic Data Providers]]
**Derived from:** [[problems/synthetic-data-providers/high-impact|High Impact]], [[problems/synthetic-data-providers/low-impact-1|Low Impact 1]], [[problems/synthetic-data-providers/low-impact-2|Low Impact 2]], [[problems/synthetic-data-providers/worker-life-1|Worker Life 1]], [[problems/synthetic-data-providers/worker-life-2|Worker Life 2]]

---

## 1. Joint Privacy-Utility Frontier Estimation
#hypothesis-testing #confidence-intervals #evaluation-metrics #entropy-cross-entropy-kl-divergence #mutual-information #bayesian-inference #gans #diffusion-models

**Problem statement:** Fidelity and privacy are reported as separate scorecards that do not compose into the claim customers are buying. A dataset can pass every fidelity check and every attack in the vendor's suite and still leak, because the suite tests the attacks the vendor thought of against an adversary the vendor assumed.

**ML task:** Characterising the achievable frontier between downstream task utility and empirical privacy risk across generator configurations, with record-level risk scoring
**Input data:** Generation runs across configurations with their hyperparameters and privacy budgets; source datasets with their statistical properties; fidelity evaluations; membership and attribute inference attack results; downstream model performance where measured; record-level nearest-neighbour distances to source data.
**Target:** A utility-risk pair per configuration, and a per-record disclosure risk score.
**Evaluation metric:** Attack success rate under a standing adversarial programme is the only honest privacy number and should be reported as a floor rather than a guarantee — the metric is how hard the vendor tried to break its own output. For utility, train-on-synthetic-test-on-real performance on the customer's actual downstream task, not distributional similarity, which is a proxy that customers have learned to distrust.
**Scope:** This is an open research problem and should be framed as one. The realistic deliverable is not a certificate but an honest frontier with stated assumptions and stated limits. Record-level risk scoring is the most tractable and immediately useful component: identifying the small fraction of synthetic records sitting close to real outliers, and suppressing them, buys most of the available risk reduction at modest utility cost. Requires a permanent adversarial evaluation team, not a one-off project. 3-4 ML engineers plus a privacy researcher, 9-12 months, ongoing thereafter.
**Data availability:** Vendors hold thousands of generation runs with evaluations attached, which is the corpus the field lacks. Downstream task performance is rarely returned by customers, which is the key missing link and is obtainable contractually.

---

## 2. Automatic Constraint Discovery from Source Data
#hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #graph-neural-networks #descriptive-statistics #data-integration

**Problem statement:** Enterprise schemas carry semantic constraints — cross-table date orderings, sums that reconcile, valid status transitions, code co-occurrence rules — that are enforced by the application that produced the data and written down nowhere. Generic generators break them silently, and solutions engineers repair them by hand in every engagement.

**ML task:** Candidate constraint generation over a schema followed by statistical validation against the real dataset, plus constraint-aware generation
**Input data:** The customer's source schema with foreign keys; the real dataset; column types, value distributions and co-occurrence patterns; temporal fields; historical constraints discovered manually in prior engagements.
**Target:** A validated constraint set — an invariant that holds across effectively all real rows and should hold in synthetic output.
**Evaluation metric:** Precision on discovered constraints as judged by the customer's data owner, since a spurious constraint over-restricts generation and degrades utility. Recall measured against constraints the customer eventually reports as broken, which is the natural label and arrives late. Constraint satisfaction rate in generated output is the operational metric.
**Scope:** Distinguishing a genuine invariant from a coincidence of the sample is the central statistical question and depends on sample size and constraint complexity — a rule holding across ten million rows is different from one holding across two hundred. Long-tail cardinality preservation in relational data is a separate and equally important gap: generators matching mean children-per-parent produce wrong tails, which is where both the interesting test cases and the privacy risk live. Constraint-aware generation by construction outperforms rejection sampling badly as constraint count rises. 2-3 ML engineers, 6 months.
**Data availability:** Source data is present during every engagement. Manually discovered constraints from prior engagements exist in solutions engineers' configuration files and are not retained as a corpus.

---

## 3. Ontology-Grounded Domain Generation
#large-language-models #transfer-learning #seq2seq #hidden-markov-models #evaluation-metrics #hypothesis-testing #feature-engineering #compliance

**Problem statement:** Generic generators produce statistically faithful clinical, financial and industrial nonsense — treatments preceding their indications, jointly impossible lab panels, transaction sequences with no merchant coherence. Domain experts reject the output in minutes, and the knowledge that would prevent it already exists in machine-readable ontologies the generators do not consult.

**ML task:** Sequence generation of event trajectories conditioned on domain ontology constraints, with automatic validation against those same ontologies
**Input data:** Source event data as trajectories rather than flat rows; clinical terminology and relationship systems (SNOMED, ICD, LOINC, RxNorm) or their financial and industrial equivalents; care pathway and quality measure logic; physical constraints where applicable; domain expert rejections from prior engagements as negative examples.
**Target:** Generated trajectories that are both statistically faithful and ontologically valid.
**Evaluation metric:** Domain rule violation rate against the ontology, which is checkable automatically and is currently checked by a human expert during a proof of concept. Alongside it, expert plausibility judgement on a sample — the honest test, since ontologies encode what is impossible rather than what is typical. Downstream task performance remains the utility measure.
**Scope:** Treating records as trajectories rather than as correlated field sets is the modelling shift that makes this work, and it points at sequence models rather than the tabular architectures most products use. The reusability argument is strong: the same clinical constraints apply at every healthcare customer, so this accumulates into a domain module rather than dissolving into per-engagement configuration. 3 ML engineers plus a clinical informaticist per domain, 6-8 months for the first domain.
**Data availability:** Ontologies are public, mature and machine readable. Source trajectory data is available during engagements. Expert rejection feedback is given verbally in proof-of-concept meetings and is not captured.

---

## 4. Divergence Localisation Between Synthetic and Source
#hypothesis-testing #confidence-intervals #descriptive-statistics #dimensionality-reduction #evaluation-metrics #k-means-clustering #cross-validation

**Problem statement:** Solutions engineers rebuild fidelity evidence from scratch in every proof of concept, and the customer finds the weak point in week three — a flattened tail, a broken constraint, a column that matters to them. The generator knows where its own output diverges most and does not say.

**ML task:** Automatic localisation of distributional divergence between synthetic and source data at column, joint, region and constraint level, with severity ranking
**Input data:** Source and synthetic datasets; schema and column semantics; discovered constraints; the customer's stated downstream task and the model they intend to train; historical proof-of-concept findings.
**Target:** A ranked list of divergences, ordered by likely impact on the customer's downstream use rather than by statistical magnitude.
**Evaluation metric:** Whether the system's top-ranked divergences match what customers actually raise during proofs of concept — a directly measurable benchmark using historical engagements. Coverage matters more than precision here: a divergence the system missed becomes a week-three surprise.
**Scope:** The ranking is the hard part and the valuable part. A statistically large divergence in an unused column matters less than a small one in the feature the customer's model depends on, which means impact estimation must be conditioned on the downstream task. Tail behaviour deserves separate treatment from central tendency, since generators systematically flatten tails and standard divergence metrics under-weight exactly that. 2 ML engineers, 4 months, and most of the value arrives from the standardised report alone before any ranking model exists.
**Data availability:** Both datasets are always present. Historical proof-of-concept findings live in sales notes and engineer notebooks rather than in a structured record, and assembling them is the first task.
