# Machine Learning Opportunities — Gig Delivery Platforms

**Industry:** [[gig-delivery-platforms|Gig Delivery Platforms]]
**Derived from:** [[problems/gig-delivery-platforms/high-impact|High Impact]], [[problems/gig-delivery-platforms/low-impact-1|Low Impact 1]], [[problems/gig-delivery-platforms/low-impact-2|Low Impact 2]], [[problems/gig-delivery-platforms/worker-life-1|Worker Life 1]], [[problems/gig-delivery-platforms/worker-life-2|Worker Life 2]]

---

## 1. Merchant Wait Prediction and Wait-Aware Dispatch
#time-series-forecasting #gradient-boosting #confidence-intervals #markov-decision-processes #convex-optimization #evaluation-metrics #worker-facing #optimization-fundamentals

**Problem statement:** Couriers are dispatched to arrive at the merchant's promised ready time rather than the realistic one, which converts predictable merchant delay into unpaid courier waiting — the largest and most resented subtraction from realised hourly earnings.

**ML task:** Predict the distribution of merchant readiness by location, hour, order composition and current load, and use it to time dispatch and to disclose expected wait on the offer
**Input data:** Historical courier arrival and pickup timestamps per merchant; order composition and size; merchant current order volume; time of day, weekday and seasonality; merchant-side readiness signals where integrated; weather and local conditions.
**Target:** Actual time between courier arrival and order handover.
**Evaluation metric:** Calibration of the predicted distribution matters more than the mean, because the courier-facing use is a range on an offer and the dispatch use is a timing decision — an overconfident point estimate reproduces the current problem with extra steps. Measure the outcome directly as total unpaid waiting minutes per engaged hour before and after, which is the number the intervention exists to reduce.
**Scope:** The modelling is straightforward and the platforms already forecast at far greater difficulty; the reason this does not exist is that the optimisation targets the customer promise and treats courier time as free. Adding realised courier earnings per engaged hour to the dispatch objective is the change, and it is a product decision with a technical implementation rather than a research problem. 2 engineers, 4-6 months.
**Data availability:** Complete. Arrival and pickup timestamps are captured on every order.

---

## 2. Realised Net Earnings Estimation Per Offer and Per Hour
#gradient-boosting #time-series-forecasting #confidence-intervals #probability-distributions #causal-inference #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Couriers decide on a gross figure that omits waiting, travel to pickup, idle time and vehicle costs, so the advertised rate and what the work actually pays diverge by an amount that varies with conditions they cannot observe.

**ML task:** Estimate expected net earnings per offer and per engaged hour, net of mileage-based vehicle costs, with the tax burden flagged and assumptions stated
**Input data:** Offer composition — base, distance, effort, promotion, tip; predicted wait; distance to pickup and from delivery to the next likely offer; historical realised durations for comparable offers; market-level demand conditions; standard vehicle cost-per-mile assumptions by vehicle class.
**Target:** Actual net earnings per engaged hour realised on comparable offers.
**Evaluation metric:** Calibration against realised outcomes, reported separately by market and hour because the divergence is condition-dependent and an aggregate figure conceals exactly when the work is worst. The honest framing is an estimate with stated assumptions rather than a figure, since vehicle costs and tax situations vary per person — presenting a precise net number would be its own form of misleading.
**Scope:** The uncomfortable property of this work is that it will show some offers and some hours to be poor value, which reduces acceptance. That is the point and it is why this does not exist; the counterargument is supply retention and the regulatory direction of travel. Platforms operating under minimum earnings standards have already built most of this. 2 engineers, 4-6 months.
**Data availability:** Complete for everything except individual vehicle costs, which must be parameterised and disclosed as assumptions.

---

## 3. Substitution Preference Learning and Stock Prediction
#contrastive-learning #k-nearest-neighbors #gradient-boosting #bert #k-means-clustering #word-embeddings #evaluation-metrics #worker-facing

**Problem statement:** Shoppers choose substitutions in ninety seconds from catalogue-adjacency suggestions, and the reputational cost of a wrong choice lands on them rather than on the inventory data that failed to predict the stockout.

**ML task:** Learn substitution acceptability from historical outcomes and rank per customer from their order history; separately forecast out-of-stock probability by item, store and hour to move the decision upstream
**Input data:** Historical substitution events with outcomes — accepted silently, accepted with complaint, refunded, rated poorly; customer order history revealing brand loyalty, dietary patterns, size and price sensitivity; product catalogue and attributes; shopper-reported availability by item, store and time; store inventory integrations where they exist.
**Target:** Whether a substitution was accepted without complaint, and whether an item will be unavailable.
**Evaluation metric:** Acceptance rate on suggested substitutions against the current catalogue-adjacency baseline, evaluated per customer rather than pooled, since the whole claim is that individual history beats category similarity. For stock prediction, precision at the threshold used to prompt a customer for a pre-agreed substitute — a false stockout warning annoys a customer, a missed one puts the shopper back in the aisle.
**Scope:** The attribution correction belongs in the same work: a substitution that followed the platform's own top suggestion should not count against the shopper's accuracy metric, and separating shopper judgement from platform recommendation in outcome data costs nothing and removes a penalty shoppers currently absorb for following advice. 2 engineers, 4-6 months.
**Data availability:** Excellent — millions of substitution events with outcomes are a direct preference dataset that is currently used for very little.

---

## 4. Deactivation Decision Quality and Error Measurement
#gradient-boosting #graph-neural-networks #confidence-intervals #hypothesis-testing #bert #evaluation-metrics #compliance #worker-facing

**Problem statement:** Deactivation removes people's incomes, is triggered by automated systems on frequently thin and one-sided evidence, and its error rate is unknown to the organisation operating it because a wrongly deactivated courier generates no contradicting record.

**ML task:** Assemble structured evidence per case including complainant history, estimate the probability that a flag reflects genuine violation, and measure false positive rates through randomised audit of unappealed deactivations
**Input data:** Delivery history, location and timing traces, proof-of-delivery photographs; the complaint and the complainant's own refund and complaint rate across all couriers; account tenure and volume; prior flags and their resolutions; appeal text and outcomes; a deliberately randomised audit sample of deactivations that were not appealed.
**Target:** Whether the deactivation was correct, established by deep review of the audit sample rather than by appeal outcome alone.
**Evaluation metric:** The false positive rate among unappealed deactivations is the number this exists to produce, and it cannot come from appeals — the appealing population is not representative, since people with the least capacity to contest are least likely to appeal. A randomised deep-reviewed audit sample is the only honest instrument. Report precision separately by tenure, because the cost of an error on a four-year full-time courier is not comparable to one on a two-week account.
**Scope:** Complainant history is the single most informative unused signal: a customer with an anomalous refund-request rate across many couriers is highly diagnostic and is rarely surfaced to the agent. Consequence-weighted routing — more time and deeper evidence where the income loss is larger — is a process change with a larger effect than any model. 2 engineers plus an operations lead, 6 months.
**Data availability:** Complete within the platform; the audit sample must be deliberately created and is the part requiring an organisational decision.
