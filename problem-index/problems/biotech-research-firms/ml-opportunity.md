# Machine Learning Opportunities — Biotech Research Firms

**Industry:** [[biotech-research-firms|Biotech Research Firms]]
**Derived from:** [[problems/biotech-research-firms/high-impact|High Impact]], [[problems/biotech-research-firms/low-impact-1|Low Impact 1]], [[problems/biotech-research-firms/low-impact-2|Low Impact 2]], [[problems/biotech-research-firms/worker-life-1|Worker Life 1]], [[problems/biotech-research-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Medicinal Chemist's Design Preferences
#tacit-knowledge-ml #graph-neural-networks #perceptron-and-mlps #contrastive-learning #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Senior medicinal chemists choose which designs to make each cycle using a feel for structure they cannot specify. The ML problem is to learn each programme's chemists' preferences from pairwise choices captured in the design meeting, rank new designs (including generative output) the way they would, and measure which preferences predict assay outcomes.

**ML task:** Learning to rank from pairwise preferences (Bradley–Terry-style objective on a molecular encoder), with a separate multi-task head predicting assay outcomes so preference and outcome can be compared
**Input data:** Candidate structures as molecular graphs and fingerprints; pairwise "which would you make?" choices with the prompt context (potency, solubility, synthesis) and chemist ID; the programme's registry of made compounds with potency, selectivity, ADME and early safety results; route-planning feasibility scores.
**Target:** Probability that chemist or team prefers design A over B under a stated criterion; downstream, predicted assay values for made compounds; agreement between preference rank and later measured outcome.
**Evaluation metric:** Pairwise AUROC on held-out choices, reported against the chemists' own test-retest agreement as the ceiling. Novartis's published study found κ ~0.6 within chemists and 0.32–0.40 between them, and reached ~0.75 AUROC. Second metric: enrichment of compounds that later met the programme's candidate criteria among top-ranked designs, measured prospectively. Missing a good design costs more than reviewing a poor one, so recall at the shortlist size matters more than precision.
**Scope:** The data collection challenge comes first: choices must be captured inside the design meeting at near-zero effort, as quick pairwise comparisons in the tool chemists already use, because historical meetings left no labels. The labelling challenge is that chemists change their own answer roughly one time in five (derived from κ ~0.6 on a two-way choice) and bundle several criteria into one choice, so prompts must name the criterion, a sample of pairs must be repeated to estimate intra-rater reliability, and per-chemist models should be kept alongside the team model. The deployment challenge is speed and explanation: the ranking must be ready before the meeting and show the nearest past compounds behind each judgement, or chemists ignore it. 2 ML engineers and 1 computational chemist embedded with two programmes, 6–9 months. The first value is retrieval ("designs like this failed solubility eleven times") before any ranker is trusted.
**Data availability:** Registries and assay data are clean at most biotechs that use an ELN. Preference labels do not exist and must be collected; Novartis released its annotated pairs and the MolSkill code, which give a pretrained starting point. Large pharma has the scale; a single biotech has two or three chemists, so cross-programme pooling within a CRO or a platform is the realistic route.

---

## 2. Toxicologic Pathology Lesion Detection and Severity Grading
#cnns #semantic-segmentation #transfer-learning #contrastive-learning #evaluation-metrics #compliance #worker-facing

**Problem statement:** A pathologist reads every tissue from every animal in a GLP toxicology study, records findings and assigns severity grades. The task is to pre-screen whole-slide images to flag tissues with probable findings and propose severity grades, so the pathologist confirms rather than searches.

**ML task:** Weakly supervised whole-slide classification (normal vs. finding) per tissue, segmentation of common lesion types, and ordinal severity regression
**Input data:** Scanned H&E whole-slide images from rodent and non-rodent studies; the pathologist's tabulated findings with tissue, lesion term (INHAND nomenclature) and severity; peer-review changes; study metadata (species, strain, sex, dose group).
**Target:** Per-tissue probability of any finding; lesion class; severity grade 1–5.
**Evaluation metric:** Sensitivity on tissues with findings at a fixed specificity, because a missed lesion in a high-dose group can change a NOAEL and therefore the starting clinical dose. Severity grading is scored by weighted κ against the study pathologist and against the peer reviewer, with pathologist–peer-reviewer agreement as the ceiling.
**Scope:** Control-group tissues are abundant and make a strong normal baseline. Rare lesions are the hard tail. GLP use requires the system to be validated and the pathologist to remain the decision-maker, and no formal standard yet exists for judging AI slide analysis in nonclinical pathology. 3 engineers plus a pathologist lead, 9–12 months to a validated screening aid for two species.
**Data availability:** Slides and findings sit at CROs and sponsors. Each study belongs to its sponsor, so pooling needs consent agreements or must train on control groups and historical data the CRO may use.

---

## 3. Dose-Response Curve Triage for Assay Data
#gradient-boosting #bayesian-inference #maximum-likelihood-estimation #hypothesis-testing #evaluation-metrics #automation #quick-win

**Problem statement:** Classify every dose-response curve from plate-based assays as acceptable, flat, bell-shaped, incomplete or artefactual, propose well masks, and fit potency with honest uncertainty, so scientists review only the curves that need judgement.

**ML task:** Multiclass classification of curve shape plus Bayesian four-parameter logistic fitting with outlier-robust likelihood
**Input data:** Raw plate-reader values with plate maps; control wells; historical curves with scientists' masks, refits and final reported values; compound solubility and assay metadata.
**Target:** Curve class; recommended masked wells; IC50/EC50 with credible interval.
**Evaluation metric:** Agreement with expert curve review at the auto-accept threshold, with the rate of auto-accepted curves later overturned as the safety metric; calibration of the credible intervals against replicate measurements.
**Scope:** Labels already exist in every registry that records masks and refits. 1 data scientist and 1 engineer, 3 months to production for one assay family.
**Data availability:** Internal and plentiful at any biotech running assays weekly; masks are often stored but the reasons are not, and should be captured going forward.

---

## 4. CRO Report and Dataset Extraction Into Sponsor Records
#large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #data-integration #automation

**Problem statement:** Extract results, conditions and identifiers from heterogeneous CRO deliverables into structured records linked to the sponsor's compounds and batches, and check them against the study's own SEND data where it exists.

**ML task:** Document understanding (tables in PDFs and images) with schema mapping and entity resolution of compound, batch and sample identifiers
**Input data:** CRO final and interim reports, Excel deliverables, SEND datasets, the sponsor's registry, prior manually curated records as supervision.
**Target:** Structured result rows (assay, condition, value, unit, compound, batch, study) with provenance and confidence.
**Evaluation metric:** Field-level accuracy at the auto-write threshold, with zero tolerance for silent identifier errors: a confident wrong batch link is worse than a blank. Secondary metric: time from deliverable to queryable record.
**Scope:** Prior curated records provide supervision; vendor layouts vary and drift. 2 engineers, 4 months for the five most common deliverable types.
**Data availability:** Sponsors own their deliverables, so there is no access barrier for a sponsor-side tool. Cross-sponsor training would need consent.

---

## 5. GLP Study Slippage Forecasting
#survival-analysis #gradient-boosting #feature-engineering #confidence-intervals #evaluation-metrics #workflow-orchestration

**Problem statement:** Predict which GLP studies will deliver their draft report late, and by how much, while there is still time to act, from the study's design, events and resourcing.

**ML task:** Time-to-event modelling of report delivery with time-varying covariates
**Input data:** Study type, species and duration; protocol amendment and deviation counts; QA finding counts and response times; pathology queue length; study director portfolio size; sponsor comment rounds; historical study timelines.
**Target:** Days from planned to actual draft and final report.
**Evaluation metric:** Concordance index and calibration of the predicted probability of missing the promised date at each study milestone. Recall on studies that slip more than two weeks is the operational metric, because those are the ones that move a sponsor's IND date.
**Scope:** CROs hold years of study timelines in their scheduling and study management systems. 1 data scientist, 3–4 months.
**Data availability:** Internal to each CRO; timelines are operational data rather than sponsor study data, which keeps it clear of the ownership restrictions on results.
