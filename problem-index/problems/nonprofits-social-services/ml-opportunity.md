# Machine Learning Opportunities — Social Services Nonprofits

**Industry:** [[nonprofits-social-services|Social Services Nonprofits]]
**Derived from:** [[problems/nonprofits-social-services/high-impact|High Impact]], [[problems/nonprofits-social-services/low-impact-1|Low Impact 1]], [[problems/nonprofits-social-services/low-impact-2|Low Impact 2]], [[problems/nonprofits-social-services/worker-life-1|Worker Life 1]], [[problems/nonprofits-social-services/worker-life-2|Worker Life 2]]

---

## 1. Client Needs Assessment from Intake Conversations (Tacit Knowledge ML)
#gradient-boosting #bert #multiclass-classification #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced case managers read a client's intake narrative — what they say, how they say it, what they omit — and identify underlying needs the client hasn't explicitly stated. A client requesting help with utility bills may actually be facing eviction; a client describing "family stress" may be experiencing domestic violence; a client minimizing substance use may need immediate referral to treatment. This pattern recognition develops over years of practice and is the difference between a new case manager who takes the presenting problem at face value and a veteran who reads between the lines.

**ML task:** Multi-label classification on intake text + structured intake data to predict the full set of service needs (housing instability, substance use disorder, domestic violence, mental health crisis, food insecurity, employment barriers, legal issues, child welfare risk) beyond the client's self-reported presenting problem.

**Input data:** Free-text intake narratives (case manager notes from initial assessment), structured intake form fields (demographics, self-reported needs, referral source, prior service history), and optionally audio features from recorded intake conversations (speech rate, pause patterns, affect).

**Target:** Multi-label binary vector across 12-15 standardized need categories, where positive labels indicate needs the client has but did not explicitly present with. Ground truth comes from retrospective labeling: compare needs identified at intake vs. needs confirmed through subsequent service delivery over 6 months.

**Evaluation metric:** Recall-weighted F1 across need categories, with recall prioritized over precision because a missed domestic violence flag is far more dangerous than a false positive that triggers an unnecessary screening conversation. Per-category AUC-ROC to identify which needs the model captures well vs. poorly.

**Scope:** Requires partnership with 3-5 large social services agencies (200+ case managers) to access historical intake records with 6-month follow-up data. BERT-based text encoder for intake narratives combined with gradient-boosted trees for structured fields. Labeling requires experienced case managers to retrospectively annotate whether each need was present but unstated at intake — expect 60-70% inter-annotator agreement on ambiguous cases (substance use, DV), requiring adjudication protocols. Team of 2 ML engineers + 1 domain expert, 9-12 month build including data collection and annotation.

**Data availability:** Moderate difficulty. Intake narratives exist in case management systems (Apricot, ETO, Penelope) but are often poorly structured free text with inconsistent quality. The critical labeling challenge is that the "ground truth" — what needs the client actually had — only emerges over months of service delivery and may never be fully documented. Experienced case managers may disagree with each other on retrospective labels because their tacit knowledge is partially intuitive and context-dependent.

---

## 2. Program Outcome Prediction
#gradient-boosting #causal-inference #tabular-ml #revenue-impact

**Problem statement:** Predict whether a specific client will achieve the target outcome for a given program (e.g., stable housing at 12 months, employment at 6 months, sobriety at 90 days) based on their characteristics at enrollment, enabling better resource allocation and honest effectiveness reporting.

**ML task:** Binary classification per program-outcome pair, with causal adjustment via propensity score weighting to estimate treatment effects rather than just individual predictions.

**Input data:** Client demographics, intake assessment scores (VI-SPDAT, PHQ-9, AUDIT-C), prior service history, program enrollment details (dosage, attendance pattern, case manager assignment), neighborhood-level features (housing market tightness, unemployment rate, public transit access), and partner referral data.

**Target:** Binary outcome achieved/not-achieved at the program-defined time horizon. Secondary target: time-to-outcome for survival analysis framing (days to stable housing, days to employment).

**Evaluation metric:** AUC-ROC for individual prediction; Average Treatment Effect (ATE) and Conditional Average Treatment Effect (CATE) estimates with bootstrap confidence intervals for program effectiveness. Calibration is critical — predicted probabilities must match observed rates so program directors can trust the numbers.

