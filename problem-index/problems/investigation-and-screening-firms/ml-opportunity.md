# Machine Learning Opportunities — Investigation & Background Screening Firms

**Industry:** [[investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Derived from:** [[problems/investigation-and-screening-firms/high-impact|High Impact]], [[problems/investigation-and-screening-firms/low-impact-1|Low Impact 1]], [[problems/investigation-and-screening-firms/low-impact-2|Low Impact 2]], [[problems/investigation-and-screening-firms/worker-life-1|Worker Life 1]], [[problems/investigation-and-screening-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Surveillance Investigator's Read of a Subject
#tacit-knowledge-ml #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Veteran surveillance investigators judge, within hours, when and where a claimant is likely to move and whether a day is worth continuing — a read built over thousands of assignments that they cannot specify and that leaves with them. The ML problem is to predict the probability and timing of meaningful activity for a subject on a given day from what is known at ordering and in the field, and to surface the veteran's pattern to the junior and to the adjuster deciding whether to order.

**ML task:** Time-to-event modelling of first meaningful activity within a surveillance day (with censoring at termination), plus day-level binary classification of "activity obtained" and a ranking of candidate days and start times per assignment
**Input data:** Assignment records (claim type, injury and work restrictions, claimant age and household, address confidence, vehicles, prior surveillance results, upcoming exam, deposition and hearing dates); field logs with timestamps for start, vantage changes, sightings and termination; video segment metadata; public social media activity timestamps; day of week, weather and local events; investigator identity and tenure.
**Target:** Time from start to first meaningful activity (censored at termination); whether the day produced activity graded as usable on a shared three-point scale by investigator and adjuster; where available, whether the evidence changed the claim's handling (return to work offer, reduced settlement, denial upheld).
**Evaluation metric:** Concordance and time-dependent calibration of the survival model, and expected usable activity per billed hour for model-recommended schedules versus the firm's historical schedules, measured prospectively on held-out months. Report agreement with senior investigators' plans as a separate diagnostic, with their own consistency on repeated cases as the ceiling. A missed activity window costs a re-order; an unnecessary day costs the hours, so the decision threshold should be set from the carrier's cost per hour and the value of usable footage.
**Scope:** The data collection challenge comes first: the investigator's reasons for a start time, a vantage or a termination exist only in their head, so the system needs a near-zero-effort capture surface — one-tap reasons and short voice notes on the phone already used for the log — and historical narrative logs must be parsed into events after the fact. The labelling challenge is that "activity" is contested and experts disagree with themselves about whether footage was worth it, so a shared grading scale with repeated grading on a sample is needed to measure intra- and inter-rater reliability before any outcome label is trusted; claim outcomes are slow and confounded and serve as a secondary label only. The deployment challenge is that the recommendation must arrive before the investigator leaves home and the score before the adjuster orders, inside existing case management and claims systems, and must beat the veteran's own call visibly or be ignored. 2 ML engineers and a field-operations lead at a regional or national firm, 6–9 months, with value first appearing as retrieval ("subjects like this one were active before 7 a.m. on weekdays") before any score is shown to carriers.
**Data availability:** Investigation firms hold years of narrative logs, hours and footage; carriers hold the claim facts and outcomes. Assignment data is the carrier's under service agreements, so a model must be trained per firm or under an explicit data-use clause, and outcome labels require the carrier's cooperation.

---

## 2. Disposition and Reportability Extraction from Court Records
#transformers #large-language-models #seq2seq #feature-engineering #evaluation-metrics #compliance #automation

**Problem statement:** Court records arrive as index rows, scanned dockets and clerk-typed charge and disposition text that differ by state and county. Classify each charge's final disposition, severity and dates into a standard schema, and determine whether it is reportable for a given employment purpose, jurisdiction and salary on the decision date.

**ML task:** Information extraction and multi-class classification of charge, statute, severity, disposition (convicted, dismissed, deferred, diverted, nolle prosequi, sealed or expunged, pending) and sentence completion date, followed by rule application for reportability
**Input data:** County and state court index results, docket text and scanned case summaries; state statute tables; the firm's historical normalised records; reinvestigation outcomes where a disposition was disputed; state and local reportability rules versioned by date.
**Target:** A structured record per charge with field-level confidence; a reportable or not-reportable flag with the rule cited.
**Evaluation metric:** Field-level precision and recall on a stratified test set built from disputed and audited records, with recall on "non-conviction or sealed record read as a conviction" errors weighted most heavily — reporting a dismissed or sealed charge as a conviction is the error that becomes an FCRA claim. Track human-review rate at the confidence threshold used in production.
**Scope:** Disposition vocabulary is finite but local, and the long tail of county-specific phrasing is the work. A model with retrieval over each county's examples, plus deterministic reportability rules, is realistic for 2 ML engineers and a compliance analyst in 4–6 months; continuous monitoring of new phrasing per county is permanent.
**Data availability:** Large screeners hold millions of normalised records and their dispute corrections; smaller agencies depend on vendors. Raw court data is public, but bulk-data agreements with some courts restrict redistribution.

---

## 3. Activity Detection and Automatic Logging in Surveillance Video
#cnns #object-detection #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Surveillance produces hours of footage of a door or a driveway and minutes of a subject doing something. Detect when the subject is visible and what physical activity they perform (lifting, carrying, bending, driving, using tools), time-stamp it, and draft the activity log the investigator now writes by hand.

**ML task:** Person detection and tracking with re-identification of the subject across clips, plus temporal action recognition into a small activity taxonomy relevant to work restrictions
**Input data:** Investigator footage from handheld and fixed cameras at long focal lengths, often through windscreens, with timestamps and GPS; the investigator's reference photo of the subject; existing reports with time-stamped observations as weak labels.
**Target:** Segments where the subject is visible; activity labels with start and end times; a draft log entry per segment.
**Evaluation metric:** Recall on segments containing the subject (a missed segment is lost evidence; a false segment costs seconds of review), and agreement between drafted and investigator-final log times within a tolerance. Activity classification is reported per class, with lifting and carrying weighted most because those contradict typical restrictions.
**Scope:** Pretrained detection and action models transfer, but long-lens, low-light, windscreen footage and frequent occlusion make the domain hard; the classifier must stay descriptive and never infer impairment. 2 engineers, 5–7 months to a tool that cuts review time; on-device processing is a later stage.
**Data availability:** Firms hold large footage archives and the reports written from them; footage belongs to the commissioning carrier or law firm, so training needs per-client consent or in-firm processing, and it contains bystanders whose images must be handled carefully.

---

## 4. Verification Route and Time-to-Close Prediction
#logistic-regression #random-forests #feature-engineering #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** For each open employment, education or licence verification, predict which route will close it fastest (instant database, known employer contact, email, third-party verifier, candidate documents) and how long it will take, so the queue is worked in the right order and the employer gets an honest estimate.

**ML task:** Multi-class route selection with per-route success probabilities, and regression of days to close
**Input data:** Historical verification attempts with source, route, contact, outcome and timestamps; employer and school identifiers resolved to entities; the firm's contact book; candidate-supplied details; seasonality.
**Target:** Route that closed the item; days from order to closure; "unable to verify" outcomes.
**Evaluation metric:** Calibration of route success probabilities and mean absolute error on days to close against the current average-based estimate; operationally, the share of reports held open past the employer's service level by a single verification.
**Scope:** Tabular and well bounded once employer and school names are resolved, which is the main effort. 1 data scientist and 1 engineer, 3–4 months.
**Data availability:** Every screener holds its attempt logs; entity resolution of employer names is needed first.

---

## 5. Cross-Registry Entity Resolution for Due Diligence
#graph-theory #word-embeddings #k-nearest-neighbors #large-language-models #evaluation-metrics #compliance #data-integration

**Problem statement:** An enhanced due diligence report depends on deciding which companies and people in different national registries, court records and press reports are the same entity, across transliterations and missing identifiers. Propose links with evidence so the analyst confirms rather than searches.

**ML task:** Pairwise entity matching with learned name and address embeddings across scripts, candidate generation by nearest neighbours, and graph-based consolidation of ownership and officer links
**Input data:** Registry extracts, officer and shareholder lists, court and insolvency records, adverse-media articles; the firm's prior analyst-confirmed matches and non-matches.
**Target:** Match or non-match per candidate pair with confidence and the supporting fields; consolidated entity graph.
**Evaluation metric:** Precision at high recall on analyst-confirmed pairs, reported per script and jurisdiction; a false link that attributes a fraud judgment to the wrong company is worse than a missed link the analyst finds manually.
**Scope:** Commercial ownership graphs exist; the firm-specific value is matching across its own sources and its confirmed history. 1–2 engineers, 4–6 months.
**Data availability:** Registries and court records are public or licensed; analyst-confirmed matches sit in prior engagement files, which are client-confidential, so only the method and anonymised match pairs can be reused across engagements.
