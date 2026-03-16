# Machine Learning Opportunities — Language Schools

**Industry:** [[language-schools|Language Schools]]
**Derived from:** [[problems/language-schools/high-impact|High Impact]], [[problems/language-schools/low-impact-1|Low Impact 1]], [[problems/language-schools/low-impact-2|Low Impact 2]], [[problems/language-schools/worker-life-1|Worker Life 1]], [[problems/language-schools/worker-life-2|Worker Life 2]]

---

## 1. Proficiency Diagnosis from Speech and Writing Samples
#bert #lstm #multiclass-classification #nlp #speech-processing #tacit-knowledge-ml

**Problem statement:** Experienced placement testers can hear a student speak for 30 seconds and diagnose not just the CEFR level but the learner's native language, specific fossilized errors, and whether those errors are developmental or permanent — a multi-dimensional classification that takes years of immersion to develop and that testers cannot fully articulate as rules. This tacit diagnostic skill is the bottleneck for student placement, class composition, and individualized instruction planning.

**ML task:** Multiclass classification (CEFR band A1-C2, 12 sub-bands) + auxiliary multi-label classification (L1 identification from ~30 common source languages, fossilization pattern detection from a taxonomy of ~50 common error types)
**Input data:** 60-120 second audio recordings of structured elicitation tasks (picture description, prompted response) transcribed via ASR, plus a 100-200 word written paragraph. Features include: acoustic features (pitch contour, speech rate, pause distribution, vowel formant trajectories), ASR transcript with confidence scores, dependency-parsed text, lexical frequency profile, error annotations against target-language grammar.
**Target:** Primary: CEFR sub-band (e.g., B1.2). Auxiliary: L1 classification, binary fossilization flags per error category, developmental-vs-fossilized label per detected error.
**Evaluation metric:** Quadratic-weighted kappa for CEFR band (must exceed 0.85 to match inter-rater reliability of trained human testers); macro-F1 for L1 identification; per-category F1 for fossilization detection. Asymmetric cost: over-placement (student placed too high) is 2x more costly than under-placement because it causes immediate classroom failure and dropout.
**Scope:** Requires partnership with 10-20 language schools to collect 5,000-10,000 placement sessions with expert annotations. Expert annotators must provide not just the level score but the diagnostic reasoning (which features drove the decision) — this meta-annotation is the hardest data to collect because it forces tacit knowledge into explicit form. A joint acoustic-text model architecture (LSTM encoder for audio features feeding into a BERT-based text encoder with cross-attention) is needed; transfer learning from existing L2 speech corpora (ICNALE, NICT-JLE, Cambridge Learner Corpus) can bootstrap but domain-specific fine-tuning is essential. Team: 2 ML engineers, 1 SLA (second language acquisition) domain expert, 1 data engineer. Timeline: 12-18 months to production-grade MVP.
**Data availability:** Moderate difficulty. Raw placement recordings exist at most schools but are rarely archived systematically. The Cambridge Learner Corpus and ETS TOEFL datasets provide partial coverage but lack the diagnostic annotations (L1 interference patterns, fossilization labels) that make this system valuable beyond a simple level score. The labeling process requires SLA-trained annotators, not just language teachers — a significant cost bottleneck.

---

## 2. Student Dropout Prediction
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Language school students drop out at rates of 25-40% before completing their target proficiency goal, often after plateauing at intermediate levels. Schools detect attrition only when the student fails to re-enroll — by which time intervention is impossible. Early identification of at-risk students would allow targeted engagement (schedule adjustment, supplementary tutoring, motivational check-ins) before the student disengages.

**ML task:** Binary classification (will drop out before next session vs. will re-enroll), predicted at the midpoint of each session to allow intervention time.
**Input data:** Tabular features per student per session: attendance rate, assignment completion rate, grade trajectory (slope of scores over time), session-over-session proficiency gain (delta CEFR sub-band), number of class changes/transfers, visa status (F-1 students have enrollment-maintenance incentives that reduce dropout), payment history (late payments correlate with disengagement), engagement signals from LMS (login frequency, time on platform, discussion forum participation), and demographic features (L1, age, prior study duration).
**Target:** Binary label: did/did not re-enroll for the subsequent session. Secondary target: did/did not complete the original proficiency goal stated at intake.
**Evaluation metric:** AUPRC (area under precision-recall curve) preferred over AUROC due to class imbalance (~30% positive). Minimum viable recall of 0.70 at precision 0.50 — it is better to flag a student who does not drop out (false positive) than to miss one who does (false negative), because the intervention cost (an advisor conversation) is low.
**Scope:** Requires 3-5 years of historical enrollment data from 5-10 schools, with at least 2,000 student enrollment episodes. Feature engineering is straightforward; the main challenge is linking records across fragmented systems (SIS, LMS, accounting software). Gradient-boosted trees (XGBoost/LightGBM) will likely outperform deep learning given tabular features and modest dataset size. Team: 1 ML engineer, 1 data engineer. Timeline: 4-6 months.
**Data availability:** High for schools with electronic SIS records; low for schools still running on spreadsheets. The critical feature — proficiency gain trajectory — requires that the school has administered periodic assessments with scored outcomes, which not all do consistently.

