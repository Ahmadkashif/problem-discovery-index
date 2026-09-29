# Machine Learning Opportunities — Retail Media Networks

**Industry:** [[retail-media-networks|Retail Media Networks]]
**Derived from:** [[problems/retail-media-networks/high-impact|High Impact]], [[problems/retail-media-networks/low-impact-1|Low Impact 1]], [[problems/retail-media-networks/low-impact-2|Low Impact 2]], [[problems/retail-media-networks/worker-life-1|Worker Life 1]], [[problems/retail-media-networks/worker-life-2|Worker Life 2]]

---

## 1. Incremental and Displacement-Adjusted Value of a Sponsored Placement
#causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #monte-carlo-methods #evaluation-metrics #probability-distributions #revenue-impact

**Problem statement:** Attributed ROAS counts sales to shoppers who searched a brand by name and would have bought anyway, and subtracts nothing for the organic sale the sponsored slot displaced. The retailer is the only party who can measure the truth and the only party with a reason not to.

**ML task:** Causal effect estimation from continuous randomised placement holdouts, combined with counterfactual ranking to quantify displacement, producing incremental net revenue per placement class
**Input data:** Randomised holdout assignment at session or auction level; the organic ranking that would have been served without ads, retained per impression; purchase records joined at customer identity; query class (brand-name, category, generic), category, placement type; shopper history and prior brand purchase.
**Target:** Incremental units and incremental net revenue — the treated-minus-control difference, minus the value of the displaced organic result.
**Evaluation metric:** Interval coverage validated against a small number of large, properly-powered reference holdouts. Report separately by query class, because brand-name and category queries have entirely different incremental profiles and reporting them blended is the mechanism by which the current number stays high. Displacement must be reported as its own line, not netted silently.
**Scope:** The technical work is modest — the instrumentation is a holdout flag and retaining the no-ads ranking — and the project is difficult for organisational reasons. Build it to report both the brand's number (incremental units of their product) and the retailer's number (incremental category revenue and basket), because those conflict precisely where reported ROAS is currently highest. 2 ML engineers plus a causal specialist, 4-6 months technically, considerably longer to adopt.
**Data availability:** Complete. Impression, ranking, identity and purchase all sit in one system. This is the best-instrumented causal question in advertising and the least-answered.

---

## 2. Constrained Ranking Over Relevance, Margin, Availability and Ad Revenue
#convex-optimization #gradient-boosting #bayesian-optimization #evaluation-metrics #feature-engineering #k-nearest-neighbors #revenue-impact #transfer-learning

**Problem statement:** Placement is ranked on bid times predicted click because that is what the licensed ad platform optimises. The retailer's actual objective includes unit margin, regional availability, private label position and basket-building value, none of which reach the ad stack.

**ML task:** Joint ranking of organic and sponsored results under an explicit multi-term objective with retailer-set weights and hard availability constraints
**Input data:** Query and shopper context; predicted relevance and click for each candidate; advertiser bid; unit margin by SKU and fulfilment path; live regional inventory; return rate and fulfilment cost; basket-attachment statistics; private label flags and category policy.
**Target:** Profit per session rather than ad revenue per impression, with availability as a constraint rather than a term.
**Evaluation metric:** Online profit per session against the incumbent ranker, with ad revenue, category margin and shopper outcome all reported — a change that raises profit while degrading relevance is a loan against next quarter and the evaluation must be able to see that. Off-policy estimation from logged auctions is necessary for iteration speed and must be checked against live tests before any weight change ships.
**Scope:** Joining the organic and sponsored rankers is the hard part and it is mostly organisational plumbing — two stacks, two teams, two vendors. It is also the prerequisite for measuring displacement at all, which makes it worth doing for two reasons at once. 3 ML engineers plus a merchandising analyst, 6-9 months.
**Data availability:** Every input exists inside the retailer; almost none of it currently reaches the ad platform. This is a data integration project wearing a ranking project's clothes.

---

## 3. The Long-Run Cost of Ad Load in Basket and Return Frequency
#causal-inference #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #time-series-forecasting #revenue-impact

**Problem statement:** Every sponsored slot costs something in shopper experience, and the cost shows up in basket size and return frequency over months while the revenue shows up this week. No retailer can currently state the trade-off for their own store.

**ML task:** Long-horizon causal estimation of ad density effects on customer-level outcomes, using randomised or staggered variation in ad load across sessions, categories and cohorts
**Input data:** Ad load actually served per session (slot count, position, share of first screen); session outcomes — conversion, basket size, category breadth; customer-level return frequency and spend over the following quarters; randomised or naturally staggered ad load variation; cohort covariates.
**Target:** Customer-level spend and return frequency at 30, 90 and 180 days as a function of cumulative ad exposure density.
**Evaluation metric:** The per-session effect is small and the confounding is enormous, so this stands or falls on whether the variation is genuinely randomised — observational estimates here will be confidently wrong and should not be shipped. Report effects with intervals wide enough to be honest, and state the minimum detectable effect explicitly, because leadership will read a null as permission.
**Scope:** Long horizons mean the first credible answer is a year out, which is the main reason nobody has started. Survival framing on return-visit timing is more sensitive than spend differences and is the better primary outcome. 2 ML engineers plus a causal specialist, 12-18 months to a defensible estimate.
**Data availability:** Loyalty-identified transaction history gives the long-horizon outcomes for a large share of shoppers at most grocers and pharmacies; thinner at general merchandise retailers with lower identification rates, where the selection into being identified is itself a confounder.

---

## 4. Purchase-Structure Audience Models and Match-Corrected Offsite Lift
#logistic-regression #gradient-boosting #survival-analysis #k-means-clustering #dimensionality-reduction #causal-inference #compliance #evaluation-metrics

**Problem statement:** Offsite segments are built with generic recency-frequency heuristics that ignore the structure in a purchase history, and offsite lift is measured on partially-matched exposure data with a selection bias that flatters the result.

**ML task:** Replenishment-aware and switching-aware propensity modelling for audience construction, plus a selection-corrected lift estimator for clean-room measurement calibrated against onsite causal estimates
**Input data:** Longitudinal transaction history at household level; category replenishment intervals and position in cycle; promotion exposure and brand-switch events; basket composition; offsite exposure logs returned into the clean room; match status and its correlates; onsite randomised holdout results for the same customer base.
**Target:** For audiences, purchase of the target category or brand within the flight window. For measurement, incremental sales among the exposed, corrected for selection into the matched population.
**Evaluation metric:** Audiences are judged by incremental lift, never by match rate or segment size — the metrics currently sold. For the lift estimator, the calibration target is the onsite causal estimate on a comparable population, which is the rare case where a ground truth exists in the same building.
**Scope:** The interesting modelling is the replenishment timing — knowing that a household is eleven days into a fourteen-day cycle is worth more than any demographic segment, and it is a survival problem with a clean label. The measurement correction needs the match status correlates, which the platforms return grudgingly and incompletely. 3 ML engineers plus a privacy engineer, 6-9 months.
**Data availability:** Transaction history is rich and long. Offsite exposure returns are aggregated and partial by design, and that limitation is permanent rather than temporary — the model has to be built to live with it.
