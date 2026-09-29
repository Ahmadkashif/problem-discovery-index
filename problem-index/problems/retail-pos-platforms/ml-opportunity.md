# Machine Learning Opportunities — Retail POS Platforms

**Industry:** [[retail-pos-platforms|Retail POS Platforms]]
**Derived from:** [[problems/retail-pos-platforms/high-impact|High Impact]], [[problems/retail-pos-platforms/low-impact-1|Low Impact 1]], [[problems/retail-pos-platforms/low-impact-2|Low Impact 2]], [[problems/retail-pos-platforms/worker-life-1|Worker Life 1]], [[problems/retail-pos-platforms/worker-life-2|Worker Life 2]]

---

## 1. Pooled Sell-Through Curves and Markdown Optimisation
#survival-analysis #gradient-boosting #time-series-forecasting #causal-inference #confidence-intervals #feature-engineering #cross-validation #evaluation-metrics #revenue-impact

**Problem statement:** Markdown timing and depth decide a specialty retailer's seasonal margin and are chosen by looking at the rack. Enterprise retail has had markdown optimisation for two decades; it required planning analysts, which no independent can employ. The POS platforms hold the item-level sales and inventory history those systems consume, across hundreds of thousands of merchants.

**ML task:** Survival modelling of unit sell-through as a function of time-in-season and price, pooled across merchants, plus an optimisation over the markdown schedule
**Input data:** Item-level transactions with price and date; inventory receipts and positions; category and seasonal structure; store and market attributes; comparable items across the merchant base with their own price paths; weather and local seasonality; historical end-of-season residuals and clearance realisations.
**Target:** Units sold per period at a given price, and residual inventory at season end.
**Evaluation metric:** Realised margin under recommended versus actual markdown schedules, evaluated on held-out seasons — a policy comparison rather than a prediction accuracy score. Report calibration of the residual inventory forecast separately, since that is what merchants will check first and what determines whether the recommendation is believed.
**Scope:** Product resolution across merchants is the hard prerequisite and gates everything — without knowing that merchant A's item is comparable to merchant B's, there is no pooling and no model. Price endogeneity is the second difficulty: merchants discount in response to weak demand, so naive estimation recovers their markdown policy rather than the demand response. Cross-merchant variation in pricing for comparable goods in comparable markets is the identification strategy. 3-4 ML engineers plus a retail planner, 8-10 months.
**Data availability:** Transaction volume is excellent. Catalogue quality is the binding constraint and is poor exactly in the specialty categories where the value is highest. Cost data is often missing or wrong, which matters because the objective is margin rather than revenue.

---

## 2. Cross-Merchant Product Resolution and Attribute Induction
#bert #word-embeddings #cnns #k-nearest-neighbors #large-language-models #transfer-learning #dbscan #evaluation-metrics

**Problem statement:** The same vendor's item is entered by hundreds of merchants, each typing a partial description in their own words with their own attributes. No canonical record exists, which forces every merchant to duplicate the work and blocks every cross-merchant analysis downstream.

**ML task:** Entity resolution over merchant catalogue records into canonical products, plus induction of per-vertical attribute schemas from what merchants actually record
**Input data:** Merchant catalogue records (names, descriptions, vendor codes, categories, prices, images); vendor line sheets and catalogue documents; UPC and GTIN data where present; merchant vertical and category assignments.
**Target:** A canonical product identifier per merchant catalogue record, with a merged attribute set; and a per-vertical attribute schema.
**Evaluation metric:** Cluster purity and pairwise F1 against a manually adjudicated sample, reported separately for barcoded goods (easy, high baseline) and specialty goods (the actual problem). Silent false merges are the dangerous error — combining two genuinely different products corrupts every downstream analysis — so precision must be weighted well above recall.
**Scope:** Text embeddings on short, abbreviated, merchant-authored names do most of the work; product images add substantial signal for apparel and hard goods. Vendor style codes are the strongest single feature where present and are inconsistently captured. Attribute schema induction should come from clustering what merchants record rather than from an authored taxonomy, which is how every previous attempt has become stale. 3 ML engineers, 6 months.
**Data availability:** Enormous volume of merchant-authored records, no labels, and merchant catalogues are commercially sensitive — cross-merchant use requires terms most platforms have but should verify. Images are increasingly present and under-used.

---

## 3. Inventory Record Accuracy as a Probability
#bayesian-inference #gradient-boosting #hypothesis-testing #confidence-intervals #change-point-detection #feature-engineering #evaluation-metrics

**Problem statement:** Channel sync propagates the recorded quantity faithfully, including when it is wrong. Merchants compensate with buffer stock, a permanent availability tax applied because nobody trusts the count. Nothing models how wrong the count is likely to be.

**ML task:** Posterior estimation of true on-hand quantity given recorded quantity, time since verification, and item and store characteristics; plus classification of discrepancy cause
**Input data:** Recorded quantities and their history; cycle count and physical inventory results as ground truth observations; sales velocity; price; category; receiving records; return transactions; register void and correction events; store layout and staffing; time since last verified count.
**Target:** Counted quantity at verification, giving the error relative to the record; and for diagnosis, the eventual attributed cause where one was determined.
**Evaluation metric:** Calibration of the posterior — when the model says the count is right with 95% confidence, it should be right 95% of the time — measured against subsequent counts. For counting prioritisation, error units discovered per counting hour against the current rotation, which is the number that justifies the change.
**Scope:** Cycle count results are the only ground truth and they are sparse and non-randomly located, which biases the training set toward whatever the rotation happens to cover. Deliberately randomising a small fraction of counts is a cheap and necessary fix. Discrepancy cause classification is limited by the fact that causes are rarely recorded, so it starts as unsupervised pattern analysis. 2 ML engineers, 4-5 months.
**Data availability:** Transaction and adjustment data is complete. Count history exists but is often stored as adjustments rather than as count events, losing the distinction between "we counted and it was right" and "nothing happened."

---

## 4. Category-Level Sales Forecasting for Open-to-Buy
#time-series-forecasting #gradient-boosting #exponential-smoothing #linear-regression #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Open-to-buy planning at independents runs on a spreadsheet with planned sales set as last year plus a percentage, goes stale within weeks, and is the basis for purchase commitments made months ahead with minimum order quantities attached.

**ML task:** Multi-horizon category-level sales forecasting per store with prediction intervals, feeding a budget projection that updates continuously
**Input data:** Category sales history by store and week; inventory positions at cost; on-order commitments with expected receipt dates; markdown history; store attributes and market; local seasonality, weather and events; comparable stores across the merchant base for categories with thin local history.
**Target:** Category sales by month for the planning horizon, and the derived open-to-buy balance.
**Evaluation metric:** Interval calibration matters more than point accuracy, because the buyer's decision is how much room the plan has rather than what the number is. Report performance against the merchant's own last-year-plus-percentage baseline, which is the honest comparison and a low bar the category has never been measured against.
**Scope:** Pooling across comparable stores is what makes forecasting viable for a single independent with thin history, and requires the same product and category resolution as the markdown work. The larger practical value may be simply maintaining the open-to-buy view live from data already in the platform, which requires no forecasting at all and should ship first. 2 ML engineers plus a merchandise planner, 4-5 months.
**Data availability:** Sales history is strong. Inventory at cost and on-order commitments are frequently incomplete or maintained outside the system, which is the main obstacle to a live plan and is a product problem rather than a modelling one.
