# Machine Learning Opportunities — Testing Laboratories

**Industry:** [[testing-laboratories|Testing Laboratories]]
**Derived from:** [[problems/testing-laboratories/high-impact|High Impact]], [[problems/testing-laboratories/low-impact-1|Low Impact 1]], [[problems/testing-laboratories/low-impact-2|Low Impact 2]], [[problems/testing-laboratories/worker-life-1|Worker Life 1]], [[problems/testing-laboratories/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Reviewer's Call on Chromatographic Data
#tacit-knowledge-ml #cnns #gradient-boosting #transfer-learning #evaluation-metrics #feature-engineering #compliance #worker-facing

**Problem statement:** Senior reviewers look at a finished GC-MS or LC-MS/MS batch and "know" which automatic integrations are wrong, which QC anomalies are matrix rather than method, and which batches are clean — a judgement built over thousands of chromatograms that is never written down. The ML problem is to learn that judgement from the reviewer's own historical actions and outcomes, so the reviewer sees the suspect results first and clean batches can be reviewed by exception.

**ML task:** Peak-level multi-class classification (accept automatic integration / manual reintegration likely / interference or co-elution / carryover / rerun) plus a calibrated sample-level probability that a senior reviewer would intervene, and batch-level ranking for the review queue
**Input data:** Raw chromatographic traces and extracted ion chromatograms exported from the chromatography data system; automatic integration events and parameters; audit-trail records of manual integrations with justifications; internal standard responses, ion ratios and retention times; QC results for the batch (blank, LCS, matrix spike, duplicate, calibration checks); instrument maintenance history; method, matrix and client site; reviewer actions and later outcomes (amended reports, proficiency results, field duplicate agreement).
**Target:** Reviewer action per peak and per sample in the reviewers' own vocabulary; a release-without-intervention probability per sample; and agreement between model and senior reviewer.
**Evaluation metric:** Recall on results a senior reviewer changed or rejected, measured at the auto-release rate the lab is willing to accept — a released result that should have been reintegrated is a defensibility failure, while a false flag costs a reviewer a minute. Report agreement against the reviewers' own inter-rater and test-retest agreement on a re-reviewed sample, which is the ceiling. Validate strictly by time and by instrument, because a model that looks good on random splits has seen tomorrow's column.
**Scope:** The data collection challenge comes first: the reviewer's reasons must be captured as they work, so the first deliverable is a one-click reason vocabulary inside the existing review screen, and historical actions must be reconstructed from audit trails where accepted results leave no trace. The labelling challenge is that reviewers disagree with themselves and drift after assessment findings, so a sample of batches must be re-reviewed blind to estimate reliability, and outcome labels (amendments, PT failures) are sparse and late. The deployment challenge is that the tool must be faster than a reviewer's glance, must never alter raw data or integrations, and must be validated for ISO/IEC 17025 (and Part 11 where pharmaceutical work is involved). Start with one high-volume method family such as volatiles or PFAS; 2 ML engineers, 1 senior chemist and a QA lead, 9–12 months to a validated triage tool.
**Data availability:** Raw data and audit trails sit in every lab's chromatography data system and are exportable, though vendor formats differ. The decisive asset — labelled reviewer decisions with reasons — does not exist yet and must be built prospectively. Results belong to clients, so training stays inside one lab network.

---

## 2. Holding-Time and Turnaround Risk Prediction
#gradient-boosting #survival-analysis #time-series-forecasting #optimization-fundamentals #feature-engineering #workflow-orchestration #revenue-impact

**Problem statement:** Predict, for every logged sample, the probability that it misses its holding time or promised turnaround given the current backlog, instrument status and the real durations of each step for that matrix — early enough for supervisors to re-plan.

**ML task:** Time-to-event modelling of each sample's path through prep, analysis and review, with a classifier for holding-time breach and a forecast of daily workload by method; feeds a batch-assembly optimiser
**Input data:** LIMS event logs (receipt, login, prep start and end, run, review, release) with timestamps; method, matrix, client and rush flags; holding-time rules; instrument run logs and downtime; analyst rosters and qualifications; historical re-preparation and dilution rates by matrix and client site.
**Target:** Probability of holding-time breach; predicted release time; predicted daily load per method and instrument.
**Evaluation metric:** Recall on actual breaches at a flag rate supervisors can act on (missing a breach costs a recollection; a false alarm costs a re-plan), and mean absolute error on release time against the LIMS due-date baseline. Calibration matters because supervisors will act on the probabilities.
**Scope:** Mostly data engineering: LIMS event logs are complete but messy, and step durations must be reconstructed per matrix. 1 data scientist and 1 engineer, 4–5 months to a daily risk board; the optimiser is a second phase.
**Data availability:** Every lab with a LIMS has years of event history. Re-preparation reasons are often free text and need light labelling.

---

## 3. Test Programme Scoping from Product Descriptions
#large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #feature-engineering #automation #revenue-impact

**Problem statement:** Given a manufacturer's product description, datasheets and target markets, propose the list of applicable safety, EMC, radio and battery standards and tests, identify existing certificates that can be leveraged, and estimate chamber time — as a draft for the scoping engineer.

**ML task:** Attribute extraction from unstructured product documents, retrieval over standards' scope clauses and the lab's past test plans, and multi-label prediction of applicable standards; regression for effort from similar past projects
**Input data:** Quote requests, datasheets, schematics and bills of materials; the lab's historical quotes and the test plans actually executed; standards' scope and applicability clauses; module and component certificates; project time records.
**Target:** Set of applicable standards and test blocks per market; leverageable reports; estimated chamber days and engineering hours.
**Evaluation metric:** Recall of standards in the executed test plan is primary — a missed standard becomes a change order or a non-compliant product; precision second. Effort error measured against actual hours.
**Scope:** The lab's own history of quotes versus executed plans is the training set and the main asset. 2 engineers and a senior compliance engineer part time, 4–6 months for one product family (IT and audio-video equipment with radios).
**Data availability:** Quotes and executed plans are internal and plentiful at large labs; standards text is licensed, so retrieval uses scope clauses the lab is entitled to use.

---

## 4. Colony Counting and Typical-Colony Classification on Agar Plates
#cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Count colonies and classify them as typical or atypical for the medium from plate images, flag plates outside the countable range or with spreaders, and propose colonies for confirmation.

**ML task:** Instance segmentation and object detection of colonies, with per-colony classification by medium and target organism
**Input data:** Standardised images of plates at read time under controlled lighting, labelled by medium and method; microbiologists' counts and picks; confirmation results for picked colonies.
**Target:** Colony count per plate; typical/atypical label per colony; countable-range and spreader flags.
**Evaluation metric:** Count agreement within the method's accepted counting tolerance against expert reads, and recall on typical colonies of target organisms — a missed typical colony on a pathogen medium is a false negative with public-health consequences, so recall outranks precision on those media.
**Scope:** Imaging hardware and lighting standardisation matter as much as the model. Commercial automated colony counters exist; the gap is classification of typical colonies across the lab's actual media. 1 ML engineer and 1 microbiologist, 5–6 months per group of media.
**Data availability:** Images must be collected prospectively; counts and confirmation results already exist in the LIMS.

---

## 5. Early Prediction of 28-Day Concrete Strength
#gradient-boosting #linear-regression #bayesian-inference #confidence-intervals #feature-engineering #quick-win

**Problem statement:** Predict the 28-day compressive strength of each placement from its mix design, field measurements and seven-day breaks, and flag placements likely to fall below specification weeks before the 28-day result.

**ML task:** Regression with prediction intervals, updated as early breaks arrive
**Input data:** Mix designs and supplier; batch tickets; field slump, air content and concrete and ambient temperature; curing conditions and time to pickup; seven-day (and three-day where run) breaks; fracture type; historical 28-day results for the same mix and plant.
**Target:** 28-day strength with an interval; probability of falling below the specified strength.
**Evaluation metric:** Mean absolute error on 28-day strength and recall on below-specification placements at a useful lead time — a missed low pour is discovered after the structure is loaded on it.
**Scope:** A classic, well-documented regression problem; the work is in assembling clean joined records. 1 data scientist, 2–3 months for a firm with several years of results.
**Data availability:** Construction materials testing firms hold years of field and break data; field sheets on paper must be digitised first, which the field app in worker-life 1 does going forward.
