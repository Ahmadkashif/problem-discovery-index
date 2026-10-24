# Machine Learning Opportunities — Powersports & Boat Dealers

**Industry:** [[powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Derived from:** [[problems/powersports-and-boat-dealers/high-impact|High Impact]], [[problems/powersports-and-boat-dealers/low-impact-1|Low Impact 1]], [[problems/powersports-and-boat-dealers/low-impact-2|Low Impact 2]], [[problems/powersports-and-boat-dealers/worker-life-1|Worker Life 1]], [[problems/powersports-and-boat-dealers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Used-Unit Manager's Condition Read
#tacit-knowledge-ml #cnns #object-detection #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** An experienced used-boat or powersports manager walks a trade-in for ~15 minutes (estimate) and "knows" whether the transom is wet, whether the engine has been run hard, whether a side-by-side has been rolled, and what it will really bring in April. The ML problem is to learn that read from captured walkaround evidence joined to what the unit later cost and sold for, and to put a recommended allowance range, with its evidence, in front of the appraiser before they write a number.

**ML task:** Multi-label damage and condition detection from photos and short video (gelcoat cracks, oxidation, corrosion, upholstery wear, frame repairs, aftermarket parts), plus regression of reconditioning cost and realised wholesale and retail price, plus time-to-sale survival modelling
**Input data:** Guided walkaround photos and video by zone (hull, transom, deck, helm, engine, lower unit, trailer; or frame, suspension, drivetrain, plastics); moisture-meter readings by zone; compression numbers; engine data downloads (hours by RPM band, fault codes) where the engine supports them; storage and use history from the customer interview; make, model, year, engine; region and month; the guide value; the manager's allowance and condition notes; later repair orders against the unit, days on lot and final sale price from the DMS.
**Target:** Damage labels per image region; reconditioning cost; season-adjusted realised price; days to sale; and agreement between the model's range and the manager's allowance.
**Evaluation metric:** Mean absolute error of (allowance + reconditioning − realised price) on held-out units, reported by decile of error, because the money is lost in the tail: a model that is a little better on average and much better on the worst 10% of trades is the goal. Measure strictly out of time across a full season. For the detectors, recall on structural findings (soft transom, stringer or frame damage) matters more than precision: a missed structural defect costs thousands, a false flag costs a closer look. Report the model's agreement with managers against managers' own agreement with themselves on re-appraised units, which is the ceiling.
**Scope:** The data collection challenge comes first and is most of the work: the expert's read has to be captured while they perform it, which means a phone workflow that guides the walkaround in under fifteen minutes and records readings without slowing the deal; history before the workflow exists is a price and nothing else. The labelling challenge is that experts disagree with themselves (the same manager appraises differently when the lot is full and the floorplan is aging), realised price mixes condition with season and sales effort, and units refused or wholesaled immediately are selected; labels need season adjustment, a re-appraisal sample to estimate intra-rater reliability, and fresh condition labels from a marine surveyor or master technician on a subset. The deployment challenge is that the range must appear before the manager commits and must beat a guide lookup on the hard units, with the evidence shown so the manager can defend it to the customer. 2 ML engineers and a mobile engineer working with one dealer group, 9–12 months; value appears first as an appraisal record and a grading of past trades, months before any model is trusted.
**Data availability:** Realised prices and repair orders already sit in every dealer's DMS, unjoined to appraisals. Images and readings don't exist yet and must be collected prospectively. A dealer group with 50–100 stores (MarineMax, OneWater, a powersports group) produces enough trades in a season; a single store does not.

---

## 2. Aged-Unit Risk and the Stocking Order
#survival-analysis #gradient-boosting #time-series-forecasting #bayesian-inference #feature-engineering #revenue-impact

**Problem statement:** Predict, for each floored new unit and each candidate unit in next model year's stocking order, the probability it sells before its OEM interest period ends and before its first curtailment, so the manager can order the mix that turns and act early on units that won't.

**ML task:** Time-to-sale survival modelling with competing risks (retail sale, dealer trade, wholesale), plus a demand forecast by configuration and market used to score a proposed stocking order
**Input data:** Unit-level inventory history from the DMS (model, length, engine, colour, package, price, date floored, date sold, discounts given); lender terms by unit (interest-free end date, curtailment schedule); OEM retail programmes by month; local registration data by segment where licensed; boat-show dates; weather and lake-level series; interest rates.
**Target:** Days to sale and probability of sale before each deadline; expected carrying cost and discount if unsold.
**Evaluation metric:** Concordance index and calibration of sale-before-curtailment probabilities on a held-out model year; the business metric is units past first curtailment at model-year end and total carrying cost against the dealer's actual outcome. Over-ordering costs more than under-ordering in a soft year, so the stocking optimiser should be judged at the dealer's own cost of capital.
**Scope:** Inventory histories are clean in the DMS; lender terms are in statements and contracts and need ingestion once per lender. A single store's history is thin for rare configurations, so pooling across a group or a hierarchical Bayesian prior across stores is needed. 1 data scientist and 1 engineer, 4–6 months for a group; OEM programme data is the messy input.
**Data availability:** The dealer holds its own inventory and sales history; registration data is licensable from Statistical Surveys or Info-Link; OEM programme bulletins are issued to dealers monthly and must be extracted.

---

## 3. Warranty Claim Drafting and Rejection Risk
#large-language-models #bert #logistic-regression #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** From a repair order and the technician's notes, draft each OEM's warranty claim (labour operation, failure code, cause and correction wording, photo and parts-return checklist) and score its risk of rejection before it is submitted.

**ML task:** Structured extraction and generation into OEM-specific claim schemas, plus binary classification of rejection risk with reason codes
**Input data:** Repair orders, technician notes and photos; OEM claim formats, labour-time tables, failure code lists and policy bulletins; the dealer's claim history with outcomes (paid, rejected, adjusted, charged back) and rejection reasons.
**Target:** Filled claim fields per OEM; probability of rejection and the likely reason.
**Evaluation metric:** Share of claims paid on first submission and claim dollars paid within the filing window, against the dealer's baseline. For the classifier, recall on claims that will be rejected matters more than precision, since a false alarm costs a minute of review and a missed rejection costs a resubmission or a lost claim. Field-level accuracy against what an experienced administrator would file.
**Scope:** Each OEM's rules are a library to build and maintain; the language model work is turning free-text notes into each OEM's wording. Rejection history is the training signal and exists in the portals and the DMS for any dealer that has filed for a few years. 1 ML engineer and 1 integration engineer, 4–5 months for the first three OEMs.
**Data availability:** Dealers hold their own repair orders and claim outcomes; OEM rules come from dealer-only portals and bulletins, so a vendor needs dealer credentials and permission, and rules change with each model year.

---

## 4. Visual Part Identification Across Catalogs
#cnns #contrastive-learning #k-nearest-neighbors #transformers #feature-engineering #quick-win

**Problem statement:** Identify a part from a photo of a worn or broken original plus the customer's description and model, match it to the right diagram reference in the right OEM catalog, and resolve it to the current part number after supersession.

**ML task:** Image and text retrieval with contrastive embeddings, constrained by model and serial range, followed by rule-based supersession resolution
**Input data:** Exploded diagrams and part images from OEM and aftermarket catalogs; counter photos of returned and replaced parts; the store's lookup and order history with wrong-part returns; supersession tables; model and serial-break data.
**Target:** Ranked candidate part numbers with diagram references; a flag where a serial break or supersession makes the answer uncertain.
**Evaluation metric:** Top-1 and top-3 accuracy against the part actually installed; the business metric is wrong-part return rate and lookup time per ticket. A confident wrong answer costs a week's delay, so the system must abstain and ask for a serial number below a confidence threshold.
**Scope:** Diagrams are drawn, not photographed, so the model must bridge line art and photos of dirty parts; a few thousand labelled counter photos per OEM family get a useful first version. 1 ML engineer and 1 engineer, 3–4 months for one OEM line, longer to cover a multi-line store.
**Data availability:** Catalog content is licensed to dealers and to catalog publishers by the OEMs, which limits training use without a licence; counter photos must be collected at participating stores.

---

## 5. Spring Service Demand Forecasting
#time-series-forecasting #exponential-smoothing #temporal-fusion-transformers #gradient-boosting #workflow-orchestration #worker-facing

**Problem statement:** Forecast weekly commissioning, tune-up and repair demand by job type and skill for the coming season, so the service manager can pre-book work into the shoulder months, schedule technicians and stock parts before the spring rush.

**ML task:** Hierarchical weekly demand forecasting by store, job type and technician skill, with weather and calendar covariates
**Input data:** Several years of repair orders by job type and labour hours; storage and winterization contracts held by the dealer; units sold last season (first service due); weather, water temperature and ice-out dates; Easter, Memorial Day and local lake openings; recall campaigns announced by OEMs.
**Target:** Weekly labour hours demanded by job type and skill; peak backlog in days.
**Evaluation metric:** Weighted absolute percentage error on weekly hours over the March–June window, scored on a held-out season; the business metric is billed hours per technician across the year and the peak backlog in days. Under-forecasting the peak costs more (lost jobs, angry customers) than over-forecasting by a week.
**Scope:** A straightforward forecasting problem once repair orders are classified by job type, which needs a text classifier over free-text repair lines. Exponential smoothing per store is the baseline; a temporal fusion transformer pays only across a group. 1 data scientist, 2–3 months.
**Data availability:** Repair orders and storage contracts sit in the dealer's DMS; weather data is public.
