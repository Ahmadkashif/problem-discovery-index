# Machine Learning Opportunities — Auto Body Shops

**Industry:** [[auto-body-shops|Auto Body Shops]]
**Derived from:** [[problems/auto-body-shops/high-impact|High Impact]], [[problems/auto-body-shops/low-impact-1|Low Impact 1]], [[problems/auto-body-shops/low-impact-2|Low Impact 2]], [[problems/auto-body-shops/worker-life-1|Worker Life 1]], [[problems/auto-body-shops/worker-life-2|Worker Life 2]]

---

## 1. Hidden Damage Prediction from Exterior Collision Photos
#cnns #linear-regression #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #matrix-algebra #tacit-knowledge-ml

**Problem statement:** Experienced collision estimators look at external damage and predict hidden damage behind panels — they've internalized how force propagates through vehicle-specific crush structures over thousands of teardowns. This tacit knowledge means their initial estimates capture 80-90% of actual damage, while new estimators miss 30-50%, triggering costly supplement cycles.

**ML task:** Multi-label regression (predict probability and severity of hidden damage for each component behind visible damage)
**Input data:** Pre-teardown exterior photos from multiple angles (4-8 per vehicle), vehicle make/model/year, impact point and direction (annotated or inferred), visible damage severity indicators
**Target:** Per-component hidden damage predictions: binary presence + severity score for 30-50 common hidden components (radiator support, condenser, absorber, rails, cross-members, inner panels), calibrated to estimate dollar amounts
**Evaluation metric:** Component-level AUC for presence detection; MAE on dollar amount predictions. Primary business metric: reduction in supplement-to-initial-estimate ratio.
**Scope:** Requires 20,000-50,000 paired photo sets (pre-teardown + post-teardown itemized damage). Data exists — every teardown generates this pair — but it's not systematically collected. 3-4 person team, 12-18 month build. Vehicle-specific models needed (2019 Camry ≠ 2019 F-150). Cold start problem for rare models.
**Data availability:** CCC ONE processes millions of estimates annually with photos. Pairing pre-teardown photos with final supplement data is the key data engineering challenge. Partnership with CCC or Mitchell required for scale. Individual shops generate 500-2,000 repairs per year — sufficient for common models only.

---

## 2. Repair Time and Cycle Time Prediction
#gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff

**Problem statement:** Cycle time is the #1 DRP scorecard metric, but predicting it requires understanding parts availability, supplement probability, paint booth capacity, and technician workload simultaneously.

**ML task:** Regression (predict total cycle time in days from initial estimate characteristics)
**Input data:** Initial estimate line items, vehicle make/model/year, damage severity indicators, parts type mix (OEM/aftermarket/recycled), shop capacity metrics (current WIP, booth utilization), insurer identity (supplement behavior patterns), historical cycle times for similar repairs
**Target:** Calendar days from drop-off to delivery
**Evaluation metric:** MAE in days; percentage within 1-day accuracy. Secondary: identify which repairs are at risk of exceeding DRP thresholds.
**Scope:** Trainable on 10,000-50,000 historical repairs from shop management systems. 2-person team, 4-6 months. Feature engineering around parts availability and insurer behavior patterns is the key challenge.
**Data availability:** Body shop management systems contain full repair timelines. CCC and Mitchell have aggregated data across thousands of shops. Multi-shop data improves parts delay prediction.

---

## 3. Parts Availability and Delivery Prediction
#gradient-boosting #time-series-forecasting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #expectation-variance-covariance

**Problem statement:** Parts delays cause 30-40% of cycle time extensions. Parts managers order based on listed availability, which is often inaccurate — parts show "in stock" but arrive 3-5 days late.

**ML task:** Regression (predict actual delivery date for each part order)
**Input data:** Part number, supplier, listed availability, historical delivery performance for this supplier/part combination, time of year, geographic location, part type (OEM vs. aftermarket)
**Target:** Actual delivery date (or days-to-delivery)
**Evaluation metric:** MAE in days; percentage of predictions within 1-day accuracy. Critical: catch long-tail delays (>7 days) which cause the most cycle time damage.
**Scope:** Trainable on 100,000+ historical parts orders. 1-2 person team, 3-4 months. Integration with PartsTrader and supplier APIs provides rich features.
**Data availability:** Parts order history with timestamps exists in shop management systems and PartsTrader. Delivery confirmation data less consistently recorded — requires PO-to-receipt matching.

---

## 4. Supplement Amount Prediction for Insurance Negotiations
#gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff

**Problem statement:** Shops know supplements are coming but can't predict the amount, leading to poor cash flow planning and production scheduling. Insurers use supplement uncertainty as leverage.

**ML task:** Regression (predict total supplement amount and number of supplement rounds)
**Input data:** Initial estimate total and line items, vehicle make/model/year, impact type and severity, insurer identity, shop's historical supplement patterns, estimator identity
**Target:** Total supplement dollar amount; secondary: number of supplement rounds needed
**Evaluation metric:** MAE on dollar amount; MAPE as percentage of initial estimate
**Scope:** Trainable on 20,000-50,000 repair files with complete initial + supplement data. 1-2 person team, 3-4 months. Challenge: supplement amounts are partly a function of negotiation skill, not just damage — model must separate damage-driven from negotiation-driven variance.
**Data availability:** Estimating platforms (CCC, Mitchell) contain complete estimate histories. Insurer-specific patterns are learnable from sufficiently large datasets. Data partnership with estimating platform required.

---

## 5. Paint Color Match Prediction
#cnns #linear-regression #transfer-learning #loss-functions #evaluation-metrics #gradient-descent #backpropagation #tacit-knowledge-ml

**Problem statement:** Matching paint on a repaired panel to the existing vehicle finish requires accounting for paint oxidation, sun exposure patterns, clear coat condition, and the specific spray technique. Experienced painters adjust formulas by eye; new painters rely on manufacturer codes that rarely match perfectly on vehicles over 3 years old.

**ML task:** Regression (predict color formula adjustments from vehicle condition photos)
**Input data:** Photos of existing paint under controlled lighting (adjacent panel to repair area), vehicle age, color code, geographic region (sun exposure patterns), clear coat condition assessment
**Target:** Formula adjustment parameters: tint bias (red/blue/yellow), metallic/pearl density adjustment, clear coat blending approach
**Evaluation metric:** Delta-E color difference measurement (ΔE < 1.0 is invisible to human eye). Target: ΔE < 1.5 on 90% of matches.
**Scope:** Requires spectrophotometer ground truth paired with photos. 2-3 person team, 9-12 months. Controlled lighting during photo capture is critical. Camera calibration across devices adds complexity.
**Data availability:** Paint mixing systems (PPG, Axalta, BASF) contain formula databases. Pairing actual mixed formulas with photos of the target vehicle is the data collection challenge. Partnership with paint manufacturer needed.
