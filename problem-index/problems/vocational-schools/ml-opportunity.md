# Machine Learning Opportunities — Vocational Schools

**Industry:** [[vocational-schools|Vocational Schools]]
**Derived from:** [[problems/vocational-schools/high-impact|High Impact]], [[problems/vocational-schools/low-impact-1|Low Impact 1]], [[problems/vocational-schools/low-impact-2|Low Impact 2]], [[problems/vocational-schools/worker-life-1|Worker Life 1]], [[problems/vocational-schools/worker-life-2|Worker Life 2]]

---

## 1. Hands-On Skill Proficiency Assessment from Performance Observation
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced trade instructors watch a student perform a task — welding a joint, wiring a panel, bending conduit, cutting tile — and know within seconds whether the work is job-ready. This judgment integrates visual cues (bead consistency, wire routing symmetry, cut straightness), body mechanics (hand steadiness, posture, tool angle), and process adherence (sequence of operations, safety compliance) into a holistic assessment the instructor cannot fully articulate. The goal is to capture this tacit evaluation in a vision model that provides consistent, explainable competency scores.

**ML task:** Multiclass classification (per-competency dimension: acceptable / marginal / unacceptable) from video frames or short clips of student work and work products
**Input data:** Overhead or workstation-mounted camera feeds capturing (a) the work product in progress and completed state (e.g., weld bead, wired panel, plumbing joint) and (b) the student's hand/tool positioning during execution. Still frames of completed work products for post-hoc grading. Metadata: trade type, specific task, student experience level.
**Target:** Multi-label multiclass scores across 3-6 competency dimensions per trade (e.g., for welding: bead appearance, penetration quality, undercut presence, porosity, body position). Each dimension classified as acceptable/marginal/unacceptable. Ground truth from expert instructor consensus labels (minimum 3 instructors labeling each sample to handle disagreement).
**Evaluation metric:** Cohen's kappa (inter-rater agreement between model and expert consensus), with a target of kappa > 0.70 matching the agreement level between experienced instructors themselves. Secondary metric: per-dimension accuracy, with higher weight on safety-critical dimensions (e.g., structural weld integrity > cosmetic appearance).
**Scope:** This is a hard, multi-year project requiring trade-specific model development. Start with one high-volume trade (welding is ideal: visual signal is strong, existing AWS inspection standards provide partial label structure). Initial dataset: 5,000+ labeled work product images from 3+ schools, with 3-instructor consensus labels. Requires CV/ML engineer, domain expert (master instructor), and 6-9 months for MVP on a single trade. Each additional trade is a new data collection and fine-tuning effort.
**Data availability:** Data collection is the primary bottleneck. Schools don't currently capture video of student work; cameras must be installed. Labeling requires compensating experienced instructors ($50-100/hr) for structured evaluation sessions. The labeling challenge is acute: instructors may disagree with themselves when re-grading the same work weeks later (test-retest reliability of ~0.75 for subjective assessments). AWS, NCCER, and trade certification bodies have some standardized visual inspection criteria that can anchor label definitions, but the tacit component — body mechanics, process fluency — has no existing label schema and must be developed from scratch.

---

## 2. Student Completion Risk Prediction
#gradient-boosting #binary-classification #tabular-ml #quick-win

**Problem statement:** Vocational programs have 30-50% dropout rates, with most attrition occurring in the first 6 weeks. Schools need early warning to intervene with tutoring, schedule adjustments, or financial aid counseling before a student disappears.

**ML task:** Binary classification (will complete program: yes/no) with rolling prediction updated weekly
**Input data:** Structured tabular features from SIS: attendance rate (daily), grade trajectory (weekly assessments), financial aid status and balance, commute distance, program type, enrollment pathway (direct vs. referral), demographics, prior education, hands-on vs. theory grade differential. Time-series features: attendance trend slope, grade velocity, engagement decay rate.
**Target:** Binary label: completed program (graduated or earned credential) vs. did not complete (withdrew, failed out, transferred). Labeled from historical cohort data (most schools have 3-5 years).
**Evaluation metric:** Recall at 80% precision — the cost of missing an at-risk student (lost tuition + lower placement rates) far exceeds the cost of unnecessary intervention (a check-in conversation). AUC-ROC as a secondary ranking metric.
**Scope:** Achievable quick win. 2-3 months with a single ML engineer and access to 3+ years of SIS export data. Gradient-boosted trees (XGBoost/LightGBM) on tabular features will outperform more complex approaches given small dataset sizes (500-2,000 students per school). Feature engineering is the key effort — particularly attendance pattern features and financial stress proxies.
**Data availability:** SIS systems export attendance and grade data readily (CSV/API). Financial aid data is more sensitive (FERPA) but available internally. Historical completion labels are straightforward. Main challenge is sample size: individual schools may have only 500-1,500 students per year, so a multi-school consortium approach significantly improves model quality.

