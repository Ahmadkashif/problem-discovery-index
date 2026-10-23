# Machine Learning Opportunities — Aerospace Parts Suppliers

**Industry:** [[aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Derived from:** [[problems/aerospace-parts-suppliers/high-impact|High Impact]], [[problems/aerospace-parts-suppliers/low-impact-1|Low Impact 1]], [[problems/aerospace-parts-suppliers/low-impact-2|Low Impact 2]], [[problems/aerospace-parts-suppliers/worker-life-1|Worker Life 1]], [[problems/aerospace-parts-suppliers/worker-life-2|Worker Life 2]]

---

## 1. Second Reader for Penetrant and Radiographic Indications
#tacit-knowledge-ml #cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #worker-facing #compliance

**Problem statement:** Level II inspectors decide whether an FPI indication or a radiographic density change on a rotating part or structural casting is a relevant defect, using pattern recognition built over years that they cannot specify. The ML problem is to learn that judgement, per part family, from captured images and the inspectors' own dispositions, and run it as a second reader that flags missed indications and calls that differ from the site's history.

**ML task:** Object detection and instance segmentation of indications on UV-A FPI images and digital radiographs, followed by calibrated classification (relevant/non-relevant, defect type, accept/reject against the customer's criteria)
**Input data:** UV-A-calibrated images captured in the booth at the moment of disposition; digital radiographs with reader annotations; part number, feature location, serial, heat lot and operation; penetrant line parameters (dwell, wash, developer); reference radiograph severity levels; downstream outcomes (sectioning, CT, findings at later operations, customer returns).
**Target:** Indication masks with type and severity; part-level accept/reject/re-process; a "hard call" flag for Level III review.
**Evaluation metric:** Recall on relevant indications at the inspector-confirmed level is the binding metric: a missed crack is a safety escape, while a false flag costs a few seconds of second look. Report probability-of-detection curves by indication length against the hard-truth subset, and false-flag rate per part as the adoption metric. Measure agreement with held-out dispositions against inspectors' own repeat-read agreement, which is the ceiling.
**Scope:** The data collection challenge comes first: nobody photographs FPI indications today, so the project starts by fitting booths with calibrated cameras and a one-tap marking step that does not slow a Nadcap-audited process. The labelling challenge is that inspectors disagree with each other and with themselves, and hard truth is rare. Plan repeat reads on a sample to estimate intra- and inter-rater reliability, weight hard-truth cases heavily, and avoid training a model that simply learns the average inspector's mistakes. The deployment challenge is that the certified inspector remains the decision-maker and any method change needs customer acceptance, so the model ships as an assistive second reader at booth speed, never as an autonomous disposition. 2 ML engineers, 1 imaging engineer and a Level III NDT lead at one plant, 9–12 months to a credible second reader on two or three part families.
**Data availability:** Owned by each supplier, and it does not exist yet for FPI. Radiographs exist in digital systems at larger plants, but dispositions are part-level. Defence-part images are ITAR-controlled and must stay on premises or in a US-person-only enclave. Public NDT image sets are small and not aerospace-specific, so transfer learning helps only at the start.

---

## 2. Requirement Extraction From Drawings and Models for First Articles
#object-detection #cnns #transformers #large-language-models #feature-engineering #evaluation-metrics #automation

**Problem statement:** Given a drawing (vector PDF, scanned raster, or a model-based definition), extract every requirement that must appear on AS9102 Form 3 (dimensions with tolerances, GD&T frames, surface finishes, thread and hole callouts, and requirements stated in general and flag notes), place balloons, and structure each as a characteristic with nominal, limits and inspection method.

**ML task:** Layout detection of annotation regions, OCR of dimension text and feature control frames, parsing into a structured schema, and LLM extraction of requirements from note text, with confidence per characteristic
**Input data:** Drawing sheets with revision blocks; MBD files with PMI (STEP AP242 where available); the shop's past ballooned drawings and accepted FAI reports as supervision; customer supplier-quality requirement documents.
**Target:** A ballooned drawing and a Form 3 characteristic list; flags for low-confidence or ambiguous items; a Form 2 skeleton of materials and special processes called out in notes.
**Evaluation metric:** Characteristic recall against the accepted FAI report is the headline: a missed characteristic gets the report rejected, while an extra balloon costs a minute of review. Track precision, time to a complete balloon set, and first-time acceptance by the customer's quality representative. Report scanned legacy drawings and MBD separately; they behave differently.
**Scope:** Vector drawings are near solved; scans with hand revisions and note-heavy drawings are the hard tail. MBD needs a different front end entirely. 2 engineers, 4–6 months to beat manual ballooning on the shop's own part mix; this is a credible two-week demo on public sample drawings and the AS9102 form template.
**Data availability:** Every supplier holds years of ballooned drawings and accepted FAIRs, which are excellent supervision, but they are customer-proprietary and often export-controlled, so training happens per customer or on sanitised samples.

---

## 3. Spare-Parts Quote Estimation and Win Probability
#gradient-boosting #logistic-regression #feature-engineering #regularization #cross-validation #evaluation-metrics #revenue-impact

**Problem statement:** For each spare-parts RFQ (government on DIBBS, or commercial), predict whether the shop can bid (approved source, data available, first article test status), the hours and cost to make the part from its drawing and routing features, and the probability of winning at a given price from award history.

**ML task:** Rule and classifier screen for eligibility; gradient-boosted regression of setup and cycle hours and outside-processing cost; logistic model of award probability conditioned on price relative to past awards, quantity and set-aside status
**Input data:** Solicitation text and clauses; NSN, CAGE and part-number cross-references; drawing features from entry 2; the shop's job history (quoted versus actual hours, material, outside processing); public award history by NSN.
**Target:** Bid/no-bid with the blocking reason; predicted hours and cost with an interval; win probability by price.
**Evaluation metric:** Mean absolute percentage error of predicted against actual hours on completed jobs, by part family, with interval coverage; calibration and Brier score of win probability on later awards. The asymmetric cost is a winning quote that loses money, so under-prediction of hours is penalised more than over-prediction.
**Scope:** Eligibility screening is mostly rules plus extraction and delivers value first. Hour estimation needs a few hundred completed jobs per part family. 1–2 data scientists, 4 months.
**Data availability:** Award history is public and messy; job actuals sit in the shop's ERP and need cleaning; quotes that were not won are rarely kept, which biases the win model until capture starts.

---

## 4. Line-Level Delinquency Prediction Across Outside Processing
#survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** Predict, for every open purchase-order line and every lot at an outside processor, the completion date and the probability of missing the customer's need date, early enough for the expediter to recover it.

**ML task:** Time-to-event modelling of operation and outside-processing dwell times with censoring, aggregated to line-level ship-date distributions; ranking of at-risk lines
**Input data:** ERP routings and operation completions; outside-processing shipments and receipts by processor and process; processor confirmation emails; customer portal need dates and delinquency lists; material receipts; machine and inspection queues.
**Target:** Predicted completion date with interval per lot and line; probability of delinquency at 2, 4 and 8 weeks.
**Evaluation metric:** Concordance index for dwell-time ranking and calibration of interval coverage; recall of lines that went delinquent at a four-week horizon, since a late warning is no warning. Track promise-date accuracy (share of committed dates met) as the business metric.
**Scope:** The data integration is most of the work, because outside-processor events arrive by email and phone. 1 data scientist and 1 integration engineer, 4–5 months at one supplier.
**Data availability:** Internal ERP data exists but outside-processing timestamps are patchy; processors' own data is theirs and rarely shared.

---

## 5. Nonconformance and Corrective-Action Retrieval
#bert #transformers #k-nearest-neighbors #large-language-models #evaluation-metrics #compliance #workflow-orchestration

**Problem statement:** Classify every nonconformance report and customer corrective-action request by defect mode and likely root-cause category, retrieve similar past cases and the corrective actions taken, and flag recurrence where a closed action failed to prevent the same failure.

**ML task:** Multi-label text classification of defect mode and root cause; dense retrieval of similar nonconformances; recurrence detection across part families and customers
**Input data:** Nonconformance reports, MRB dispositions, SCARs and 8D responses, inspection results, traveller data, and corrective-action records.
**Target:** Defect mode and root-cause labels; top-k similar cases; a recurrence flag with the failed action named.
**Evaluation metric:** Top-3 root-cause category accuracy against quality-engineer labels and recall of true recurrences, since a missed recurrence is how a supplier ends up on a prime's probation list. Measure response assembly time before and after.
**Scope:** Modest ML, real value: most suppliers have a few thousand nonconformance records in free text. 1 engineer, 3 months.
**Data availability:** Internal records exist but labelling is inconsistent; a few hundred records relabelled by the quality manager make a workable training set.
