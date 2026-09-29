# Machine Learning Opportunities — Vector Search Vendors

**Industry:** [[vector-search-vendors|Vector Search Vendors]]
**Derived from:** [[problems/vector-search-vendors/high-impact|High Impact]], [[problems/vector-search-vendors/low-impact-1|Low Impact 1]], [[problems/vector-search-vendors/low-impact-2|Low Impact 2]], [[problems/vector-search-vendors/worker-life-1|Worker Life 1]], [[problems/vector-search-vendors/worker-life-2|Worker Life 2]]

---

## 1. Production Retrieval Quality Estimation from Weak Signals
#evaluation-metrics #hypothesis-testing #confidence-intervals #logistic-regression #bayesian-inference #large-language-models #bert #revenue-impact

**Problem statement:** The category reports recall against brute-force search, which measures the index and not whether the retrieved documents answer the question. Real quality depends on the embedding model, chunking, query distribution and corpus, and nobody measures it on production traffic — application teams discover failures anecdotally and tune by whether the anecdote improved.

**ML task:** Estimating relevance from unlabelled downstream behaviour, calibrated against a small human-judged anchor set
**Input data:** Production queries and returned result sets with scores; downstream signals — query reformulation, source click-through, whether a generated answer cited a retrieved chunk, conversation escalation, session abandonment; a periodically refreshed human-judged evaluation set drawn from real queries; corpus and chunking metadata.
**Target:** Per-query retrieval quality, anchored on human relevance judgements and extrapolated through the behavioural signals.
**Evaluation metric:** Correlation between the estimated quality signal and human judgement on the held-out anchor set, which is the only way to know whether the free signals mean anything. Report the estimator's ability to detect an injected regression — deliberately degrading retrieval and measuring how quickly the signal moves — since regression detection is the primary operational use.
**Scope:** The human anchor set is the expensive component and it is bounded: a few hundred real queries with judged relevance is sufficient for regression detection and configuration comparison. Failure attribution is the genuinely useful output — distinguishing an answer absent from the corpus, present but badly chunked, present but ranked below the cut, and retrieved but ignored downstream, each of which has a different fix and which are currently indistinguishable. 2-3 ML engineers plus an information retrieval specialist, 5-6 months.
**Data availability:** Queries and results are complete inside the database. Downstream signals live in the application and require instrumentation the vendor must ask for, which is the main obstacle and is the same obstacle that keeps the vendor at the infrastructure layer.

---

## 2. Query-Adaptive Hybrid Weighting
#logistic-regression #bayesian-optimization #optimization-fundamentals #evaluation-metrics #hypothesis-testing #feature-engineering #word-embeddings

**Problem statement:** Hybrid search reliably beats either lexical or dense retrieval alone, and the weighting is left at the documentation default because tuning requires an evaluation set the customer never built. Worse, the correct weighting is not constant — identifier queries want lexical, conceptual queries want dense — and a single global parameter is a compromise across both.

**ML task:** Query classification into retrieval-strategy classes, with per-class weighting optimised against a generated evaluation set
**Input data:** Query text and its token characteristics; embedding model vocabulary coverage for the query terms; corpus statistics; retrieval results under varying weightings; relevance labels from the anchor set and from synthetically generated question-chunk pairs.
**Target:** The weighting that maximises retrieval quality for a given query, and the query class that predicts it.
**Evaluation metric:** Retrieval quality improvement over the fixed default weighting on the held-out anchor set, which is the honest comparison and a low bar nobody has measured against. Report per-class results separately, since the gain concentrates in identifier-like queries where dense retrieval fails hardest.
**Scope:** Generating an evaluation set from the corpus itself — producing questions that a given chunk answers — is the unlock that makes tuning possible for every customer and is now straightforward. Out-of-vocabulary detection for the embedding model is the sharpest single feature: a query containing rare identifiers or code fragments should route lexically and this is predictable before retrieval runs. Reranking should be treated as a conditional decision based on first-stage score distributions rather than an always-on stage. 2 ML engineers, 4 months.
**Data availability:** Query logs are complete. Relevance labels are absent and must be generated synthetically and anchored on a small human set, which is the standard approach and works well for tuning even where it would be inadequate for absolute measurement.

