# Machine Learning Opportunities — Facilities Management Firms

**Industry:** [[facilities-management-firms|Facilities Management Firms]]
**Derived from:** [[problems/facilities-management-firms/high-impact|High Impact]], [[problems/facilities-management-firms/low-impact-1|Low Impact 1]], [[problems/facilities-management-firms/low-impact-2|Low Impact 2]], [[problems/facilities-management-firms/worker-life-1|Worker Life 1]], [[problems/facilities-management-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Building Engineer's Read of the Plant
#tacit-knowledge-ml #lstms-and-grus #autoencoders #gradient-boosting #survival-analysis #evaluation-metrics #worker-facing

**Problem statement:** Experienced building engineers recognise, from BAS trend shapes, equipment sounds and the wording of work orders, that a chiller, air handler, pump or boiler is heading for failure or that a call is not what it says. The ML problem is to learn those reads from the engineers' own in-the-moment annotations and the subsequent work-order outcome, and to surface them to technicians and incoming teams who lack the experience.

**ML task:** Per-asset sequence classification over BAS trend windows (early-warning pattern present or not, by failure family), unit-specific anomaly scoring from a model of each machine's own normal operation, and time-to-intervention estimation; secondary text classification of incoming work orders into "likely different from stated" categories
**Input data:** BAS trend logs at 1–15 minute intervals (supply and return temperatures, valve and damper positions, fan and pump status, chiller kW, approach temperatures), alarm histories, CMMS work orders with free text and any failure codes, PM records, engineers' short voice or tap annotations attached to assets during rounds, and on a few critical machines vibration or acoustic sensors.
**Target:** Engineer-annotated early-warning labels by failure family; "intervention or failure within N days" per asset; agreement between model and engineer on held-out annotations.
**Evaluation metric:** Lead time and precision at a fixed alert budget per building per week. A technician will act on two good alerts a week and ignore ten, so precision at low volume matters more than overall recall. For the annotation task, agreement with held-out engineer labels, reported against the engineer's own test-retest agreement as the ceiling. Evaluate strictly by time and by building, because a model that has seen the same unit's future is leaking it.
**Scope:** The data collection challenge comes first: the engineer's read must be captured while they work, so the product needs a near-zero-effort annotation surface (a few spoken words on the mechanical-room round, attached to the asset by QR code or location), and historical work orders must be aligned to trend windows after the fact. The labelling challenge is that successful interventions erase the failure that would prove the call right, and engineers disagree with themselves across seasons, so outcomes are defined as intervention-or-failure and a sample is re-annotated to measure consistency. The deployment challenge is speed and audience: the alert has to beat the expert, which in practice means serving the night technician and the post-transition team. 2 ML engineers and 1 controls engineer embedded at three or four large accounts, 9–12 months, with value appearing first as asset-level retrieval ("the last three times this AHU did this") before any classifier is trusted.
**Data availability:** BAS trend data exists in most large buildings but is often retained for only weeks to months, stored in vendor formats and owned by the client, so access agreements come first. Work orders are plentiful and poorly coded. Engineer annotations do not exist and must be built prospectively; that capture is most of the project.

---

## 2. IFM Baseline Cost Prediction at Bid
#gradient-boosting #bayesian-inference #confidence-intervals #feature-engineering #monte-carlo-methods #revenue-impact

**Problem statement:** Before a bid closes, predict the annual maintenance labour hours, reactive work-order volume and subcontract spend each site in a target portfolio will generate, with honest uncertainty, from the asset list, building attributes and whatever spend history the RFP provides, so the price reflects the building's true cost rather than the incumbent's numbers.

**ML task:** Hierarchical regression of site-level annual cost components with partial pooling across building types and regions, plus simulation of the portfolio-level cost distribution for pricing
**Input data:** The provider's own history across accounts it has run: site attributes (type, gross area, age, climate zone, operating hours, criticality), asset counts by class and age, PM task libraries, actual labour hours, reactive work orders and subcontract spend per site per year, and the bid-time data it had for those same sites, including the asset list error discovered at transition.
**Target:** First-year and steady-state annual hours and spend per site by service line; the gap between the bid-time asset list and the transition-verified list.
**Evaluation metric:** Out-of-sample error on held-out accounts, judged on the portfolio total rather than per site, because pricing risk lives at the contract level. Calibration of the prediction intervals matters most: an 80% interval that contains the actual only half the time will misprice every account the same way. Underestimates cost more than overestimates on a fixed-price contract, so report the bias separately.
**Scope:** The hard part is assembling a clean history that joins bid-time inputs to delivered outcomes across accounts, which most providers have never done, because bid models and account P&Ls live in different teams. 1 data scientist, 1 pricing analyst and a data engineer, about 6 months to a first model, which is useful only to firms with several hundred sites of delivered history.
**Data availability:** Held by the large IFM providers, in pricing files, CMMS instances and account financials. Client-owned CMMS instances may restrict reuse of site-level records, so the model should train on the provider's own cost and labour data.

---

## 3. Self-Delivery Versus Subcontract Allocation
#optimization-fundamentals #linear-regression #monte-carlo-methods #feature-engineering #revenue-impact #workflow-orchestration

**Problem statement:** For each service line in each region of a live account, decide whether the provider's own technicians or a subcontractor should do the work, given the expected work volume, travel, skill mix, SLA penalties and the pass-through markup the contract allows.

**ML task:** Cost-to-serve regression for self-delivered work (labour hours, travel, utilisation by region and skill) feeding a constrained optimisation of the delivery mix, with scenario simulation over demand uncertainty
**Input data:** Work orders with labour hours and travel times by technician and site; technician skills, wages and utilisation; subcontractor invoices by trade and region; SLA performance by delivery route; contract pass-through and markup terms.
**Target:** Expected margin and SLA attainment per service line and region under each delivery choice; recommended mix and the volume threshold at which it flips.
**Evaluation metric:** Margin and SLA attainment of the recommended mix against the actual mix on held-out periods, using the account's own costs. Report the robustness of the recommendation to demand swings, because a decision that flips with a 10% volume change is not actionable.
**Scope:** Modest modelling with demanding data joins: technician time must be attributed to work orders cleanly, which in practice means repairing time-card data. 1 operations research analyst and 1 data engineer, 4–5 months for a regional pilot.
**Data availability:** All inside the provider, in CMMS, payroll and AP systems, but rarely joined. Subcontractor price data is the provider's own invoice history.

---

## 4. Service Desk Request Classification and Priority
#bert #transformers #large-language-models #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Classify every incoming occupant request (from phone transcript, email, portal or app) into trade, asset, priority and likely root cause, and route it to the right technician or subcontractor inside the SLA response window.

**ML task:** Multi-label text classification (trade, asset class, priority) with calibrated confidence, plus retrieval of the site's recent work orders on the same asset to detect repeats
**Input data:** Historical requests with their final corrected classification, the work order that resolved them, site and asset registers, priority definitions from each contract, and call transcripts.
**Target:** Trade, asset class, priority tier, and a duplicate or repeat flag; human escalation when confidence is low.
**Evaluation metric:** Accuracy on priority above all, weighted asymmetrically: a true emergency classified as routine is a safety and SLA failure, while a routine call raised to priority 1 wastes a callout. Measure first-time-right dispatch rate and the share of requests needing no human triage.
**Scope:** Labels exist in volume, as every closed ticket carries the classification it ended with, though corrections are noisy. 1 ML engineer and a service desk lead, 3–4 months to production on one large account.
**Data availability:** Held by the providers and the CMMS vendors in the service desk record; transcripts need consent and retention handling.

---

## 5. Subcontractor Invoice Anomaly Detection
#large-language-models #gradient-boosting #k-nearest-neighbors #gaussian-mixture-models #descriptive-statistics #revenue-impact

**Problem statement:** Extract line items from subcontractor invoices, validate them against the work order, rate card and contract terms, and flag invoices whose amount is unusual for the job even when it sits under the not-to-exceed.

**ML task:** Document extraction into structured lines, rule validation against rate cards, and density-based anomaly scoring of invoice amount given job features (trade, asset class, region, hours, time of day)
**Input data:** Invoice PDFs; work orders with NTE, asset and completion data; rate cards by subcontractor, trade and region; contract markup and approval rules; history of disputed and credited invoices.
**Target:** Extracted line items; rule violations; an anomaly score and a reason; a predicted dispute outcome.
**Evaluation metric:** Recovered value per hour of reviewer time against current manual review, and precision at the review budget the AP team can handle. Missing an overbill costs money and credibility with the client; a false flag delays a subcontractor's payment, so keep false-flag rates low for trusted vendors.
**Scope:** Extraction is now reliable with document-capable language models; the value is in the per-account rule library and the comparison set of similar jobs. 1 ML engineer and 1 AP lead, 4 months.
**Data availability:** Invoices and work orders sit with the provider; disputed-invoice outcomes are in email and need reconstructing for a training set.