---

## 3. Optimal Class Composition
#bayesian-network #regression #tabular-ml #data-integration

**Problem statement:** When a school has 30 students to distribute across three B1 sections, the assignment is currently done by availability (who can attend which time slot) and sometimes by the program director's gut sense of which L1 mixes produce productive interaction. Research in SLA shows that class composition — L1 diversity, proficiency-range spread, personality dynamics — significantly affects learning outcomes, but no school systematically optimizes for it.

**ML task:** Constrained optimization with a learned objective function. The regression model predicts per-student session-end proficiency gain as a function of class composition features; the optimizer assigns students to sections to maximize total predicted gain subject to capacity, schedule, and L1-balance constraints.
**Input data:** Historical class rosters with composition features: per-student CEFR sub-band at session start, L1, age, gender, learning goal (academic vs. conversational), years of prior study. Outcome: per-student CEFR sub-band gain at session end. Contextual features: class size, instructor ID (as a random effect), session duration, time of day.
**Target:** Predicted CEFR sub-band gain (continuous, regression). The downstream optimization uses this prediction as the objective function.
**Evaluation metric:** RMSE on held-out student-session pairs. Deployed value measured by A/B test: average proficiency gain in optimized sections vs. manually assigned sections over a 3-session period.
**Scope:** Requires historical roster + outcome data from schools that administer consistent pre/post assessments — a narrower data pool than dropout prediction. Bayesian network or hierarchical Bayesian regression preferred to capture instructor random effects and small-sample uncertainty. The optimization layer (integer programming with constraints) is standard OR, not ML. Team: 1 ML engineer, 1 operations researcher. Timeline: 6-9 months.
**Data availability:** Low-moderate. Few schools maintain structured pre/post assessment data linked to class rosters. A prospective data collection partnership (standardized pre/post testing at partner schools) may be necessary for the first 2-3 cohorts.

---

## 4. Assessment Item Difficulty Calibration
#logistic-regression #bayesian-network #regression #tabular-ml

**Problem statement:** Language schools that create their own quizzes, tests, and placement instruments have no systematic way to calibrate item difficulty. A grammar question that the item writer considers "B1-level" may actually discriminate at A2 or B2, producing unreliable assessments. Item response theory (IRT) calibration is standard in large-scale testing but requires psychometric expertise and sample sizes that small schools do not have.

**ML task:** Item parameter estimation (IRT 2-parameter logistic model: difficulty + discrimination) from response data, with Bayesian priors to handle small sample sizes per item.
**Input data:** Item-response matrices: rows = students, columns = items, values = correct/incorrect (or partial credit on a 0-3 scale for constructed-response items). Student-level covariates: CEFR level at time of test, L1, session number. Item-level covariates: skill targeted (grammar, vocabulary, reading, listening), CEFR level intended by the item writer, item format (multiple choice, fill-in-blank, short answer).
**Target:** Per-item difficulty parameter (continuous, mapped to CEFR sub-band scale) and discrimination parameter (how sharply the item separates adjacent proficiency levels).
**Evaluation metric:** Item-level calibration accuracy: correlation between estimated difficulty and expert-rated difficulty on a held-out item set. Test-level reliability: Cronbach's alpha or marginal reliability coefficient for tests assembled from calibrated item pools.
**Scope:** Can start with a single school's test bank (200-500 items) and 500+ student response records. Bayesian IRT models (using Stan or PyMC) handle the small-N-per-item problem well. The main challenge is convincing schools to share response-level data, which they may consider proprietary. Team: 1 ML engineer with psychometrics background. Timeline: 3-5 months for calibration engine; ongoing as new items are added.
**Data availability:** Moderate. Schools that use digital testing (Google Forms, LMS quizzes) have response data but rarely in a structured item-response matrix format. Manual test results require digitization. The cold-start problem for new items is addressed by informative priors from item covariates.
