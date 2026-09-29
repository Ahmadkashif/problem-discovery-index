# Machine Learning Opportunities — Robo-Advisors

**Industry:** [[robo-advisors|Robo-Advisors]]
**Derived from:** [[problems/robo-advisors/high-impact|High Impact]], [[problems/robo-advisors/low-impact-1|Low Impact 1]], [[problems/robo-advisors/low-impact-2|Low Impact 2]], [[problems/robo-advisors/worker-life-1|Worker Life 1]], [[problems/robo-advisors/worker-life-2|Worker Life 2]]

---

## 1. Behavioural Risk Tolerance Estimation
#logistic-regression #gradient-boosting #survival-analysis #bayesian-inference #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering

**Problem statement:** Allocation is determined by a risk score from a six-question form completed in calm conditions about hypothetical losses. The platform then observes what every client actually does in every real decline and never checks the two against each other, so the clients allocated beyond their actual tolerance discover it by selling at the bottom.

**ML task:** Estimation of realised risk tolerance from behavioural sequences, and prediction of capitulation before it happens
**Input data:** Questionnaire responses and assigned scores; login frequency and timing relative to market moves; time on performance screens; allocation changes with direction and timing; contribution pauses and resumptions; withdrawals; behaviour in each prior drawdown with the drawdown's depth and duration; account balance, tenure and goal; realised money-weighted versus time-weighted return.
**Target:** A continuously updated behavioural risk estimate, and the probability of a de-risking action or withdrawal within a short horizon.
**Evaluation metric:** Precision and lead time on capitulation prediction, evaluated only on held-out drawdown episodes, since in-sample performance across a single market regime proves nothing. The harder and more important metric is whether the behavioural estimate predicts next-drawdown behaviour better than the questionnaire score does — a direct head-to-head that has, as far as the public record shows, never been published by anyone holding this data.
**Scope:** Drawdowns are rare, which makes labels sparse in exactly the dimension of interest, so episode-level cross-validation and honest uncertainty matter more than model sophistication. The gap between stated and behavioural tolerance is the headline number and nobody computes it. What to do when the two disagree is a genuine fiduciary question that should be settled with compliance before the model is built, not after. 2 ML engineers and 1 quantitative researcher, 6 months.
**Data availability:** Complete and internal, and unusually clean — the stated preference is recorded before any market event, followed by a full behavioural record. It is the best-structured natural experiment in consumer finance.

---

## 2. Intervention Uplift Measurement
#causal-inference #gradient-boosting #hypothesis-testing #confidence-intervals #large-language-models #bert #evaluation-metrics #revenue-impact

**Problem statement:** Platforms send messages during declines intended to prevent panic selling, and measure them on open rates. Whether any of them change the decision is untested, and the message most commonly sent arrives after the sale has already happened.

**ML task:** Uplift modelling on intervention timing, channel and content, against the decision to sell or pause contributions
**Input data:** Historical interventions with timing, channel and content; recipient behaviour before and after; market conditions at the moment of delivery; the behavioural risk estimate; prior drawdown responses; a randomised holdout arm.
**Target:** The change in probability of capitulation attributable to a specific intervention on a specific client at a specific moment.
**Evaluation metric:** Uplift against a randomised control arm, measured on the decision rather than on engagement. This requires deliberately withholding intervention from a control group during a market decline, which is uncomfortable and is the only way to know whether the intervention works — a platform that has never held out has no evidence that its crisis communications do anything at all, and several plausibly make things worse by drawing attention to the decline.
**Scope:** The valuable finding is likely to be about timing rather than content: the effective intervention is probably earlier and lighter than the current one, and identifying the pre-capitulation window is the useful output. Segment-level heterogeneity matters — the message that steadies one client may alarm another — which is exactly what uplift modelling is for. Ethical review of the holdout design should be genuine rather than procedural. 2 ML engineers and 1 researcher, 5 months.
**Data availability:** Intervention history exists but is usually not randomised, which limits what can be learned from it retrospectively and argues for building the experimental infrastructure before the next decline rather than after.

