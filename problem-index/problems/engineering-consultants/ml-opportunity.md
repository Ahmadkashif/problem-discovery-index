# Machine Learning Opportunities — Engineering Consultants

**Industry:** [[engineering-consultants|Engineering Consultants]]
**Derived from:** [[problems/engineering-consultants/high-impact|High Impact]], [[problems/engineering-consultants/low-impact-1|Low Impact 1]], [[problems/engineering-consultants/low-impact-2|Low Impact 2]], [[problems/engineering-consultants/worker-life-1|Worker Life 1]], [[problems/engineering-consultants/worker-life-2|Worker Life 2]]

---

## 1. Project Scope Creep Detection from Communication Patterns
#gradient-boosting #feature-engineering #cross-validation #evaluation-metrics #bert #word-embeddings #conditional-probability-and-bayes-theorem #bias-variance-tradeoff #gradient-descent #tacit-knowledge-ml

**Problem statement:** Experienced PEs and project managers develop an instinct for when a project is heading toward scope creep — they read the pattern of client emails increasing in frequency, the "one more thing" requests that individually seem small, the design review meetings that keep reopening settled decisions. A senior PM knows two weeks into a project whether the scope is going to hold or blow up. Junior PMs don't recognize the pattern until the budget is already spent. This intuition from running hundreds of projects is the most valuable tacit knowledge in engineering consulting, and it can be encoded into a model that flags at-risk projects from communication and meeting metadata.

**ML task:** Binary classification (scope creep risk vs. on-track) from multi-modal communication features
**Input data:** Project communication metadata — email thread counts, frequency, reply latency, and word counts per week between firm and client; meeting minutes with reopened-item flags; RFI and change request logs; client feedback sentiment extracted via NLP from email bodies. Sourced from Deltek Vantagepoint project records, BST Global workflow data, Newforma project information management logs, and email/calendar integrations (Outlook, Google Workspace).
**Target:** Binary label: project experienced >5% scope creep (measured as uncompensated additional scope hours relative to contracted fee) within 60 days of the prediction window. Secondary regression target: predicted magnitude of scope creep as a percentage of contracted fee.
**Evaluation metric:** Precision-recall AUC with recall weighted 2x — missing a project that is about to blow its scope is far more expensive than a false alarm that prompts a PM to review a healthy project. F2-score as the summary metric. Calibrated probability outputs are essential so PMs can triage by risk level.
**Scope:** Requires 3+ years of historical project data from a mid-size firm (100+ completed projects) with email metadata and project financials linked at the project level. A 2-person team (ML engineer + data engineer for the email/calendar integration pipeline) needs 10-14 weeks. The hardest part is feature engineering from communication patterns — building reliable signals from email frequency curves, meeting cadence changes, and NLP-extracted sentiment from client correspondence. Start with a single office or discipline to control for cultural communication norms. The labeling challenge is real: senior PMs may disagree on when scope creep "started" versus when it became visible, so ground truth should be tied to financial outcomes (uncompensated hours) rather than subjective PM judgment.
**Data availability:** Medium-low. The raw data exists across email servers, Deltek Vantagepoint or BST Global project records, and Newforma document logs, but it has never been joined into a single training dataset. Email metadata requires IT cooperation and privacy review. The labeling is straightforward once you define scope creep financially — every firm tracks actual vs. budgeted hours at project closeout. The deployment challenge is that the model must surface warnings early enough (2-4 weeks before budget impact) to be actionable, which means the communication pattern features must be predictive well before the financial signals confirm the problem.

---

## 2. Project Budget Burn Rate Anomaly Detection
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #bias-variance-tradeoff #gradient-descent #revenue-impact

**Problem statement:** Detect projects whose labor burn rate is deviating from expected trajectories early enough for PMs to intervene with scope renegotiation or change orders, rather than discovering margin loss at project closeout.

**ML task:** Anomaly detection on time-series burn curves + regression to predict final cost-at-completion
**Input data:** Historical timesheet records per project (hours by person, discipline, phase, week), contract fee schedules, project metadata (type, size, client, duration), milestone completion dates. Sourced from Deltek/Ajera/BST exports and timesheet systems.
**Target:** Binary flag for "project at risk of >10% fee overrun" at each weekly checkpoint, plus continuous prediction of final cost-at-completion as a percentage of contracted fee.
**Evaluation metric:** Precision-recall AUC on the at-risk flag, with recall weighted 2x (missing an at-risk project is costlier than a false alarm). MAE on cost-at-completion regression.
**Scope:** Requires 2-3 years of historical project data from a firm with 50+ completed projects to establish baseline burn curves by project type. A single ML engineer can build and validate the model in 8-12 weeks. The main challenge is data cleaning — timesheet data is notoriously messy with miscoded phases and retroactive corrections. Start with one project type (e.g., site civil) before generalizing.
**Data availability:** Medium. Firms using Deltek or Ajera have the raw data but it requires significant cleaning. Smaller firms on spreadsheets will need a data ingestion pipeline. Labeling is straightforward — the "ground truth" is the final project P&L, which every firm tracks.

