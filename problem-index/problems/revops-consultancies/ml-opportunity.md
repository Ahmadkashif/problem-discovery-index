# Machine Learning Opportunities — RevOps Consultancies

**Industry:** [[revops-consultancies|RevOps Consultancies]]
**Derived from:** [[problems/revops-consultancies/high-impact|High Impact]], [[problems/revops-consultancies/low-impact-1|Low Impact 1]], [[problems/revops-consultancies/low-impact-2|Low Impact 2]], [[problems/revops-consultancies/worker-life-1|Worker Life 1]], [[problems/revops-consultancies/worker-life-2|Worker Life 2]]

---

## 1. Forecast Scoring and Calibrated Pipeline Probability
#time-series-forecasting #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #probability-distributions #evaluation-metrics #revenue-impact

**Problem statement:** Forecasts are produced weekly and overwritten weekly, so the series required to score them does not exist. Stage probabilities are set by convention and never checked against this business's observed close rates, and judgement adjustments are applied by people whose accuracy is unknown to everyone including themselves.

**ML task:** Retain a weekly pipeline snapshot series, score forecast error by horizon and segment, recalibrate stage and category probabilities empirically, and produce a forecast distribution rather than a point
**Input data:** Weekly full-pipeline snapshots with stage, amount, close date, owner and forecast category; the roll-up and each judgement adjustment with its author; actual closed outcomes; segment, product and deal characteristics; seasonality and period-boundary effects.
**Target:** Actual bookings for the period, and per-opportunity close outcome.
**Evaluation metric:** Forecast error by weeks-out is the headline, and calibration matters more than point accuracy — a forecast eleven weeks out should carry a wide interval and be honest about it, and the current practice of a single confident number is the failure being corrected. Evaluate judgement adjustment as a measurable quantity: does the adjusted forecast beat the raw roll-up, by author, with enough history to be meaningful. That number will be unwelcome in some organisations and is the most valuable output.
**Scope:** Snapshot retention is a week of engineering and is the precondition for everything; it should be the first deliverable of any engagement in this discipline and almost never is. The obstacle after that is political rather than technical, because scoring makes individual accuracy visible. Several quarters of retained history are needed before anything can be said. 1 data engineer and 1 data scientist, 3 months to instrument, 4 quarters to conclude.
**Data availability:** Currently destroyed by the process that creates it. Everything needed exists at the moment of the weekly cycle and is discarded.

---

## 2. Behavioural Data Distortion Metrics for CRM
#gradient-boosting #change-point-detection #hypothesis-testing #dbscan #confidence-intervals #evaluation-metrics #data-integration #feature-engineering

**Problem statement:** CRM data quality is discussed as completeness because that is what vendors sell against. The distortions that break revenue analysis are behavioural — stages advanced because a manager asked, close dates pushed a fortnight at a time, opportunities created at period boundaries — and are measured nowhere.

**ML task:** Learn per-business baselines for stage dwell, close date change patterns, creation timing and amount entry, and detect drift and anomaly against them
**Input data:** Full field history for opportunities including stage transitions and close date changes with timestamps; opportunity creation timing relative to period and forecast-call boundaries; amount values and their revision history; loss reason selection and the time taken to select it; activity data from email and calendar for comparison against recorded state.
**Target:** Not a label but a characterisation — the distribution of each behaviour for this business, with drift detection against its own baseline.
**Evaluation metric:** The useful test is downstream: does attaching these metrics to a forecast improve its calibration. A segment whose stage transitions are manager-driven rather than event-driven should carry wider forecast intervals, and if the distortion metrics do not improve calibration when included, they are describing something that does not matter.
**Scope:** Baselines must be per-business — a ninety-day enterprise cycle and a fourteen-day transactional one have entirely different healthy dwell distributions, and a generic threshold flags one and misses the other. The reporting design is an ethical requirement rather than a preference: these metrics describe individuals' behaviour, and a data quality programme that becomes performance management produces better-looking and worse-quality data. Report at team and process level. 1 data scientist, 3-4 months.
**Data availability:** Field history tracking is frequently disabled or truncated for volume reasons, which is the most common blocker and is a configuration change.

---

## 3. Account Potential Estimation and Equitable Territory Allocation
#gradient-boosting #convex-optimization #confidence-intervals #k-means-clustering #causal-inference #optimization-fundamentals #evaluation-metrics #revenue-impact

**Problem statement:** Territories are balanced on proxies like account count while realistic potential depends on propensity, penetration, competitive presence and renewal timing — so attainment distribution is bimodal and attrition concentrates among representatives with unwinnable allocations.

**ML task:** Estimate per-account expected revenue potential from the organisation's own history, then allocate accounts to representatives as a constrained optimisation balancing expected potential subject to geography, specialisation and continuity
**Input data:** Account history with this vendor — purchases, expansions, churn, engagement; firmographic and technographic attributes; competitive presence where observable; renewal timing and contract structure; historical representative attainment with the territories that produced it; constraints on geography, industry specialisation and relationship continuity.
**Target:** Realised revenue per account over the planning year, aggregated to territory potential.
**Evaluation metric:** Account-level potential should be evaluated on held-out years, but the decisive output is the equity measurement: the predicted distribution of attainment across the proposed allocation, and the share of attainment variance attributable to territory rather than performance. That number is what changes the planning conversation and it is the thing nobody can currently demonstrate.
**Scope:** The potential model must be fitted to this organisation's own history rather than bought as a firmographic score, because what predicts potential differs completely between enterprise and transactional businesses. The optimisation is a standard shape once the estimate exists. Planning is annual and time-pressured, so the tool has to run in days. 1-2 data scientists, 4-6 months.
**Data availability:** Good. Account history and attainment records exist; competitive presence is the weakest input and is partially inferable.

---

## 4. Automated Engagement Diagnostic From CRM Structure
#large-language-models #gradient-boosting #k-nearest-neighbors #bert #change-point-detection #evaluation-metrics #automation #tacit-knowledge-ml

**Problem statement:** Every RevOps engagement spends its first weeks rediscovering the same findings through interviews, and the findings are computable directly from the client's systems in a day.

**ML task:** Compute the standard diagnostic set from CRM and marketing automation data, compare against cross-client baselines the firm has accumulated, and rank findings by their association with downstream revenue outcomes
**Input data:** The client's CRM objects, field history, stage definitions and conversion rates; marketing automation and handoff data; pipeline coverage and velocity; forecast history availability; the firm's accumulated cross-client baselines for comparable businesses.
**Target:** Whether an identified finding, when remediated, was followed by a measurable improvement — which requires the firm to retain outcomes across engagements.
**Evaluation metric:** Agreement with experienced consultants' own manual findings on engagements where both were produced, as the initial validation. The more valuable measure is predictive: which findings, across the firm's portfolio, are actually associated with subsequent improvement — because the current practice ranks recommendations by consultant conviction and some of the standard advice may not survive that test.
**Scope:** The diagnostic itself is straightforward computation and delivers most of the value by compressing three weeks into a day and arriving with numbers rather than assertions. The cross-client comparison requires the firm to build a baseline corpus, which is a process decision it has not made. 1-2 engineers, 4-6 months.
**Data availability:** Client systems are accessible during engagements. Cross-client baselines require deliberate retention and anonymisation.
