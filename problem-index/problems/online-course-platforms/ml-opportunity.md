# Machine Learning Opportunities — Online Course Platforms

**Industry:** [[online-course-platforms|Online Course Platforms]]
**Derived from:** [[problems/online-course-platforms/high-impact|High Impact]], [[problems/online-course-platforms/low-impact-1|Low Impact 1]], [[problems/online-course-platforms/low-impact-2|Low Impact 2]], [[problems/online-course-platforms/worker-life-1|Worker Life 1]], [[problems/online-course-platforms/worker-life-2|Worker Life 2]]

---

## 1. Knowledge Tracing: Estimating What a Learner Actually Knows
#hidden-markov-models #bayesian-inference #lstms-and-grus #transformers #confidence-intervals #maximum-likelihood-estimation #evaluation-metrics #probability-distributions

**Problem statement:** Platforms report progress — the percentage of material viewed — as if it were learning. Capability is latent, assessments are noisy, and the interaction data that could support a genuine estimate has been accumulating unused for fifteen years.

**ML task:** Model per-skill mastery as a latent state updated by each learner interaction, producing a calibrated mastery estimate with uncertainty rather than a progress percentage
**Input data:** Fine-grained interaction telemetry — pauses, rewinds, replays, playback speed, time on segment, abandonment and return; quiz attempts with item-level responses and timing; open-ended submissions and their assessments; skill tagging of content at the segment level; the learner's history across other courses.
**Target:** Performance on held-out assessment items testing the same skill, and — the stronger target where it can be obtained — performance after a delay, which is what distinguishes learning from recognition.
**Evaluation metric:** Predictive accuracy on future item responses is the standard measure and is not sufficient alone, because a model can predict quiz performance well while tracking nothing more than recent exposure. The decisive test is delayed retention: does the mastery estimate predict performance weeks later, when the fluency from a clear video has faded. Report calibration, since the estimate's use is to tell a learner what they can and cannot yet do.
**Scope:** Skill tagging of content at segment granularity is the unglamorous prerequisite and the usual point of failure; without it every model is tracing courses rather than skills. The literature here is deep and mature, which makes this unusually well-posed for a category that has ignored it. 3 ML engineers plus an instructional designer, 9-12 months.
**Data availability:** The richest in this cluster. Interaction telemetry is complete; item-level response data exists; delayed retention data requires deliberately scheduling spaced assessment, which nobody does and which is the main new collection needed.

---

## 2. Automated Assessment of Open-Ended Work With Calibrated Grading
#large-language-models #transformers #bert #evaluation-metrics #confidence-intervals #contrastive-learning #transfer-learning #hypothesis-testing

**Problem statement:** Assessment that demonstrates capability requires open-ended work — code, a design, an analysis, a piece of writing — which was too expensive to evaluate at scale. Peer review was the scalable substitute and is unreliable. This constraint has genuinely changed and the category has deployed the new capability as a question-answering chatbot instead of as an assessor.

**ML task:** Grade open-ended submissions against a rubric, with specific evidenced feedback, calibrated against expert graders and reporting its own uncertainty
**Input data:** Learner submissions; rubrics with level descriptors; expert-graded reference submissions spanning the quality range; the course material the work is meant to demonstrate; historical instructor feedback on similar work.
**Target:** The grade and the feedback an expert instructor would give, on the same rubric.
**Evaluation metric:** Agreement with expert graders, measured properly — inter-rater agreement against a panel rather than against one grader, since experts disagree and the ceiling is their agreement with each other. Publish the calibration; a grading system whose accuracy is unstated should not be issuing anything a learner relies on. Measure differential performance across learner populations explicitly, including non-native English speakers, because unequal grading accuracy in an educational credential is a direct harm and is the failure mode most likely to go unnoticed.
**Scope:** The feedback matters more than the grade: specific, evidenced, pointing at the submission, is what changes a learner's trajectory. The system should defer visibly when a submission is outside what it can assess rather than guessing, because a learner cannot evaluate a wrong assessment. Human review on appeal is a design requirement. 3 ML engineers plus an assessment specialist, 9-12 months.
**Data availability:** Submissions are abundant. Expert-graded reference sets must be created deliberately and are the project's real cost.

---

## 3. Abandonment Prediction and Readiness Matching
#survival-analysis #gradient-boosting #graph-neural-networks #k-nearest-neighbors #confidence-intervals #causal-inference #evaluation-metrics #feature-engineering

**Problem statement:** Most abandonment is silent and looks like ordinary churn, while a substantial share of it is placement failure — a learner missing two unstated prerequisites who struggles, blames themselves and leaves in week two.

**ML task:** Predict time-to-abandonment and its cause, and infer each course's real prerequisite structure from which prior knowledge distinguishes learners who succeed from those who stop at a given point
**Input data:** Learner histories across courses with outcomes; struggle signals — repeated attempts, rewinds, long pauses, help-seeking; course content and its stated level; abandonment points; completion outcomes conditioned on prior course completion.
**Target:** Abandonment within the following two weeks and the lesson at which it occurs; separately, the set of prior concepts predictive of success in a given course.
**Evaluation metric:** Lead time matters more than raw accuracy — a prediction made after the learner has stopped is worthless, so measure accuracy at 7 and 14 days before the event. For prerequisites, the validation is interventional: learners routed through an inferred prerequisite first should complete at a higher rate than a matched control, and without that test the inferred structure is just correlation with prior enrolment.
**Scope:** The recommendation objective must change from enrolment to expected mastery gain, which is a business decision as much as a modelling one — the current objective is why popular courses dominate regardless of fit. Lesson-level content representation, so a learner can be sent to one module instead of a forty-hour course, is the same modelling work applied at a finer grain. 2 ML engineers, 6-9 months.
**Data availability:** Complete inside the platform, and unusually clean because everything happens in one system.

---

## 4. Content Decay Detection From Behaviour and External Change
#change-point-detection #bert #large-language-models #gradient-boosting #word-embeddings #evaluation-metrics #time-series-forecasting #automation

**Problem statement:** Technical courses are materially wrong within eighteen months, ranking signals accumulate over years and therefore reward age, and decay is discovered when a learner complains in the Q&A.

**ML task:** Detect decayed course segments by combining internal behavioural signals with the referenced subject's external change history, localised to a lesson and timestamp
**Input data:** Drop-off and rewind concentration by lesson timestamp over time; Q&A thread content clustered by topic and location; review text and refund reasons; course transcripts and on-screen content; external change sources — release notes, documentation diffs, regulatory calendars — matched to the course's subject.
**Target:** Whether a specific course segment is materially outdated, confirmed by instructor or reviewer assessment.
**Evaluation metric:** Precision at segment level is what makes this actionable — telling an instructor their course is outdated is not usable; telling them lesson fourteen between four and seven minutes shows a fourfold drop-off spike since the tool's April release, with twelve Q&A threads about the changed menu, is a thirty-minute fix. Measure lead time against the first learner complaint, which is the current detection mechanism.
**Scope:** The external change signal is domain-specific — a framework has release notes, a tax course has a legislative calendar, a design tool has interface redesigns — so this is built per domain rather than generically, which is why no universal feature exists. Feeding the output into a decay-adjusted ranking is what aligns marketplace incentives with maintenance. 2 ML engineers, 6-9 months for the first two domains.
**Data availability:** Internal signals are complete. External change monitoring requires per-domain integrations and is the ongoing cost.
