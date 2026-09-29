# Machine Learning Opportunities — Subscription Commerce

**Industry:** [[subscription-commerce|Subscription Commerce]]
**Derived from:** [[problems/subscription-commerce/high-impact|High Impact]], [[problems/subscription-commerce/low-impact-1|Low Impact 1]], [[problems/subscription-commerce/low-impact-2|Low Impact 2]], [[problems/subscription-commerce/worker-life-1|Worker Life 1]], [[problems/subscription-commerce/worker-life-2|Worker Life 2]]

---

## 1. Delivery-Sequence Survival Modelling with Operational Cause Attribution
#survival-analysis #gradient-boosting #causal-inference #confidence-intervals #hypothesis-testing #logistic-regression #evaluation-metrics #revenue-impact

**Problem statement:** Most cancellations occur within the first three deliveries for specific operational reasons — a box that diverged from the sign-up impression, a cadence mismatched to consumption, a damaged item, an unexplained value proposition — and the category reports a monthly churn rate and increases acquisition spend.

**ML task:** Survival modelling with the delivery as the time unit rather than the calendar month, with covariates drawn from what was actually in each box and what happened to it
**Input data:** Per-delivery contents, ship and arrival dates, delivery exceptions and damage reports; sign-up quiz responses and the marketing creative the customer converted from; skip, swap and pause events; support contacts and their categories; item-level feedback where collected; cancellation timing and stated reason.
**Target:** Cancellation hazard by delivery number, with attribution to operational causes.
**Evaluation metric:** Calibration of hazard by delivery number is the primary measure, since the intervention decision depends on knowing when risk concentrates. For attribution, effect sizes with confidence intervals per cause — the useful output is that damaged deliveries raise cancellation hazard by a measurable amount, which converts an operational failure into a quantified retention cost that operations will act on.
**Scope:** Stated cancellation reasons are unreliable and should be treated as a weak signal at most — the customer has decided and is choosing the least confrontational option, which is why price dominates every such survey. The operational record is the honest evidence. Confounding is real: customers who receive damaged items may differ systematically, so the strongest findings come from natural variation such as carrier-caused damage that is plausibly independent of the customer. 2-3 ML engineers, 5 months.
**Data availability:** Excellent and unusual — the same customer observed repeatedly against a known expectation, with the full operational record of what they received. Item-level satisfaction feedback is the notable gap and is a product change rather than a data one.

---

## 2. Consumption Rate Inference and Cadence Optimisation
#bayesian-inference #survival-analysis #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #time-series-forecasting

**Problem statement:** A monthly delivery of something consumed every seven weeks accumulates, and accumulation is the most reliable predictor of cancellation in replenishment subscriptions. The company knows what it shipped and not what was used, and offers a small set of intervals chosen for operational convenience.

**ML task:** Latent consumption rate estimation per customer from skip, swap and reorder behaviour, feeding a per-customer cadence recommendation
**Input data:** Delivery history with quantities; skip and delay events; swap behaviour; add-on and one-off purchases indicating shortfall; pause events; product category consumption norms; household or usage attributes from onboarding; cancellation outcomes.
**Target:** The customer's actual consumption rate, and the shipping interval that minimises both accumulation and shortfall.
**Evaluation metric:** Reduction in cancellation hazard for customers whose cadence was proactively adjusted, measured against a holdout — the intervention is the test and it is straightforward to run. Skip rate is a useful proxy that responds quickly and can validate the model before churn outcomes are available.
**Scope:** Skip behaviour is the primary observable signal for accumulation and is currently used only for billing. Proactive cadence adjustment is where the value sits: waiting until a customer cancels and offering a cadence change as a retention save is far weaker than proposing it when the skip pattern first appears. The operational objection — that varied cadences complicate fulfilment — is real and is partly offset by the smoothing benefit it creates for the monthly peak. 2 ML engineers, 4 months.
**Data availability:** Skip, swap and delivery data are complete in every subscription platform. Actual consumption is never observed directly, which is what makes this a latent variable problem rather than a lookup.

---

## 3. Inventory-Constrained Box Assignment
#optimization-fundamentals #convex-optimization #gradient-boosting #k-nearest-neighbors #contrastive-learning #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Curated subscription is a prediction with a shipping cost attached, and it is made by rules derived from an ageing sign-up quiz. Standard recommenders optimise engagement with a shown item; this problem is bundle satisfaction under novelty and non-repetition constraints, satisfiable from constrained inventory across every subscriber simultaneously.

**ML task:** Preference modelling with sparse feedback, embedded in an assignment optimisation over subscribers and available inventory
**Input data:** Quiz responses and their age; delivery history per customer with contents; skip, swap, return and item feedback where collected; downstream retention outcomes; product attributes; warehouse inventory positions and costs; bundle-level satisfaction signals.
**Target:** The assignment of items to subscribers maximising expected satisfaction and retention subject to inventory constraints.
**Evaluation metric:** Retention effect of assigned boxes against the rules-based baseline, measured on a holdout — the only evaluation that matters, since offline preference accuracy does not capture bundle effects or novelty. Report repetition rate and variety measures alongside, because a model optimising narrow preference accuracy will send near-identical boxes, which is a visible product failure.
**Scope:** Feedback sparsity is the binding constraint and is fixable by product: collecting lightweight per-item reactions would transform the data situation, and most companies collect nothing and learn from cancellation, the latest and least informative signal available. Bundle effects — variety, coherence, a standout item — are not representable in standard recommendation frameworks and are what customers actually judge. The assignment layer matters because giving every subscriber their top item is impossible. 3 ML engineers, 6 months.
**Data availability:** Delivery and outcome history is complete. Per-item feedback is the missing input and its absence is the reason curation quality has stalled across the category.

---

## 4. Fulfilment Wave Forecasting and Smoothing
#time-series-forecasting #gradient-boosting #optimization-fundamentals #confidence-intervals #convex-optimization #evaluation-metrics #logistic-regression

**Problem statement:** Billing and shipping cluster onto a few days, producing a peak several times the average day, staffed with temporary labour trained monthly and priced accordingly by logistics providers. The planner works with a number that does not firm up until days before, because skips confirm late and swaps change the pick.

**ML task:** Per-subscriber skip probability prediction feeding a wave volume forecast, plus optimisation of billing date allocation to smooth the peak
**Input data:** Subscriber base with plan, tenure and cadence; historical skip and pause behaviour per subscriber; swap patterns; new sign-up and cancellation flows; box contents and pick complexity; historical wave volumes and realised staffing; carrier capacity and pickup schedules.
**Target:** Shipment volume and pick complexity by day, and a billing date allocation minimising peak load subject to customer expectations.
**Evaluation metric:** Forecast accuracy at the specific horizon staffing decisions are made — typically one to two weeks out, where the current forecast is weakest — rather than aggregate monthly accuracy. For smoothing, realised peak-to-average ratio and the associated labour and logistics cost, against the pre-change baseline.
**Scope:** Skip prediction per subscriber is the piece that improves the forecast most, since the current method applies a historical average skip rate to the active base and misses that skip propensity varies enormously by tenure and cadence fit. Smoothing is a product decision with an operational payoff, and the assumption that customers require a fixed date is testable and probably overstated in most categories. Pick optimisation for variable box contents is a distinct warehouse problem that standard systems handle poorly. 2 ML engineers plus an operations planner, 4-5 months.
**Data availability:** Complete within the subscription and fulfilment systems. Pick complexity and warehouse labour data often sit with a third-party logistics provider and require a data-sharing arrangement.
