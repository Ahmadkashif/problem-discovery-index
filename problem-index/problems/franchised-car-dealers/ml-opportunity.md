# Machine Learning Opportunities — Franchised Car Dealers

**Industry:** [[franchised-car-dealers|Franchised Car Dealers]]
**Derived from:** [[problems/franchised-car-dealers/high-impact|High Impact]], [[problems/franchised-car-dealers/low-impact-1|Low Impact 1]], [[problems/franchised-car-dealers/low-impact-2|Low Impact 2]], [[problems/franchised-car-dealers/worker-life-1|Worker Life 1]], [[problems/franchised-car-dealers/worker-life-2|Worker Life 2]]

---

## 1. Learning the New-Car Manager's Order Board
#tacit-knowledge-ml #gradient-boosting #survival-analysis #causal-inference #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Experienced new-car managers decide which offered configurations to take, decline or trade from the OEM's allocation using a feel for the local market they cannot specify. The ML problem is to predict, for each offered unit, its time-to-sale and gross at this store, estimate what declined configurations would have done, and surface the manager's own historical pattern with its track record at the moment of the next order.

**ML task:** Survival regression (time-to-retail-sale with right-censoring for units still in stock) and gross-profit regression by configuration and store; counterfactual estimation for declined configurations using pooled outcomes from comparable stores; a take/decline/trade recommendation optimised against days supply, gross and the open stair-step gap
**Input data:** OEM allocation and order-bank offers with timestamps; the manager's accept, decline and dealer-trade decisions; DMS vehicle sales history (VIN, configuration, days in stock, front gross, incentives applied); inventory snapshots; licensed local registration share by segment and trim (see [[niches/auto-dealers-independent/registration-market-intelligence/profile|Vehicle Registration & Market Intelligence Data]]); website vehicle detail page views and leads by configuration; monthly programme rules and stair-step targets; seasonality and weather.
**Target:** Days from delivery to retail sale (censored); front gross at sale net of incentives; probability of becoming a 90-day aged unit; and, as a secondary signal, agreement with the manager's decision.
**Evaluation metric:** Concordance index and calibration of the survival model, evaluated strictly out of time on later order cycles, never on random splits. Decision value is measured by back-simulation: days supply and gross of the recommended mix versus the mix actually ordered, against a "repeat last quarter's mix" baseline. Missing an aged unit costs more than recommending against a unit that would have turned, so recall on future 90-day aged units matters more than precision. Agreement with the manager is reported against the manager's own consistency on repeated, near-identical offers as the ceiling.
**Scope:** The data collection challenge comes first: the decision happens in an OEM portal that records the order but not the reason, so history must be rebuilt from order-bank snapshots, allocation notices and trade logs joined to DMS sales, and prospective capture needs a one-click reason code inside a short order window. The labelling challenge is that outcomes are censored, confounded by later price and incentive moves, and missing entirely for configurations never ordered, and managers disagree with themselves after a month of aged inventory; pooled group data and causal methods address the counterfactual, and repeated annotation on a sample measures intra-manager consistency. The deployment challenge is speed and trust: the recommendation must arrive inside the order window, faster than the manager's own scan, with comparable units and the stair-step arithmetic shown. 2 ML engineers and 1 data engineer working with a dealer group of 10+ stores of one brand, 6–9 months; value appears first as a retrieval view ("last 12 of this configuration sold in a median 11 days") before any recommendation is trusted.
**Data availability:** Sales history and inventory sit in the dealer's DMS, which the dealer can export but whose third-party access terms vary by vendor. Allocation and order-bank data sit in OEM portals, usually without an API. Registration data is licensable. The decision reasons do not exist and must be captured going forward.

---

## 2. Warranty Claim Rejection and Chargeback Risk
#bert #transformers #gradient-boosting #feature-engineering #evaluation-metrics #compliance #automation

**Problem statement:** Before a warranty claim is submitted, predict whether the OEM will reject it and whether it will be charged back in a later audit, and say why, so the administrator fixes the claim before it costs money.

**ML task:** Binary classification of rejection and of chargeback-within-audit-window, plus multi-class classification of the likely reason; text classification of the technician's complaint-cause-correction story against the claimed operation code
**Input data:** Repair-order lines (labour op code, claimed and guide labour time, causal part, parts retained), technician story text, diagnostic trouble codes and test notes, prior-authorisation records, photos attached (yes/no), technician and administrator IDs, OEM response codes for past claims, resubmission history and audit chargeback letters.
**Target:** Rejected on first submission (yes/no); charged back within the statutory window (yes/no, e.g. six months under Virginia § 46.2-1571); rejection or chargeback reason category.
**Evaluation metric:** Recall of claims later rejected or charged back at a fixed review budget (for example, the riskiest 10% of claims), because a missed defect costs the full claim while a false flag costs a minute of review; dollars of rejection and chargeback avoided per administrator hour. Calibration matters for setting the review threshold per OEM.
**Scope:** Each OEM's rules differ, so models are trained per brand on a group's pooled claim history; the story classifier transfers across brands better than the structured rules. 1–2 ML engineers, 4–5 months for one brand family, with an OEM rule library maintained alongside. Chargebacks are rarer than rejections and need longer history.
**Data availability:** Claims and OEM responses are in the DMS warranty module and OEM portal statements; audit letters are often PDFs or paper. The dealer owns its claim history; pooling across dealers needs each dealer's consent.

