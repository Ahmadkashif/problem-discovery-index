# Machine Learning Opportunities — Clinical Laboratories

**Industry:** [[clinical-laboratories|Clinical Laboratories]]
**Derived from:** [[problems/clinical-laboratories/high-impact|High Impact]], [[problems/clinical-laboratories/low-impact-1|Low Impact 1]], [[problems/clinical-laboratories/low-impact-2|Low Impact 2]], [[problems/clinical-laboratories/worker-life-1|Worker Life 1]], [[problems/clinical-laboratories/worker-life-2|Worker Life 2]]

---

## 1. Learning the Technologist's Read of a Held Result
#tacit-knowledge-ml #gradient-boosting #feature-engineering #transfer-learning #evaluation-metrics #conditional-probability-and-bayes-theorem #worker-facing

**Problem statement:** Senior medical laboratory scientists recognise spurious results — IV-fluid contamination, EDTA carry-over, delayed separation, haemolysis interference, wrong blood in tube — from the pattern across a panel and the patient's history, a read they cannot fully specify. Learn that read from held results, the technologist's action and what later settled the truth, and score every held result before it is released or phoned.

**ML task:** Multi-label classification of specimen-integrity failure type with calibrated probabilities, plus per-fluid regression of contamination fraction; site adaptation of a pooled model with a small local label set
**Input data:** Held and auto-released results with full panels, prior results and time since prior, draw time, location and collector, tube types, order sequence, instrument flags and serum indices (haemolysis, icterus, lipaemia), medication administration records for IV fluids, and the technologist's action and comment; simulated admixtures of common fluids into real results for rare classes.
**Target:** Per held result, the probability of each failure type and of "real"; ground truth from recollection results, corrected reports, transfusion and medication records and expert adjudication on a sample.
**Evaluation metric:** Sensitivity at the lab's current flag rate, so the model is judged on catching more without holding more, and Matthews correlation coefficient because spurious results are rare. Report site-by-site: the best published pipeline kept sensitivity at a second hospital but its MCC fell from 0.747 to 0.387 as false flags rose (Clin Chem 2025). Missing a contaminated critical value costs a patient treatment; a false flag costs a technologist about 30 seconds, so recall on critical-range results outweighs precision.
**Scope:** The data collection challenge comes first: capturing each held result with its context and the technologist's decision at the bench, and joining it afterwards to the recollection or corrected report, which today live in different systems. The labelling challenge is that contamination is a matter of degree and technologists disagree with themselves at different hours. Labels need repeated review on a sample to measure intra-rater agreement, and simulated admixtures to cover rare fluids. The deployment challenge is speed and trust: the score must appear in the middleware before the technologist finishes reading, carry a plain explanation of the analytes that drove it, and start as a ranked queue rather than an auto-release. 2 ML engineers, 1 clinical chemist and an LIS analyst, 6–9 months per site, with a held-result ledger delivered first.
**Data availability:** Every hospital and reference lab holds years of results and comments in its LIS; the joins to recollections and medication records need interface work and a data-use agreement. Labels exist only as free text and must be built. Published methods and simulation approaches are open.

---

## 2. Slide Triage and Second Read for Anatomic Pathology
#transformers #cnns #contrastive-learning #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Pathologists read every biopsy in arrival order, though a minority carry malignancy or need immunostains. Rank digitised cases by likelihood of a significant finding, pre-order likely stains, and give a second read that flags missed foci before sign-out.

**ML task:** Weakly supervised multiple-instance classification of whole-slide images on a pathology foundation model, with tile-level localisation and calibrated case-level probabilities
**Input data:** Whole-slide H&E images, specimen type and clinical history from the requisition, prior diagnoses, ordered and resulted immunostains, final signed diagnoses and amendments.
**Target:** Case-level categories (benign, atypical, malignant, needs stains) and tile heatmaps; secondary targets of stains the pathologist eventually ordered and of section-quality defects (folds, chatter, incomplete sections) that the histology bench can recut overnight before the case is read.
**Evaluation metric:** Sensitivity for malignancy at the operating point that keeps the "low priority" bucket clean (negative predictive value close to 1), plus time from accession to sign-out for cases ranked high. Missed malignancy is the dominant cost; over-ranking only reorders the queue. Evaluate on another lab's scanner and stain to expose site shift.
**Scope:** Foundation models and FDA-authorised products now exist for prostate and breast. The work is extending to the lab's case mix, integrating with the AP LIS and image management system, and validating under CLIA as the lab's own procedure. 2–3 ML engineers and a pathologist lead, 9–12 months per organ system, after the lab has digitised.
**Data availability:** Only labs that scan routinely have the images; most still read glass. Final diagnoses are in the AP LIS. Labelling at case level is free from sign-out; tile-level labels need pathologist time.