---

## 3. Employer-Student Match Scoring
#gradient-boosting #ranking #tabular-ml #data-integration

**Problem statement:** Career services coordinators match graduates to employers based on geography and program completion — missing fit signals like specific skill strengths, employer culture, shift preferences, transportation access, and historical retention patterns. The result is poor matches that don't stick: 20-30% of placements fail within 90 days.

**ML task:** Learning-to-rank (rank employers for each graduating student by predicted placement success and 90-day retention)
**Input data:** Student features: competency scores by skill area, attendance reliability, commute radius, shift availability, career interests survey, instructor soft-skill ratings. Employer features: company size, trade specialty, historical hire-to-retention ratio from this school, wage offered, shift patterns, location, time since last hire. Interaction features: student skill profile similarity to previously successful placements at that employer, geographic distance, program-to-job alignment score.
**Target:** Ranked list of employers per student, with ground truth from historical placement-and-retention data (placed + retained 90 days = positive, placed + churned < 90 days = weak positive, not placed = unlabeled). Pairwise ranking labels derived from retention outcomes.
**Evaluation metric:** NDCG@5 (normalized discounted cumulative gain for top-5 employer recommendations). Secondary: 90-day retention rate for model-recommended vs. coordinator-selected placements (A/B test after deployment).
**Scope:** Medium complexity, 4-6 months. Requires integrating SIS student data with employer CRM data — the integration work is 60% of the effort. LambdaMART or gradient-boosted ranking model. Needs 2+ years of historical placement data with retention outcomes. Team: 1 ML engineer, 1 data engineer for integrations, career services domain expert.
**Data availability:** Student academic data is available from SIS. Employer data is the weak link — most schools track employer contacts in spreadsheets with inconsistent fields. Historical placement outcomes (who was placed where, retention duration) often exist in career services spreadsheets but are messy, incomplete, and unstandardized. A 3-6 month data cleanup and structuring effort is required before model training can begin.

---

## 4. Curriculum Effectiveness Analysis from Placement Outcomes
#bert #text-classification #regression #nlp #tabular-ml

**Problem statement:** Program directors cannot answer "which curriculum changes actually improved employment outcomes?" because there's no structured link between specific course content, student competency development, and post-graduation placement success. Curriculum changes are made based on anecdote and evaluated by vibes.

**ML task:** (a) NLP text classification to extract skill entities from job postings and map them to curriculum competencies; (b) Regression to model the relationship between curriculum feature changes and placement outcome changes over time
**Input data:** (a) Job posting text from Indeed, ZipRecruiter, and employer-direct feeds filtered by trade, geography, and recency. School curriculum documents: course syllabi, learning outcomes, competency checklists. (b) Tabular: curriculum version history (what changed when), cohort-level placement rates, employer satisfaction survey scores, time-to-placement, wage at placement.
**Target:** (a) Skill-to-competency alignment matrix: for each curriculum competency, how many active job postings require it (demand score) and how well student performance on that competency predicts placement (predictive value score). (b) Regression target: cohort placement rate as a function of curriculum features (courses offered, hours allocated per skill area, certification prep included).
**Evaluation metric:** (a) F1 score for skill extraction NER against manually labeled job posting sample. Spearman correlation between model-generated demand scores and program director expert rankings. (b) MAE on held-out cohort placement rate predictions; feature importance analysis is more valuable than prediction accuracy for this use case.
**Scope:** 6-9 month project combining NLP and tabular ML. The NLP skill extraction component can bootstrap from existing taxonomies (ONET skill classifications, NCCER competency frameworks) and fine-tune BERT on trade-specific job posting language. The regression component requires 5+ years of cohort data with curriculum version tracking — many schools don't have clean records of what changed when. Team: 1 NLP engineer, 1 data analyst, program director advisory input.
**Data availability:** Job posting data is commercially available (Lightcast/EMSI APIs, $15-30K/year). Curriculum documents exist but are unstructured (Word docs, PDFs). The biggest gap is curriculum version history: most schools don't systematically track which syllabus version each cohort received, requiring retrospective reconstruction from program director interviews and archived documents.
