# Machine Learning Opportunities — Defense Systems Manufacturers

**Industry:** [[defense-systems-manufacturers|Defense Systems Manufacturers]]
**Derived from:** [[problems/defense-systems-manufacturers/high-impact|High Impact]], [[problems/defense-systems-manufacturers/low-impact-1|Low Impact 1]], [[problems/defense-systems-manufacturers/low-impact-2|Low Impact 2]], [[problems/defense-systems-manufacturers/worker-life-1|Worker Life 1]], [[problems/defense-systems-manufacturers/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Propellant Operator's and Radiographer's Calls
#tacit-knowledge-ml #cnns #semantic-segmentation #gradient-boosting #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Senior propellant operators read a batch's process record and know when it will cast and cure well, and Level III radiographers read a cured motor's CT and know which indications matter. The ML problem is to learn both judgements from historical batches, dispositions and test outcomes, and give them to operators and inspectors on new and existing lines while the call is still being made.

**ML task:** (a) Batch-level outcome prediction from multivariate process curves and ingredient lot attributes (probability that the batch yields a rejectable grain or fails lot acceptance); (b) 3D semantic segmentation of CT volumes for voids, cracks, inclusions and bondline separations, with measured size and location against acceptance criteria
**Input data:** Process historian data per batch; ingredient lot certificates; operator interventions and deviations with timestamps; CT volumes and radiographers' marked dispositions; static-fire and lot acceptance test results tied to batch and motor serial numbers.
**Target:** Batch outcome class (accept, accept with deviation, reject) and the radiographer's disposition; voxel-level defect masks; agreement between model and radiographer.
**Evaluation metric:** For CT, recall on rejectable indications at the radiographer's operating point is the binding metric, because a missed void or debond can become a flight failure while a false flag costs a few minutes of review; report per-defect-class recall and the radiographer's own repeat-read agreement as the ceiling. For batches, area under the precision-recall curve on the rare reject class, evaluated strictly by time (train on older batches, test on newer) because ingredient lots and equipment drift.
**Scope:** The data collection challenge is first: the operator's decision and reason have to be captured during the mix in a hazardous bay, so the capture surface must be a one-tap confirmation, and historical batches need their historian data, deviations and CT dispositions joined by serial number after the fact. The labelling challenge is that rejects and test failures are rare and destructive, and radiographers disagree near the boundary, so labels need repeated blind reads on a sample to estimate intra- and inter-rater agreement. The deployment challenge is qualification and speed: the tool can only advise the qualified operator and inspector, must return its read before casting starts or before the radiographer opens the volume, and must run on premises under ITAR. Team of 2 ML engineers, a process engineer and a Level III radiographer seconded part-time, 9–12 months for one motor family at one plant, with retrieval of similar past batches delivering value before any classifier is trusted.
**Data availability:** Held only by motor and munitions plants (incumbents, Army ammunition plant operators, new entrants), on segregated networks under ITAR and sometimes classification. CT volumes and historian data usually exist; the joined record and the operators' reasons mostly do not, and building them is most of the work.

---

## 2. Estimate-at-Completion Drift and Reach-Forward Loss Early Warning
#gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Programme estimates at completion move late and in large steps: Lockheed Martin's missiles segment recognised about $1.4B of reach-forward losses on one classified programme in 2024. Given monthly earned value, schedule and staffing data by control account, predict which accounts and contracts will see a material EAC increase in the next two to six reporting periods.

**ML task:** Control-account-level and contract-level time-to-event modelling of a material EAC increase, plus regression of the eventual completion cost against the current EAC
**Input data:** Monthly cost and schedule performance by control account (budgeted, earned and actual cost, CPI and SPI trends); integrated master schedule float erosion and critical-path changes; headcount and overtime; open material shortages and supplier delinquencies; risk register entries; variance narratives (as text features); contract type and phase.
**Target:** Occurrence and timing of an EAC increase above a materiality threshold; final cost at completion for closed contracts.
**Evaluation metric:** Lead time gained versus the month the programme actually raised its EAC, at a fixed false-alarm rate that programme control can absorb; concordance index for the time-to-event model; mean absolute percentage error of completion cost against the independent EAC formulas (CPI-based and CPI×SPI-based) that analysts already use as baselines. A late warning is close to worthless, so lead time is the headline.
**Scope:** Closed contracts provide labelled histories; the prime's own archive of monthly reports is the asset. Data are CUI or classified, so models run inside programme control's enclave. 2 data scientists and a programme control lead, 6 months to a first model on one business unit's closed contracts.
**Data availability:** Each prime holds its own monthly earned value history. Government cost agencies hold the cross-contractor version, which is contractor-proprietary and not shareable, so a vendor model must be trained per customer.

---

## 3. Basis-of-Estimate Hours from Analogous Actuals
#bayesian-linear-regression #k-nearest-neighbors #large-language-models #confidence-intervals #feature-engineering #compliance

**Problem statement:** For each work breakdown element in a new proposal, retrieve the most comparable completed jobs, estimate hours with an uncertainty range from their actuals, and draft the basis-of-estimate narrative, so estimates trace to evidence and draw fewer questioned hours.

**ML task:** Similarity retrieval over work-content descriptions plus hierarchical Bayesian regression of hours on size and complexity drivers, with LLM drafting of the narrative from the selected analogies
**Input data:** Historical proposals and bases of estimate; labour and material actuals by charge number; work breakdown structure dictionaries; programme attributes (quantity, phase, technology readiness); government evaluation findings and negotiated outcomes.
**Target:** Hours per element with a credible interval; the analogies used; the realised actuals for closed jobs.
**Evaluation metric:** Out-of-time calibration (share of actuals falling within the stated interval) and median absolute error against realised hours, compared with the estimators' original estimates; share of hours questioned in government review before and after adoption.
**Scope:** The hardest part is mapping old charge numbers to work content consistently. 1 data scientist and 1 estimating lead, 4–5 months for one product line.
**Data availability:** Internal to each contractor; actuals are clean, past bases of estimate are scattered across proposal archives, and evaluation findings are often held only in email.

---

## 4. Test Telemetry Anomaly Ranking and Automated Data Reduction
#autoencoders #lstms-and-grus #change-point-detection #evaluation-metrics #feature-engineering #worker-facing #automation

**Problem statement:** After each test event, rank the telemetry segments most likely to be real anomalies (not sensor faults) against the article's prior behaviour, so the test engineer reviews tens of segments instead of thousands of channels.

**ML task:** Multivariate time-series anomaly detection with sensor-fault classification, plus change-point detection for transients
**Input data:** Raw and converted telemetry from prior events of the same article and configuration; calibration files; predicted envelopes from analysis; prior anomaly reports and their resolutions.
**Target:** Ranked anomalous segments labelled real, instrumentation or expected transient; resolution class from past failure reviews.
**Evaluation metric:** Recall of anomalies later confirmed in failure review, at the number of segments an engineer can review before the next event; time from data arrival to quick-look report. Missing a real anomaly costs far more than reviewing a false one.
**Scope:** Each test article has few events, so models must pool across articles of a family and use physics-based predicted envelopes as features. 2 ML engineers with a test engineering lead, 6 months for one test stand or range.
**Data availability:** Held by the manufacturer's test organisation and the government ranges, under ITAR and often classification; prior anomaly resolutions are in report PDFs and need extraction.

---

## 5. Sub-Tier Shortage Prediction for Munitions Bills of Material
#graph-neural-networks #survival-analysis #gradient-boosting #feature-engineering #data-integration #revenue-impact

**Problem statement:** Predict which parts and materials in a missile or round's multi-level bill of material will go short or late in the next one to three quarters (motor cases, nozzles, igniters, energetic ingredients, seekers' electronics) given supplier, order and market signals.

**ML task:** Part-level time-to-shortage prediction over a supplier–part graph, combining order-book features with network position (single sources, shared sub-tier suppliers)
**Input data:** Multi-level bills of material; purchase order history, promised versus actual dates and lead-time trends; supplier attributes and financial signals; single-source and sole-source flags; public award data from SAM.gov and industrial base programme announcements; shortage and expedite logs.
**Target:** Late delivery beyond a threshold or a line-stopping shortage, per part, within the horizon.
**Evaluation metric:** Precision at the top of the ranked list (buyers can act on a few dozen parts a week) and lead time over the date the shortage was actually escalated. A predicted shortage that is already on the expediter's hot list adds nothing.
**Scope:** The internal order book is the core; external supplier mapping from vendors such as Exiger or Air enriches the graph. 2 data scientists, 5–6 months for one programme's bill of material.
**Data availability:** Each prime and tier-1 holds its own; sub-tier visibility beyond tier 2 is poor and is what the supply-chain illumination vendors sell.
