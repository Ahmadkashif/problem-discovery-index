# Machine Learning Opportunities — Self-Insured Benefit & Risk Pools

**Industry:** [[self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Derived from:** [[problems/self-insured-benefit-pools/high-impact|High Impact]], [[problems/self-insured-benefit-pools/low-impact-1|Low Impact 1]], [[problems/self-insured-benefit-pools/low-impact-2|Low Impact 2]], [[problems/self-insured-benefit-pools/worker-life-1|Worker Life 1]], [[problems/self-insured-benefit-pools/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Claims Manager's Early Read on Police and Civil Rights Claims
#tacit-knowledge-ml #gradient-boosting #large-language-models #survival-analysis #evaluation-metrics #feature-engineering #compliance #revenue-impact

**Problem statement:** A pool's senior liability claims manager reads a new use-of-force, false-arrest or employment complaint and knows within weeks whether it is headed past the pool's retention. The read is formed on facts no structured field holds, and it leaves with the person. The ML problem is to learn that read from the manager's own dated reserves and notes plus closed outcomes, and give it to the next adjuster with its track record.

**ML task:** Calibrated binary classification (will the claim's ultimate incurred value exceed the retention?) plus survival modelling of time to close, with LLM extraction of structured features from complaints, police reports and claim notes
**Input data:** First notice and complaint documents; police incident and use-of-force reports; claim notes and reserve history with timestamps; allegation type, injury, video present, officer and department history, plaintiff counsel, venue and judge; member exposures (sworn officers, jail beds); public verdict and settlement reports for comparables.
**Target:** Ultimate incurred above or below the retention ($1M–$2M at CIRSA); closed value band; months to close; agreement between model and manager at the first reserve.
**Evaluation metric:** Recall of retention-piercing claims at a fixed review budget (for example the top 10% of new claims flagged), and calibration (Brier score) of the exceedance probability, measured strictly out of time by report year, because legal climates shift (Colorado's S.B. 20-217) and random splits leak them. Report agreement with held-out manager reads against the manager's own test-retest consistency as the ceiling. A missed seven-figure claim costs settlement leverage and reinsurer notice. A false flag costs an hour of senior review, so recall dominates.
**Scope:** The data collection challenge is the core: the manager's expected outcome and settle-or-defend lean must be captured at intake and each reserve change through a confirm-in-seconds form drafted from the file, and history must be reconstructed from notes where it exists. The labelling challenge is that outcomes are rare, slow (three to six years to close, estimate) and venue-dependent, and the same manager reserves differently after a recent verdict, so labels need repeat annotation on a sample and venue-adjusted outcome bands. The deployment challenge is speed and privilege: the read must land inside the first reserve window, faster than the manager's recall, and outside documents that are discoverable. 2 ML engineers, 1 claims-domain lead and counsel review, 6–9 months with one large pool, longer for a consortium.
**Data availability:** Each pool holds its own claims with reserve histories, but one pool sees few seven-figure police claims, so useful models need a multi-pool consortium under data-sharing agreements. Defence counsel evaluations are often privileged and should stay out of training data unless counsel agrees. Verdict reports are licensable from verdict reporters.

---

## 2. Catastrophic Claimant Early Warning for Stop-Loss and Case Management
#gradient-boosting #lstms-and-grus #survival-analysis #evaluation-metrics #feature-engineering #compliance #revenue-impact

**Problem statement:** Predict, from the first months of a member's claims, which members of a health fund will exceed the specific stop-loss deductible within the next twelve months, so the fund files timely notices, refers to case management and sets its contribution allocation with eyes open.

**ML task:** Binary classification and time-to-threshold survival modelling over claim sequences
**Input data:** Medical and pharmacy claims with diagnosis, procedure and drug codes; pre-certifications and inpatient notifications; eligibility and hour-bank status; prior-year large-claimant lists; stop-loss contract deductibles and lasers.
**Target:** Paid amount exceeds the specific deductible within 12 months of the first signal; days to crossing.
**Evaluation metric:** PR-AUC and recall at the top 0.5–1% of members, because large claimants are rare (Sun Life counts claims per million covered employees). Report lead time gained over the TPA's existing 50%-of-deductible notice. Calibration matters for reserves and contribution projections.
**Scope:** Commercial risk-adjustment models exist. The gap is fund-specific sequence models tied to the stop-loss contract and run monthly at the TPA. 1–2 data scientists, 4–6 months, under a business associate agreement, with clinical review of top-flagged cases.
**Data availability:** The TPA and PBM hold the claims under BAAs for the fund; a fund of 5,000 members sees only a few crossings a year (estimate), so pooled training across a TPA's book needs each fund's consent. Labels are objective once the plan year runs out.

---

## 3. Which Loss-Control Recommendations Actually Reduce Claims
#causal-inference #gradient-boosting #hypothesis-testing #confidence-intervals #large-language-models #worker-facing #compliance

**Problem statement:** Estimate the effect of completing each type of loss-control recommendation (playground surfacing, sidewalk repair, pursuit policy, jail cell checks, fleet driver checks) on subsequent claim frequency and severity at the member, so consultants recommend what works and members fix it.

**ML task:** Causal effect estimation (difference-in-differences and causal forests) with LLM classification of free-text recommendations into a hazard taxonomy
**Input data:** Years of site-visit reports and recommendation letters; completion records; member exposures; claims by cause of loss and location; member characteristics.
**Target:** Change in claim frequency and incurred cost by cause in the two to three years after completion versus comparable members that did not complete.
**Evaluation metric:** Effect estimates with confidence intervals and placebo tests on unrelated claim causes; the honest outcome for many recommendation types will be "not detectable," which is itself useful. Classifier accuracy against consultant-labelled recommendations comes second.
**Scope:** The hardest part is turning narrative reports into structured, dated recommendations with completion status, which most pools do not track. 1 data scientist and 1 loss-control lead, 5 months on a pool with 10+ years of reports.
**Data availability:** Held by each pool; completion data is sparse and must be collected going forward.

---

## 4. Property Schedule Validation and Replacement-Cost Estimation for Public Assets
#cnns #object-detection #gradient-boosting #k-nearest-neighbors #feature-engineering #data-integration #automation

**Problem statement:** Find unscheduled, misdescribed and undervalued buildings in a pool's statement of values before the property renewal, using imagery, parcel data and the pool's own schedule and claims.

**ML task:** Object detection on aerial imagery to match structures to schedule lines; regression of replacement cost per square foot by public occupancy type; anomaly flags for values stale against construction cost trend
**Input data:** Members' schedules (address, occupancy, construction, year built, area, value); aerial and street imagery; parcel and building-footprint data; appraisal results where performed; property claims with adjusted values.
**Target:** Match or no match per footprint; estimated replacement cost; flag when the scheduled value falls outside the predicted interval.
**Evaluation metric:** Precision of "unscheduled building" flags (each false flag costs a member's time); mean absolute percentage error of replacement cost against recent appraisals and claim settlements, reported by occupancy type, with coverage of wastewater plants and fire stations reported separately.
**Scope:** 2 engineers, 4–6 months. Public occupancies are thinly represented in commercial valuation data, so appraisal results across many pools are the limiting asset.
**Data availability:** Schedules and claims belong to each pool; imagery and parcels are licensable or public; appraisals are pool-commissioned.

---

## 5. Stop-Loss Contract and Claims Packet Extraction
#large-language-models #transformers #feature-engineering #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Turn each stop-loss policy into machine-readable rules and assemble each reimbursement packet automatically, predicting which items the carrier will query.

**ML task:** Clause extraction from contracts and plan documents into a schema; document classification and completeness checking of packets; classification of likely carrier queries
**Input data:** Stop-loss policies and endorsements; plan documents and amendments; historical filings with carrier correspondence and outcomes; itemised bills and eligibility histories.
**Target:** Contract fields (basis, deductibles, lasers, eligible expense definition, filing deadline); packet completeness; query or denial reason.
**Evaluation metric:** Field-level exact match on contract terms, with errors on filing deadlines and paid-through dates weighted heaviest because they forfeit money; recall on packets that historically drew queries.
**Scope:** 1–2 engineers, 3–4 months. Contract language is semi-standard by carrier, so extraction generalises well once a few carriers' forms are covered.
**Data availability:** Policies and filings are held by funds, TPAs and brokers; correspondence history exists in email and must be gathered.