---

## 3. Denial and Missing-Information Prediction at Accessioning
#large-language-models #gradient-boosting #logistic-regression #feature-engineering #revenue-impact #automation

**Problem statement:** Lab claims fail on information supplied by ordering offices — diagnosis codes outside a test's covered list, missing insurance, missing Z-codes, bundling rules. Predict each requisition's denial risk and collectable value while the specimen is still in the lab, and extract the fields from scanned requisitions.

**ML task:** Document field extraction from requisitions (vision-language model) plus binary denial classification and expected-payment regression per test line
**Input data:** Requisition images and electronic orders, accessioned data, payer and plan, test codes, diagnosis codes, ordering provider and office history, NCD and LCD covered-code lists, historical claims, remittances and denial reason codes.
**Target:** Field values; probability of denial by reason group; expected payment per line.
**Evaluation metric:** Precision in the top decile of flagged requisitions, because client services can only call so many offices a day, and dollars recovered per call. Field extraction is measured by exact-match accuracy on diagnosis codes, where an error changes coverage.
**Scope:** 2 engineers and a billing analyst, 4–6 months. Labels come from history: every denied and paid line is a label. The hard part is getting the prediction into the accessioning workflow before the specimen is run.
**Data availability:** The lab's own claims, remits and requisition images; NCD and LCD lists are public.

---

## 4. Expected Payment and Underpayment Detection Against the Fee Schedule
#bayesian-inference #change-point-detection #hypothesis-testing #descriptive-statistics #revenue-impact #quick-win

**Problem statement:** Commercial and Medicare Advantage lab contracts are priced as percentages of the Medicare CLFS, which resets from 1 January 2027 with cuts capped at 15% a year. Detect, per payer and code, when payments depart from what the contract and the current schedule imply, and separate systematic short-pays from noise.

**ML task:** Rules-based expected-payment computation, plus hierarchical Bayesian estimation of payer-by-code payment ratios and change-point detection after each quarterly fee schedule update
**Input data:** Public CLFS files by quarter, the lab's contracts as structured terms, 835 remittances and 837 claims, adjustment reason codes.
**Target:** Expected payment per line; posterior probability that a payer-code pair is systematically underpaid; estimated recoverable dollars.
**Evaluation metric:** Recovered dollars per appeal filed and the false-positive rate of payer-level findings confirmed by payers. A false finding costs credibility with the payer; a missed one costs money every day it continues.
**Scope:** 1–2 engineers and a reimbursement analyst, 3 months to a working tool; a demo runs in two weeks on public CLFS files and synthetic remits. Contract term capture is the slow step.
**Data availability:** The CLFS is public; remits and contracts are the lab's own.

---

## 5. Specimen Pickup Forecasting and Stability-Window Routing
#time-series-forecasting #exponential-smoothing #optimization-fundamentals #monte-carlo-methods #automation

**Problem statement:** Couriers run fixed routes to practices and lockboxes while specimens age toward stability limits. Forecast pickup volume and readiness by stop and hour, and route to minimise specimens arriving outside their windows.

**ML task:** Hierarchical time-series forecasting of specimens per stop and time slot, plus vehicle routing with time windows and stochastic travel times
**Input data:** Historical pickups by stop and time, test mix, practice schedules, lockbox scans, GPS traces, traffic, specimen rejection records with reasons.
**Target:** Specimen count and earliest-ready time per stop; route plans; probability each specimen arrives within its window.
**Evaluation metric:** Specimens rejected or recollected for stability per thousand picked up, and route miles per specimen. Rejection matters more than mileage.
**Scope:** 2 engineers, 4–6 months. Mostly operations research once pickups are scanned at the stop.
**Data availability:** Large labs log pickups and GPS; many small labs log nothing beyond the driver's sheet.
