# Machine Learning Opportunities — Self-Storage Operators

**Industry:** [[self-storage-operators|Self-Storage Operators]]
**Derived from:** [[problems/self-storage-operators/high-impact|High Impact]], [[problems/self-storage-operators/low-impact-1|Low Impact 1]], [[problems/self-storage-operators/low-impact-2|Low Impact 2]], [[problems/self-storage-operators/worker-life-1|Worker Life 1]], [[problems/self-storage-operators/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Revenue Manager's Read of Who Will Stay
#tacit-knowledge-ml #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Experienced revenue managers and owners look at a tenant's file and "know" whether an increase will be absorbed or will push the tenant out: the contractor on autopay stays, the weekend visitor emptying the unit leaves. The ML problem is to learn that read from their override decisions and the outcomes that followed, and surface it as a calibrated move-out risk on every tenant in the increase batch.

**ML task:** Binary classification of move-out within 90 days of an increase notice, with a time-to-move-out survival model as the main output and a calibrated probability per tenant
**Input data:** Tenant ledger history (tenure, in-place rent, every past increase and response, autopay, late payments, protection-plan status); unit attributes (size, climate control, floor, drive-up); in-place rent against the current street rate for the same unit type; gate and smart-lock access frequency over the last 90 days; the expert's past override decisions and one-click reasons ("moving out", "business tenant", "complained last time"); local competitor rates and new supply.
**Target:** Move-out (or lien) within 30, 90 and 180 days of the notice; time to move-out; agreement between the model's risk band and the expert's override.
**Evaluation metric:** Brier score and calibration by risk decile on held-out, later batches, never on a random split, which leaks seasonal effects. Agreement with expert overrides is reported against the expert's own test-retest agreement on re-shown files as the ceiling. Recall on high-risk tenants matters more than precision: a missed leaver costs a tenancy worth ~$1,000–2,000 a year (estimate), and a false flag costs a few dollars of forgone increase.
**Scope:** The data-collection challenge comes first: the expert's read must be captured inside the batch-approval screen as a one-click reason on overrides, and historical decisions must be reconstructed from approval logs. The labelling challenge is that move-outs have many causes and increases were not randomly assigned. Larger increases went to tenants the expert judged stable, so the model must be trained with that selection in mind, and the expert's own consistency measured on re-scored samples. The deployment challenge is speed and trust: risk must appear in the screen the expert already uses, beside a reason, faster than their scan. 1 data scientist and 1 engineer with one regional operator or third-party manager, ~5 months, starting with 2–3 years of ledger history.
**Data availability:** Every facility system holds the ledger and the move-outs. Access logs exist where gates or smart locks are integrated. The expert's reasons do not exist and must be captured from now on. Third-party managers hold owners' ledgers under management agreements, so a pooled model needs owner consent.

---

## 2. ECRI Increase-Size Optimiser (the Two-Week MVP)
#causal-inference #survival-analysis #monte-carlo-methods #optimization-fundamentals #compliance #revenue-impact #quick-win

**Problem statement:** Given each tenant's move-out risk, choose the increase that maximises expected net rent over the next 12 months, subject to state notice periods, emergency caps and the operator's own fairness rules. A two-week MVP builds this on a synthetic tenant ledger and street rates operators post publicly.

**ML task:** Dose-response (uplift) estimation of move-out hazard as a function of increase size and the gap to street rate, followed by constrained optimisation over a grid of increase sizes per tenant
**Input data:** For the MVP: a synthetic ledger of ~20,000 tenants over 36 months, generated with known latent price sensitivity by tenant type, so that the true effect of each increase is known; publicly posted street rates for one metro, read from operators' own websites, to set the gap to market; a rules table of notice periods and caps (California's 30 days' notice to amend, Los Angeles County's former 10% emergency cap). In production: the operator's real ledger and deliberately randomised small variations in increase size.
**Target:** Expected 12-month net rent per tenant at each candidate increase (0%, 4%, 8% … 30%), and the chosen increase with its notice date.
**Evaluation metric:** On synthetic data, error between estimated and true dose-response curves, and net rent achieved against two baselines: a flat rule (every tenant +10%) and "raise to street rate". In production, net rent per notice after 12 months of induced move-outs in randomised holdout cells. No recommendation may break a notice period or cap. That is a hard constraint, not a metric.
**Scope:** The two-week MVP: day 1–3 ledger simulator; day 4–5 street-rate scrape and normalisation; day 6–9 survival model with doubly robust adjustment and a T-learner uplift baseline; day 10–12 optimiser and rules table; day 13–14 report comparing net rent against the baselines. A production version needs a pilot operator, two increase cycles (~12 months) of randomised cells, and legal review of the fairness rules.
**Data availability:** The synthetic ledger and public rates need no permission: listed street rates are public data. Real ledgers sit in facility software and, at managed stores, belong to the owners.

---

## 3. Street-Rate Normalisation and Vacancy Forecasting
#large-language-models #time-series-forecasting #bayesian-inference #exponential-smoothing #feature-engineering #data-integration

**Problem statement:** Turn competitors' published rate pages into a like-for-like daily rate for each unit type in a store's chosen comp set, and forecast each unit type's vacancy over the next 30 days so web rates move before units sit empty.

**ML task:** Information extraction from rate pages and promotion text into a normalised schema, then hierarchical time-series forecasting of move-ins and move-outs by unit type
**Input data:** Daily snapshots of competitors' public rate pages; promotion text and fees; the store's own move-ins, move-outs, reservations and web-traffic history; seasonality; monthly TractIQ or Yardi Matrix indices as priors.
**Target:** Effective monthly rent per competitor unit type over a typical stay; 30-day forecast of vacant units by type at the store.
**Evaluation metric:** Extraction accuracy against a hand-labelled set of 1,000 rate pages, with promotions weighted by their effect on effective rent. Forecast error as weighted absolute percentage error on vacant units by type, with interval coverage. Under-forecasting vacancy is costlier, because empty units earn nothing.
**Scope:** 1 engineer and 1 data scientist, ~3 months for one metro. Unit-label normalisation (floor, access, door size) is the hard tail. Bayesian pooling across stores helps small unit types with few move-ins.
**Data availability:** Rate pages are public. Move-in history is in every facility system. Market indices are licensed.

---

## 4. Delinquency Roll-Rate and Pre-Lien Triage
#markov-chains #logistic-regression #evaluation-metrics #compliance #automation

**Problem statement:** Predict which delinquent tenants will pay before the lien sale, which will abandon the unit, and which will dispute, so outreach goes to tenants who will pay. The statute engine keeps every unit on its legal track either way.

**ML task:** Multi-state Markov roll-rate model (current, 15, 30, 45, 60 days, sale, cured) with a logistic model of transition probabilities per tenant
**Input data:** Payment and late-fee history; notice dates and delivery evidence; contact attempts and responses; tenure; unit contents category where recorded; access after the overlock; past cure behaviour; state of the facility.
**Target:** Probability of cure before the sale date; probability of abandonment; expected recovery.
**Evaluation metric:** Calibration of cure probability by state and delinquency stage, and recovered past-due rent per contact hour against current outreach order. Precision on "will abandon" matters most, because those files can skip outreach and go straight to the statutory steps, which are never skipped.
**Scope:** 1 data scientist, ~3 months on 2–3 years of delinquency history. The model ranks outreach and never changes a statutory step or date.
**Data availability:** Facility systems hold the ledger and notice history. Contact outcomes are often in call-centre notes and need extraction.

---

## 5. Unit-State Inference from Access Events
#hidden-markov-models #change-point-detection #cnns #worker-facing #automation

**Problem statement:** Infer each unit's true state (in use, being emptied, abandoned, vacant but locked, overlock breached) from smart-lock, gate and sensor events and the ledger, so the store manager checks only the doors that disagree.

**ML task:** Hidden Markov model per unit over daily access-event features, change-point detection for move-out in progress, and an image classifier for lock type and position on door photos where no smart locks exist
**Input data:** Smart-lock and door events (Nokē and similar), gate code entries, unit motion sensors, ledger status, payment events, door photos from the manager's phone.
**Target:** Inferred unit state and a mismatch flag against the ledger; lock type and position per photo.
**Evaluation metric:** Precision of mismatch flags confirmed on the manager's walk (a false flag wastes a walk; a miss costs rent). Recall is measured on periodic full audits. Moving-out detection is scored by lead time before the move-out is recorded.
**Scope:** 1 engineer and 1 data scientist, ~4 months with an operator that has smart locks on most units. The photo classifier needs ~5,000 labelled door images, collected on consenting sites with no people in frame.
**Data availability:** Access events sit in the lock vendor's cloud and the facility system, under the operator's service agreement. Photos must be collected for the purpose.
