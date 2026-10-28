# Machine Learning Opportunities — Auto Parts Distributors & Stores

**Industry:** [[auto-parts-distributors|Auto Parts Distributors & Stores]]
**Derived from:** [[problems/auto-parts-distributors/high-impact|High Impact]], [[problems/auto-parts-distributors/low-impact-1|Low Impact 1]], [[problems/auto-parts-distributors/low-impact-2|Low Impact 2]], [[problems/auto-parts-distributors/worker-life-1|Worker Life 1]], [[problems/auto-parts-distributors/worker-life-2|Worker Life 2]]

---

## 1. Learning the Counter Pro's Fitment Resolution
#tacit-knowledge-ml #contrastive-learning #transformers #gradient-boosting #k-nearest-neighbors #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** When the catalog returns several candidate parts for a vehicle, veteran counter professionals pick the one that fits using knowledge they cannot write down: production splits, unreliable qualifiers, a shop's brand habits, known catalog errors. The ML problem is to learn that choice from their resolved lookups and the returns that followed, and to rank the candidates for less experienced staff.

**ML task:** Learning-to-rank over the candidate set returned by the catalog, with a calibrated confidence for routing (auto-accept, suggest, escalate to a senior person)
**Input data:** Decoded vehicle configuration (NHTSA vPIC fields plus any build data the store holds), the shop's stated vehicle and words, catalog candidates with their ACES qualifiers and PIES attributes, supplier and brand, the shop's purchase and return history, store-level return history by application, and optional photos of the old part.
**Target:** The candidate that was sold and kept (not returned for fit within ~30 days), with returned-for-fit candidates as hard negatives and recurring overrides of the catalog's first listing as a separate catalog-error label.
**Evaluation metric:** Top-1 accuracy on multi-candidate lookups and the fitment-return rate of auto-accepted lines, measured strictly forward in time and split by shop, because a random split leaks a shop's repeat orders. Report against agreement between senior counter pros on a double-reviewed sample as the ceiling. Precision matters most at the auto-accept threshold: a confident wrong part costs a second run and the shop's trust, while an honest "ask a senior" costs seconds.
**Scope:** The data collection challenge comes first. The request and the candidate list are not stored today, so the lookup screen, the phone and text channels and the returns desk must be instrumented and joined to invoice lines; a pilot needs ~3–6 months of capture across ~20–50 stores before the hard cases are numerous enough. The labelling challenge is that experts disagree with themselves (the house brand goes out when the premium line is short) and returns are noisy, so return reasons must be captured at the desk and a sample re-reviewed by two or three senior staff. The deployment challenge is speed: the ranking must appear within a second or two of the VIN decode, inside an Epicor, MAM, Autologue or chain point-of-sale screen. Team of 2 ML engineers and 1 data engineer with one chain or programme group, ~6–9 months to a production pilot; ranking on structured fields works within ~2 months, and photo matching comes later.
**Data availability:** Invoice, return and shop data belong to the distributor. Catalog data is licensed (VCdb subscriptions cost $3,150–$12,075 a year; supplier files arrive under trading-partner terms), so a model trained on it stays inside the licensee. The request side mostly doesn't exist historically and must be captured. The chains hold the largest lookup logs and are unlikely to share them.

---

## 2. Shop Order Intake: Call or Text to VIN to the Fitting Part
#large-language-models #transformers #seq2seq #k-nearest-neighbors #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Turn a shop's phone call, text message or e-catalog note ("2014 F-150, 5.0, front pads and rotors, the good ones, and a caliper for the right side") into a structured order: decode the VIN or stated vehicle, match each item to the fitting part, check branch and hub stock, and return a priced quote the counter releases.

**ML task:** Speech or text to structured request (entity extraction of vehicle, job and parts) + VIN decoding + retrieval and matching against the fitment catalog + a calibrated binary classifier per line for safe-to-release
**Input data:** Call transcripts and text messages, VINs or year-make-model-engine, the NHTSA vPIC decode, the catalog's applications, branch and hub inventory, the shop's price matrix and brand preferences, and historical orders paired with what the counter actually sent.
**Target:** Per line, the part number, quantity and brand the counter would release, plus a flag for lines that need a human (ambiguous qualifier, no stock, unclear request).
**Evaluation metric:** Fitment-return rate on released lines, measured against the store's baseline, and the share of lines released without edit at a fixed error ceiling. Quantity and side errors (left versus right, axle sets) are weighted heavily because they send the wrong goods.
**Scope:** A two-week MVP is buildable on public data: a text and transcript parser with an LLM, VIN decoding through NHTSA's free vPIC API, matching against a synthetic ACES/PIES-style catalog of a few hundred applications (the real VCdb and supplier files are licensed and cannot be redistributed), and a priced quote from mock branch stock. The demo should show the hard parts honestly: vPIC returns engine and trim but not the brake package or production split, so the agent must ask the shop one clarifying question when candidates remain. Production needs 2 engineers for ~3–4 months per business system, plus the licensed catalog. The vendor field doing this for distributors generally is profiled at [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]]; what differs here is VIN and fitment matching, voice and text channels, and the hot-shot that follows.
**Data availability:** Orders and invoices are the distributor's own; call recordings exist only where stores record calls; text orders sit in messaging tools. vPIC is public. Catalog data is licensed to the distributor and must stay inside its deployment.

