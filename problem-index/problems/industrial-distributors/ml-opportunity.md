# Machine Learning Opportunities — Industrial Distributors

**Industry:** [[industrial-distributors|Industrial Distributors]]
**Derived from:** [[problems/industrial-distributors/high-impact|High Impact]], [[problems/industrial-distributors/low-impact-1|Low Impact 1]], [[problems/industrial-distributors/low-impact-2|Low Impact 2]], [[problems/industrial-distributors/worker-life-1|Worker Life 1]], [[problems/industrial-distributors/worker-life-2|Worker Life 2]]

---

## 1. Learning the Veteran's Part Identification
#tacit-knowledge-ml #contrastive-learning #transformers #cnns #k-nearest-neighbors #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Veteran inside reps and counter staff turn messy requests — free text, a customer stock code, a superseded part number, a photo of a worn bearing or nameplate, a pair of caliper readings — into the one catalogue item or accepted interchange that fits, using knowledge they cannot write down. The ML problem is to learn that mapping from their resolved history and surface a ranked, explained shortlist to less experienced staff.

**ML task:** Multimodal retrieval and learning-to-rank over the distributor's catalogue and interchange graph, plus a calibrated confidence for routing (auto-accept, suggest, escalate)
**Input data:** Inbound request text from emails, POs and phone notes; customer stock codes and purchase history; photos of parts, markings and nameplates; measured dimensions entered at the counter; the catalogue with attributes; manufacturer cross-reference tables; ERP order lines and returns.
**Target:** The SKU finally sold and kept (not returned for fit), with accepted interchanges as positive pairs and returned or rejected candidates as hard negatives; a per-customer preference signal (brand, seal, clearance class).
**Evaluation metric:** Top-1 and top-5 accuracy on held-out resolutions, measured strictly forward in time and by customer, because random splits leak a customer's repeat orders. Report against expert agreement on a double-reviewed sample as the ceiling. Calibration matters most: on breakdown calls a confident wrong answer costs far more than an honest "escalate", so the routing threshold is set for very high precision on auto-accepted lines.
**Scope:** The data collection challenge comes first: the request must be captured as it arrived and linked to the order line it produced, which means instrumenting the inbox, counter and phone, because the ERP keeps only the sale. The labelling challenge is that experts disagree with themselves — a substitute accepted when stock is short is refused when it isn't — so a sample needs repeated review to estimate agreement, and returns must be split by reason. The deployment challenge is speed: the shortlist has to appear faster than walking to the veteran, seconds for text and under a minute for a photo. 2 ML engineers and 1 data engineer with one mid-size distributor, ~6–9 months, with retrieval over text and part numbers useful within ~2 months and photo identification later.
**Data availability:** Catalogue, order and return data are the distributor's own. The request side mostly doesn't exist historically and must be captured from email archives and new instrumentation. Manufacturer interchange data is partial and licence-restricted; part photos must be collected at the counter.

---

## 2. RFQ and Purchase Order Line Matching for No-Touch Entry
#large-language-models #transformers #k-nearest-neighbors #logistic-regression #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Extract header and line items from inbound RFQs and POs in any format, match each line to the distributor's SKU and the customer's contract price, and decide which drafts can go into the ERP without a human touching them.

**ML task:** Document extraction (layout-aware) + entity resolution of line text to SKUs + calibrated binary classification of each line as safe-to-auto-enter
**Input data:** Email bodies and attachments (PDF, spreadsheet, scanned images); customer master and ship-tos; customer part-number cross-references; contract and SPA price files; historical POs paired with the orders reps actually entered.
**Target:** Structured header fields (customer, PO number, ship-to, dates) and per-line SKU, quantity, unit of measure and price; a no-touch flag per line.
**Evaluation metric:** No-touch rate at a fixed error ceiling — the share of lines entered without edits while keeping post-entry error under an agreed level (e.g. ~0.5%, estimate). Unit-of-measure and quantity errors are weighted heavily because they ship the wrong goods. Measure on each distributor's own inbox, since vendor demo sets flatter the result.
**Scope:** Extraction is close to solved by current LLMs; matching to SKUs with customer-specific codes is the hard part and overlaps with entry 1. 2 engineers, ~3–4 months to a production pilot on one ERP; each new ERP integration adds weeks. This is the workflow the AI quoting and order-entry vendors are racing to own.
**Data availability:** Every distributor has years of PO emails and the orders keyed from them; aligning the two is mechanical but tedious. No public dataset exists; synthetic POs over public manufacturer catalogues work for demos.

