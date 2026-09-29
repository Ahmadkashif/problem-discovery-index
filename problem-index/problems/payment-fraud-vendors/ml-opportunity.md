# Machine Learning Opportunities — Payment Fraud Vendors

**Industry:** [[payment-fraud-vendors|Payment Fraud Vendors]]
**Derived from:** [[problems/payment-fraud-vendors/high-impact|High Impact]], [[problems/payment-fraud-vendors/low-impact-1|Low Impact 1]], [[problems/payment-fraud-vendors/low-impact-2|Low Impact 2]], [[problems/payment-fraud-vendors/worker-life-1|Worker Life 1]], [[problems/payment-fraud-vendors/worker-life-2|Worker Life 2]]

---

## 1. Randomised Decline Allowance and Unbiased Decision Evaluation
#causal-inference #logistic-regression #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Fraud models are trained and evaluated on chargebacks, which exist only for approved transactions. The region of the decision surface the model declines is therefore permanently unlabelled, the training set consists entirely of transactions the system chose to approve, and false declines — the larger commercial harm in card-not-present commerce — are estimated by survey rather than measured.

**ML task:** Design and operation of a permanent randomised approval allowance in the decline region, with propensity-corrected estimation everywhere else
**Input data:** Full scored transaction records including those declined; the model score and its drivers as the known propensity function; outcomes for the randomised allowance arm including chargebacks and subsequent customer behaviour; merchant-supplied customer lifetime value; retry and cross-merchant network activity by the same identity.
**Target:** Unbiased estimates of fraud rate and false decline rate by score band, and a model trained on a population that is not entirely self-selected.
**Evaluation metric:** The headline deliverable is a false decline rate with a confidence interval, which does not currently exist anywhere in the industry. Model improvement should be measured on the randomised arm only, since any evaluation on the selected population is a statement about a distribution the model created. Stratify the allowance by score band and concentrate it near the decision boundary, where the information per approved-fraud dollar is highest.
**Scope:** The cost is bounded, budgetable and visible, while the bias it corrects is invisible and permanent — which is precisely why the trade is not made, and why making it is a durable competitive position rather than a technique anyone can copy overnight. Where randomisation is refused, inverse propensity weighting or doubly robust estimation gives a defensible correction, because unusually in this setting the selection mechanism is fully known: it is the scoring model itself. Lifetime value belongs in the objective, since the cost of a decline is not the order margin but every future order placed elsewhere. 2 ML engineers and 1 econometrician, 6 months, plus a standing loss budget.
**Data availability:** Everything except the randomised arm exists today. Creating that arm is a product and commercial decision, not a data engineering one.

---

## 2. Merchant Embeddings and Cold Start Transfer
#transfer-learning #gradient-boosting #k-means-clustering #bayesian-inference #confidence-intervals #evaluation-metrics #feature-engineering #data-integration

**Problem statement:** Every new merchant is a new definition of normal, and a general model applied to one produces high false positives in exactly the weeks the merchant is judging the product. Merchant category is a weak proxy — two apparel retailers with different price points and acquisition channels behave nothing alike.

**ML task:** Learned merchant representations for principled transfer, with Bayesian threshold setting under explicit cold-start uncertainty
**Input data:** Order composition, value distribution, customer acquisition channel mix, geography, fulfilment model, device and session patterns across all merchants on the network; early transaction history for the new merchant; imported historical orders where the merchant can supply them; outcomes by merchant over time.
**Target:** A merchant embedding supporting nearest-neighbour transfer, and posterior-derived decision thresholds that tighten as evidence accumulates.
**Evaluation metric:** False positive rate in the first four, eight and twelve weeks compared against the vendor's current onboarding baseline — the onboarding window is the only one that matters here, since it determines whether the account survives. Calibration of the posterior matters more than point accuracy: a model that knows it is uncertain and says so allows a threshold to be set rationally rather than by a consultant's caution.
**Scope:** Separating benign distribution shift from an actual attack is the genuinely hard core of this problem and recurs beyond onboarding, whenever a merchant launches a campaign that brings a new customer profile. Showing a new merchant the approval and review rates that comparable merchants experienced in each of their first twelve weeks removes most early-relationship friction and needs no modelling at all. 2 ML engineers, 5 months.
**Data availability:** Cross-merchant behavioural data is the network's core asset and is fully available. Merchant-supplied historical orders vary in quality and completeness.

