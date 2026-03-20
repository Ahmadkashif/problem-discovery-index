# Machine Learning Opportunities — Public Adjusters

**Industry:** [[public-adjusters|Public Adjusters]]
**Derived from:** [[problems/public-adjusters/high-impact|High Impact]], [[problems/public-adjusters/low-impact-1|Low Impact 1]], [[problems/public-adjusters/low-impact-2|Low Impact 2]], [[problems/public-adjusters/worker-life-1|Worker Life 1]], [[problems/public-adjusters/worker-life-2|Worker Life 2]]

---

## 1. Hidden Damage Identification from Visible Loss Patterns (Primary Opportunity — Tacit Knowledge ML)
#cnns #gradient-boosting #transfer-learning #object-detection #feature-engineering #evaluation-metrics #loss-functions #backpropagation #gradient-descent #cross-validation #tacit-knowledge-ml

**Problem statement:** An experienced public adjuster walks through a fire-damaged home and sees charred kitchen cabinets — but immediately knows to check the adjacent walls for heat-compromised electrical wiring, the HVAC ducts for smoke particulate contamination, the attic insulation above the kitchen for heat damage, and the opposite side of the shared wall for smoke migration. They see a water stain on a first-floor ceiling and know the second-floor bathroom supply line, the subfloor, and the insulation between floors are likely compromised. This "visible damage → hidden damage" inference is the single most valuable skill in public adjusting — it's the difference between a $50,000 recovery and a $150,000 recovery on the same loss. Junior adjusters and catastrophe-deployed temporary inspectors lack this pattern recognition, documenting only what's visible and missing 30-50% of the legitimate claim value.

**ML task:** Multi-label classification (predict which hidden damage categories are likely present) plus regression (estimate the dollar value of probable hidden damage by category)
**Input data:** Inspection photos of visible damage (annotated by location within the structure), loss cause (fire, water, wind, hail), construction type (wood frame, masonry, steel), building age, building size and layout, geographic location (climate zone affects damage patterns), initial Xactimate estimate of visible damage
**Target:** Probability of hidden damage by category (e.g., P(electrical damage behind fire-adjacent wall) = 0.85, P(HVAC contamination from smoke) = 0.92, P(subfloor damage below water stain) = 0.78); estimated cost per hidden damage category; prioritized inspection checklist
**Evaluation metric:** Recall on hidden damage category prediction (target: 0.85+ — must not miss legitimate damage categories); precision targeting 0.60+ (acceptable false positive rate for inspection recommendations that prove unnecessary); MAE on hidden damage value estimation (target: within 20% of actual documented value)
**Scope:** Requires 5,000-10,000 claims with complete before/after documentation — initial visible-damage-only estimate paired with the final supplemented estimate that includes hidden damage found during thorough inspection. 3-4 person team (CV engineer, construction domain expert, data engineer, annotator), 12-18 months. Data collection challenge: most adjusters don't separately document what was initially visible vs. what was discovered through investigative inspection — the final estimate includes everything. Building the paired dataset requires either retrospective reconstruction from photo timestamps and estimate line item dates, or prospective data collection with a structured two-phase documentation protocol. Labeling challenge: "hidden" damage is a continuum — some damage is merely hard to see (requiring ladder access), while some requires destructive testing (opening walls) to confirm. The model must distinguish between "go look here" recommendations and "this definitely exists" predictions. Deployment challenge: the model must operate in the field during inspection, providing recommendations in real-time as the adjuster photographs visible damage. Mobile inference with variable photo quality and no internet connectivity (common in disaster zones) is required.
**Data availability:** Public adjusting firms have thousands of completed claims with initial and supplemented estimates. Photo documentation varies widely in quality and completeness. Xactimate estimate files contain structured line items that can be labeled by damage category. Multi-firm data aggregation (anonymized) would dramatically improve the model but requires overcoming competitive reluctance to share claim data.

---

## 2. Claim Value Estimation at Intake
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #linear-regression #probability-distributions #expectation-variance-covariance #confidence-intervals

**Problem statement:** When a potential client calls, the public adjuster must quickly estimate the likely claim value to decide whether to take the case on contingency. Currently, this is done by asking the client to describe the damage and making a rough mental estimate — experienced adjusters are within 30% of actual; inexperienced ones are off by 50-100%.

**ML task:** Regression (predict total claim settlement value from intake information)
**Input data:** Loss cause, property type (residential/commercial), property size (sq ft), property age, property location (ZIP code → construction costs, carrier behavior), client description of damage, policy limits (if known), whether emergency services were involved (fire department, water mitigation), carrier identity (some carriers are more aggressive negotiators)
**Target:** Predicted settlement value with confidence interval; predicted fee at standard contingency rate
**Evaluation metric:** MAPE targeting <30%; percentage of estimates within 25% of actual settlement (target: >60%)
**Scope:** Requires 3,000-10,000 closed claims with intake information and final settlement amounts. 1-person team, 3-4 months. Challenge: intake information is sparse and verbal — structured data collection at intake must be implemented.
**Data availability:** Closed claims with settlement amounts exist in every firm. Intake information is rarely structured — phone notes, text messages. Implementing a structured intake questionnaire is prerequisite to model training.

