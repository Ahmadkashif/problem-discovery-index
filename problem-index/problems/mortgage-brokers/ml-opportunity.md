# Machine Learning Opportunities — Mortgage Brokers

**Industry:** [[mortgage-brokers|Mortgage Brokers]]
**Derived from:** [[problems/mortgage-brokers/high-impact|High Impact]], [[problems/mortgage-brokers/low-impact-1|Low Impact 1]], [[problems/mortgage-brokers/low-impact-2|Low Impact 2]], [[problems/mortgage-brokers/worker-life-1|Worker Life 1]], [[problems/mortgage-brokers/worker-life-2|Worker Life 2]]

---

## 1. Lender Approval Prediction & Ranking (Tacit Knowledge Capture)
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #probability-distributions #tacit-knowledge-ml #revenue-impact

**Problem statement:** Experienced mortgage brokers intuitively match borrower profiles to the right wholesale lender from a panel of 30-50 options, weighing credit nuances, lender overlays, current appetite, and turn times in a judgment that takes years to develop and cannot be articulated as rules. This tacit expertise must be captured as a ranking model.

**ML task:** Learning-to-rank (pairwise or listwise) with per-lender approval probability estimation
**Input data:** Borrower features from 1003 application (credit score, DTI, LTV, employment type, income documentation type, property type, loan amount, loan purpose, occupancy type), lender features (current rate sheet pricing, published overlays, recent 30-day approval/denial rates, average turn time, lock policies), and historical submission-outcome pairs from the brokerage's LOS.
**Target:** Ranked list of lenders ordered by composite score of approval probability, rate competitiveness, and expected close speed. Ground truth is the actual submission outcome (approved/denied/counter-offered) and final rate/terms achieved.
**Evaluation metric:** NDCG@5 for ranking quality; secondary metrics of approval-rate lift vs. baseline (the broker's historical first-choice accuracy) and mean rate delta (did the model's top pick yield a better rate than the broker's actual choice). Recall matters more than precision — missing a good lender is worse than including one that doesn't work out.
**Scope:** Requires 6-12 months of historical loan-level submission data with outcomes from the brokerage's LOS, plus integration with lender rate sheet APIs or scraped rate data. Initial build for a single brokerage with 1,000+ annual submissions is a 2-3 person team over 4-6 months. Biggest challenge is encoding lender overlays — many are PDF documents updated weekly — into structured features. The model must retrain or fine-tune frequently (weekly or biweekly) as lender appetites shift.
**Data availability:** Submission-outcome data exists in every LOS but is rarely exported or analyzed. Lender rate sheets are distributed daily via email or portals (Optimal Blue, Mortech, Lender Price) but not in ML-ready format. Labeling is implicit — the outcome is the label — but capturing "what the senior broker would have chosen" for counterfactual training requires active data collection (shadow recommendations).

---

## 2. Borrower Fall-Through Prediction
#gradient-boosting #logistic-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #bias-variance-tradeoff #revenue-impact

**Problem statement:** 20-35% of mortgage applications that reach processing stage fall through before closing — borrowers find a better rate, fail to provide documents, lose qualification due to job changes, or simply go dark. Brokers invest 10-20 hours of processor time per file before discovering it won't close.

**ML task:** Binary classification — will this loan close or fall through?
**Input data:** Application-stage features (credit score, DTI, LTV, loan amount, property type, rate locked vs. floating), behavioral signals (response time to document requests, number of outstanding conditions, days since last borrower contact, referral source type), and market signals (rate movement since application, competitor rate positioning).
**Target:** Binary label: closed vs. fell through. Predicted as a probability score updated daily throughout the pipeline.
**Evaluation metric:** AUROC with emphasis on precision at high-recall operating points — the brokerage wants to catch 80%+ of fall-throughs early, even at the cost of some false positives that trigger extra attention on loans that would have closed anyway.
**Scope:** Requires 2-3 years of historical pipeline data (2,000-5,000 closed + fallen-through loans). A single ML engineer can build this in 2-3 months. Feature engineering around behavioral signals (borrower responsiveness patterns) is the key differentiator vs. a naive credit-score model.
**Data availability:** All data lives in the LOS. The main gap is behavioral timestamps — most LOS platforms log document uploads and status changes but don't systematically track borrower response times to requests. A lightweight tracking layer may need to be added.

---

## 3. Rate Lock Timing Optimization
#lstms-and-grus #time-series-forecasting #rnns #backpropagation #gradient-descent #loss-functions #evaluation-metrics #expectation-variance-covariance #revenue-impact

**Problem statement:** Brokers must decide daily whether to lock or float each loan in their pipeline. The decision depends on rate direction forecasts, days to expected closing, borrower rate sensitivity, and lock expiration costs — but brokers currently decide by gut.

**ML task:** Time-series forecasting of short-term rate movements (1-14 day horizon) combined with a decision layer that maps forecasts to lock/float recommendations per loan.
**Input data:** Daily MBS pricing (FNCL 30-year coupon stack), 10-year Treasury yields, Fed Funds futures, economic indicator releases (NFP, CPI, PCE, housing starts), Fed commentary sentiment scores, and per-loan context (current rate, lock expiration window, days to expected close, borrower rate sensitivity estimate).
**Target:** Directional rate movement over 1, 3, 7, and 14-day horizons (continuous bps change). Secondary target: optimal lock/float decision per loan evaluated by realized rate vs. counterfactual.
**Evaluation metric:** MAE on bps change prediction; Sharpe-like ratio on lock timing decisions (average bps saved per lock decision normalized by variance). The model must beat a "lock immediately" baseline by at least 3-5 bps on average to justify the complexity.
**Scope:** This is the hardest ML problem in the set. Rate forecasting in short horizons is noisy and regime-dependent. A team of 2 (one quant/ML, one mortgage domain expert) needs 4-6 months minimum. Historical MBS and Treasury data is freely available; the pipeline integration and per-loan decision layer is the custom work. Backtesting must account for look-ahead bias and regime changes.
**Data availability:** MBS and Treasury data is publicly available (FRED, Bloomberg, MBS Live archives). Loan-level lock timing history exists in the LOS. The challenge is not data volume but signal-to-noise — short-term rate movements are partially efficient.

---

## 4. Referral Source ROI Prediction
#gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #descriptive-statistics #revenue-impact

**Problem statement:** Mortgage brokers spend 15-30% of revenue on referral relationships (real estate agents, financial planners, builders, past clients) but have no systematic way to predict which referral sources will produce closed loans vs. unqualified leads. Marketing spend is allocated by relationship warmth, not data.

**ML task:** Regression — predicted lifetime closed-loan value per referral source over the next 12 months.
**Input data:** Historical referral source features (referral volume by month, lead-to-close conversion rate, average loan size, referral consistency/recency, source category — realtor vs. builder vs. past client vs. financial planner), relationship investment features (meals/events/gifts spent, co-marketing costs, time invested in relationship), and market context (source's own business volume trends, geographic market conditions).
**Target:** 12-month forward closed-loan commission revenue attributable to each referral source. Ground truth is the actual revenue realized, available after the prediction window.
**Evaluation metric:** MAE on revenue prediction; secondary metric of rank correlation (Spearman) between predicted and actual source value — the brokerage cares more about correctly ranking sources than nailing the exact dollar figure.
**Scope:** Simplest model in this set. A single analyst/ML engineer can build it in 4-6 weeks using 3-5 years of CRM and LOS data. The main challenge is data hygiene — referral source attribution is often inconsistently recorded in CRM systems, requiring cleanup before modeling.
**Data availability:** CRM data (referral source, lead date, contact history) and LOS data (loan close date, commission amount) exist in separate systems. Joining them requires a referral source ID match that may need manual reconciliation for historical data. Going forward, clean attribution tagging at lead intake solves this.
