# Machine Learning Opportunities — Player Research Firms

**Industry:** [[player-research-firms|Player Research Firms]]
**Derived from:** [[problems/player-research-firms/high-impact|High Impact]], [[problems/player-research-firms/low-impact-1|Low Impact 1]], [[problems/player-research-firms/low-impact-2|Low Impact 2]], [[problems/player-research-firms/worker-life-1|Worker Life 1]], [[problems/player-research-firms/worker-life-2|Worker Life 2]]

---

## 1. Predictive Validity of Research Findings
#causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #data-integration #tacit-knowledge-ml

**Problem statement:** A firm runs hundreds of studies a year, delivers each across an organisational boundary, and never learns which findings were implemented or whether the change worked — so the field's accumulated expertise is a personal pattern library built from projects whose outcomes nobody observed.

**ML task:** Link structured findings to implementation status and subsequent telemetry, and estimate which methods, sample sizes and severity ratings actually predict behavioural change
**Input data:** Findings recorded as structured testable claims with severity and stated confidence; implementation status per finding; the client's telemetry slice for the specific metric the finding predicted — completion at a named step, retention in a named window; build contents so co-shipped changes are visible; study method, sample size and participant composition.
**Target:** Whether the predicted behavioural change occurred, and its magnitude.
**Evaluation metric:** Predictive validity by method and by severity rating, which is the field's missing evidence base. Attribution must be handled honestly: where a finding shipped in a build with nine other changes, the analysis should report that it cannot be isolated rather than claiming credit — a firm that says so is being more useful than one that does not, and the honest version is also the one that survives client scrutiny. Where staged rollout was possible, use it and say so.
**Scope:** The precondition costs nothing: findings recorded as structured claims rather than as slides, which makes them checkable later. The outcome return is a narrow, specific data-sharing ask most clients would grant, framed as the mechanism by which the next study gets better. The commercial obstacle is that a firm proposing to check whether its own past recommendations worked is proposing unbilled work with possibly unflattering results. 2 ML engineers plus a research lead, 9-12 months.
**Data availability:** Findings exist as documents and must be restructured going forward. Telemetry exists at the client and is not shared because nobody asked narrowly enough.

---

## 2. Automated Session Coding and Cross-Session Aggregation
#transformers #cnns #large-language-models #bert #contrastive-learning #evaluation-metrics #automation #confidence-intervals

**Problem statement:** A study generates forty hours of gameplay video, think-aloud audio and observer notes, and the coding that turns it into findings is manual work compressed into the days before a readout — so researchers watch selectively, which reintroduces the observer bias the method exists to control.

**ML task:** Detect struggle, confusion, repeated failure, backtracking, hesitation and verbal frustration across every session, aligned to game state, and aggregate to identify patterns recurring across participants
**Input data:** Screen recordings with game state from instrumentation or from the recording itself; think-aloud audio with transcription and speaker separation; webcam video where captured; moderator notes and marks; task completion records; telemetry from the live game for the same moments.
**Target:** Event codes matching what a trained researcher would assign, validated against manually coded sessions.
**Evaluation metric:** Agreement with human coders, measured against multiple coders rather than one, since the ceiling is their agreement with each other and inter-rater reliability in qualitative coding is imperfect by nature. The operationally decisive metric is coverage: whether a first pass over all twelve sessions beats a careful pass over three, which is the real comparison against current deadline-compressed practice. Report false positives on struggle detection separately — a system that flags every pause will be ignored.
**Scope:** Aggregation is where the finding actually lives: eight of twelve participants hesitating at the same element is the result, and it requires consistent coding across all sessions, which manual analysis under deadline does not deliver. Clip retrieval by what happened is the cheapest high-value piece. Automatic joining to live telemetry puts the quantitative and qualitative views of the same phenomenon side by side, which researchers currently do in their heads. 3 ML engineers with multimodal experience, 9-12 months.
**Data availability:** Sessions are recorded as standard. Manually coded sessions exist as the label set and are plentiful.

---

## 3. Screener Honesty and Sample Representativeness
#logistic-regression #gradient-boosting #bayesian-inference #confidence-intervals #k-means-clustering #hypothesis-testing #evaluation-metrics #feature-engineering

**Problem statement:** Participants who want the incentive answer qualifying questions in the way that qualifies them, and researchers frequently discover this during the session rather than before. Separately, findings generalise to a player population whose distribution on the dimensions that matter is never compared to the sample's.

**ML task:** Predict screener misreporting from response patterns, panel history and short pre-task behaviour; and measure sample representativeness against the live population on question-relevant dimensions
**Input data:** Screener responses and their internal consistency; panel participation history and frequency; behaviour in a short skill or familiarity pre-task; session outcomes where experience claims were contradicted; live game telemetry giving the target population's distribution on genre experience, platform familiarity and motivation profile.
**Target:** Whether the participant's claimed experience matches their demonstrated experience.
**Evaluation metric:** Precision at the exclusion threshold, since wrongly excluding an honest participant costs them an incentive and the study a valid data point. Measure the contamination rate before and after — the useful output is how much of a typical panel fails verification, a number the field does not have. For representativeness, the deliverable is a stated comparison per study rather than a model score, so a finding can carry an explicit statement of how far it should be expected to generalise.
**Scope:** Practice effects need tracking alongside: panel members who take many studies become unrepresentative through familiarity with being researched, and participation history is recorded and rarely used. Constructing a panel for the specific question — genuine newcomers for comprehension studies, experienced players for late-game work — is the structural improvement that a general pool cannot provide. 1-2 ML engineers, 4-6 months.
**Data availability:** Screener and panel data sit with playtesting platforms. Target population distributions sit in client telemetry and require the same sharing arrangement as item 1.

---

## 4. Small-Sample Inference for Twelve-Participant Studies
#bayesian-inference #confidence-intervals #probability-distributions #hypothesis-testing #monte-carlo-methods #evaluation-metrics #maximum-likelihood-estimation #law-of-large-numbers-and-clt

**Problem statement:** Studies run with small participant counts because sessions are expensive, and findings are reported into development teams with a definiteness the numbers do not support — because a hedged finding does not get acted on, which is a real incentive that degrades the evidence.

**ML task:** Quantify what a small sample supports — the probability that an observed problem affects a given share of the population — and express it in a form a development team can act on
**Input data:** Per-participant observations from the study; historical studies with both small-sample findings and subsequent live telemetry confirming or refuting them, which calibrates the relationship; participant representativeness measures; problem type and severity.
**Target:** The population prevalence of an observed problem, estimated from the sample with honest uncertainty and calibrated against outcomes where item 1 supplies them.
**Evaluation metric:** Calibration against live telemetry outcomes on the subset where returns exist — if the method says a problem affects 30-70% of players, it should be in that range roughly as often as claimed. This is the check that would tell the field how much twelve sessions is actually worth, which is its oldest methodological question and has never been answered empirically. Evaluate the communication format separately by whether teams act differently on strong versus weak findings, since a correct interval that is ignored has not solved the problem.
**Scope:** The reporting format is as much of the project as the statistics. Part of why researchers overstate is that hedged findings are ignored; a format that conveys evidential strength in an actionable way — near-certain, suggestive and worth testing — removes the incentive to overstate. 1 ML engineer plus a statistician and a research lead, 6-9 months.
**Data availability:** Study data is held. The calibration depends on outcome returns from item 1, which makes these two a single programme.
