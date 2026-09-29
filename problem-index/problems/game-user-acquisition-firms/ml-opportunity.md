# Machine Learning Opportunities — Game User Acquisition Firms

**Industry:** [[game-user-acquisition-firms|Game User Acquisition Firms]]
**Derived from:** [[problems/game-user-acquisition-firms/high-impact|High Impact]], [[problems/game-user-acquisition-firms/low-impact-1|Low Impact 1]], [[problems/game-user-acquisition-firms/low-impact-2|Low Impact 2]], [[problems/game-user-acquisition-firms/worker-life-1|Worker Life 1]], [[problems/game-user-acquisition-firms/worker-life-2|Worker Life 2]]

---

## 1. Heavy-Tail Lifetime Value Prediction
#survival-analysis #probability-distributions #bayesian-inference #maximum-likelihood-estimation #gradient-boosting #confidence-intervals #loss-functions #evaluation-metrics

**Problem statement:** Most revenue comes from a very small fraction of players, and at prediction time almost none of them have distinguished themselves. A model minimising average error fits the mass of low-value players and is systematically wrong about the quantity that determines the outcome.

**ML task:** Predict the full value distribution per cohort rather than its mean, with a loss respecting the heavy tail, plus the revision profile between early and mature estimates
**Input data:** Early cohort behaviour at the granularity attribution permits; acquisition source, creative, geography and platform; historical cohorts with fully matured value; the game's content and monetisation state during each cohort's life; suppression status and campaign volume.
**Target:** Cohort value at 90 and 180 days, as a distribution — and specifically the upper quantiles, which is where the decision lives.
**Evaluation metric:** Tail accuracy reported separately and prominently: performance at the 95th and 99th percentiles of cohort value, since a model with excellent average error and a poor tail has failed at the only thing it was for. Report the revision profile — how much cohorts like this one moved between day three and day thirty — because that number should govern scaling decisions and is currently invisible to the person making them. Calibration of the predictive distribution matters more than point accuracy, as the output prices a bid.
**Scope:** Threshold-based identifier suppression depends on campaign volume, making it a modellable missingness mechanism rather than absence — ignoring it biases against small campaigns and quietly penalises the exploration that finds new sources. 3 ML engineers, 9-12 months.
**Data availability:** Matured cohorts accumulate slowly, which paces validation regardless of engineering speed. Attribution granularity is the binding constraint on features.

---

## 2. Separating Player Value From Content Effect
#causal-inference #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** A cohort's realised value depends heavily on what the game ships in the following months, and the model attributes all of it to the acquisition source — which misprices sources, misdirects budget, and makes an unresolvable quarterly argument between UA and the game team.

**ML task:** Decompose realised cohort value into acquisition-attributable and content-attributable components, using the same sources observed across many content periods
**Input data:** Cohort outcomes by acquisition source across time; content release and event calendar with type and reception; monetisation and balance changes; the same sources' performance in different content periods; player-level engagement with specific content.
**Target:** The share of cohort value attributable to who was acquired versus what shipped afterwards.
**Evaluation metric:** The decomposition must reconstruct observed cohort values, with an explicit residual. Validate by prediction: source quality estimates corrected for content should predict future cohort performance better than uncorrected ones on held-out periods — if they do not, the decomposition is describing noise. Report a content-adjusted baseline per source, which is the artefact that makes UA evaluation fair and is the practical output.
**Scope:** This is straightforward analysis that nobody runs because neither function benefits from raising it, and both would benefit from having it. It also directly improves source evaluation, which is the commercial argument that gets it funded. 2 ML engineers plus a causal specialist, 6-9 months.
**Data availability:** Complete on both sides and held by different teams, which is the entire obstacle.

---

## 3. Creative Claim Accuracy and Cohort-Value Creative Evaluation
#cnns #transformers #contrastive-learning #causal-inference #survival-analysis #gradient-boosting #compliance #evaluation-metrics

**Problem statement:** Ads depicting mechanics the game does not contain are widespread and are evaluated on install cost, which hides their entire effect. Whether they acquire anything of value once the resulting churn is counted is measurable and largely unmeasured.

**ML task:** Compare what a creative depicts against what the game actually contains, and evaluate creative on cohort value at 30 and 90 days rather than on installs
**Input data:** Creative video, playable content and static assets; the game's own build — mechanics, art style, progression, interface — as the reference; install and early retention by creative; cohort value outcomes at the granularity attribution permits; platform policy enforcement history.
**Target:** A claim-accuracy assessment per creative, and cohort value attributable to the creative that acquired the player.
**Evaluation metric:** For accuracy, agreement with human judgement on a labelled set, reported by genre — the line between attractive presentation and misrepresentation is genre-specific and the model should be calibrated per genre rather than universally. For value, the decisive comparison is creative ranked by install cost against creative ranked by day-90 cohort value; if the ordering differs substantially, the industry's standard evaluation is selecting the wrong creative, which is the finding.
**Scope:** Aggregated attribution suppresses creative-level outcome data, so the evaluation works at cohort level with deliberate creative-to-cohort structuring. Quantifying policy risk — which creatives are most likely to draw enforcement and what that costs — from the operator's own history and the public record turns an internal argument that is currently moral into one that is commercial, which is the form in which it can be won. 2-3 ML engineers with multimodal experience, 9-12 months.
**Data availability:** Creatives and builds are held. Cohort-level value linkage requires deliberate campaign structuring.

---

## 4. Portfolio Cross-Promotion Under a Net Objective
#convex-optimization #causal-inference #markov-decision-processes #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** A publisher's own games are its cheapest acquisition channel, and allocation between them is decided by internal negotiation against per-title install targets — while the cost of moving a player from one title to another goes unmeasured.

**ML task:** Estimate the net portfolio effect of cross-promotion per title pair and player segment using randomised or staggered exposure, then allocate promotions per player against a portfolio objective
**Input data:** Cross-promotion exposure with randomisation; player value and engagement in the source title before and after; destination title adoption and value; title pair characteristics — genre, session length, time of day; player identity resolved across the publisher's titles; per-title profit and loss structure.
**Target:** Total portfolio revenue over a long horizon, not destination installs.
**Evaluation metric:** The effect on the source title must be measured and reported alongside the destination's gain, because that is the cost nobody currently counts. The interesting output is the complement-versus-substitute classification per title pair — whether cross-promotion adds portfolio revenue or merely moves it — which is measurable, currently assumed, and would change which titles a publisher promotes to which audiences.
**Scope:** Randomisation is available to every publisher and is the only route to the net effect; observational comparison is confounded by which players get shown what. The allocation itself is a constrained optimisation once the effects are known. The obstacle is organisational: where each title carries its own profit and loss, a portfolio objective requires someone above both to own it. 2 ML engineers, 6-9 months.
**Data availability:** Complete within a publisher. Cross-title identity resolution is usually already in place through platform or publisher accounts.
