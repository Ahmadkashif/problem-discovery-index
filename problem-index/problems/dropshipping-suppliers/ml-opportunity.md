# Machine Learning Opportunities — Dropshipping Suppliers

**Industry:** [[dropshipping-suppliers|Dropshipping Suppliers]]
**Derived from:** [[problems/dropshipping-suppliers/high-impact|High Impact]], [[problems/dropshipping-suppliers/low-impact-1|Low Impact 1]], [[problems/dropshipping-suppliers/low-impact-2|Low Impact 2]], [[problems/dropshipping-suppliers/worker-life-1|Worker Life 1]], [[problems/dropshipping-suppliers/worker-life-2|Worker Life 2]]

---

## 1. Hierarchical Supplier Reliability Estimation
#bayesian-inference #gradient-boosting #survival-analysis #confidence-intervals #hypothesis-testing #change-point-detection #evaluation-metrics #revenue-impact

**Problem statement:** Merchants commit their storefront and customer relationship to suppliers they have never met, on ratings that measure volume more than performance, aggregated across catalogues and destinations where performance varies enormously. The platform holds every order it has ever routed and computes a star.

**ML task:** Hierarchical estimation of fulfilment reliability, defect rate and stock failure probability at supplier, product category and destination granularity, with change detection on decline
**Input data:** Order history with supplier, product, destination, timestamps and fulfilment events; tracking event streams; disputes and their outcomes; returns with reasons; merchant-side signals including customer complaints and marketplace metric impacts where obtainable; supplier tenure and volume.
**Target:** Fulfilment time distribution, defect rate and stock failure probability for a supplier-product-destination cell.
**Evaluation metric:** Calibration of the predicted distributions on held-out orders, particularly in thin cells where the naive average is meaningless — the whole point is producing usable estimates with honest intervals rather than either a misleading number or silence. Report interval width as a first-class output, since a merchant needs to know when the estimate is weak.
**Scope:** Small samples are the defining statistical challenge: most supplier-product-destination cells have few orders, which is exactly why hierarchical pooling across a supplier's products and across similar suppliers is the correct approach rather than the aggregation that destroys the granularity merchants need. Attribution between supplier, carrier and customs is genuinely muddy and requires the tracking event stream to separate. Decline detection matters more than the level, since a lagging average is what currently misleads merchants about a supplier whose quality just changed. 2-3 ML engineers, 5 months.
**Data availability:** Order and tracking data is complete and has been accumulating since these platforms started. Merchant-side outcome data — whether the customer was satisfied — is the signal that matters most and sits outside the platform, obtainable only by asking.

---

## 2. Quantile Delivery Time Prediction
#time-series-forecasting #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #change-point-detection

**Problem statement:** Merchants promise delivery windows they invent, because nobody publishes the real distribution for a specific supplier, service and destination. Late delivery against a promise drives marketplace penalties, refunds and poor reviews, and the platform holds tracking history for millions of orders.

**ML task:** Quantile regression on end-to-end delivery time by supplier, shipping service, destination and season, with customs clearance modelled as a distinct component
**Input data:** Tracking event streams with timestamps by carrier and facility; supplier processing times; shipping service and origin facility; destination country and region; declared value and product category for duty exposure; seasonal periods and known disruptions; realised delivery dates.
**Target:** The delivery date distribution, and specifically the quantile a merchant can commit to.
**Evaluation metric:** Quantile coverage — when the model says ninety per cent of orders arrive within a window, that must hold — rather than mean absolute error, since the merchant is making a promise and the cost is asymmetric and concentrated in the late tail. Report coverage separately for peak and disruption periods, where static estimates fail exactly when it matters most.
**Scope:** Customs clearance is a large, destination-specific component of variance that nobody models and that is observable in the tracking event stream as a gap between arrival and onward movement. Seasonal and disruption shifts move the distribution substantially for weeks, which means the model must adapt rather than serve a static estimate. The output should be a commitable quantile, not a mean — the wrong statistic is a large part of why current estimates disappoint. 2 ML engineers, 4 months.
**Data availability:** Tracking aggregation gives complete event streams. Realised delivery is confirmed. Declared value and duty outcomes are inconsistently captured, which limits the customs modelling.

---

## 3. Supplier Vetting Signal Validation and Network Detection
#gradient-boosting #graph-neural-networks #dbscan #confidence-intervals #hypothesis-testing #evaluation-metrics #change-point-detection #compliance

**Problem statement:** Sourcing analysts approve suppliers from registration documents, a sample order and a call, then never learn whether the approval was right. Suppliers removed for cause reappear under new entities, which a document check structurally cannot catch.

**ML task:** Predicting post-approval performance from vetting signals, plus graph-based detection of related supplier entities
**Input data:** Vetting records with registration details, sample order outcomes, call notes and listing characteristics; subsequent supplier performance including fulfilment reliability, disputes and merchant churn; supplier attributes — addresses, contacts, bank details, listing patterns, product overlap; removal events with reasons; new registrations.
**Target:** Post-approval reliability, and whether a new supplier entity is related to a previously removed one.
**Evaluation metric:** For signal validation, predictive validity of each vetting check against subsequent performance, reported per signal so that checks predicting nothing can be dropped and effort concentrated on those that matter. For network detection, precision on flagged relationships, since accusing a legitimate new supplier of being a re-registration is a serious error.
**Scope:** Closing the feedback loop requires no modelling at all and is the highest-value change: routing post-approval performance back to the analyst who approved them is the only mechanism by which vetting judgement improves, and it costs nothing. Sample orders placed without being identifiable as samples materially change what the sample reveals and are a straightforward process fix. Network detection is adversarial and the flagged output must go to a human, both because the error is serious and because the parties will contest it. 2 ML engineers plus a sourcing lead, 4-5 months.
**Data availability:** Vetting records exist in varying structure. Post-approval performance is complete. Supplier attribute data for the graph is held at registration and is exactly the data a re-registering party will vary.

---

## 4. Dispute Evidence Assembly and Outcome Prediction
#cnns #large-language-models #bert #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance

**Problem statement:** Agents adjudicate between merchant and supplier over an item nobody in the dispute has seen, with a forwarded photograph and two conflicting accounts. A meaningful share of decisions are wrong in one direction or the other, and the agent has a commercial relationship with both parties.

**ML task:** Image comparison between the received item and the listing, plus base rate assembly and consistency prediction across comparable disputes
**Input data:** Dispute submissions with photographs and narratives; listing images and descriptions; order and tracking history; supplier dispute rates by product and destination; historical dispute decisions and their outcomes; return reasons; whether the merchant or supplier subsequently churned.
**Target:** The dispute outcome as decided, and separately, consistency with how comparable disputes were resolved.
**Evaluation metric:** Consistency across comparable cases is the honest metric here — there is frequently no ground truth about what actually happened, so the measurable objective is that similar disputes are decided similarly, which is both fairer and currently not the case. For image comparison, accuracy in detecting mismatch against listing images and in flagging photographs that do not correspond to the order.
**Scope:** This assists an adjudication and must not appear to make it, both because the evidence genuinely does not establish the facts and because both parties are customers who will contest an automated decision. The higher-value application is prevention: disputes cluster on identifiable supplier-product-destination combinations, and surfacing that to merchants before they list is worth more than resolving the dispute afterwards. A feedback route to sourcing and catalogue, aggregating dispute patterns by supplier, closes the loop the queue currently absorbs. 2 ML engineers, 4 months.
**Data availability:** Dispute records with photographs and decisions are complete. Listing images are held. Whether the decision was actually correct is unknowable in most cases, which is why consistency rather than accuracy is the tractable target.
