# ML Opportunities — Grant Writers

**Industry:** [[grant-writers|Grant Writers]]
**Tags:** #bert #gradient-boosting #llm #binary-classification #regression #text-classification #text-generation #time-series-forecasting #change-point-detection #nlp #tabular-ml #tacit-knowledge-ml #revenue-impact #compliance

---

## 1. Grant-Organization Fit Prediction from RFP Analysis (Primary Opportunity — Tacit Knowledge ML)

#bert #gradient-boosting #binary-classification #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced grant writers read an RFP and intuitively assess whether an organization has a realistic chance of winning — recognizing signals in funder language, budget ceilings, review criteria weighting, and competitive landscape that take 5-10 years to develop. Junior writers and small nonprofits without this expertise waste 40-80 hours on proposals that never had a realistic chance, but the assessment criteria exist only as tacit pattern recognition in the heads of senior professionals.

**ML task:** Binary classification — predict whether an organization will be funded for a specific grant opportunity.

**Input data:** RFP text (parsed into structured fields: eligibility criteria, review criteria with weights, budget ceiling, program priorities, evaluation methodology), organization profile (mission statement, prior awards, budget size, geographic focus, program descriptions, key personnel CVs), and historical context (prior relationship with funder, number of previous applications, sector competitiveness metrics).

**Target:** Binary outcome: funded (1) or not funded (0). Secondary target: estimated reviewer score percentile for federal grants with available scoring data.

**Model:** Two-stage. BERT-based encoder processes RFP text and organization descriptions to produce semantic alignment embeddings across multiple dimensions (mission alignment, methodological match, capacity fit). These embeddings feed into a gradient-boosted classifier along with structured features (budget ratio, prior award count, funder-applicant history) to predict funding probability.

**Evaluation:** PR-AUC as primary metric given class imbalance (~15-25% positive rate). Calibration quality measured by Brier score — the probability estimates must be trustworthy for go/no-go decisions. Target: model-recommended proposals should have 30%+ win rate vs. 15% baseline.

**Scope:** High difficulty. 9-12 months to production. Requires NLP pipeline for RFP parsing, organization profiling, and outcome matching. Team: 2 ML engineers, 1 NLP specialist, 1 grant writing domain expert. Federal grants are the MVP target due to data availability; foundation grants require data partnerships.

**Data availability:** Federal grant outcomes are public (USAspending.gov, NIH Reporter, NSF Award Search) — millions of funded awards with organization profiles. The critical gap is losing proposals, which are not public. Proxy: treat all registered-but-unfunded organizations in SAM.gov for a given program as negative examples. Foundation data is available via Candid/990 filings but lacks the RFP text. Building a comprehensive training set requires partnering with 10-20 grant writing firms to access their historical win/loss data with associated RFPs.

---

## 2. Win Probability Estimation with Reviewer Score Prediction

#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** Federal grants are scored by peer reviewers on defined criteria (e.g., NIH uses Significance, Investigators, Innovation, Approach, Environment on a 1-9 scale). Writers cannot predict which criteria will differentiate their proposal from competitors, leading to uniform effort allocation rather than strategic emphasis.

**ML task:** Multi-output regression — predict reviewer scores for each criterion given the proposal text and organization profile.

**Input data:** Proposal full text (specific aims, research strategy, budget justification), organization profile, PI qualifications, preliminary data strength indicators, and program-specific features (study section, funding mechanism, resubmission status).

**Target:** Predicted score for each review criterion (1-9 scale for NIH, analogous scales for other agencies), plus overall impact score.

**Model:** BERT encoder for proposal text features combined with gradient-boosted regression for structured features. Trained on NIH summary statements (which include criterion-level scores for reviewed applications).

**Evaluation:** MAE per criterion, with focus on rank-order accuracy (does the model identify the weakest criterion correctly?). Target: MAE < 1.0 on 9-point scale, correct identification of the weakest criterion 60%+ of the time.

**Scope:** Moderate-high. NIH summary statements are available to applicants but not centrally archived — requires data collection partnerships with universities and research institutions willing to share. 6-9 months to MVP on NIH-specific model.

**Data availability:** Moderate. NIH summary statements include criterion scores but are only available to the applicant institution. A consortium of 20-50 institutions could provide thousands of training examples. NSF panel summaries are less structured but available through similar channels.

---

## 3. Funder Priority Shift Detection

#gradient-boosting #change-point-detection #tabular-ml #time-series-forecasting #nlp

**Problem statement:** Foundation and federal funding priorities shift gradually — a foundation that funded direct service programs for 10 years may pivot toward systems change or policy advocacy. Writers who don't detect these shifts waste proposals targeting last year's priorities.