---

## 3. Fraud Ring Linking and Case Consolidation
#graph-neural-networks #graph-theory #k-means-clustering #k-nearest-neighbors #gradient-boosting #evaluation-metrics #worker-facing #automation

**Problem statement:** A fraud ring produces dozens of superficially distinct orders sharing a device pattern, an email structure, an address cluster or a payment instrument, and they arrive as separate cases to separate analysts at separate moments, each reviewed from scratch in under a minute.

**ML task:** Entity and ring resolution over the transaction graph, with case consolidation and precedent retrieval for review
**Input data:** Device fingerprints and browser characteristics; email and phone structure and reputation; shipping and billing address normalisation and clustering; payment instrument and BIN patterns; session and behavioural telemetry; cross-merchant network activity; historical confirmed rings and their eventual outcomes.
**Target:** Linked case groups representing one actor or ring, with the linking evidence exposed, plus ranked similar historical cases.
**Evaluation metric:** Precision on links is the binding constraint, because a wrongly merged case propagates a decline across unrelated legitimate customers — the failure mode is worse than the manual status quo. Measure the reduction in distinct review decisions per thousand flagged transactions, and the consistency of decisions across analysts on linked cases, which is currently unmeasured and known to be poor.
**Scope:** Linking is the single largest available improvement to review operations and typically collapses a substantial fraction of the queue into a handful of real actors. Precedent retrieval transfers tacit analyst pattern recognition — this email structure, this address pattern, this order composition — to everyone on their first week and keeps it after they leave. Decision consistency measurement across analysts on near-identical cases is a small addition with real calibration value. 2 ML engineers, 5 months.
**Data availability:** Excellent. All linking signals are already collected; cross-merchant consortium data makes the graph far stronger than any single merchant's view.

---

## 4. Representment Win Prediction and Evidence Selection
#gradient-boosting #bert #large-language-models #k-nearest-neighbors #evaluation-metrics #feature-engineering #compliance #workflow-orchestration

**Problem statement:** Contesting a chargeback means assembling reason-code-specific evidence within a deadline, at a win rate that varies enormously by code and issuer, with the decision of what to contest made by a rule about order amount rather than by any estimate of probability.

**ML task:** Win probability prediction per dispute, learned evidence selection per reason code and issuer, and narrative generation from assembled evidence
**Input data:** Historical representments with reason code, issuer, amount, evidence submitted and outcome; order, delivery, authentication and support records; customer history and prior disputes; descriptor and policy details; pre-dispute deflection outcomes.
**Target:** Probability of winning if contested, the evidence set most likely to persuade, and a drafted cover narrative.
**Evaluation metric:** Calibration of win probability is what redirects effort correctly — the decision rule is expected recovery against assembly cost, so a well-calibrated fifteen percent is more useful than a confident but wrong ranking. For evidence selection, measure win rate uplift against the merchant's current template bundle, holding reason code and issuer fixed, since both dominate the outcome.
**Scope:** Pre-dispute deflection through Order Insight and Ethoca is far cheaper than representment and is underused for what is essentially a data plumbing reason — having order detail available at the issuer's enquiry moment. It should be built before any modelling. The quieter opportunity is feedback: chargeback outcomes are evidence about the original approval decision, about descriptors and policies, and about which customers dispute, and they are currently treated purely as a recovery workflow. 2 ML engineers, 4 months.
**Data availability:** Good. Representment history and outcomes are retained; evidence sources are spread across order, shipping, authentication and support systems and require assembly.
