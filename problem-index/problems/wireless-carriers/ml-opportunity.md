# Machine Learning Opportunities — Wireless Carriers

**Industry:** [[wireless-carriers|Wireless Carriers]]
**Derived from:** [[problems/wireless-carriers/high-impact|High Impact]], [[problems/wireless-carriers/low-impact-1|Low Impact 1]], [[problems/wireless-carriers/low-impact-2|Low Impact 2]], [[problems/wireless-carriers/worker-life-1|Worker Life 1]], [[problems/wireless-carriers/worker-life-2|Worker Life 2]]

---

## 1. Learning the RF Engineer's Diagnosis of a Degraded Sector
#tacit-knowledge-ml #graph-neural-networks #gradient-boosting #causal-inference #evaluation-metrics #feature-engineering #worker-facing

**Problem statement:** Senior RF engineers look at a degraded sector's counters, its neighbours and recent changes and "just know" whether the cause is interference, passive intermodulation, coverage, congestion, a neighbour or mobility error, hardware or backhaul, and which action will fix it. The ML problem is to learn that diagnosis from the engineers' own confirmed records and the measured outcome, and offer it, with precedents, to whoever works the sector next.

**ML task:** Multi-class root-cause classification at sector level over the sector-neighbour graph, plus a ranking of candidate actions by estimated effect, conditioned on the predicted cause
**Input data:** Hourly performance counters per sector and carrier (drops, accessibility, throughput, uplink noise floor, PRB utilisation, handover success by neighbour); RSRP and SINR distributions; neighbour relation tables; configuration and parameter change logs for the sector and its neighbours; hardware alarms; site type, band and antenna metadata; drive-test and crowdsourced samples where available; and the diagnosis ledger: engineer-confirmed cause, action and expected effect.
**Target:** Cause class per investigation; for each candidate action, the change in the sector's composite KPI two to four weeks later relative to matched control sectors.
**Evaluation metric:** Top-2 accuracy on cause against held-out senior-engineer labels, reported against the seniors' own inter-rater and test-retest agreement as the ceiling. For actions, the estimated KPI lift of recommended versus actual actions using the matched-control design, evaluated strictly out of time. Recall on hardware and PIM causes matters more than precision, because missing them leaves a sector degraded for weeks, while a false flag costs an engineer a few minutes. A wrong recommendation that triggers an unneeded climb should be counted as a cost.
**Scope:** Data collection comes first and is the hardest part. The expert's diagnosis has to be captured while they work, so the system must draft the record from the charts they opened and the change they submitted and ask for a one-click confirmation. History can be partly reconstructed from change tickets but will be thin. Labelling has two problems. Engineers disagree with themselves, so a sample of cases needs repeated, blinded annotation to estimate the ceiling. The outcome is confounded by traffic, events and neighbour changes, so labels need a matched-control or difference-in-differences design rather than before-and-after. Deployment has to be faster than the engineer's own glance at the dashboard and live inside the worst-offender workflow, ideally as an app on the vendor's management platform. Expect 2 ML engineers, 1 RF subject-matter lead and a data engineer embedded with one market's optimisation team for 9–12 months. Value shows first as retrieval ("the last five sectors with this uplink signature were PIM") before any classifier is trusted.
**Data availability:** Counters and change logs are complete but often sit in vendor-managed systems, and access must be negotiated contract by contract. The decisive asset, confirmed diagnoses, doesn't exist yet and must be built prospectively. Regional carriers own their data outright and are easier first partners.

---

## 2. Alarm-to-Dispatch Triage for Field Technicians
#gradient-boosting #survival-analysis #bayesian-inference #feature-engineering #evaluation-metrics #worker-facing #automation

**Problem statement:** For each site alarm, predict whether it will self-clear and how soon, whether it is explained by a utility power outage, and which part a visit is most likely to need, so the technician can decide whether to wait, call the utility or drive with the right spare.

**ML task:** Time-to-clear survival model; binary classification of utility-power cause; multi-class classification of required part or action
**Input data:** Alarm streams with codes and timestamps; site type, equipment generation and power configuration; battery and generator telemetry; utility outage feeds where available; weather; prior tickets and visit outcomes at the site and similar sites; spare parts used on past visits.
**Target:** Time from alarm to recovery without a visit; power-cause flag; part or action recorded on the visit that resolved the ticket.
**Evaluation metric:** Concordance and calibration of the time-to-clear distribution, because the technician acts on "80% chance it clears in 20 minutes", not on a point estimate. Recall on alarms that will not self-clear is the binding constraint: telling a technician to wait on a real outage extends it. Business measures are avoided trips, first-visit fix rate and outage minutes, compared in a staggered rollout across territories.
**Scope:** Tabular and well-labelled once ticket closure codes are cleaned; closure codes are notoriously inconsistent and need a mapping effort with technicians. 1–2 data scientists, 4–6 months for one region.
**Data availability:** Alarms, tickets and parts usage are the carrier's own. Utility outage data varies by utility and may need scraping or agreements.