---

## 3. Bearing Damage Classification and Root Cause From Photos
#cnns #transfer-learning #semantic-segmentation #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Classify failed bearings by the ISO 15243 damage families (rolling contact fatigue, wear, corrosion, electrical erosion, plastic deformation, fracture and cracking) and likely root cause (lubrication, contamination, misalignment, overload, mounting, stray current) from photos taken at the counter or in the plant, so the distributor can recommend the fix, not just the replacement.

**ML task:** Multi-label image classification with damage-region segmentation, plus a root-cause classifier using image output and application data
**Input data:** Photos of raceways, rolling elements and cages; bearing type and application (motor, pump, gearbox, fan); operating notes; failure-analysis reports from manufacturer and distributor application engineers.
**Target:** ISO 15243 damage mode labels (several can co-occur), segmentation masks of damage areas, and a root-cause category.
**Evaluation metric:** Per-class recall and macro-F1 on damage modes, and top-2 accuracy on root cause, against a panel of application engineers. Electrical erosion and contamination deserve high recall because both repeat until the cause is fixed.
**Scope:** 1–2 ML engineers working with a distributor's or manufacturer's application engineering group, ~6 months. The standard notes several mechanisms often act at once, so labels are multi-label and expert agreement is modest; collecting a few thousand labelled failures is the main cost.
**Data availability:** Manufacturers publish failure-analysis guides with example images; real labelled sets sit in manufacturer and distributor failure-analysis files and must be gathered and consented.

---

## 4. SPA Claim Leakage and Denial Prediction
#gradient-boosting #logistic-regression #large-language-models #feature-engineering #compliance #revenue-impact

**Problem statement:** Find sale lines that qualified for a special pricing agreement or rebate but were never claimed, and predict which submitted claims will be denied and why, before the claim window closes.

**ML task:** Record linkage of sale lines to agreement terms + binary classification of denial risk with reason codes
**Input data:** SPA documents and rebate programme terms (extracted from PDFs); ERP invoice lines with cost, sell price, ship-to and dates; part-number aliases and interchanges; historical claims with manufacturer responses and denial codes.
**Target:** Per line: eligible-but-unclaimed (yes/no) and expected recovery; per claim: probability of denial and the likely denial reason.
**Evaluation metric:** Recovered dollars per review hour, and precision at the top of the unclaimed list, because analysts work it from the top. For denial prediction, AUC plus calibration, tracked by manufacturer since rules differ.
**Scope:** 1 data scientist and 1 engineer, ~3 months. The extraction of agreement terms is the slow part; the model is modest once terms and lines are joined.
**Data availability:** Fully internal to the distributor. Denial histories are often in email and portal downloads and need consolidating.

---

## 5. Slot-Level Demand Forecasting for Vending and VMI
#time-series-forecasting #exponential-smoothing #gradient-boosting #bayesian-inference #feature-engineering #automation

**Problem statement:** Forecast dispense and usage at the level of a single bin or vending slot inside a customer's plant, and set reorder points and visit schedules from that forecast and from the cost of a stockout at that slot.

**ML task:** Intermittent-demand forecasting across many short, sparse series, with hierarchical pooling across customers, items and slots, followed by inventory-policy optimisation
**Input data:** Vending dispense logs by employee, job and time; bin scans or weight sensor readings; customer shift calendars and production schedules where shared; item attributes; consignment cost.
**Target:** Distribution of demand per slot per replenishment interval; recommended min/max and visit date.
**Evaluation metric:** Stockout rate and average consigned inventory at equal service level, plus visits per programme. Forecast error alone misleads on intermittent series, so evaluate with a simulated replenishment backtest.
**Scope:** 1–2 data scientists, ~4 months for a pilot on a few programmes. The modelling is well understood; the work is cleaning dispense data and agreeing stockout costs with account managers.
**Data availability:** Dispense data is logged by the vending platform, but it describes the customer's consumption, so programme agreements must permit its use beyond billing.