**Scope:** Requires HMIS data linked with program-level enrollment and outcome records. Propensity score models need careful feature engineering to address selection bias (clients who enroll in intensive programs differ systematically from those who don't). Team of 2 ML engineers + 1 statistician with causal inference experience, 6-9 month build. The hardest part is data linkage across systems, not the modeling itself.

**Data availability:** HMIS data is standardized and available through local Continuum of Care agencies, but access requires data-sharing agreements that take 3-6 months to negotiate. Program-level outcome data quality varies enormously — some programs track outcomes rigorously, others use inconsistent definitions or stop tracking after the grant period ends.

---

## 3. Donor Lapse Prediction
#gradient-boosting #survival-analysis #tabular-ml #worker-facing

**Problem statement:** Predict which donors in a nonprofit's portfolio are at risk of lapsing (ceasing giving entirely) within the next 6 months, enabling proactive stewardship before the relationship deteriorates beyond recovery.

**ML task:** Survival analysis / time-to-event prediction, framed as the hazard of donor lapse given their engagement trajectory. Secondary framing as binary classification (will this donor lapse in the next 180 days?).

**Input data:** Giving history (amount, frequency, recency, gift designation, giving channel), email engagement metrics (open rate, click rate, unsubscribe signals), event attendance history, communication log entries (personal meetings, phone calls, handwritten notes), wealth screening data if available, and seasonal giving patterns (year-end surge donors vs. monthly givers).

**Target:** Binary lapse indicator at 6-month horizon, where lapse is defined as no gift within 180 days for a donor whose prior giving pattern predicted at least one gift in that window. For survival analysis framing: time from last gift to confirmed lapse or right-censoring.

**Evaluation metric:** Concordance index (C-index) for survival model; precision at top-20% risk tier for actionable intervention targeting (development directors can only personally steward 30-50 donors per quarter, so the model must rank-order risk effectively). False negative cost is high — missing a $10,000/year donor's lapse signal is expensive.

**Scope:** Straightforward ML problem with well-understood feature engineering. The main challenge is that most nonprofits have small donor databases (500-2,000 donors) with limited engagement tracking history. A cross-organization model trained on anonymized data from 50+ nonprofits via a platform like Bloomerang or Little Green Light would have sufficient volume. Team of 1 ML engineer, 3-4 month build. Cold-start problem for new donors requires a separate onboarding engagement model.

**Data availability:** High for giving history (every CRM tracks this). Moderate for email engagement (requires integration with Mailchimp/Constant Contact). Low for personal communication logs (development directors track these inconsistently, often in personal notebooks rather than CRM fields).

---

## 4. Volunteer Retention and Reliability Prediction
#gradient-boosting #binary-classification #tabular-ml #workflow-orchestration

**Problem statement:** Predict which volunteers are likely to no-show for a specific upcoming shift and which volunteers are at risk of permanently disengaging from the organization, enabling proactive schedule management and retention outreach.

**ML task:** Two related binary classification tasks: (1) shift-level no-show prediction (will this volunteer show up for this specific shift?), and (2) volunteer-level churn prediction (will this volunteer stop volunteering within the next 90 days?).

**Input data:** Volunteer profile data (demographics, skills, certifications, onboarding date), shift history (attendance rate, cancellation rate, preferred days/times, role types), communication responsiveness (reply latency to shift reminders, app login frequency), contextual features for shift-level prediction (day of week, weather, competing community events, time since last shift), and organizational engagement signals (newsletter opens, social media interaction, event attendance beyond volunteering).

**Target:** For no-show prediction: binary attended/no-show per confirmed shift assignment. For churn prediction: binary active/churned at 90-day horizon, where churned means zero shifts completed and zero shift sign-ups.

**Evaluation metric:** For no-show prediction: precision-recall AUC, optimizing for recall at a threshold that triggers backup volunteer activation (if the model predicts >60% no-show probability, the coordinator gets an alert 24 hours before the shift). For churn prediction: AUC-ROC with emphasis on catching disengagement early enough for intervention — a 30-day early warning is useful, a 7-day warning is too late.

**Scope:** Relatively simple feature engineering with well-structured data that volunteer management platforms already capture. The main modeling challenge is class imbalance (no-show rates of 20-30% mean the positive class is the minority) and the cold-start problem for new volunteers with no history. Ensemble of gradient-boosted trees with careful temporal cross-validation (cannot use future shifts to predict past no-shows). Team of 1 ML engineer, 2-3 month build. Best deployed as a feature within an existing volunteer management platform rather than a standalone product.

**Data availability:** High if built within an existing volunteer platform (Galaxy Digital, VolunteerHub) that already captures attendance records and shift assignments. Low if trying to aggregate data from nonprofits using spreadsheets, which is still the majority.
