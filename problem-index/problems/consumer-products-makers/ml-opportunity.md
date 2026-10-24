# Machine Learning Opportunities — Consumer Products Makers

**Industry:** [[consumer-products-makers|Consumer Products Makers]]
**Derived from:** [[problems/consumer-products-makers/high-impact|High Impact]], [[problems/consumer-products-makers/low-impact-1|Low Impact 1]], [[problems/consumer-products-makers/low-impact-2|Low Impact 2]], [[problems/consumer-products-makers/worker-life-1|Worker Life 1]], [[problems/consumer-products-makers/worker-life-2|Worker Life 2]]

---

## 1. Reading the Burn Test and Choosing the Wick
#tacit-knowledge-ml #cnns #semantic-segmentation #gradient-boosting #bayesian-optimization #gaussian-processes #evaluation-metrics #compliance

**Problem statement:** An experienced chandler watches a test candle burn and judges whether the melt pool, flame and glass behaviour will pass, then picks the next wick to try from a feel for how this wax, fragrance and vessel behave. The ML problem is to measure the burn from video the way the chandler reads it, and to recommend the first wicks to test for a new recipe from the maker's own history.

**ML task:** (a) Per-frame semantic segmentation of flame, melt pool and soot deposits in burn-test video, producing time series of flame height, flicker, melt-pool diameter as a share of the vessel and time to full pool; (b) a pass/fail and quality model per recipe-wick pair; (c) a sequential recommender that proposes the next wick to test to minimise test rounds.
**Input data:** Fixed-camera video of each test candle at set intervals; glass temperature from a thermocouple or infrared sensor; weight loss per burn cycle; recipe record (wax blend and lot, fragrance supplier, code, flash point and load, dye, vessel diameter and glass type, wick series and size, pour and cure dates); the chandler's notes and final pass decision; later retailer complaints and returns by item where they can be matched.
**Target:** Segmentation masks; continuous burn metrics; the chandler's pass, fail or "go up a size / down a size" call; ASTM F2417 flame-height and end-of-life outcomes from third-party test reports.
**Evaluation metric:** For segmentation, intersection-over-union against chandler-annotated frames and agreement of derived flame height with ruler measurements. For the recommender, the number of test rounds to a passing wick against the chandler's own historical rounds on held-out scents; a model that only matches the chandler's first guess saves nothing. Recall on unsafe pairings (flame above the specification limit, glass overheating) matters more than precision: a missed high flame is a recall, a false alarm is one more test candle.
**Scope:** The data collection challenge is the core of the project: every test burn must be filmed under controlled light and draught and tied to a structured recipe record, which most makers keep as spreadsheets with free-text fragrance names, and fragrance oils are proprietary mixtures known only by supplier code and a few properties. The labelling challenge is that chandlers disagree with themselves (the same melt pool is "full" one day and "shallow" the next), so a sample of burns needs repeat annotation to measure intra-rater agreement, and the hard outcome labels (incidents in homes) are rare and arrive months later. The deployment challenge is that the recommendation must beat the chandler's first guess on a bench laptop in a small plant, and the chandler signs off. 1 computer-vision engineer and 1 ML engineer working with a maker's lab for 6–9 months (estimate), starting with automated burn measurement, which is useful on its own, before any recommender.
**Data availability:** Held only by makers, in notebooks and spreadsheets; video does not exist until someone starts filming. A large maker or a wick supplier (whose application labs run thousands of test burns for customers) is the natural first data holder.

---

## 2. Deduction Validity and Recoverability
#gradient-boosting #large-language-models #bert #feature-engineering #survival-analysis #evaluation-metrics #revenue-impact #tacit-knowledge-ml

**Problem statement:** A seasoned deductions analyst glances at a retailer deduction and knows whether it is worth disputing: this retailer's shortage claims on this lane are usually carrier-caused, that defective allowance was agreed, that fine was charged on a load the retailer's own carrier collected late. Predict, for every deduction, whether it is invalid, what evidence would win it and how much will be recovered before the retailer's dispute window closes.

