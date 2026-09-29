# Machine Learning Opportunities — Digital Audio Platforms

**Industry:** [[digital-audio-platforms|Digital Audio Platforms]]
**Derived from:** [[problems/digital-audio-platforms/high-impact|High Impact]], [[problems/digital-audio-platforms/low-impact-1|Low Impact 1]], [[problems/digital-audio-platforms/low-impact-2|Low Impact 2]], [[problems/digital-audio-platforms/worker-life-1|Worker Life 1]], [[problems/digital-audio-platforms/worker-life-2|Worker Life 2]]

---

## 1. Allocation Counterfactuals and Policy Simulation
#monte-carlo-methods #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #descriptive-statistics #compliance

**Problem statement:** Royalties are divided by share of total streams, which discards the per-subscriber listening record the platform holds in full. The user-centric alternative has been argued for a decade without anyone publishing what it would actually pay whom, and recent policy changes — stream thresholds, minimum play durations — moved real money with no distributional analysis disclosed.

**ML task:** Compute rights-holder outcomes under alternative allocation rules from complete listening logs, and simulate the distributional effect of proposed policy changes before adoption
**Input data:** Per-subscriber listening records with duration and context; subscription revenue by market and period; catalogue and rights-holder mapping; current pro-rata calculations and deductions; proposed policy parameters.
**Target:** Payout per rights holder under each allocation rule, per market and period — an accounting computation rather than a prediction.
**Evaluation metric:** Correctness is verified by reconciliation: every allocation rule must distribute exactly the available pool, and the pro-rata computation must reproduce the actual payments before any counterfactual is believed. The meaningful output is the distributional comparison — who gains, who loses, by how much, broken out by catalogue size, genre and independence — reported with the uncertainty introduced by the imperfect parts, which are mostly rights mapping rather than listening data.
**Scope:** This is engineering at scale rather than difficult modelling, which is what makes its absence striking. The obstacle is entirely willingness: publishing the counterfactual settles an argument that some parties benefit from leaving unsettled. Running the same machinery as a pre-adoption simulation for policy changes would convert unilateral announcements into negotiated ones. 2-3 data engineers plus an analyst, 6-9 months.
**Data availability:** Complete within the platform. Rights mapping quality is the binding limitation and overlaps directly with item 3.

---

## 2. Relational Streaming Fraud Detection With Contestable Outcomes
#graph-neural-networks #dbscan #change-point-detection #gradient-boosting #k-means-clustering #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** Because the pool is fixed, artificial streams take money from every legitimate rights holder rather than creating new money. Detection based on per-account thresholds is exactly what fraudulent operations are engineered around, and a false positive withholds a real artist's income on the basis of an algorithm they cannot see.

**ML task:** Detect coordinated inflation from account relationship structure, shared infrastructure and catalogue-level behaviour, producing evidence a human can evaluate and an artist can contest
**Input data:** Play events with account, device, network, timing and context; account creation and payment characteristics; the account-to-catalogue bipartite graph; upload and catalogue patterns including bulk functional-audio releases; confirmed historical fraud cases and their resolutions.
**Target:** Confirmed coordinated inflation as adjudicated by the integrity team, supplemented by unsupervised structure where labels are absent.
**Evaluation metric:** Precision at the withholding threshold is the governing number, because the cost of a false positive lands entirely on an artist's income. The hardest and most important discrimination is a coordinated campaign versus a devoted fanbase streaming an album repeatedly on release day — these look similar on volume and differ in relational structure, and performance should be reported specifically on that confusion rather than on the aggregate. Every withholding decision must carry evidence sufficient for an appeal.
**Scope:** The graph is what thresholds cannot replicate and where the organised money is. An appeal path with human review is a design requirement rather than a courtesy: this system decides whether people are paid. Adversarial drift means continuous retraining and a monitored detection rate. 3 ML engineers plus an integrity analyst, 9-12 months.
**Data availability:** Complete inside the platform. Cross-platform coordination is invisible to any single platform and is a permanent blind spot worth stating.

---

## 3. Joint Entity Resolution Across Parties, Works and Recordings
#graph-neural-networks #bert #word-embeddings #k-nearest-neighbors #contrastive-learning #gradient-boosting #evaluation-metrics #compliance

**Problem statement:** Royalties that cannot be matched to a rights record accumulate unpaid, and the failures concentrate on live and DJ recordings, remixes, classical repertoire, and non-Latin-script names — with the people affected generally unaware the money exists.

**ML task:** Resolve writers, works and recordings jointly using name similarity, co-credit structure, release context, temporal patterns and audio fingerprint, producing confidence-scored candidate matches and proactive owner notifications
**Input data:** Metadata from distributors, labels, publishers and societies; industry identifiers where present; the collaboration and release graph; audio fingerprints; historical resolved matches and disputes.
**Target:** The correct rights holder for a recording and its underlying composition, validated against confirmed claims.
**Evaluation metric:** Precision at the auto-allocation threshold must be very high, since a wrong allocation pays the wrong person and is harder to reverse than a delay. Report recall separately on the known-difficult classes — non-Latin scripts, classical, remixes, live recordings — because aggregate recall will look respectable while those categories stay broken, which is the current state. Measure the size of the unmatched pool over time as the outcome that matters.
**Scope:** Joint resolution is materially more accurate than resolving each entity in isolation: an unknown credit is far more identifiable when the other credits on the recording are known and the candidate has worked with two of them. Audio fingerprinting anchors the recording side and is underused as a rights signal. Proactive notification of likely owners is the process change that actually empties the pool, and is straightforward once candidates are scored. 3 ML engineers, 9-12 months.
**Data availability:** Metadata is abundant and dirty. Confirmed historical matches exist at societies and publishers and are the label source.

---

## 4. Cold-Start Discovery From Audio and Scene Structure
#contrastive-learning #autoencoders #transformers #graph-neural-networks #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #transfer-learning

**Problem statement:** More than a hundred thousand recordings arrive daily with no behavioural signal, into a system optimised for immediate engagement — an objective that reliably favours the familiar and leaves most of the catalogue with almost no plays ever.

**ML task:** Learn representations combining audio content with the artist's collaboration and scene graph to give a new recording an informative prior, and optimise recommendation surfaces for successful introduction rather than session engagement
**Input data:** Audio itself; artist collaboration, label and release relationships; geographic and venue context; early signals from small communities; listener histories; playlist composition and editing history.
**Target:** Whether a listener introduced to a recording becomes a repeat listener over the following weeks — introduction-to-retention rather than a play.
**Evaluation metric:** Retention after introduction, measured at 7 and 30 days, is the metric that distinguishes building an audience from generating a stream, and it should be reported per surface so the platform learns which of its discovery mechanisms actually build careers. Evaluate the cold-start case explicitly — recordings with no prior plays — since aggregate recommendation quality is dominated by the catalogue that already has history and will hide the failure entirely.
**Scope:** The scene graph is what makes content-based cold start work; audio similarity alone places a new recording next to a better-known one that gets recommended instead. Optimising for long-horizon listener value rather than session engagement is a business decision as much as a modelling one, and it is the decision that determines whether anything here changes. 3 ML engineers, 9-12 months.
**Data availability:** Audio and behavioural data are complete. Scene and collaboration structure is partially present in metadata and partially inferable from co-occurrence.
