# Machine Learning Opportunities — Affiliate Networks

**Industry:** [[affiliate-networks|Affiliate Networks]]
**Derived from:** [[problems/affiliate-networks/high-impact|High Impact]], [[problems/affiliate-networks/low-impact-1|Low Impact 1]], [[problems/affiliate-networks/low-impact-2|Low Impact 2]], [[problems/affiliate-networks/worker-life-1|Worker Life 1]], [[problems/affiliate-networks/worker-life-2|Worker Life 2]]

---

## 1. Partner-Class Incrementality and Introduction Versus Interception
#causal-inference #hypothesis-testing #bayesian-inference #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Commission is awarded on last click, which structurally pays the partner closest to checkout — coupon extensions, loyalty toolbars, trademark bidders — and pays nothing to the publisher who introduced the product. The network holds the full click path and the confirmed transaction and uses them to execute a rule rather than to answer the question.

**ML task:** Causal estimation of revenue effect per partner class from randomised session-level suppression, plus classification of each conversion path as introduction or interception from observable pre-exposure signals
**Input data:** Full click paths with partner identity, timing and referring context; confirmed transactions with basket and return outcome; shopper prior exposure to the merchant and the product; search terms where available; merchant-side promotional calendar; randomised suppression assignment for the treated arm.
**Target:** Merchant revenue under suppression versus control, per partner class. For the path model, whether the shopper had prior intent toward the specific product before the affiliate touch.
**Evaluation metric:** For incrementality, interval coverage against larger reference experiments, reported per partner class per merchant rather than pooled — pooling is how the uncomfortable classes hide. For the introduction classifier, held-out accuracy against labelled paths and, more usefully, agreement with the suppression experiment: introduction-classified paths should show substantially higher incremental effect, and if they do not the classifier is describing something else.
**Scope:** The experiment requires merchant-side implementation to suppress tracking for a randomised arm, and the partners being measured will object. Building it merchant-side rather than network-side is the politically feasible path and is also the one merchants will trust. 2 ML engineers plus a causal specialist, 6-9 months.
**Data availability:** Click paths and transactions are complete inside the network. Prior-intent signals are partial and the classifier has to be honest about what it cannot see. The suppression arm must be built and does not exist anywhere today.

---

## 2. Publisher-Merchant Matching from Demonstrated Conversion Behaviour
#word-embeddings #bert #contrastive-learning #k-nearest-neighbors #graph-neural-networks #gradient-boosting #evaluation-metrics #dimensionality-reduction

**Problem statement:** Merchants recruit from a directory sorted by size, so everyone recruits the same saturated partners and the mid-tail is invisible. The network knows exactly what each publisher's traffic converts on, across every merchant, and uses that to populate a leaderboard.

**ML task:** Learn joint embeddings of publisher content and audience conversion behaviour, and of merchant product catalogues, to rank fit at content-cluster level rather than domain level
**Input data:** Publisher content (pages, topics, product mentions) and its conversion record across all merchants — category, basket size, return rate, conversion rate; merchant catalogue and customer base; existing publisher-merchant relationships as a bipartite graph; the recruiting merchant's own customer overlap where they will share it.
**Target:** Whether a newly-formed publisher-merchant pairing produces sustained incremental revenue at twelve months, not whether it produces a click.
**Evaluation metric:** Evaluate on held-out relationships formed after a cutoff date, measuring sustained revenue rather than activation — most recruitment succeeds at getting a link placed and fails at producing anything. Report separately for the two opposite queries a merchant may have: partners who reach an audience the merchant already has versus partners who extend beyond it, because a single ranking answers neither well.
**Scope:** Content-cluster granularity is what unlocks the mid-tail, since a large site converts on some sections and not others. The bipartite relationship graph carries strong signal and also strong popularity bias that has to be corrected or the model will recommend the same saturated partners the directory already does. 2 ML engineers, 4-6 months.
**Data availability:** Excellent and unique to networks. Publisher content requires crawling; conversion outcomes are already held.

---

## 3. Relational Fraud and Compliance Detection
#graph-neural-networks #dbscan #change-point-detection #k-means-clustering #gradient-boosting #evaluation-metrics #compliance #feature-engineering

**Problem statement:** Cookie stuffing, trademark bidding, coupon leakage and incentivised traffic are policed by global thresholds applied per account, while the organised end of the problem operates across many accounts sharing infrastructure and behaviour.

**ML task:** Graph-based detection of coordinated publisher accounts, plus per-partner-class learned baselines with change detection for novel tactics
**Input data:** Click and conversion streams with device, network and timing fingerprints; account registration and payout details; referring URL and search term data; publisher content; coupon code appearance across the open web; historical confirmed fraud cases with their outcomes.
**Target:** Confirmed policy violation as adjudicated by the compliance team, and — separately and more usefully — departure from the learned normal for that partner class, which does not require a label.
**Evaluation metric:** Precision at the review threshold is the operative metric, because every false positive costs an analyst hours and a partner relationship. Measure the false positive rate against legitimate partners explicitly and separately by partner class; a system tuned on the aggregate will quietly punish content publishers whose patterns differ most from the majority. Track time-to-detection for newly-emerged tactics as the real test of whether the baseline approach beats rules.
**Scope:** The graph is the part rules cannot replicate and where the organised money is. Learned class-specific baselines fix the false-positive problem that makes global thresholds unusable. Both need a human adjudication loop — this system should never suspend an account autonomously, because the cost of being wrong falls entirely on someone's income. 2 ML engineers plus a compliance analyst, 6-9 months.
**Data availability:** Strong within a network. Cross-network coordination is invisible to any single network, which is a real and permanent blind spot.

---

## 4. Transaction Validation and Reversal Prediction
#gradient-boosting #survival-analysis #k-nearest-neighbors #logistic-regression #confidence-intervals #evaluation-metrics #automation #worker-facing

**Problem statement:** Affiliate managers approve tens of thousands of transactions a month by hand, and commission paid on transactions that later reverse has to be clawed back from partners who have already been paid — including small creators for whom it matters.

**ML task:** Predict the probability and timing of reversal per transaction at validation time, and classify transactions as routine or requiring review
**Input data:** Transaction attributes — merchant, category, basket composition and size, discount applied, partner class, shopper history, device and geography; historical reversal outcomes with timing; merchant return policy and seasonal return patterns; partner's own historical reversal rate.
**Target:** Reversal within the merchant's return window, and the time to reversal.
**Evaluation metric:** Calibration matters more than discrimination, because the output is used to decide whether to hold or release money to a partner — and an overconfident hold on a legitimate transaction damages a relationship for no gain. Measure the share of transactions that can be auto-approved at a fixed false-approval budget; that number is the whole business case. Report performance separately for small partners, who are hurt most by errors in either direction.
**Scope:** The routine-versus-review split is the immediately valuable half and is straightforward. Reversal timing as a survival problem is what turns clawbacks into holds, and needs per-merchant return-window structure. 1-2 ML engineers, 3-4 months — the most tractable item here.
**Data availability:** Complete transaction and reversal histories sit in every network. Merchant-side return reasons are richer and usually not shared.