**ML task:** Document understanding and classification of remittances and portal claim records into a normalised reason taxonomy; binary classification of validity; regression of expected recovery; time-to-resolution modelling for prioritisation.
**Input data:** Remittance advices and EDI payment documents; retailer portal claim detail; invoices, bills of lading, proof-of-delivery scans, advance ship notices; promotion agreements and buyer emails; carrier and 3PL records; historical dispute outcomes by retailer, code and analyst.
**Target:** Valid or invalid; recovered amount; days to resolution; the evidence set that won.
**Evaluation metric:** Recovered dollars per analyst hour against the current queue, measured on out-of-time deductions. Precision on "dispute" matters more than recall, because retailers penalise or ignore suppliers who file weak disputes, but the cost of a missed invalid deduction below the write-off threshold is exactly the money the model is meant to find.
**Scope:** Extraction is commodity with current language models; the value is the per-retailer outcome history that teaches which disputes win. 1–2 ML engineers and an integration engineer, 4–6 months to a first model for two or three retailers (estimate). Funded vendors already sell versions of this (see the agents note).
**Data availability:** Each maker holds its own outcomes; vendors hold them across clients under service agreements, which limits pooled training to what their contracts allow.

---

## 3. Seasonal and New-Item Demand From Retailer POS
#time-series-forecasting #temporal-fusion-transformers #exponential-smoothing #k-nearest-neighbors #feature-engineering #evaluation-metrics #worker-facing

**Problem statement:** Forecast weekly store and distribution-centre demand for seasonal programmes and new items (a holiday scent, a back-to-school marker set) from retailer point-of-sale and inventory data, early enough to set the plant's build and the last re-order.

**ML task:** Hierarchical probabilistic forecasting (SKU by retailer by store or DC by week) with cold-start forecasts for new items from attribute similarity to past launches, and in-season updating from the first weeks of sell-through.
**Input data:** Retailer POS, store and DC inventory and open orders from each portal; item attributes (scent family, colour, price point, vessel, pack count); programme commitments and planogram counts; promotion calendars; prior seasons' sell-through and markdowns.
**Target:** Weekly unit sales with prediction intervals; end-of-season sell-through; probability of stock-out by store.
**Evaluation metric:** Weighted absolute percentage error at the level the plant plans, plus pinball loss on the intervals; for seasonal items, end-of-season unsold units and lost sales against the planner's own forecast. Over-forecast costs markdowns and returns; under-forecast loses the season, so report both.
**Scope:** The data plumbing (portal connectors, item mapping, calendar alignment) is most of the work; the models are known. 1 data engineer and 1 data scientist, 3–5 months (estimate).
**Data availability:** Suppliers can export their own POS from retailer portals under each retailer's terms; vendors such as Alloy.ai and Crisp already harmonise it.

---

## 4. Finish and Assembly Defect Detection
#cnns #autoencoders #object-detection #transfer-learning #evaluation-metrics #automation #quick-win

**Problem statement:** Detect visual defects at the end of the line (casket finish runs, orange peel and scratches; brush heads with uneven trim or loose filaments; off-centre wicks and surface pitting in candles; pen and marker assembly faults) where inspectors judge by eye.

**ML task:** Unsupervised anomaly detection on images of good product, with object detection for known defect classes once enough examples are labelled.
**Input data:** Line-camera images under fixed lighting; inspector accept and reject decisions; rework and return records.
**Target:** Defect present, defect type and location.
**Evaluation metric:** Recall on defects that reach the customer, measured against inspector re-checks; false-reject rate as the cost side, because a false reject stops a line.
**Scope:** Well-trodden technique; the work is lighting, cameras and per-product tuning. 1 engineer, 2–3 months per line (estimate).
**Data availability:** Created by installing cameras; defect labels come from inspectors, who need a fast way to tag.

---

## 5. Compliance Mapping From Formulas and Documents
#large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #compliance #automation #data-integration

**Problem statement:** For each SKU, extract ingredients and components from formulas, safety data sheets, IFRA certificates and supplier declarations, map them to the rules that apply (CPSC certificates, Prop 65 listed chemicals, art-material labelling, retailer chemical registrations) and draft the certificate, warning and label text.

**ML task:** Information extraction and entity resolution of chemical names and CAS numbers against regulatory lists; rule matching; generation of certificate fields and label text with citations.
**Input data:** SDS and IFRA PDFs, supplier declarations, bills of materials, test reports, the Prop 65 list, CPSC rule texts, retailer manuals.
**Target:** Rule applicability per SKU; drafted General Certificate of Conformity fields and eFiling data elements; warning decisions.
**Evaluation metric:** Recall on rules that apply (a missed certificate or warning is a held shipment or a Prop 65 notice), audited by the compliance coordinator on a stratified sample.
**Scope:** 1 ML engineer plus a regulatory specialist, 3–4 months for a single product family (estimate); rule content can be licensed from regulatory-intelligence vendors.
**Data availability:** Formulas and declarations are the maker's own; supplier formula detail is often withheld, so the model must work from declared ranges.