---

## 3. Settlement Timeline Prediction
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #survival-analysis #time-series-forecasting #probability-distributions #expectation-variance-covariance

**Problem statement:** Settlement timelines range from 4 weeks to 18+ months depending on carrier, claim complexity, and negotiation dynamics. Predicting timeline enables cash flow forecasting and case prioritization.

**ML task:** Regression (predict days to settlement from current case state)
**Input data:** Loss cause, carrier identity, claim complexity indicators (number of coverage sections, commercial vs. residential, attorney involvement), current negotiation stage, number of supplements filed, carrier adjuster response pattern (days between communications), comparable claim settlement timelines
**Target:** Predicted days to settlement from current date; updated weekly as case progresses
**Evaluation metric:** MAE in days (target: <30 days); percentage within 2 weeks of actual (target: >50%)
**Scope:** Requires 2,000-5,000 closed claims with timeline data (dates of key events: inspection, initial estimate submission, carrier response, supplement filings, appraisal, settlement). 1-person team, 2-3 months.
**Data availability:** Claims management systems contain date stamps for key events. Carrier identity is known. Challenge: different carriers behave differently (some settle quickly, some delay systematically), and carrier behavior may change over time as staffing and strategy shift.

---

## 4. Policy Coverage Gap Detection
#bert #transfer-learning #attention-mechanisms #transformers #word-embeddings #loss-functions #evaluation-metrics #entropy-cross-entropy-kl-divergence #conditional-probability-and-bayes-theorem

**Problem statement:** Commercial policies contain coverage sections and endorsements that public adjusters commonly miss — ordinance or law coverage, equipment breakdown, business income with extended period of indemnity, newly acquired property. Automatically analyzing the policy to flag all applicable coverages for a given loss type would increase recoveries and reduce missed-coverage risk.

**ML task:** Text classification (for each coverage section/endorsement in the policy, classify whether it applies to the reported loss type)
**Input data:** Full policy text (base policy + endorsements + schedules), reported loss type and description, property characteristics
**Target:** Applicable/not-applicable classification for each coverage section; estimated recovery potential per applicable section; commonly-missed coverage flags
**Evaluation metric:** Recall on applicable coverage detection (target: 0.95+ — must not miss applicable coverages); precision targeting 0.70+ (some false positives acceptable — better to flag and review than to miss)
**Scope:** Requires 1,000-3,000 policies paired with claims that identify which coverages were ultimately applied. 2-person team (NLP engineer, insurance domain expert), 6-9 months. Policy parsing is the primary challenge — endorsements modify base policy language in complex ways.
**Data availability:** Public adjusting firms have policies paired with claims. Policy digitization varies — some are clean PDFs, others are scanned with variable OCR quality. Insurance policy language is semi-standardized (ISO forms) but endorsements vary by carrier and state.

---

## 5. Carrier Negotiation Strategy Optimization
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #expectation-variance-covariance #probability-distributions

**Problem statement:** Different insurance carriers respond to different negotiation strategies — some settle quickly when presented with thorough documentation, others delay systematically until appraisal is invoked, and some have specific triggers (dollar thresholds, line item categories) that escalate the claim to senior adjusters with more settlement authority. Experienced public adjusters know each carrier's patterns; juniors negotiate blindly.

**ML task:** Recommendation (suggest optimal negotiation strategy based on carrier, claim characteristics, and historical outcomes)
**Input data:** Carrier identity, carrier adjuster identity (some adjusters within the same carrier behave differently), claim size and type, documentation thoroughness score, current negotiation stage, prior interaction history on this claim, historical outcomes for similar claims with the same carrier
**Target:** Recommended next action (submit supplement, invoke appraisal, request supervisor review, accept offer, counter at X%), predicted outcome probability for each action, predicted time-to-settlement for each strategy path
**Evaluation metric:** Settlement amount relative to initial carrier offer when using recommended strategy vs. adjuster's default strategy; time-to-settlement comparison
**Scope:** Requires 5,000-10,000 claims with detailed negotiation histories (offers, counter-offers, actions taken, outcomes). 2-person team, 6-9 months. Challenge: negotiation data is unstructured — emails, phone notes, letters. Must be extracted and structured before modeling.
**Data availability:** Claims files contain negotiation correspondence but in unstructured format. Building a structured negotiation database from historical files requires significant data engineering. Carrier behavior patterns are proprietary to each public adjusting firm and unlikely to be shared.
