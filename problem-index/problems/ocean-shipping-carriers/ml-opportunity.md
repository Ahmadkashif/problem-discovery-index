# Machine Learning Opportunities — Ocean Shipping Carriers

**Industry:** [[ocean-shipping-carriers|Ocean Shipping Carriers]]
**Derived from:** [[problems/ocean-shipping-carriers/high-impact|High Impact]], [[problems/ocean-shipping-carriers/low-impact-1|Low Impact 1]], [[problems/ocean-shipping-carriers/low-impact-2|Low Impact 2]], [[problems/ocean-shipping-carriers/worker-life-1|Worker Life 1]], [[problems/ocean-shipping-carriers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Trade Desk's Read of Which Bookings Will Load
#tacit-knowledge-ml #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced trade managers "know" which customers' bookings will turn up, which will shrink and which will vanish when a cheaper slot appears, and they set overbooking and roll decisions on that read. It leaves with them. The ML problem is to learn the read from booking history and the desk's own recorded decisions, and give every booking a calibrated probability of loading on its sailing.

**ML task:** Binary classification (loads on booked sailing or not) with calibrated probabilities, plus regression of booked-to-loaded quantity shrinkage, and time-to-cancellation survival modelling for the booking's life before cut-off
**Input data:** Booking records with creation, amendment and cancellation timestamps; customer and forwarder history; rate paid relative to the week's index (Drewry WCI, Xeneta, FBX) and to the contract rate; lead time to cut-off; competitor blank sailings and capacity changes; holiday calendars (Lunar New Year, Golden Week); the desk's own overbooking targets, protect and roll decisions with reasons once a decision ledger exists.
**Target:** Load/no-load on the booked sailing; loaded TEU against booked TEU; cause of failure where coded (shipper cancellation, cargo not ready, customs hold, carrier roll).
**Evaluation metric:** Brier score and reliability curves on held-out sailings, strictly out of time and by trade. Revenue impact is measured in a replay: recommended overbooking levels against what the desk actually did, scored on empty slots plus the value of high-paying cargo rolled. Errors are asymmetric: an empty slot is lost revenue once, while rolling a key account's cargo can lose the contract, so roll recommendations need a protected-customer constraint. The desk's own test-retest consistency on a sample is the ceiling for agreement.
**Scope:** The data collection challenge comes first: the desk's private estimates and reasons are not in any system, so the first deliverable is a near-zero-effort decision ledger inside the booking-acceptance screen, with reasons drafted for one-click confirmation. The labelling challenge is that "did not load" mixes shipper cancellations, factory delays and carrier rolls, and trade managers disagree with themselves after a run of bad weeks, so causes must be coded from documents and a sample re-judged to measure consistency. The deployment challenge is speed: the probability must appear before the desk commits space in the weekly allocation call, and beat the trade manager's own recall of the customer. 2 ML engineers, 1 data engineer and a pricing lead embedded with one trade, 6–9 months, starting with one lane and showing value first as "this customer's last 20 bookings" before any model is trusted.
**Data availability:** Carriers hold years of booking and load data internally; outsiders cannot get it, so this is an in-house or embedded-vendor build. Index rates are licensable. Decision reasons do not exist yet and must be captured prospectively.

---

## 2. Shipping Instruction Extraction and Draft B/L Validation
#large-language-models #transformers #evaluation-metrics #feature-engineering #automation #data-integration

**Problem statement:** Convert shipping instructions received as email bodies, PDFs, scans and spreadsheets into a structured draft bill of lading, reconciled with the booking, and flag fields likely to need amendment before issue.

**ML task:** Layout-aware document extraction into the DCSA bill-of-lading schema, plus field-level classification of amendment risk
**Input data:** SI documents of every format; booking records; the shipper's historical SIs and the amendments made to them; party master data; HS code tables; dangerous goods and reefer rules; trade-lane manifest requirements (US 24-hour and ISF, EU ICS2).
**Target:** Field values with confidence; reconciliation flags against the booking; probability that each field is amended after issue.
**Evaluation metric:** Field-level exact match on parties, cargo description, container and seal numbers, weights and HS codes, weighted by the cost of an error (a wrong consignee or container number costs far more than a formatting slip); straight-through rate at a fixed error ceiling; and post-issue amendment rate against the current manual baseline.
**Scope:** A demo is two weeks on synthetic SIs generated against the public DCSA schema; a production system is 2–3 engineers for 4–6 months, mostly on validation rules and the carrier-system integration rather than the extraction model. The hard part is the long tail of shipper formats and destination rules.
**Data availability:** Carriers hold millions of SIs and their amendment history, and labels come almost free, because the issued B/L is the corrected answer for each SI. SIs and booking requests are the shipper's or forwarder's submissions; the US manifest copy becomes public through CBP's AMS release (recalled; see [[niches/customs-brokers/import-export-transaction-data/profile|Import & Export Transaction Data Providers]]). Booking confirmations, draft and master bills and amendment history are carrier records, and house bills belong to the issuing NVOCC. So a vendor trains per carrier under that carrier's service agreement, a pooled model needs each carrier's consent, and outsiders start from synthetic SIs and the public DCSA schemas.

---

## 3. Weather-Corrected Speed–Fuel Baselines for Performance Claims and Emissions
#gaussian-processes #linear-regression #feature-engineering #confidence-intervals #compliance #revenue-impact

**Problem statement:** Estimate, for each ship, the fuel it should burn at a given speed, draught, trim, hull condition and weather, so that charter party speed and consumption claims, hull-cleaning decisions and EU ETS and FuelEU forecasts rest on a defensible baseline.

**ML task:** Probabilistic regression of fuel consumption on speed through water, draught, trim, wind, waves and current, with uncertainty, and change-point tracking of hull and propeller fouling
**Input data:** Noon reports or high-frequency sensor data; hindcast weather and ocean data; sea trial and shop test curves; hull cleaning and dry-dock dates; bunker delivery notes and fuel specifications; public EU MRV annual figures per ship as a sanity check.
**Target:** Expected daily consumption with a confidence interval; the fouling penalty over time; good-weather performance under charter party definitions.
**Evaluation metric:** Out-of-sample error on held-out voyages, and calibration of the intervals, since a performance claim turns on whether over-consumption exceeds the warranted allowance with confidence. Bias matters more than variance: a baseline that is systematically optimistic manufactures claims.
**Scope:** 1–2 data scientists with a naval architect, 4–6 months per vessel class. Noon-report data is noisy and self-reported, so the honest product is wide intervals that narrow with sensor data.
**Data availability:** Owners and operators hold noon reports and sensors; charterers receive noon reports for chartered tonnage; weather hindcasts are licensable; EU MRV annual per-ship emissions are published.

---

## 4. Vessel Arrival and Schedule-Recovery Forecasting
#temporal-fusion-transformers #time-series-forecasting #gradient-boosting #evaluation-metrics #workflow-orchestration

**Problem statement:** Forecast each vessel's arrival and berthing time at every remaining port in its rotation, and the knock-on arrival of every booking after a blank sailing, port omission or re-routing, so service desks and customers get a realistic date with a range.

**ML task:** Multi-horizon probabilistic forecasting of port arrival and berthing times, plus booking-level re-planning estimates under network changes
**Input data:** AIS positions; published schedules and proforma rotations; port congestion and berth-wait data; weather routing; carrier operations messages on omissions and blank sailings; historical arrival deviations by port, terminal and season.
**Target:** Arrival and berthing time distributions per port call; booking-level estimated availability date.
**Evaluation metric:** Mean absolute error in hours at 7, 3 and 1 days out, coverage of the 80% interval, and the share of bookings given an availability date that held. Lateness matters more than earliness for downstream demurrage.
**Scope:** 2 ML engineers, 4 months to a strong baseline. Arrival prediction is a crowded vendor space (project44, Portcast and others), so the carrier-side value is in the booking re-plan after a network decision, which only the carrier can compute.
**Data availability:** AIS is licensable; schedules are public; network decisions and booking data are internal.

---

## 5. Demurrage and Detention Dispute Triage
#bert #logistic-regression #large-language-models #compliance #automation

**Problem statement:** Classify incoming D&D disputes by reason and predict which charges will be waived, so billing teams resolve each within the FMC's 30-day window and fix the upstream causes.

**ML task:** Multi-class text classification of dispute emails by reason (terminal closed, no appointments, vessel delay, wrong party, free-time error), plus probability that the charge is waived or reduced
**Input data:** Dispute emails and attachments; invoice data with the 46 CFR 541 elements; container milestones; terminal appointment and closure records; historical outcomes.
**Target:** Dispute reason; outcome (upheld, reduced, waived); evidence that supports or defeats the dispute.
**Evaluation metric:** Macro-F1 on reason codes; calibration of waiver probability; time to resolution against the 30-day limit. Wrongly upholding a valid dispute risks an FMC charge complaint, so recall on valid disputes outranks precision.
**Scope:** 1 ML engineer and a billing lead, 3–4 months. The model triages and drafts; a person decides.
**Data availability:** Carriers and NVOCCs hold their disputes and outcomes, and terminal appointment and closure records come from terminal systems; reasons are rarely coded today and must be labelled from history.
