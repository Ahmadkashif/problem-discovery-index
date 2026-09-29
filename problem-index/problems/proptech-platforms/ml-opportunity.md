# Machine Learning Opportunities — Proptech Platforms

**Industry:** [[proptech-platforms|Proptech Platforms]]
**Derived from:** [[problems/proptech-platforms/high-impact|High Impact]], [[problems/proptech-platforms/low-impact-1|Low Impact 1]], [[problems/proptech-platforms/low-impact-2|Low Impact 2]], [[problems/proptech-platforms/worker-life-1|Worker Life 1]], [[problems/proptech-platforms/worker-life-2|Worker Life 2]]

---

## 1. Single-Operator Demand Curve Estimation for Rent Setting
#logistic-regression #gradient-boosting #causal-inference #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** The industry's dominant rent-setting method — recommending prices from pooled non-public data contributed by competing landlords — is under antitrust challenge and banned in several jurisdictions. Operators still have to price units, and what a single operator can legitimately do with only its own funnel and public listing data has never been seriously attempted.

**ML task:** Demand curve estimation from observational funnel data, with the renewal decision modelled as a binary outcome conditional on offered price
**Input data:** Per-listing enquiry volume, tour bookings, application starts and completions, days on market and lease price; renewal offers with accepted or vacated outcomes; unit and property attributes; seasonality; publicly posted asking rents; turnover cost components (vacancy days, make-ready spend, concession, leasing cost).
**Target:** For new leases, probability of lease at a given price within a horizon. For renewals, probability of acceptance at a given increase.
**Evaluation metric:** Calibration across the price range, not accuracy — the model is used to choose a price, so it must be trustworthy at prices other than the one that was set. Report expected-revenue improvement against the operator's actual pricing under a policy comparison, with explicit uncertainty.
**Scope:** Endogeneity is the central difficulty: prices were set in response to the same conditions that drove demand, so naive regression recovers the operator's pricing policy rather than the demand curve. Renewals are the cleaner problem and should be built first — the population is the operator's own residents, the outcome is unambiguous, and no competitor data is involved at any point. Small, disclosed price variation where lawful helps identification enormously. 3 ML engineers plus an economist, 6-9 months, with counsel involved in the design rather than after it.
**Data availability:** Lease outcomes are complete. The funnel above them is under-collected — most platforms record leases signed and discard enquiry and abandonment detail, which is exactly the demand signal needed. Fixing that capture is a prerequisite product change.

---

## 2. Work Order Classification and Escalation Risk
#bert #large-language-models #word-embeddings #gradient-boosting #feature-engineering #evaluation-metrics #confidence-intervals

**Problem statement:** A work order arrives as a resident's sentence and a dropdown they did not understand. Triage decides the trade, the urgency and the vendor, and the difference between routine and emergency is currently the resident's own priority selection, which is unreliable in both directions. A slow leak treated as routine becomes a water damage claim.

**ML task:** Multiclass classification of the underlying issue from free text plus unit context, and a separate binary model for escalation to a damage event
**Input data:** Resident description text, submitted photographs, unit and building age, plumbing and system type where recorded, prior work orders on the same unit and component, season, the trade eventually dispatched, the resolution, and downstream insurance claims or emergency callouts.
**Target:** The actual issue category as resolved by the technician; and separately, whether the ticket escalated to emergency or a damage claim within a defined window.
**Evaluation metric:** For classification, top-3 accuracy since the operational use is trade selection. For escalation, recall at a manageable alert volume is what matters — the base rate is low and the cost asymmetry is extreme, so the model should be tuned to over-flag and measured on how many claims it would have caught per false alarm.
**Scope:** Escalation labels are rare and must be assembled from insurance claims and emergency work orders, which sit in different systems. Photographs at submission add substantial signal and are increasingly common. 2 ML engineers plus a maintenance operations lead, 4-5 months.
**Data availability:** Work order volume is enormous across these platforms. Resolution categories are recorded inconsistently and often as a technician's free text, requiring an extraction pass. Claim linkage is the weakest join and the most valuable.

---

## 3. Vendor Performance Measurement from Recurrence
#survival-analysis #gradient-boosting #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #causal-inference

**Problem statement:** Maintenance vendors are selected on relationship and responsiveness. Whether their repairs actually hold is directly observable — a repeat work order on the same unit and component after a repair is a failed repair — and no platform computes it.

**ML task:** Time-to-recurrence modelling per vendor per work category, with adjustment for the difficulty of the jobs each vendor receives
**Input data:** Work orders with vendor, category, unit, component, completion date and invoice amount; subsequent work orders on the same unit and component; quoted versus invoiced amounts; response and completion times; property and unit condition attributes.
**Target:** Recurrence of the same issue within a horizon, treated as a survival outcome with censoring at move-out or portfolio exit.
**Evaluation metric:** Discrimination between vendors after adjusting for job mix, with confidence intervals wide enough to be honest about small samples — most vendors do few jobs, and the temptation to rank on three observations is the main way this analysis goes wrong. Report the number of jobs required before a vendor's score becomes meaningful.
**Scope:** Confounding is the real work: good vendors get the hard jobs, older buildings recur more regardless of vendor, and a vendor working one property is not comparable to one working forty. Hierarchical modelling with property effects handles this. The output should be a decision aid for dispatch, not a public league table. 2 ML engineers, 4 months.
**Data availability:** Complete within the platform and entirely unused. Component-level identification of what was repaired is the main quality gap, since work orders frequently record a category rather than a component.

---

## 4. Make-Ready Scope and Duration Prediction
#gradient-boosting #time-series-forecasting #survival-analysis #feature-engineering #confidence-intervals #evaluation-metrics #optimization-fundamentals

**Problem statement:** Turnover coordination is done by phone by a site manager, and the ready date promised to leasing is a guess. Scope surprises discovered mid-turn cascade through vendor bookings and are the main cause of extended vacancy, which is pure loss.

**ML task:** Multi-label prediction of required make-ready scope at notice-to-vacate, plus duration forecasting per scope element and a scheduling optimisation over vendor availability and task dependencies
**Input data:** Unit age, last renovation date, tenancy length, move-in and move-out inspection records and photographs, work order history during tenancy, resident deposit disposition history, prior turns on comparable units, vendor availability calendars and historical vendor lead times.
**Target:** The scope actually performed and the realised duration per element, plus total days from notice to rent-ready.
**Evaluation metric:** For scope, per-element recall — a missed element is the surprise that causes the cascade, while a spurious one is caught at inspection. For duration, quantile accuracy, since the ready date given to leasing should be a date the operator can commit to rather than an optimistic mean.
**Scope:** Move-in and move-out inspection photographs are the highest-signal input and are increasingly captured through the platform's own inspection apps, which makes a vision component worthwhile. The scheduling layer is classical optimisation once durations are honest. 2-3 ML engineers, 5-6 months.
**Data availability:** Good and improving as inspection capture becomes standard. Historical scope is recorded through invoices rather than as a structured scope list, so the target requires derivation from vendor line items.
