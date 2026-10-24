# Machine Learning Opportunities — Pharmaceutical Manufacturers

**Industry:** [[pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Derived from:** [[problems/pharmaceutical-manufacturers/high-impact|High Impact]], [[problems/pharmaceutical-manufacturers/low-impact-1|Low Impact 1]], [[problems/pharmaceutical-manufacturers/low-impact-2|Low Impact 2]], [[problems/pharmaceutical-manufacturers/worker-life-1|Worker Life 1]], [[problems/pharmaceutical-manufacturers/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Senior Investigator's Root-Cause Read
#tacit-knowledge-ml #transformers #large-language-models #gradient-boosting #survival-analysis #evaluation-metrics #compliance

**Problem statement:** Senior QA investigators read a new deviation and recognise it as a recurrence, a procedure-design problem dressed as human error, or a material issue, a judgement built over hundreds of investigations that is recorded only as a conclusion. The ML problem is to learn that read from historical deviations, the related cases investigators cited, and whether each root cause held, and to surface it for the next investigator.

**ML task:** Retrieval of related historical deviations, plus multi-class ranking of candidate root-cause categories with a calibrated probability that the stated cause will hold (no recurrence of the same failure mode within 12 months)
**Input data:** QMS deviation and CAPA records (description, product, equipment, step, lot, investigator, root-cause category, narrative, linked deviations); batch record exceptions and alarms; equipment maintenance and calibration logs; material lot genealogy; later deviations on the same equipment, product and step
**Target:** Root-cause category as finally assigned; related-deviation links; recurrence of the same failure mode, as survival time to recurrence with censoring for products not run again
**Evaluation metric:** Recall@10 for related-deviation retrieval, judged against links senior investigators make on a held-out sample. For the root-cause ranking, agreement with senior investigators measured against their own test–retest agreement on re-read cases, which sets the ceiling. For durability, concordance of predicted against actual time to recurrence, evaluated strictly forward in time. Missing a recurrence costs a repeat 483 observation; a false "possible recurrence" costs the investigator a few minutes, so recall matters more than precision.
**Scope:** The data collection challenge is first: the expert's reasoning has to be captured while they investigate, so the tool must log what they search, open and cite without adding steps, and historical narratives must be normalised (equipment named three ways, root-cause taxonomies changed at each QMS migration). The labelling challenge is that recurrence is a late, noisy label (it depends on whether the product ran again and whether the next failure was recognised as the same), and investigators disagree with themselves, so a sample of deviations needs blind re-reading to estimate intra-rater reliability. The deployment challenge is speed and validation: suggestions must appear as the deviation is opened, faster than the investigator's recall and the QMS keyword search, inside a validated system whose outputs become part of the GMP record. 2 ML engineers, 1 data engineer and a senior QA lead seconded part-time, 6–9 months for one site, starting with retrieval before any ranking is shown.
**Data availability:** Each plant holds roughly 5–15 years of deviations in its QMS (estimate) (TrackWise, Veeva, MasterControl); exports are feasible but messy. Recurrence labels must be derived. FDA's public warning letters and 483 observations (2,837 drug citations in FY2025) give an external label for what the agency calls an inadequate investigation.

---

## 2. Granulation and Compression End-Point From Process Signals
#tacit-knowledge-ml #gaussian-processes #time-series-forecasting #feature-engineering #transfer-learning #automation

**Problem statement:** Experienced operators and process engineers judge the end-point of a wet granulation by the feel of the mass, the sound of the impeller and the power-draw curve, and adjust a tablet press by the look and sound of the tablets. Predict granule and tablet quality (particle size, hardness, dissolution) from in-process signals so the end-point and press settings stop depending on who is on shift.

**ML task:** Multivariate time-series regression with uncertainty: predict end-of-process critical quality attributes from impeller power, torque, temperature, spray rate and NIR spectra; recommend the stop point and press adjustments
**Input data:** High-frequency process historian data from granulators, fluid-bed dryers and tablet presses; in-line NIR where installed; batch-level release and in-process results; operator end-point decisions and notes
**Target:** Granule particle size distribution and moisture at end of granulation; tablet hardness, weight variation and dissolution
**Evaluation metric:** Prediction error on dissolution and hardness against release results, with calibrated prediction intervals so the operator knows when to trust the call. Out-of-spec misses are costly (a rejected or reworked batch), so the model is judged on recall of batches heading out of range at a fixed false-alarm rate.
**Scope:** Gaussian process or partial-least-squares baselines, then sequence models where data allow. Transfer across products and equipment trains is the hard part: each product has few batches a year. Any use in release decisions moves into FDA's process analytical technology and real-time release framework, which needs validation and regulatory filing, so first use is advisory. 1–2 process data scientists with an MSAT engineer, 4–6 months per product family.
**Data availability:** Historians hold years of signals at most large plants, less at small ones. Operator end-point decisions are rarely recorded and must be captured going forward.

---

## 3. Batch Record Exception Detection
#cnns #transfer-learning #autoencoders #feature-engineering #compliance #automation

**Problem statement:** Flag the entries in an executed batch record, paper or electronic, that a QA reviewer must look at, so review proceeds by exception instead of page by page.

**ML task:** Handwriting and form recognition on scanned paper records; per-entry anomaly scoring against the product's historical distribution; rule checks for missing signatures, out-of-sequence times and calculation errors
**Input data:** Scanned executed batch records and master batch records; eBR entry logs; historical QA review comments and corrections; deviation links
**Target:** Entries QA corrected or questioned in historical reviews; missing or illegible entries; out-of-trend values within specification
**Evaluation metric:** Recall of entries that historical QA review flagged, at the share of entries left for human review. A missed GMP error that reaches release is the costly failure, so recall is fixed near 100% on critical entries and the share of pages reviewed is what improves.
**Scope:** Handwriting recognition on gloved, cleanroom-written forms needs fine-tuning on the plant's own records. Product-specific limits come from history. 2 ML engineers and a QA reviewer, 4–6 months, with validation of the review-by-exception procedure as the long pole.
**Data availability:** Plants hold archives of executed records (paper scans or eBR). QA corrections are on the pages or in review logs, so labels exist but need extraction.

---

## 4. Form 483 Observation Classification and CAPA Drafting From the Public Corpus
#bert #large-language-models #k-nearest-neighbors #word-embeddings #evaluation-metrics #compliance #quick-win

**Problem statement:** Given an inspectional observation or an internal audit finding, retrieve how FDA has described the same deficiency in warning letters, what it called inadequate in firms' responses, and draft a CAPA plan and response section that meets the March 2026 draft guidance on 483 responses (root cause, systemic scope, dated actions, effectiveness checks).

**ML task:** Multi-label classification of observations to CFR sections and quality systems; nearest-neighbour retrieval over warning letter passages; retrieval-grounded generation of a response and CAPA draft
**Input data:** FDA warning letters (public), the yearly inspection observation spreadsheets (713 system-generated drug 483s and 2,837 citations in FY2025), FDA Data Dashboard citations and compliance actions, released 483s, the firm's own deviations and CAPAs
**Target:** CFR section and quality system per observation; the warning-letter passages FDA later wrote about comparable responses; a draft response
**Evaluation metric:** Retrieval precision@5 judged by QA reviewers; for drafts, reviewer edit distance and a checklist score against the draft guidance's required elements. The outcome label that matters (did FDA judge the response adequate, or escalate to a warning letter) is public only for escalated cases, so the model learns more about failure than success.
**Scope:** Buildable in two to four weeks from public data as a demonstration. Value in production needs the firm's own CAPA history and validation if drafts enter the QMS. 1–2 engineers.
**Data availability:** Warning letters, observation spreadsheets and the Data Dashboard are public (the Dashboard API needs a key). Firms' 483 responses are mostly unpublished. Redica holds a FOIA-assembled archive of 483s, EIRs and responses.

---

## 5. Generic Product Shortage and Discontinuation Risk
#survival-analysis #gradient-boosting #feature-engineering #confidence-intervals #data-integration #revenue-impact

**Problem statement:** Estimate, for each generic product in a portfolio or on a buyer's contract, the probability of a supply interruption or discontinuation in the next 12 months, from public market structure and the manufacturer's own supply data.

**ML task:** Time-to-event modelling of shortages and discontinuations at product and NDC level
**Input data:** FDA and ASHP shortage records; number of approved and marketing ANDA holders per molecule; API supplier counts from DMF lists; FDA inspection classifications, import alerts and warning letters by site; price erosion series; drug amount reporting where available; the firm's own capacity, inventory and supplier quality records
**Target:** Onset of shortage or discontinuation within 12 months
**Evaluation metric:** Time-dependent concordance and calibration of 12-month risk, with precision among the top-decile flagged products as the operational number. The base rate is low, so precision at the top matters more than overall AUC.
**Scope:** Public-data version in 2–3 months by 1–2 data scientists; manufacturer-side value depends on joining internal supply data. Causes are partly unknowable (59% of 2025 shortages had no stated cause), which caps accuracy.
**Data availability:** Shortage, approval, DMF and inspection data are public. Prices and volumes need licensed data. Manufacturer data is internal.
