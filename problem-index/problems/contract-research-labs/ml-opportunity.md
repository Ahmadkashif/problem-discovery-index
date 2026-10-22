# Machine Learning Opportunities — Contract Research Labs

**Industry:** [[contract-research-labs|Contract Research Labs]]
**Derived from:** [[problems/contract-research-labs/high-impact|High Impact]], [[problems/contract-research-labs/low-impact-1|Low Impact 1]], [[problems/contract-research-labs/low-impact-2|Low Impact 2]], [[problems/contract-research-labs/worker-life-1|Worker Life 1]], [[problems/contract-research-labs/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Investigator's Effort and Feasibility Read
#tacit-knowledge-ml #gradient-boosting #large-language-models #survival-analysis #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced principal investigators read a technical approach and "know" it is an eight-month problem dressed as four, or that a milestone will slip because the material will not cooperate until the third route — a judgement formed over decades of projects that juniors lack and that leaves at retirement. The ML problem is to learn that read from the firm's own history of estimates and outcomes and give every PI a calibrated second opinion before the price is fixed.

**ML task:** Regression of the ratio of actual to estimated hours per technical task, plus time-to-milestone survival modelling, conditioned on the task description, the team and the sponsor
**Input data:** Basis-of-estimate spreadsheets and the technical approach sections of past proposals; the firm's timekeeping records by contract, task and labour category; milestone and final reports; contract modifications and scope changes; LLM-extracted features from task descriptions (novelty of the material or method, whether a prior project used it, number of interfaces with other tasks, dependence on outside facilities).
**Target:** Actual-to-estimated hours ratio per task; whether and when each stated milestone was met; and agreement between the model's flag and senior PIs' own blind ratings of the same estimates.
**Evaluation metric:** Calibration and interval coverage of the predicted overrun ratio, measured strictly out of time on later projects — random splits leak the firm's evolving practice. For milestones, concordance index and Brier score at the stated milestone date. Missing a large overrun matters more than over-warning, because a firm-fixed-price overrun comes straight out of a thin margin; report recall on overruns above 50%. The ceiling for agreement with experts is their own test-retest agreement on repeated estimates.
**Scope:** The data collection challenge comes first: hours are charged by contract line rather than by technical task, so historical estimates must be aligned to actuals by hand or with LLM-assisted mapping, and future estimates need a capture step that costs the PI seconds, not minutes. The labelling challenge is that experts disagree with themselves — the same PI estimates the same kind of task differently after a recent overrun — and that an overrun can be a scope change rather than a bad estimate, so a sample needs repeated blind estimation and change orders must be separated from estimate error. The deployment challenge is speed and trust: the flag must appear while the PI is building the estimate, cite the closest past tasks and their outcomes, and run inside the firm's enclave because defense task descriptions are often controlled. 1 ML engineer and 1 analyst with a senior PI as domain lead, 6–9 months for a 100-person firm with five or more years of records; retrieval of similar past tasks delivers value before any regressor is trusted.
**Data availability:** Every firm holds its own proposals, timesheets and reports, usually in three disconnected systems. Mid-size firms with ten years of cost-type work have thousands of task-level comparisons once aligned; small firms have too few and need a pooled or vendor model, which export control and sponsor confidentiality make hard.

---

## 2. Topic Triage and Award Probability from Public Award History
#word-embeddings #transformers #logistic-regression #k-nearest-neighbors #evaluation-metrics #revenue-impact

**Problem statement:** Given a new solicitation topic and a firm's capability record, estimate the probability that this firm wins if it bids, so a firm facing per-firm proposal caps from FY2027 spends its allowance on the topics it can convert.

**ML task:** Retrieval of similar past topics and awards by embedding similarity, followed by a calibrated binary classifier of award given bid
**Input data:** Public SBIR/STTR award records (DoD alone made 34,704 awards to 6,093 firms over FY2012–2023), topic texts and agency, the firm's own submissions with win/loss outcomes and debrief notes, and features such as incumbent presence (prior awards on near-identical topics), topic-author office, and overlap between topic language and the firm's past reports.
**Target:** Award or no award for each submitted proposal; secondarily, Phase II award following Phase I.
**Evaluation metric:** Brier score and calibration by decile, plus the win rate of the top-k topics the model recommends against the firm's historical selection at the same proposal count. Because only bid topics have outcomes, report results with inverse-propensity weighting for the firm's past selection behaviour.
**Scope:** Public award data gives the "who wins this kind of topic" signal for free; losing proposals are invisible publicly, so firm-level outcome data is essential. 1 data scientist, 3–4 months to a useful ranking; Phase I-to-Phase II linkage is unreliable in SBA data (the National Academies says so), so that label needs the firm's own records.
**Data availability:** Awards and topics are public. A firm's losses and debriefs are private and short — tens to low hundreds of proposals — so the model should borrow strength from public award patterns.

---

## 3. Instance Segmentation of Nanoparticles in Electron Micrographs
#cnns #semantic-segmentation #object-detection #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Replace hand-tracing of touching and overlapping particles in TEM and SEM images with a model that outlines each particle and produces size and shape distributions a sponsor will accept.

**ML task:** Instance segmentation (star-convex or mask-based) with uncertainty flags for unsplittable agglomerates
**Input data:** Micrographs at several magnifications from the lab's instruments, with scale bars and acquisition metadata; a few dozen images per material class annotated by the lab's own staff; corrections captured during review.
**Target:** Per-particle masks, equivalent diameters and shape descriptors; flagged regions requiring human review.
**Evaluation metric:** Instance-level F1 at an IoU threshold, and — the measure sponsors care about — agreement of the resulting size distribution with expert manual counts (difference in median and spread, Kolmogorov–Smirnov distance). Under-segmentation of agglomerates biases sizes upward, so report it separately.
**Scope:** Published work reached about 85% F1 with 30–40 annotated TEM images using a U-Net-based model, so the build is modest: 1 ML engineer, 2–3 months for a first material class, then incremental per class. The hard part is the review loop and versioned traceability for reports.
**Data availability:** Every materials lab has thousands of unannotated micrographs; annotation is the cost, and the lab's own scientists are the only qualified annotators.

---

## 4. Funding-Provenance and Export-Sensitivity Classification for Deliverables
#bert #transformers #large-language-models #evaluation-metrics #compliance #automation

**Problem statement:** For every section, figure and table in a deliverable, predict which funding source generated it and whether it carries export-control or CUI sensitivity, so the right data-rights legend, distribution statement and warning are applied before it leaves the firm.

**ML task:** Passage- and figure-level multi-class classification of funding provenance, plus binary classification of export-control sensitivity, with retrieval against the firm's prior reports
**Input data:** Past deliverables with their applied legends; contract data-rights clauses and funding records; internal R&D reports; the firm's technology control plan; contracts staff review decisions.
**Target:** Funding source per passage (specific award, internal R&D, private commercial work), required legend and distribution statement, export-sensitivity flag.
**Evaluation metric:** Recall on passages that needed a protective legend and did not get one is the binding metric — a missed legend can forfeit rights for years, while a false flag costs a reviewer a minute. Measure reviewer time per deliverable before and after.
**Scope:** Labels come from historical deliverables and contracts staff decisions; provenance is easier when the system can trace text reuse back to earlier documents. 1 ML engineer and a contracts lead, 4–5 months. The model proposes and logs; a person approves every outgoing deliverable.
**Data availability:** Held entirely by each firm; marking practice has been inconsistent, so historical labels need a cleanup pass by the contracts team.

---

## 5. Closed-Loop Experiment Planning for Nanomaterial Synthesis
#bayesian-optimization #gaussian-processes #feature-engineering #evaluation-metrics #automation

**Problem statement:** Choose the next synthesis or deposition run — temperatures, precursor ratios, times, annealing steps — to reach a target property (particle size, coating thickness, conductivity) in fewer experiments than a scientist's one-variable-at-a-time search.

**ML task:** Sequential experimental design by Bayesian optimisation over a Gaussian-process surrogate, with constraints for safety and instrument limits
**Input data:** The lab's historical run logs (parameters, instrument settings, outcomes from characterisation), prior literature values, and each new run's measured result — ideally fed straight from the segmentation pipeline in entry 3.
**Target:** Measured property per run; recommended next run with expected improvement.
**Evaluation metric:** Number of runs to reach the target specification against the lab's historical campaigns on comparable problems; simple regret after a fixed budget of runs.
**Scope:** The optimisation is well understood; the barrier is clean run logs, because parameters live in paper notebooks and instrument PCs. 1 research engineer, 3 months for one synthesis route, with value proportional to the cost of each run.
**Data availability:** Run histories exist in notebooks and are rarely digitised; sponsors may own results generated on their contracts, which limits reuse across projects.
