# Machine Learning Opportunities — Mobile Game Publishers

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]
**Derived from:** [[problems/mobile-game-publishers/high-impact|High Impact]], [[problems/mobile-game-publishers/low-impact-1|Low Impact 1]], [[problems/mobile-game-publishers/low-impact-2|Low Impact 2]], [[problems/mobile-game-publishers/worker-life-1|Worker Life 1]], [[problems/mobile-game-publishers/worker-life-2|Worker Life 2]]

---

## 1. Prototype Selection With Measured False Negatives
#survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #causal-inference #probability-distributions #hypothesis-testing #evaluation-metrics

**Problem statement:** Kill decisions are made on day-one retention from a few thousand installs against thresholds nobody derived, and every analysis of what predicts success runs on the games that passed the filter — so the funnel validates itself and its false negative rate is unknown.

**ML task:** Estimate the probability that a prototype reaches each subsequent stage and eventual outlier performance, conditioned on genre and prototype completeness, with a randomised below-threshold allowance to recover the counterfactual
**Input data:** Prototype early metrics — retention curves, session structure, cost per install, acquisition source and test geography; prototype characteristics including genre, mechanic family and how complete the build was; the publisher's full history of prototypes with their stage outcomes; realised long-run revenue for those that scaled; randomised below-threshold advancement assignments.
**Target:** Long-run revenue, and separately the probability of being a portfolio outlier — which is the quantity that actually matters and ranks prototypes very differently from expected median performance.
**Evaluation metric:** Calibration of the advancement probability, and — the metric nobody has — the false negative rate estimated from the randomised allowance. Evaluate on outlier identification explicitly, because returns in this portfolio are dominated by rare successes and a model optimised on average outcome will select competent games and no hits. Report sampling error on the early metrics themselves; a great deal of current decision-making is below the noise floor.
**Scope:** The randomised below-threshold allowance is the whole project. It costs visible money to fund concepts the current rule would kill, it is the only route to the counterfactual, and every other estimate here depends on it. Genre-conditioned thresholds alone will very likely beat the single portfolio threshold and are cheap to derive first. 2 ML engineers plus an executive willing to fund the allowance, 9-12 months.
**Data availability:** Prototype histories are complete inside publishers and comprehensively censored by the funnel. The censoring is the problem, not the volume.

---

## 2. Soft Launch Transfer Estimation and Market Selection
#causal-inference #bayesian-inference #transfer-learning #confidence-intervals #gradient-boosting #hypothesis-testing #probability-distributions #evaluation-metrics

**Problem statement:** Games are validated in a conventional set of small test markets and scaled globally on an assumption of transferability that is applied as an informal multiplier and has never been estimated.

**ML task:** Estimate the market-pair transfer relationship for retention, monetisation and acquisition cost per genre, and select test markets to maximise information about this title's specific uncertainty
**Input data:** The publisher's portfolio of titles observed in both soft launch and global scale; cohort metrics by market, genre and acquisition source; market-level covariates — device mix, payment friction, competitive landscape, genre familiarity, income; acquisition campaign composition in test versus scale.
**Target:** Scaled-market performance given soft launch performance, with the composition difference between test and scale cohorts adjusted for.
**Evaluation metric:** Prediction error on held-out titles, reported per market pair and per genre rather than pooled, because the transfer relationship is exactly what varies between them. The specific failure to measure is the recurring one where a title validates in soft launch and does not scale — those cases should be predicted correctly by a model that adjusts for cohort composition, and if they are not the adjustment is not working.
**Scope:** Cohort composition adjustment is the unglamorous part that probably accounts for most of the current error: soft launch installs come from small low-volume campaigns and bring a different player population than a scaled launch. Market selection framed as information maximisation is a distinct and smaller piece that changes which markets are used at all. 2 ML engineers, 6-9 months.
**Data availability:** Complete within a publisher's portfolio, though the number of titles that have been through both stages is modest, which argues for genre-level pooling with hierarchical structure.

---

## 3. Joint Long-Horizon Monetisation Optimisation
#markov-decision-processes #causal-inference #bayesian-optimization #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Advertising and purchase revenue compete for the same player, tests measure one at a time on windows too short to include the retention cost, and the result is a configuration that wins every individual experiment and loses on the combined objective.

**ML task:** Optimise total revenue per player over a long horizon net of the retention hazard, with ad exposure and purchase pressure set jointly and per player rather than globally
**Input data:** Ad impressions, placements and revenue; purchase events, offers shown and their responses; session structure and progression state; retention and churn with timing; predicted purchase propensity; experiment assignments varying both monetisation channels together.
**Target:** Revenue per player over 90 and 180 days, net of the churn effect.
**Evaluation metric:** The critical requirement is a horizon long enough to contain the cost — a test window of days measures the revenue and misses the churn, systematically in the direction that favours shipping the more aggressive configuration, which is how the current practice fails. Evaluate the cross-effect explicitly: does the ad load change purchase behaviour, and by how much, which requires designs that vary both and which almost nobody runs.
**Scope:** Per-player ad exposure driven by predicted purchase propensity is a straightforward extension of targeting infrastructure most publishers already run for offers, and is probably the single largest available gain. Transferability between genres is low — an ad break in a puzzle game and one in a strategy game are different interventions — so this is fitted per portfolio. 3 ML engineers, 9-12 months including the long-horizon experiments.
**Data availability:** Complete. The constraint is experiment design and patience rather than data.

---

## 4. Population-Level Spending Distress Signatures
#change-point-detection #survival-analysis #gradient-boosting #confidence-intervals #causal-inference #evaluation-metrics #compliance #probability-distributions

**Problem statement:** Revenue is concentrated in a small minority of players, monetisation design is aimed at them, and the instrumentation distinguishes spending levels and nothing else — so an enthusiast with disposable income and someone spending in a pattern suggesting distress are indistinguishable in every dashboard the decision is made from.

**ML task:** Characterise behavioural spending patterns associated with distress at population level, and report a welfare metric alongside revenue for every monetisation change
**Input data:** Purchase events with timing, amount and escalation; session timing, duration and time of day; purchase proximity to losses, progression blocks and offer prompts; deviation from a player's own established baseline; refund and chargeback requests; self-imposed limit usage where available.
**Target:** Population-level prevalence of distress-associated patterns, and the change in that prevalence attributable to a design change — never an individual diagnosis, which this data cannot support and should not be used to claim.
**Evaluation metric:** Since there is no individual ground truth, validation is indirect and must be honest about it: association with refund and chargeback requests, with self-imposed limits, and with abrupt permanent disengagement. The operative use is comparative — does this offer design raise the share of revenue coming from rapid-escalation patterns — which needs only a consistent measure, not a validated diagnosis. Report it beside revenue in the same review where the decision is taken, which is the entire mechanism by which it changes anything.
**Scope:** This must be built as a population metric for evaluating designs, not as a per-player classifier, both because the data cannot support individual inference and because a per-player label invites uses that would be considerably worse than the problem. Shippable interventions — spend pacing, easily-found self-set limits, suppression of high-pressure offers for distress signatures — are the practical output, and several have been found to cost less revenue than expected, which is the evidence an internal argument needs. 2 ML engineers plus external ethics and regulatory input, 6-9 months.
**Data availability:** Complete behavioural data. No ground truth on harm, which is a permanent limitation the metric must state rather than paper over.
