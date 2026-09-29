# Machine Learning Opportunities — Customer Data Platforms

**Industry:** [[customer-data-platforms|Customer Data Platforms]]
**Derived from:** [[problems/customer-data-platforms/high-impact|High Impact]], [[problems/customer-data-platforms/low-impact-1|Low Impact 1]], [[problems/customer-data-platforms/low-impact-2|Low Impact 2]], [[problems/customer-data-platforms/worker-life-1|Worker Life 1]], [[problems/customer-data-platforms/worker-life-2|Worker Life 2]]

---

## 1. Calibrated Identity Resolution With Measured Error in Both Directions
#graph-neural-networks #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #k-nearest-neighbors #evaluation-metrics #compliance

**Problem statement:** Whether two records are the same person is decided probabilistically by a threshold somebody set at implementation, and no organisation measures its over-merge rate or its under-merge rate. The two errors have entirely different costs — one is a potential privacy incident, the other a marketing inefficiency — and a single cut-off trades them as if they were the same.

**ML task:** Pairwise and graph-level entity resolution producing a calibrated match probability, evaluated against a deliberately constructed adjudicated set, with separate operating points per downstream use
**Input data:** All identifier-bearing records — emails, hashed phones, device and cookie identifiers, addresses, loyalty and payment tokens, names; co-occurrence structure across devices and households; temporal behaviour; the existing graph's current merge decisions.
**Target:** Same-person, adjudicated by a human under controlled access using a documented rubric for the genuinely hard cases — shared households, one person with several emails, an order shipped to a friend.
**Evaluation metric:** Merge precision and split rate reported separately and never as a single score. Sampling must be stratified across the score distribution and concentrated in the ambiguous band, because random pairs are almost all trivial non-matches and a random sample will report excellent performance that means nothing. Track both rates over time so a configuration or upstream data change is visible immediately rather than after a complaint.
**Scope:** The adjudicated set is the project. A few thousand well-chosen pairs suffice, adjudication requires people who can see identifying data and therefore requires access controls and a documented process, and the rubric for hard cases is a policy artefact as much as a labelling instruction. Carrying confidence downstream so an advertising audience and a page displaying order history use different operating points is the change with the largest safety payoff and is mostly plumbing. 2-3 ML engineers plus a privacy lead, 6-9 months.
**Data availability:** The records exist. The labels do not and must be created. That asymmetry is the entire reason this has not been done anywhere.

---

## 2. Event Stream Health and Semantic Mapping
#change-point-detection #time-series-forecasting #bert #word-embeddings #gradient-boosting #evaluation-metrics #data-integration #automation

**Problem statement:** The pipeline accepts whatever arrives, so a renamed event or a removed property degrades audiences and journeys silently for weeks. Separately, different product teams implement the same concept under different names, and only one or two people know the history.

**ML task:** Forecast per-event and per-property arrival volumes and distributions to detect drift, correlate departures with deployment history, and infer semantic equivalence between differently-named events
**Input data:** Event arrival volumes and property value distributions over time; deployment and release history; event and property names and structures; behavioural position of events within sessions; downstream dependency configuration.
**Target:** For monitoring, whether an observed stream is consistent with its own forecast. For mapping, whether two event names denote the same concept, confirmed by a human.
**Evaluation metric:** Detection lead time against when the breakage was actually noticed — typically weeks, and that gap is the entire value. False alarms must stay rare enough that alerts are read, which means modelling release cycles, seasonality and campaign-driven volume properly rather than thresholding. For semantic mapping, precision on proposed equivalences matters more than recall: a wrong merge of two distinct concepts corrupts analysis quietly, so proposals go to a human and are never applied automatically.
**Scope:** Monitoring is simple and should ship first; it addresses the single most common failure mode in this category. Semantic mapping uses names, property structure and session position together — names alone are too weak and position alone too noisy. 2 ML engineers, 4-6 months.
**Data availability:** Complete inside the platform. Deployment history requires an integration that engineering teams grant readily since it also serves them.

---

## 3. Audience Overlap, Redundancy and Contact Pressure
#k-means-clustering #dimensionality-reduction #graph-neural-networks #dbscan #word-embeddings #evaluation-metrics #data-integration #revenue-impact

**Problem statement:** Organisations accumulate thousands of saved audiences with no view of which describe the same population, which are decaying because they reference events that stopped arriving, or how many audiences a single customer sits in at once.

**ML task:** Cluster audiences by membership similarity to surface redundancy, track membership decay against expectation, and compute per-customer total audience membership as a contact pressure measure
**Input data:** Audience definitions and their membership over time; the underlying customer attributes and events; audience metadata — creator, creation date, last activation; downstream campaign and channel usage; event schema status.
**Target:** Redundancy groups among audiences, decay flags, and per-customer contact pressure across all channels.
**Evaluation metric:** For redundancy, agreement with human review on a sample — the useful output is not a similarity number but a statement that these forty audiences describe six populations, with names and owners attached. For decay, precision of flags against confirmed schema breakages. Contact pressure needs no model validation; it needs to be computed at all, which is the finding.
**Scope:** Straightforward, computationally cheap and immediately legible to a customer, which makes it unusually easy to adopt. The organisational obstacle is that its output is an implicit critique of the people who built the audiences, so it should be framed as consolidation rather than cleanup. 1-2 ML engineers, 3-4 months.
**Data availability:** Entirely within the platform's own configuration and membership data.

---

## 4. Privacy Request Resolution and Propagation Tracking
#graph-neural-networks #bayesian-inference #confidence-intervals #large-language-models #gradient-boosting #evaluation-metrics #compliance #worker-facing

**Problem statement:** A deletion or access request must be fulfilled across every downstream system within a statutory window, starting from a probabilistic identity graph whose errors now cut both ways — disclosing or deleting the wrong person's data, or leaving fragments behind and failing to fulfil.

**ML task:** Confidence-aware subject resolution that surfaces marginal records for adjudication, plus a propagation model of which downstream systems plausibly hold data for a subject
**Input data:** The identity graph with per-edge match confidence; export, sync and audience activation logs by system and date; downstream system retention characteristics; historical request fulfilment records and their adjudications.
**Target:** The set of records belonging to the subject, partitioned into confident, marginal and excluded, and the enumerated set of downstream systems that received them.
**Evaluation metric:** Completeness and correctness against manually audited fulfilments, reported as two separate rates because they are two separate legal failures. The marginal band's size is itself an important output — an operator needs to know how many judgement calls a request contains before certifying it, and today that number is invisible. Measure time-to-fulfilment as the operational metric.
**Scope:** The propagation record is mostly engineering — logging at the point of export rather than reconstructing later — and it converts fulfilment from broadcast-and-hope into an enumerable checklist with evidence. The adjudication rubric for recurring hard cases, shared households above all, is a policy artefact that makes decisions consistent and defensible to a regulator. 2 ML engineers plus a privacy operator, 4-6 months.
**Data availability:** Export and sync logs often exist but are not retained or structured for this purpose. Historical fulfilment records are usually manual notes.