---

## 3. Parc-Driven Assortment From Vehicle Age and Failure Curves
#survival-analysis #gradient-boosting #bayesian-inference #time-series-forecasting #feature-engineering #revenue-impact

**Problem statement:** Forecast each store's demand for each part from the vehicles registered around it, their ages and the failure curves of each part type, rather than from sparse past sales, and recommend which SKUs to stock locally versus rely on the hub.

**ML task:** Hierarchical survival modelling of part failure by vehicle configuration and age + Bayesian pooling across stores for intermittent demand + an assortment optimisation under shelf and inventory constraints
**Input data:** Vehicle-in-operation counts by ZIP and configuration (licensed from S&P Global Mobility or Experian), the catalog's applications mapping parts to configurations, point-of-sale and invoice history by store, lookups that found no stock (lost demand), hub coverage, returns and cores.
**Target:** Expected annual demand per SKU per store, with an uncertainty band, and a stock/hub/skip recommendation.
**Evaluation metric:** Forward first-call fill rate on shop lookups and inventory turns at constant inventory dollars, in a store-level A/B or stepped rollout; pinball loss on demand quantiles for the forecasting layer. Under-stocking a fast-failing part costs more than carrying one slow mover, so the loss is asymmetric.
**Scope:** 2 data scientists and 1 data engineer, ~4–6 months with one chain region or programme group. The hard parts are joining licensed VIO to catalog applications at the configuration level and recovering lost demand from lookup logs that most systems discard. Independents would need this as a service from a programme group or business-system vendor.
**Data availability:** VIO is licensed per use; sales and lookups are the distributor's own if logged; failure curves must be estimated from the pooled data, which favours chains and programme groups.

---

## 4. Catalog Fitment Error Detection Across Supplier Files
#graph-neural-networks #graph-theory #transformers #gradient-boosting #evaluation-metrics #data-integration

**Problem statement:** Find the applications in suppliers' ACES files that are probably wrong (overlapping parts with no qualifier to tell them apart, a vehicle missing from one brand's coverage that every other brand covers, a production split one supplier ignores) before they produce wrong-part returns.

**ML task:** Link prediction and anomaly scoring on the bipartite graph of vehicle configurations and parts (with interchange edges between brands), plus a text model over qualifiers and notes; outputs ranked by expected returns
**Input data:** Suppliers' ACES and PIES files across versions, the VCdb, interchange tables, the distributor's fitment-return history by application, and counter overrides from entry 1.
**Target:** Per application, the probability it is wrong, with the type of error (missing qualifier, wrong range, missing coverage).
**Evaluation metric:** Precision at the top of the ranked list (catalog teams can review only so many flags a week), validated against confirmed supplier corrections and against returns avoided after a fix.
**Scope:** 1–2 ML engineers, ~3–4 months on one distributor's catalog. The graph is large but regular; the label set is small, so returns and overrides do much of the supervision. Useful to distributors, catalog content vendors and suppliers alike.
**Data availability:** Supplier files arrive under trading-partner terms and the VCdb is licensed; the return history is the distributor's. Results are shareable with each supplier about its own lines.

---

## 5. Core and Warranty Credit Matching and Leakage Detection
#gradient-boosting #logistic-regression #k-nearest-neighbors #feature-engineering #automation #revenue-impact

**Problem statement:** Match each returned core and warranty part to the sale it came from and to the supplier credit that should follow, predict which returns a supplier will reject, and flag credits that are overdue or short.

**ML task:** Entity resolution between returns, invoices and supplier credit memos + binary classification of acceptance risk + a rules-and-model check for credit shortfalls
**Input data:** Core tags and return scans, invoice lines with core charges, supplier core-bank rules and acceptance outcomes, credit memos (often lump sums), warranty claim codes and ageing.
**Target:** Unit-level match to a credit, acceptance probability, and an overdue or short-credit flag with the expected amount.
**Evaluation metric:** Dollar recovery rate (credits received over credits owed) and precision of the shortfall flags, since every false flag costs a clerk's call to the supplier.
**Scope:** 1 engineer and 1 analyst, ~2–3 months for a working matcher on one distributor's data; supplier-specific rules are the slow part. A quick win with a measurable return.
**Data availability:** All of it is the distributor's own transaction and credit data; supplier acceptance rules come from vendor programme documents.