---

## 3. Per-Client Harvesting Value and Cross-Account Wash-Sale Inference
#monte-carlo-methods #gradient-boosting #time-series-forecasting #dynamic-programming #confidence-intervals #evaluation-metrics #feature-engineering #data-integration

**Problem statement:** Tax-loss harvesting is quoted as a category average that describes almost no individual client, its value depends on inputs the platform already holds, and the wash-sale exposure that could disallow the losses sits in connected workplace and spousal accounts that nobody checks.

**ML task:** Simulation-based per-client value estimation under uncertainty, optimal harvest timing as a stopping problem, and cross-account wash-sale risk detection
**Input data:** Client tax situation, bracket, state and realisable gains; holdings, lots and cost basis; contribution patterns and horizon; volatility and correlation estimates per holding; substitute pair tracking error; connected held-away account holdings and contribution schedules; historical harvest events and their realised tax effect.
**Target:** An expected harvesting benefit with a distribution rather than a point; an optimal harvest trigger per lot; and a wash-sale risk flag with its source named.
**Evaluation metric:** For value estimation, calibration against realised tax effect computed from the client's own filings where available, and otherwise against a rigorous simulation with the assumptions exposed. For timing, the improvement over the current greedy threshold rule measured in after-tax terms across simulated paths. For wash-sale detection, recall matters most, since an undetected disallowance silently invalidates the benefit being marketed.
**Scope:** Greedy harvesting spends the opportunity early in a decline; treating it as an optimal stopping problem with a known horizon and estimable volatility is a clean, well-posed improvement. The fiduciary-differentiating move is telling clients for whom harvesting is worth almost nothing that this is so, which no competitor does and which the platform can compute exactly. Cross-account wash-sale warnings are feasible today for any connected account and are simply not built. 2 ML engineers and 1 quantitative researcher, 5 months.
**Data availability:** Internal holdings and tax data are complete. Held-away coverage depends on client connections and is the limiting factor, which makes connection rate itself worth optimising.

---

## 4. Semantic Communications Supervision and Complaint Detection
#bert #large-language-models #k-means-clustering #word-embeddings #k-nearest-neighbors #evaluation-metrics #compliance #automation

**Problem statement:** Supervision reviews client communications using lexicon triggers that fire on words rather than meaning, producing high volume and low yield. Meanwhile a templated message reaching two hundred thousand clients receives the same queue position as one reaching four.

**ML task:** Semantic classification of communications for performance claims, unfair risk presentation and complaint indicators, with retrieval over prior supervisory decisions
**Input data:** Historical communications with their review outcomes and reasons; marketing approvals and rejections; chat transcripts and call summaries; client messages logged as complaints and those not logged; the firm's own interpretive precedents; regulatory rule text and enforcement themes.
**Target:** A supervisory concern classification per communication, and a ranked set of the firm's own prior decisions on similar language.
**Evaluation metric:** Recall on genuine issues is the binding requirement — a missed performance promise in a message reaching the full client base is an examination finding, so the operating point must favour over-flagging — combined with a substantial reduction in total items reviewed relative to lexicon triggering. For complaint detection, recall again dominates, with abstention preferred over a confident negative, because the regulatory definition of a complaint is broader than intuition suggests.
**Scope:** Reach weighting needs no model at all and should ship first: ordering the queue by how many clients a message reaches is a one-line change with real risk reduction. Precedent retrieval is the consistency win and is what an examiner actually tests. Pre-submission checking for marketing and product teams catches most violations before the queue and quietly repairs the adversarial dynamic, since nearly all of them are unintentional. 1 ML engineer, 4 months.
**Data availability:** Historical communications and review outcomes are retained under recordkeeping rules, which makes this an unusually well-labelled corpus. Rejection reasons are often terse and benefit from structuring.