---

## 3. Index Health Monitoring and Rebuild Forecasting
#change-point-detection #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #graph-theory #optimization-fundamentals

**Problem statement:** Recall degrades under churn as tombstones accumulate and graph connectivity decays, invisibly, while latency and throughput dashboards look healthy. Rebuilds are scheduled by calendar or by complaint, consume double memory and hours of wall clock, and nobody knows whether any given rebuild was necessary.

**ML task:** Continuous recall estimation by sampling against exact search, plus forecasting of degradation to a threshold
**Input data:** Sampled queries with approximate and exact results; insertion, update and deletion rates; tombstone counts and distribution; graph connectivity statistics; index parameters; historical rebuild events with their measured before-and-after recall; corpus size and dimensionality.
**Target:** Current true recall, and time until recall crosses an operator-set threshold.
**Evaluation metric:** Accuracy of the recall estimate against a full exact evaluation, and the sampling cost required to achieve a useful confidence interval — the practical question is how few queries suffice, since the whole point is that this must be cheap enough to run continuously. For forecasting, lead time on threshold crossings.
**Scope:** The measurement itself needs no learning and is the bulk of the value: sampling a few hundred queries against an exact scan is inexpensive and is currently run at benchmark time rather than as a standing metric. Rebuild duration and resource prediction from corpus characteristics lets an SRE know whether the operation fits the maintenance window. Filtered search recall deserves separate treatment, since a selective metadata predicate over a graph index can collapse recall in a way the unfiltered measurement will not reveal. 2 ML engineers plus a systems engineer, 4 months.
**Data availability:** Complete internally and unused. Historical rebuild events with before-and-after measurements generally do not exist because the measurement was not taken, so the first months are about establishing the baseline.

---

## 4. Corpus Diagnostics and Chunking Recommendation
#dimensionality-reduction #k-means-clustering #dbscan #evaluation-metrics #hypothesis-testing #word-embeddings #bert #feature-engineering

**Problem statement:** Retrieval failures are diagnosed by solutions architects working backwards through ingestion, chunking, embedding and ranking with ad-hoc scripts. The most common causes — a relevant passage split across a chunk boundary, a corpus with heavy near-duplication, a chunk size wrong for the document structure — are computable from the index and are surfaced nowhere.

**ML task:** Corpus-level analysis producing chunk boundary quality assessment, near-duplicate detection, embedding space coverage, and chunk size recommendation
**Input data:** The document corpus with structure and length distributions; current chunking configuration; chunk embeddings; query log with retrieved chunks; documents never retrieved by any query; embedding model identity and version.
**Target:** Configuration recommendations, and per-query failure attribution against the categories of miss.
**Evaluation metric:** For chunking recommendations, retrieval quality on the anchor set under recommended versus current configuration — a direct comparison the vendor can run. For boundary analysis, precision on flagged split passages as judged by inspection, since a false flag costs an architect's attention.
**Scope:** Boundary splitting is the highest-value single diagnostic: checking whether a passage spanning two chunks would have scored higher than either half is direct, cheap and catches a failure mode that is common and non-obvious. Orphaned documents — indexed and never retrieved by any query — are trivially computable and are a strong signal of either a coverage problem or a corpus that should be pruned. Embedding drift detection, comparing distributions when a provider updates a model, protects against a failure customers currently discover weeks later through degraded answers. 2 ML engineers, 4 months.
**Data availability:** Corpus, chunks, embeddings and query logs all sit inside the database. Document structure prior to chunking is frequently discarded at ingestion, which limits boundary analysis and is a retention decision worth revisiting.