**ML task:** Change-point detection on funder giving patterns, combined with text classification on annual reports and RFP language to identify priority shifts before they become explicit.

**Input data:** Historical award data per funder (amounts, topics, organization types, geographic focus) as time series. Funder communications: annual reports, blog posts, strategy documents, press releases, RFP language changes year-over-year.

**Target:** Binary change-point flag per funder per year, plus predicted new priority direction (emerging topics, shifted geographic focus, changed organization-size preferences).

**Model:** Time-series change-point detection (BOCPD or gradient-boosted with temporal features) on award pattern features, combined with BERT-based text classification on funder communications to classify emerging priority themes.

**Evaluation:** F1-score on change-point detection with 1-year lookahead. Precision is critical — a false positive wastes writer effort pursuing a perceived shift that didn't occur.

**Scope:** Moderate. 4-6 months to MVP. Training data from Candid's 990 filings (20+ years of foundation giving data) combined with foundation website scraping for communications. Team: 1 ML engineer, 1 NLP specialist.

**Data availability:** Strong for award data (Candid, 990 filings). Moderate for communications (requires web scraping of foundation websites, which vary widely in structure). Federal priority shifts are trackable through NOFO/RFA language changes, which are archived on Grants.gov.

---

## 4. Budget Reasonableness Scoring

#gradient-boosting #regression #tabular-ml #anomaly-detection

**Problem statement:** Grant budgets that are too high get rejected for unreasonableness; budgets that are too low signal lack of capacity. Writers struggle to calibrate budgets for unfamiliar program types or funders, and there's no systematic way to benchmark against successful proposals.

**ML task:** Regression — predict the optimal budget total and per-category allocation for a given grant program, scope of work, and organization size.

**Input data:** Historical funded award amounts by program, organization budget size, geographic cost-of-living adjustment, proposed scope (number of participants, duration, activities), and budget category breakdown (personnel, fringe, travel, equipment, supplies, contractual, indirect).

**Target:** Predicted total budget and per-category allocation, with confidence interval. Anomaly flag for budget items that deviate significantly from program norms.

**Model:** Gradient-boosted regression for total budget prediction. Isolation forest for anomaly detection on budget category proportions (flagging, e.g., "Your travel budget is 3x the median for this program — reviewers may question this").

**Evaluation:** MAE on total budget prediction (target: within 10% of funded amount). Anomaly detection precision: 80%+ of flagged items should be genuinely unusual when reviewed by an experienced grant writer.

**Scope:** Low-moderate. 3-5 months to MVP. Federal award data with budget breakdowns is available through FPDS and USAspending.gov. Team: 1 ML engineer.

**Data availability:** Strong for federal grants (USAspending.gov provides award amounts and some budget detail). Weak for category-level breakdowns, which require accessing individual award records. Foundation award amounts are available via 990 filings but without budget detail.

---

## 5. Narrative Quality and Persuasiveness Prediction

#bert #llm #text-classification #nlp #regression

**Problem statement:** Grant proposal quality varies enormously, but writers have no way to benchmark their narrative against successful proposals before submission. Peer review is time-consuming and expensive, and self-assessment is unreliable.

**ML task:** Regression — predict overall narrative quality score and per-section strength scores from proposal text.

**Input data:** Full proposal text segmented by section (significance, approach, evaluation, sustainability, etc.), plus metadata (grant program, funder type, resubmission status).

**Target:** Predicted quality score per section (calibrated to reviewer scoring scales), plus specific weakness flags (e.g., "evaluation plan lacks specificity," "sustainability section relies on vague future funding assumptions").

**Model:** Fine-tuned BERT or LLM-based model trained on proposal texts paired with reviewer scores and comments. Section-level models trained on section-specific scoring criteria for major federal agencies.

**Evaluation:** Spearman rank correlation between predicted and actual reviewer scores. Target: 0.6+ correlation, with correct identification of the weakest section 55%+ of the time.

**Scope:** High difficulty. The primary challenge is access to proposal text paired with reviewer scores — this data is extremely sensitive and not publicly available. Requires partnerships with universities and nonprofits willing to share deidentified proposals with scores. 9-12 months to production. Team: 2 ML engineers, 1 NLP specialist, 1 domain expert.

**Data availability:** Very limited. Proposal texts are confidential; reviewer scores are available only to applicants. A viable path is building a proprietary dataset through a freemium tool where writers voluntarily submit proposals for scoring, with outcomes tracked over time. This is a data flywheel business — the product improves with scale.