---

## 3. Propagation Model Calibration for FCC Coverage Filings
#gaussian-processes #cnns #regularization #evaluation-metrics #hypothesis-testing #compliance #data-integration

**Problem statement:** Calibrate the carrier's propagation predictions against measured performance by clutter and terrain, so coverage maps filed at the FCC's parameters (5/1, 7/1 and 35/3 Mbps at 90% cell-edge probability and 50% loading) hold up in challenges and verification, and triage incoming challenges into concede or rebut.

**ML task:** Spatial residual modelling of measured versus predicted signal and throughput (Gaussian process or gradient-boosted residuals over terrain and clutter rasters, with CNN features from imagery for clutter); challenge classification
**Input data:** Planning-tool predictions per site and sector; drive-test and crowdsourced measurements with location, device, technology and indoor or outdoor flags; terrain, building and foliage rasters; site and antenna database; sector loading at test time; FCC challenge records.
**Target:** Residual between predicted and measured performance per hexagon and clutter class; probability that a challenge test reflects a real coverage gap rather than an indoor, wrong-technology or congestion artefact.
**Evaluation metric:** Out-of-area error and coverage-probability calibration: in hexagons claimed covered, the measured share meeting the speed should be at least 90%. Report under-claiming separately, because it costs subsidy eligibility, while over-claiming invites challenges and enforcement. For challenge triage, precision on "rebut" matters most, since a rebuttal that fails costs credibility with the FCC.
**Scope:** Methods are mature; the work is data assembly and documentation that survives scrutiny. 1 RF engineer and 1 data scientist, 4 months to the first filing cycle.
**Data availability:** Carriers hold drive tests and planning data; crowdsourced data is licensable; FCC challenge data is public.

---

## 4. Tower Lease Abstraction and Loading Reconciliation
#large-language-models #transformers #seq2seq #evaluation-metrics #feature-engineering #data-integration #automation

**Problem statement:** Extract equipment entitlements from master lease agreements, site amendments and their exhibits, and reconcile them against the carrier's installed-equipment inventory to flag overbilling, unrecorded removals and loading above entitlement.

**ML task:** Document understanding and structured extraction (including tables and drawings in scanned exhibits), amendment-chain resolution, then rule-based and learned matching against inventory records
**Input data:** Lease and amendment PDFs, often scanned; exhibits with antenna and mount schedules; tower-owner invoices; network configuration and inventory; site audit photos; structural analysis reports.
**Target:** Per site: entitled antennas, radios, cables, mount heights and weights, current rent and escalator base, and a list of discrepancies with source citations.
**Evaluation metric:** Field-level extraction accuracy at the confidence threshold where fields are accepted without review, with zero tolerance for silent errors on rent and entitlement fields. Discrepancy precision matters because each flag starts a dispute with a tower owner, so a false one wastes a negotiator's time.
**Scope:** Prior abstractions by lease administrators give supervised examples; drawings and handwritten exhibits are the hard tail. 2 engineers, 4–5 months for a pilot of a few thousand sites.
**Data availability:** The documents are the carrier's own; the inventory side needs network engineering's cooperation.

---

## 5. Bill-Change Explanation and Port-Out Risk at the Care Call
#large-language-models #causal-inference #gradient-boosting #survival-analysis #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** When a customer calls about a higher bill, explain exactly which promotion or charge changed and why, and estimate both the customer's port-out risk and which policy-allowed remedy, if any, changes that risk.

**ML task:** Retrieval-grounded explanation generation over billing and promotion records; time-to-port survival model; uplift (heterogeneous treatment effect) estimation for remedies such as goodwill credits, promotion reinstatement or plan changes
**Input data:** Bill line items across cycles; promotion enrolments with term versions; device payment plans; order and line-change history; prior contacts; network experience on the customer's usual sectors; historical remedies offered and subsequent port-outs, ideally with randomised holdouts.
**Target:** Explanation text with citations to records and term versions; port-out within 90 days; incremental reduction in port-out probability per remedy.
**Evaluation metric:** Explanation accuracy judged by senior agents against the records, with every claim traceable. For uplift, Qini or uplift curves on holdout data, plus realised retained lines per dollar of credit. A remedy model trained without holdouts will mostly learn who was going to stay anyway.
**Scope:** The explanation layer is buildable in months with clean access to billing data. The uplift layer needs a deliberate holdout policy, which takes a quarter of data collection before it can be trusted. 2–3 engineers, 6–9 months.
**Data availability:** Fully internal, but spread across billing, promotion, care and network systems that rarely share keys.
