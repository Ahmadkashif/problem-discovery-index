# Machine Learning Opportunities — Plumbing & HVAC Distributors

**Industry:** [[plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Derived from:** [[problems/plumbing-and-hvac-distributors/high-impact|High Impact]], [[problems/plumbing-and-hvac-distributors/low-impact-1|Low Impact 1]], [[problems/plumbing-and-hvac-distributors/low-impact-2|Low Impact 2]], [[problems/plumbing-and-hvac-distributors/worker-life-1|Worker Life 1]], [[problems/plumbing-and-hvac-distributors/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Applications Specialist's Selection and Substitution Judgement
#tacit-knowledge-ml #large-language-models #transformers #k-nearest-neighbors #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Veteran applications specialists read an engineer's mechanical and plumbing schedules and "just know" which of the house's models truly matches each basis-of-design line at the design conditions, which accessories the drawings imply, and which equals this engineer will approve. The ML problem is to learn those selections and approval calls from the specialist's own edits and from later submittal outcomes, and surface them to newer quoters on bid day.

**ML task:** Structured extraction of schedule lines and requirements; retrieval and ranking of candidate models from manufacturers' performance data; multi-label prediction of implied accessories; binary classification of submittal approval conditioned on spec language, engineer and product family
**Input data:** Schedule pages from drawing PDFs (equipment and fixture schedules with capacities, airflow, static pressure, electrical data, efficiency, fixture models and options), Division 22 and 23 specification sections with addenda, manufacturers' performance tables and selection-software outputs, the specialist's final selections and accessory lines with reasons, submittal responses by line, and post-award returns and change orders.
**Target:** Ranked equivalent models per schedule line with the margin against each requirement; probability that each implied accessory is needed; probability of first-pass submittal approval per substitution.
**Evaluation metric:** Top-1 and top-3 agreement with the senior specialist's selection on held-out packages split by time and by engineer; recall on accessories the senior added, at a precision the quoter will tolerate (a missed curb adapter or low-ambient kit costs a field change; a false flag costs seconds); AUC and calibration of approval predictions against actual submittal responses. Report model agreement against the specialists' own test-retest agreement on a re-selected sample as the ceiling.
**Scope:** The data collection challenge comes first: the selection runs, alternatives and reasons are thrown away today, so the quoting screen must log each line's selection inputs and outputs and a one-click reason as the specialist works, and a sample of past packages must be rebuilt from archived schedules. The labelling challenge is that experts disagree with themselves: the same veteran offers a near-match on a design-build job and refuses it on a hard-spec hospital, so two seniors re-select a sample to measure agreement, and submittal outcomes arrive weeks later from the contractor's project platform. The deployment challenge is speed: suggestions must arrive within minutes of the schedule landing, with the performance table and the engineer's history attached, faster than the veteran's own read, or they will be ignored. 2 ML engineers and a senior specialist as domain lead, 6–9 months; value appears first as schedule extraction and "accessories usually added on jobs like this" before any approval classifier is trusted.
**Data availability:** Schedules and specs arrive with every bid request; manufacturers publish performance data, though selection software is per brand. The edit trail, reasons and submittal responses do not exist in distributor systems until the workflow captures them.

---

## 2. Weather- and Regulation-Aware Branch Demand Forecasting
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #monte-carlo-methods #feature-engineering #revenue-impact

**Problem statement:** Forecast weekly demand for condensers, coils, furnaces, heat pumps and water heaters by branch and tonnage or capacity, conditioned on weather forecasts, the installed base and regulatory cutoffs, and plan components as matched sets so a branch never has the condenser without the coil.

**ML task:** Multi-horizon probabilistic forecasting with exogenous weather and regulatory covariates, followed by stochastic optimisation of pre-season buys and transfers
**Input data:** Branch sales and lost-sales signals (quotes not converted, stock-out days), cooling and heating degree-days and extreme-heat and cold-snap forecasts, installed-base age and refrigerant by territory where available, housing permits, AHRI-matched system tables, regulatory effective dates, manufacturers' allocation notices and pre-season terms.
**Target:** Quantiles of weekly demand per branch and SKU family; recommended buy, transfer and sell-down quantities.
**Evaluation metric:** Pinball loss on out-of-time seasons, with peak weeks weighted, and the operational measure that matters: matched-system fill rate in the hottest and coldest weeks against inventory dollars, compared with last year's manual plan on the same weather path. A stock-out on a heat-wave day costs a dealer relationship; a surplus costs carrying cost, so the loss is asymmetric.
**Scope:** 1 data scientist and 1 data engineer, 4–6 months for a first version on a regional distributor's history; regulatory change and allocation are modelled as scenarios rather than learned, because there are only a few such events.
**Data availability:** Sales and inventory are in the ERP; lost sales are rarely recorded and must be inferred; weather data is public; regulatory dates are public but moved in 2026, so scenario handling matters more than history.

---

## 3. Part Identification From Nameplates, Photos and Model Numbers
#cnns #contrastive-learning #transformers #k-nearest-neighbors #worker-facing #automation

**Problem statement:** Given a technician's photo of a nameplate or a failed part, or a typed model and serial number, return the exact OEM replacement and approved universal alternatives, so the counter and the text queue can answer in seconds.

**ML task:** OCR and parsing of nameplate photos; model-number normalisation and serial-date decoding; image retrieval of failed parts against catalogue images; ranking of candidate parts from bills of material and cross-reference tables
**Input data:** Nameplate and part photos from texts and counter cameras, manufacturers' parts lists and bills of material, universal-part cross-references, the distributor's sales and return history by model, and the counter person's confirmations and corrections.
**Target:** Parsed model and serial; ranked list of OEM and universal part numbers with confidence; flag when the part is superseded or obsolete.
**Evaluation metric:** Top-1 and top-3 accuracy against the part actually sold and not returned, on photos split by time and branch; wrong-part return rate as the business metric, since a wrong capacitor costs a technician a trip while a slow answer costs a minute.
**Scope:** 1–2 ML engineers, 4–6 months; nameplate OCR is mature, while failed-part image matching needs a labelled set captured at the counter. Bluon's PartsConnect shows the model-number database exists commercially.
**Data availability:** Parts lists are scattered across manufacturers' sites; the distributor holds sales and returns but not the photo-to-part link until the counter workflow captures it.

---

## 4. Warranty Claim Pre-Check and Rejection Prediction
#logistic-regression #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict which warranty claims each manufacturer will reject, and why, before they are filed, and assemble the claim fields and evidence automatically from the counter transaction.

**ML task:** Extraction of claim fields from texts, photos and invoices; binary and multi-class classification of rejection risk by reason code
**Input data:** Claim histories with each manufacturer's acceptance, rejection and reason codes; model and serial data with decoded manufacture dates; registration lookups; install dates; matched-system records; failed-part return records; invoice lines for replacement parts.
**Target:** Probability of rejection and most likely reason per claim; a completed claim payload for each portal.
**Evaluation metric:** Recovered credit dollars and first-submission acceptance rate against the current process on the same claims; precision at the top of the review queue, because a clerk can only rework so many claims a day.
**Scope:** 1 ML engineer and a warranty clerk as domain lead, 3–4 months; rejection histories give supervised labels directly, while portal submission needs per-manufacturer integration or screen automation.
**Data availability:** Claims and outcomes sit in manufacturers' portals and the distributor's credit records; exports vary by manufacturer and need joining by serial number.

---

## 5. Copper and PVC Price-Sheet Forecasting for Held PVF Quotes
#exponential-smoothing #change-point-detection #linear-regression #monte-carlo-methods #evaluation-metrics #revenue-impact

**Problem statement:** Forecast when copper tube and fitting makers and PVC pipe makers will issue new price sheets, and by how much, so the distributor can set hold periods on mechanical contractors' pipe, valve and fitting packages and flag held quotes and unreleased lines whose margin is eroding.

**ML task:** Regression of price-sheet changes on copper and resin references with lags; change-point detection on manufacturers' announcement patterns; simulation of margin at release for each open quote
**Input data:** COMEX copper settlements, PVC resin assessments where licensed, manufacturers' price sheets and effective dates, tariff changes, the distributor's replacement costs, quote and release history with hold terms and realised margins.
**Target:** Probability and size of the next price-sheet change per product family over 1–60 days; distribution of margin at release per open quote.
**Evaluation metric:** Share of PVF lines released below margin floor, against current practice on the same price path; announcement-timing forecasts scored by Brier score.
**Scope:** 1 data scientist, 2–3 months; PVC is harder than copper because the public reference is thin and pricing has been alleged to follow a weekly report now under antitrust litigation, so the model leans on the distributor's own price-sheet history.
**Data availability:** COMEX data is public; resin assessments are subscription data; price sheets and hold terms are in the distributor's systems, though hold terms are often unrecorded.