---

## 3. Service Call Understanding and Booking
#large-language-models #transformers #seq2seq #evaluation-metrics #workflow-orchestration #worker-facing #automation #revenue-impact

**Problem statement:** Turn each inbound service call or text into the right action — a booked appointment against real technician capacity, a status answer from the repair order, a recall booking, or a handoff to the advisor — without losing the caller.

**ML task:** Speech-to-text, intent classification (book, reschedule, status, approval, recall, parts, warranty question, complaint), slot extraction (VIN or plate, mileage, concern in the customer's words, preferred time, transport need), and dialogue generation constrained by scheduler and repair-order data
**Input data:** Call audio and transcripts with dispositions from call-tracking systems; text threads; DMS scheduler availability by technician skill and op code; open repair orders and technician clock status; open-recall lookups by VIN; loaner fleet availability.
**Target:** Correct intent and slots per call; a booked appointment that is kept; correct status answers; escalations for safety concerns, angry customers and complex diagnoses.
**Evaluation metric:** Share of inbound service contacts that become kept appointments, measured against the store's own pre-deployment baseline (Car Wars' network counted ~4 million appointments from ~53 million calls in 2025). Escalation recall is the safety metric: a missed brake or airbag concern or a furious customer handled by a bot costs far more than an unnecessary handoff. VIN and phone-number extraction accuracy is tracked separately because one wrong character breaks the booking.
**Scope:** The language part is now commodity; the hard part is integration with each DMS scheduler and repair-order status, and op-code and labour-time quoting rules per store. 2 engineers and 1 conversation designer, 3–4 months to a production pilot on one DMS.
**Data availability:** Call recordings and dispositions are held by the dealer and its call-tracking vendor under consent rules that vary by state; scheduler and repair-order data come through DMS integrations whose access terms the DMS vendors control.

---

## 4. Deal-Jacket Defect Detection and Add-On Pricing Disparity
#autoencoders #gradient-boosting #bayesian-inference #hypothesis-testing #confidence-intervals #compliance #evaluation-metrics

**Problem statement:** Find deal jackets with missing or inconsistent documents before funding, and detect patterns in add-on product pricing that differ across customer groups in ways a regulator or plaintiff would treat as discriminatory or deceptive.

**ML task:** Supervised classification of document defects where audit labels exist; unsupervised anomaly detection (autoencoder reconstruction error) on deal structure for novel defects; disparity testing of add-on prices and finance reserve across proxy demographic groups with Bayesian proxy estimation
**Input data:** Deal records (vehicle, price, trade, products sold and prices, lender, rate and reserve), document inventory and extracted fields from scanned or e-signed jackets, first written quote sent to the customer, state and threshold flags, compliance audit findings, cancellations and refunds.
**Target:** Defect present (yes/no, by type); anomaly score; estimated price differences by group with confidence intervals.
**Evaluation metric:** Recall of defects later found by compliance audit, lender funding review or regulator, at a false-flag rate the F&I office will tolerate; for disparity, interval width and stability of the estimates under different proxy methods. A missed defect on a California used-vehicle sale under $50,000 is a statutory violation, so recall is weighted above precision.
**Scope:** Document extraction is the bulk of the work; the anomaly model adds value only after the checklist rules are encoded. Disparity analysis is statistical rather than ML-heavy, and its output must go to counsel, not into an automated decision. 1 ML engineer, 1 compliance analyst, 4 months.
**Data availability:** The dealer owns its deal records; scanned jackets need OCR. Audit findings are sparse and sit with compliance vendors or in spreadsheets.

---

## 5. Incentive Bulletin Extraction to VIN-Level Eligibility
#large-language-models #seq2seq #transformers #data-integration #evaluation-metrics #revenue-impact #automation

**Problem statement:** Convert each OEM programme bulletin into a structured, machine-checkable rule and test every delivered deal against every live rule, so that unclaimed incentives are found and ineligible claims are stopped before audit.

**ML task:** Document-to-structure extraction (bulletin PDF or portal page to a programme schema), entity resolution of model, trim and model-year names to the store's VIN-decoded inventory, and rule evaluation over deal records
**Input data:** OEM programme bulletins and portal pages; VIN decodes; delivered-deal records with sale type, customer type and dates; OEM incentive statements and payment files; past audit chargebacks.
**Target:** Programme schema fields (programme ID, effective dates, eligible models, trims and model years, amount, stacking rules, documents required); per deal, eligible and claimed programmes.
**Evaluation metric:** Field-level exact match on extracted rules against a hand-built gold set; incentive dollars found per retail unit that the store had not claimed; zero tolerance for false eligibility on claims submitted without review, because an ineligible claim becomes an audit chargeback with interest.
**Scope:** Bulletins are semi-structured and change monthly; a human checks each extracted rule once and the deal-level matching runs automatically. 2 engineers, 3 months for one OEM, then incremental per OEM.
**Data availability:** Bulletins are distributed to dealers and are the dealer's to use; payment statements come from OEM portals; deal records from the DMS.