---

## 3. RFP Win Probability Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #maximum-likelihood-estimation #conditional-probability-and-bayes-theorem #revenue-impact

**Problem statement:** Predict the probability of winning an RFP based on firm qualifications, past relationship with the client, project characteristics, and competitive landscape, enabling principals to allocate pursuit effort to the highest-probability opportunities.

**ML task:** Binary classification (win/loss)
**Input data:** Historical RFP pursuit records including: project type, estimated fee, client name, whether the firm had prior work with the client, number of competing firms (if known), team proposed (PE count, years of experience), geographic match (firm office vs. project location), whether the firm was shortlisted, and proposal score if available. Sourced from CRM systems (Cosential/Unanet) or pursuit tracking spreadsheets.
**Target:** Binary label: won or lost the pursuit.
**Evaluation metric:** AUC-ROC as primary metric; calibrated probability outputs are critical since the goal is ranking pursuits, not just classification. Log loss as secondary metric to penalize overconfident wrong predictions.
**Scope:** Requires 200+ historical pursuit records with outcome labels for a meaningful model. A single data scientist can build this in 6-8 weeks. The main challenge is that most small firms track pursuits inconsistently — some in CRM, some in spreadsheets, some not at all. Feature engineering around "relationship strength" (prior project count, years since last project with client) is key.
**Data availability:** Low-medium. Firms with Deltek CRM or Cosential have structured data; others will need to reconstruct pursuit history from proposal folders and principal memory. Win/loss labels are easy — firms know which proposals they won.

---

## 4. Resource Utilization Forecasting
#linear-regression #time-series-forecasting #exponential-smoothing #feature-engineering #evaluation-metrics #expectation-variance-covariance #probability-distributions #automation

**Problem statement:** Forecast staff utilization rates 4-8 weeks ahead by discipline, enabling principals to identify underutilization before it erodes margins and overutilization before it causes burnout and missed deadlines.

**ML task:** Time-series regression per employee/discipline
**Input data:** Weekly timesheet data (billable hours, overhead hours, PTO) per employee over 2+ years, project schedules with planned start/end dates and staffing plans, pipeline data (proposals submitted, expected start dates, probability-weighted fee). Sourced from timesheet and project management systems.
**Target:** Predicted billable utilization rate (billable hours / available hours) per employee and per discipline for each of the next 4-8 weeks.
**Evaluation metric:** MAE on weekly utilization rate predictions; business-relevant threshold is ±5 percentage points (e.g., predicting 78% when actual is 73% is acceptable; predicting 78% when actual is 55% is not).
**Scope:** Simpler model than burn rate anomaly detection — can start with linear regression on historical utilization patterns plus known project schedules. 4-6 weeks of development for an ML engineer. The key difficulty is incorporating pipeline uncertainty — projects that are "expected to start next month" frequently slip. A probabilistic approach weighting pipeline projects by win probability (from model #2) significantly improves forecasts.
**Data availability:** High for firms with consistent timesheet systems. The critical gap is reliable forward-looking project schedule data — many firms manage schedules in principals' heads rather than in systems.

---

## 5. Drawing Review Automated Markup Detection
#cnns #object-detection #transfer-learning #loss-functions #backpropagation #evaluation-metrics #matrix-algebra #gradient-descent #automation

**Problem statement:** Detect and classify markups, redlines, and revision clouds on engineering drawing PDFs to automate the review-response cycle, replacing manual scanning of 200+ sheet drawing sets for reviewer comments.

**ML task:** Object detection + classification on rasterized drawing sheets
**Input data:** Scanned or digitally-exported PDF sheets with reviewer markups — redline annotations, cloud/bubble callouts, text comments, strike-throughs, and dimension corrections. Training data sourced from archived review sets across multiple project types (structural, civil, MEP). Each markup needs a bounding box and category label.
**Target:** Bounding boxes around each markup with classification into categories: dimension change, detail revision, note addition, general comment, code compliance flag, constructability concern. Extract associated text where legible.
**Evaluation metric:** mAP@0.5 for detection; macro F1 for category classification. Recall is more important than precision — missing a markup that requires a design change is worse than flagging a false positive.
**Scope:** Requires a labeled dataset of 2,000-5,000 marked-up drawing sheets with bounding box annotations — this is the main bottleneck. A 2-person team (ML engineer + domain expert for labeling) needs 12-16 weeks. Transfer learning from document layout detection models (e.g., LayoutLMv3, YOLO fine-tuned on technical drawings) reduces the data requirement. Start with one discipline (structural details, which have the most standardized markup conventions) before expanding.
**Data availability:** Medium. Every engineering firm has archived review sets, but they are stored as PDFs in project folders with no structured labeling. The labeling effort is significant — a domain expert needs to annotate bounding boxes and categories. Crowdsourced labeling is not viable because annotators need engineering drawing literacy.
