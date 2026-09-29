# Machine Learning Opportunities — Performance Marketing Agencies

**Industry:** [[performance-marketing-agencies|Performance Marketing Agencies]]
**Derived from:** [[problems/performance-marketing-agencies/high-impact|High Impact]], [[problems/performance-marketing-agencies/low-impact-1|Low Impact 1]], [[problems/performance-marketing-agencies/low-impact-2|Low Impact 2]], [[problems/performance-marketing-agencies/worker-life-1|Worker Life 1]], [[problems/performance-marketing-agencies/worker-life-2|Worker Life 2]]

---

## 1. Portfolio-Calibrated Cross-Platform Incrementality
#causal-inference #bayesian-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #variational-inference #evaluation-metrics #revenue-impact

**Problem statement:** Each platform reports conversions about itself on its own window and identity graph, and the sum exceeds the orders the business took. A single mid-sized advertiser lacks the power to resolve this from their own data; an agency with two hundred clients does not.

**ML task:** Hierarchical causal estimation pooling geo experiments and holdouts across a client portfolio to produce priors on platform overstatement by vertical, purchase cycle and spend level, updated per client by their own experiments
**Input data:** Geo holdout and staggered switch-on results across the client base; platform-reported conversions with their windows and modelling flags; client-side total orders and revenue at daily grain; spend by platform and campaign; vertical, purchase cycle length and price band covariates.
**Target:** Incremental revenue per platform per client, with the constraint that channel contributions plus baseline reconcile to actual total revenue.
**Evaluation metric:** Out-of-sample prediction of holdout results on clients not used to fit the prior is the real test; within-sample fit will always look excellent and means nothing. Report intervals and be explicit about where the interval is too wide to guide a decision — for small accounts it frequently will be, and saying so is the difference between a measurement product and a reassurance product. Reconciliation error against actual revenue is a hard constraint, not a diagnostic.
**Scope:** The hierarchical structure is what makes small accounts tractable: they borrow strength from the portfolio and contribute their own weak evidence back. Running the experiments requires client agreement to withhold spend, which is also a commercial conversation about the fee model, since a spend-percentage contract penalises the agency for the finding. 3 ML engineers plus a causal specialist, 12 months.
**Data availability:** Platform data is easy. Client-side revenue at daily grain requires a data-sharing agreement most clients will grant and few agencies currently ask for. Geo experiment infrastructure has to be built and is the gating item.

---

## 2. Conversion Reconciliation and Data Quality Monitoring
#change-point-detection #time-series-forecasting #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #data-integration #automation

**Problem statement:** Platform-reported conversions double-count and drift, and tracking breaks, feed outages and silent attribution-setting changes corrupt reporting upstream of everything — usually discovered when a number looks wrong in a client meeting.

**ML task:** Forecast expected volumes per conversion stream and detect departures; reconcile overlapping platform-reported conversions against client-side order totals with an explicit allocation of the excess
**Input data:** Conversion events per platform and per stream with timestamps; client order and revenue totals; site deployment history; platform API schema and setting changes; historical incident labels.
**Target:** For monitoring, whether an observed stream is consistent with its own forecast distribution. For reconciliation, the allocation of platform-claimed conversions to actual orders.
**Evaluation metric:** Time to detection on historical incidents, measured against when the incident was actually noticed — the gap is usually days to weeks and is the entire value. False alarm rate must be low enough that alerts are read; a monitor that fires on ordinary seasonality gets muted within a fortnight and is then worse than nothing. For reconciliation, the unallocated residual reported honestly rather than distributed.
**Scope:** Straightforward technically and unusually high-value because the failures are silent and credibility-destroying. Seasonality, promotions and campaign launches all produce legitimate step changes that must not fire, which is most of the modelling work. 1-2 ML engineers, 3-4 months — the fastest item here.
**Data availability:** Complete. Everything needed already flows through the agency's reporting pipeline.

---

## 3. Creative Attribute Effects Across a Client Portfolio
#cnns #transformers #contrastive-learning #transfer-learning #gradient-boosting #causal-inference #evaluation-metrics #feature-engineering

**Problem statement:** Creative is the largest controllable driver of paid social performance, agencies generate thousands of creative outcomes a year across dozens of clients, and none of it accumulates — every new client's creative starts from a moodboard.

**ML task:** Learn transferable creative attribute representations from asset content and estimate attribute effects in context, with the platform's own budget allocation treated as the confound it is
**Input data:** Creative assets — frames, hook structure, opening seconds, offer position and phrasing, presence and framing of people, motion and pacing, copy; placement and format context; audience and vertical; delivery and outcome records; balanced-rotation or explicit test data where it exists.
**Target:** Outcome rate attributable to the creative attribute, not to the asset identity, and specifically at cold start where no client-specific history exists.
**Evaluation metric:** Cold-start lift on clients and creatives never seen in training is the only meaningful measure — a model that performs after two weeks of data has replicated the platform's own optimiser. The confound must be addressed explicitly: platform-allocated spend correlates with outcome by construction, so effects estimated from ordinary delivery data are biased upward for whatever the platform favoured, and only balanced rotation or deliberate tests break it.
**Scope:** Attributes transfer across clients, assets do not — this is what makes a portfolio model legal, useful and ethically uncomplicated. Brand constraint enforcement is a separate and necessary component: brand systems, claim substantiation and regulatory copy differ per client and currently gate all generative production behind human review. 3 ML engineers with multimodal experience, 9-12 months.
**Data availability:** Assets and delivery records sit in the agency's own accounts across its whole book, which is the advantage. Clean creative effect data requires deliberate rotation the platforms discourage.

---

## 4. Account Health and Churn Prediction
#gradient-boosting #survival-analysis #logistic-regression #time-series-forecasting #confidence-intervals #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Agencies lose clients on a cycle short enough to consume their margin in pitching, and attention is allocated to whoever shouted most recently rather than to whoever is most at risk.

**ML task:** Predict time-to-churn per account from performance, engagement and relationship signals, and rank which accounts need a person this week
**Input data:** Performance trajectory against agreed targets; pacing and efficiency drift; meeting attendance and seniority of attendees; response latency and sentiment in client correspondence; unanswered requests and open escalations; contract dates and renewal windows; stakeholder changes on the client side; scope creep and unbilled work.
**Target:** Non-renewal or notice within the following two quarters, and time to that event.
**Evaluation metric:** Precision at the top of the weekly list, since that list is what an account director acts on and a wrong name costs a wasted intervention. Lead time matters as much as accuracy — a correct prediction two weeks before notice is useless, and the metric should be accuracy at 90 and 120 days out. Watch for the model simply learning that underperforming accounts churn, which is true and already known; the value is in the accounts performing acceptably whose relationship signals have turned.
**Scope:** The relationship signals carry most of the incremental information and are the sensitive part — correspondence analysis means reading staff and client communications, which needs a clear internal policy, disclosure, and restraint about what is surfaced to whom. Aggregate signals rather than individual quotes is the defensible design. 2 ML engineers, 4-6 months.
**Data availability:** Performance data is complete; CRM and calendar data is usually available; correspondence requires a deliberate decision. Historical churn labels exist and are plentiful in this industry.
