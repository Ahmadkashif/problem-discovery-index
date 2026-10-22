# Machine Learning Opportunities — Architecture Firms

**Industry:** [[architecture-firms|Architecture Firms]]
**Derived from:** [[problems/architecture-firms/high-impact|High Impact]], [[problems/architecture-firms/low-impact-1|Low Impact 1]], [[problems/architecture-firms/low-impact-2|Low Impact 2]], [[problems/architecture-firms/worker-life-1|Worker Life 1]], [[problems/architecture-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Principal's Red Pen
#tacit-knowledge-ml #cnns #object-detection #transformers #gradient-boosting #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Senior architects reviewing a construction document set "know" which details and coordination points will generate RFIs, change orders or failures — a judgement built from years on site that they cannot write down. The ML problem is to learn where they look and what they flag from their historical markups and the construction-phase outcomes, and to rank the regions of a new set by risk before the review.

**ML task:** Object detection of building elements and detail types on drawing sheets, followed by region-level risk ranking (gradient-boosted classifier over region, project and team features) calibrated to the probability of a QA/QC markup and of a design-attributable RFI or change order
**Input data:** Issued PDF sets and their Bluebeam markup layers from past QA/QC reviews; standard detail library with version history; RFI and change order logs from closed projects with sheet and detail references; project metadata (building type, delivery method, construction type, team, contractor); where obtainable, warranty and water-intrusion records.
**Target:** For each sheet region: whether the reviewer marked it, the markup category (coordination conflict, code, envelope/waterproofing, constructability, drafting), and whether it later produced a design-attributable RFI or change order.
**Evaluation metric:** Recall of reviewer markups and of later RFIs within the top-k ranked regions per set (k sized to what a principal can examine in a day), measured on projects held out by time. Recall matters more than precision: a missed parapet failure costs a change order or a claim; a false flag costs a minute. Agreement with held-out reviewer markups is reported against the reviewer's own test-retest agreement on re-reviewed sheets as the ceiling.
**Scope:** The data collection challenge is first: historical markups are free-form clouds and abbreviations that must be aligned to sheet regions, and the outcome records live in contractors' closeout archives, so the project starts with a capture surface inside the markup tool that tags each cloud with a category in one click. The labelling challenge is that principals disagree with themselves and mix risk with preference, so a sample of sheets must be re-reviewed blind to estimate intra-rater reliability, and RFI labels must separate design-attributable questions from contractor-driven ones. The deployment challenge is speed and selectivity: the ranked map must be ready the night before the review and must surface tens of regions, not hundreds, or it will be ignored. 2 ML engineers and 1 architect-domain lead, 9–12 months, with value arriving first as retrieval ("this detail produced RFIs on four of the last six projects") before any classifier is trusted.
**Data availability:** Issued sets and markups exist at every firm, scattered across Bluebeam files and paper scans. Outcome data requires closeout archives from contractors' Procore or ACC projects, which large firms can obtain and small ones rarely do. No public dataset exists; this is firm-specific data by nature.

---

## 2. Permit Comment Prediction by Jurisdiction
#bert #large-language-models #k-nearest-neighbors #transformers #evaluation-metrics #compliance #workflow-orchestration

**Problem statement:** Given a permit set and its jurisdiction, predict the plan-review comments it is likely to receive, so they can be resolved during design development rather than after a correction letter.

**ML task:** Multi-label text classification of correction comments into a code-section and issue taxonomy, plus retrieval of similar past comments and accepted responses conditioned on jurisdiction, building type and occupancy
**Input data:** Historical correction letters (PDF) and response letters from the firm's projects; code analysis sheets and project metadata; adopted code editions and local amendments by jurisdiction; where public, building department comment records exported from permit portals.
**Target:** The set of comment categories a submission will receive, with the most similar past comment text and the response that cleared it.
**Evaluation metric:** Recall at k of comment categories actually received on held-out submissions, and the share of first-round comments the firm could have pre-empted. Report by jurisdiction, because a model that is good in the firm's home city and blind elsewhere is the common failure.
**Scope:** The taxonomy is the main design work; once correction letters are parsed into structured comments, retrieval over the firm's own history gives immediate value. 1 ML engineer and 1 project architect, 4–5 months for a firm working in 10–20 jurisdictions.
**Data availability:** Every firm holds its own correction and response letters; multi-firm pooling is what makes the model strong and is the hard commercial problem. Some jurisdictions publish review comments through open permit data.

---

## 3. Submittal Compliance Extraction
#large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #automation #compliance

**Problem statement:** Extract the requirements from the project's specification section and the corresponding values from the contractor's product data and shop drawings, and flag every deviation before the reviewer opens the package.

**ML task:** Structured information extraction from specification text and manufacturer PDFs (tables, data sheets, test reports), with requirement-to-value matching and unit and test-standard normalisation
**Input data:** Project specification sections (Parts 1–3); submittal PDFs; drawing schedules (door, window, finish); approved substitution requests; past submittals with the reviewer's stamp and comments as supervision.
**Target:** For each requirement: the submitted value, a compliant / deviation / missing determination, and a draft review comment in the firm's stamp language.
**Evaluation metric:** Recall on deviations the reviewer marked, with zero tolerance for silent misses on life-safety and performance items (fire rating, structural load, air and water infiltration); precision measured as reviewer edits per draft. Time per package before and after.
**Scope:** Spec sections are well structured and past stamped submittals provide supervised examples; the hard tail is shop drawings, where the comparison is geometric. 2 engineers, 4–6 months for product-data submittals; shop drawings later.
**Data availability:** Firms hold specifications and stamped submittals for every past project; manufacturer data sheets are public. Labelling uses reviewers' existing comments.

---

## 4. Phase-Hour Forecasting for Fee Proposals
#gradient-boosting #survival-analysis #change-point-detection #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict the labour hours each AIA phase will actually consume for a proposed project, and detect early in a phase when a project is drifting off that curve, so fees are set and defended on evidence rather than the principal's recollection.

**ML task:** Quantile regression of hours by phase and role from project attributes; time-to-budget-exhaustion survival model; change-point detection on weekly burn
**Input data:** Timesheets by project, phase and role from Deltek, BQE or Monograph; fees and contract amendments; project attributes (building type, size, construction cost, delivery method, client type, number of owner-requested changes); additional-services records.
**Target:** Hours per phase (10th/50th/90th percentile); the week a phase budget is exhausted; the date burn diverges from plan.
**Evaluation metric:** Pinball loss and interval coverage on held-out projects; lead time between a detected change point and the date the PM would otherwise have noticed. Under-forecasting costs more than over-forecasting, because a fee once signed cannot be raised without an additional-services fight.
**Scope:** Modest modelling on internal data; the obstacle is timesheet hygiene, since many firms code time to projects but not phases. 1 data scientist, 3–4 months for a firm with 200+ closed projects.
**Data availability:** Firm-internal and reasonably clean at firms on Deltek or BQE; poor at small firms. Benchmarks across firms exist only as published survey averages.

---

## 5. Early-Design Carbon and Cost Surrogates
#gaussian-processes #bayesian-optimization #regularization #evaluation-metrics #compliance #data-integration

**Problem statement:** At massing stage, estimate whole-building embodied carbon and construction cost for each design option in seconds, so the team can find options that meet CALGreen's 10% embodied carbon reduction (and owner targets) before the structural system is fixed.

**ML task:** Surrogate regression with uncertainty from massing and system parameters to life-cycle GWP and cost, with Bayesian optimisation over design options
**Input data:** Completed whole-building LCAs from One Click LCA, Tally or EC3 exports; cost plans from cost consultants at each design stage; massing parameters (gross area, floors, floor-to-floor, span, structural system, enclosure ratio, glazing ratio, below-grade volume).
**Target:** Cradle-to-grave GWP per square metre and construction cost per square metre, each with a predictive interval.
**Evaluation metric:** Mean absolute percentage error and interval calibration against completed LCAs and final cost plans; ranking accuracy between options matters more than absolute accuracy, because the decision is which option to develop.
**Scope:** Gaussian processes suit the small-data regime of a single firm's few dozen completed LCAs; pooling across firms or seeding from public LCA benchmark studies improves it. 1 ML engineer and 1 sustainability lead, 4 months.
**Data availability:** Firms that have done CALGreen or LEED LCAs hold the outputs; cost plans sit with cost consultants. Public benchmark studies give priors.
