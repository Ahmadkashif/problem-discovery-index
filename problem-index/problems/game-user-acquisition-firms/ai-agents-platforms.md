# AI Agents & Platform Opportunities — Game User Acquisition Firms

**Industry:** [[game-user-acquisition-firms|Game User Acquisition Firms]]

---

## 1. Cohort Value Platform
#ai-platform #survival-analysis #probability-distributions #bayesian-inference #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact

**Concept:** A platform built for the distribution that actually matters. It predicts cohort value as a full distribution with the upper quantiles as the reported quantity, fitted and evaluated on tail accuracy rather than average error — which ranks cohorts differently from every standard implementation. It attaches the revision profile to every immature estimate, so a day-three number arrives with how much cohorts like this one typically moved by day thirty, which is the single most expensive recurring error in the discipline. And it decomposes realised value into what was acquired and what the game shipped afterwards, which corrects a systematic misattribution in source evaluation.

**Inputs:** Early cohort behaviour at available attribution granularity; source, creative, geography and platform; matured historical cohorts; the content and monetisation state during each cohort's life; campaign volume and suppression status.

**Outputs / Actions:** Predictive distributions with calibrated upper quantiles, because the output prices a bid. Revision profiles on every immature cohort. A content-adjusted source ranking that separates acquisition quality from what happened to those players later. Explicit modelling of threshold suppression, so small campaigns and new geographies stop being quietly penalised — which is where exploration happens and where the current environment biases hardest.

**Why now:** Aggregated attribution removed the user-level signal that made naive modelling tolerable, which forces the shift to cohort-level distributional prediction anyway — and the tail-aware version is the one worth building while the rebuild is happening.

**Market:** Mobile and PC game publishers, the UA agencies managing their spend, and the measurement partners whose predicted-value features currently ship generically fitted.

---

## 2. Creative Accuracy and Value Platform
#ai-platform #cnns #transformers #contrastive-learning #causal-inference #survival-analysis #compliance #evaluation-metrics

**Concept:** A platform that answers the question this industry has avoided. It compares what a creative depicts against what the game actually contains — mechanics, art style, progression, interface — as a routine automated check rather than an unspoken judgement, calibrated per genre because the line between attractive presentation and misrepresentation is genre-specific. And it evaluates creative on cohort value at 30 and 90 days rather than on install cost, attributing the churn a misleading ad causes back to the creative that caused it.

**Inputs:** Creative video, playables and static assets; the game build as the accuracy reference; install, retention and cohort value outcomes at available granularity; platform policy enforcement history across the operator's portfolio and the public record.

**Outputs / Actions:** A claim-accuracy score per creative with the specific divergences named. Creative ranked by day-90 cohort value beside creative ranked by install cost — and if the orderings differ substantially, that comparison is the finding, because it means the industry's standard evaluation selects the wrong creative. A quantified policy risk estimate, which turns an internal argument that is currently moral into one that is commercial and therefore winnable.

**Why now:** Platform enforcement is uneven but increasing and consumer protection bodies in several jurisdictions have taken an interest. An industry that measures this itself and finds the practice unprofitable removes it on its own terms; one that waits has it removed on worse ones.

**Market:** Game publishers and UA agencies, the creative production studios building the ads, and the ad networks whose policy enforcement currently rests on review rather than measurement.

---

## 3. Portfolio and Roadmap Coordination Agent
#ai-agent #convex-optimization #causal-inference #survival-analysis #time-series-forecasting #confidence-intervals #worker-facing #workflow-orchestration

**Concept:** An agent covering the two coordination failures that cost publishers most. On cross-promotion, it measures the net portfolio effect of every title pair and segment using randomised exposure — including the cost to the source title, which nobody counts — classifies pairs as complements or substitutes, and allocates promotions per player against total portfolio revenue rather than per-title install targets. On the UA-content relationship, it builds the content roadmap into payback forecasts, updates them when the roadmap moves, and evaluates UA against a content-adjusted baseline so the manager is measured on their actual contribution.

**Inputs:** Cross-promotion exposure with randomisation; player value in source and destination titles; cross-title identity; per-title profit and loss structure; the content and event roadmap with expected retention and monetisation effects; cohort outcomes across content periods.

**Outputs / Actions:** Net cross-promotion effects per title pair, with the source cost stated — which converts an internal negotiation into an optimisation. A complement-versus-substitute classification that changes which titles get promoted to which audiences. Payback forecasts that carry the roadmap dependency explicitly, turning a hidden risk into a stated assumption. Content-adjusted UA evaluation, which makes a precise-looking metric actually fair and defuses a quarterly dispute that both functions currently have no evidence for.

**Why now:** Acquisition costs rose enough after tracking restrictions that owned channels and portfolio effects matter materially more than they did, and the coordination between UA and content is still managed as two separate businesses in most publishers.

**Market:** Multi-title game publishers, the UA and portfolio functions inside them, and the agencies managing spend across a client's portfolio who currently see only one title at a time.
