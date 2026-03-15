# Machine Learning Opportunities — Restaurant Suppliers

**Industry:** [[restaurant-suppliers|Restaurant Suppliers]]
**Derived from:** [[problems/restaurant-suppliers/high-impact|High Impact]], [[problems/restaurant-suppliers/low-impact-1|Low Impact 1]], [[problems/restaurant-suppliers/low-impact-2|Low Impact 2]], [[problems/restaurant-suppliers/worker-life-1|Worker Life 1]], [[problems/restaurant-suppliers/worker-life-2|Worker Life 2]]

---

## 1. Customer Churn Prediction from Order Pattern Analysis
#gradient-boosting #binary-classification #time-series-forecasting #tabular-ml #revenue-impact

**Problem statement:** Predict which restaurant accounts will significantly reduce or stop ordering within the next 30 days, using historical order behavior, so sales reps can intervene before the account is lost.

**ML task:** Binary classification (churning vs. stable) with time-series feature engineering on rolling order windows.
**Input data:** 2-3 years of order-level ERP data per account: order dates, line items, dollar amounts, SKU categories (protein, produce, dairy, dry goods, smallwares), payment timing, credit memo history, rep visit logs (if available). Enrichment: account tenure, restaurant type (pizza, fine dining, fast casual), seasonal flags.
**Target:** Binary label — account churned (>60% revenue decline over 30 days vs. trailing 90-day baseline) within the next 30 days. Positive class is rare (~3-5% monthly).
**Evaluation metric:** Recall at top-K (optimize for recall in the top 10 accounts per rep per week — the rep can only act on ~10 flags). Secondary: precision to avoid alert fatigue. F2-score is the right composite metric, weighting recall 2x over precision.
**Scope:** 2-person team (ML engineer + data engineer for ERP extraction), 8-12 week build. Main effort is ERP data extraction and feature engineering — the modeling itself is standard gradient boosting. Requires per-distributor training due to regional and product-mix differences, but transfer learning from a base model is feasible once 3-4 distributors are onboarded.
**Data availability:** Order history data exists in every distributor's ERP but is rarely exported or warehoused. The biggest barrier is getting clean account-level data with consistent account IDs (reps sometimes create duplicate accounts). Churn labels must be constructed retrospectively — no distributor currently tracks churn systematically.

---

## 2. Cross-Sell Recommendation for Sales Reps
#gradient-boosting #recommendation #tabular-ml #revenue-impact

**Problem statement:** Identify which product categories each restaurant account is under-purchasing relative to comparable accounts, and generate specific cross-sell recommendations for the sales rep's next visit.

**ML task:** Recommendation via collaborative filtering on account-category purchase matrices, combined with a ranking model for prioritization.
**Input data:** Account-level monthly spend by product category (8-12 categories: proteins, seafood, produce, dairy, dry goods, beverages, smallwares, cleaning, paper goods). Account metadata: restaurant type, seating capacity, cuisine, price tier. Rep-account relationship tenure.
**Target:** For each account, a ranked list of product categories with predicted incremental monthly spend if the rep pitches the category. Ground truth: accounts that added a new category after a rep visit (observable in order history).
**Evaluation metric:** Mean Average Precision @ 3 (reps can realistically pitch 2-3 new categories per visit). Revenue-weighted — a correct protein recommendation is worth more than a correct paper goods recommendation.
**Scope:** 3-person team, 10-14 weeks. Collaborative filtering on a matrix of ~1,000 accounts x 10 categories is computationally trivial; the challenge is building the feedback loop (did the rep act on the recommendation, and did the account add the category?). Requires integration with rep mobile workflow to surface recommendations at the right moment.
**Data availability:** All data exists in ERP order history. Category taxonomy may need normalization across distributors. The cold-start problem is manageable — new accounts can be matched to similar restaurant profiles within 2-3 orders.

---

## 3. Demand Forecasting for Perishable Procurement
#gradient-boosting #time-series-forecasting #tabular-ml

**Problem statement:** Forecast aggregate customer demand for perishable product categories (proteins, seafood, produce) at the SKU-group level, 5-7 days ahead, to reduce spoilage and stockouts.

**ML task:** Multi-step time-series regression — predict daily demand per SKU-group for days T+3 through T+7 (the procurement lead time window).
**Input data:** Daily order volumes by SKU-group (last 2-3 years), commodity price indices (USDA protein prices, produce market reports), day-of-week and holiday features, local event calendars (convention center bookings, sports schedules), weather forecasts, account-level menu change signals (where available from ordering portals). Exogenous: restaurant openings/closings in the territory.
**Target:** Daily demand in pounds or cases per SKU-group, 5-7 days ahead. Asymmetric loss: under-forecasting (stockout) costs 3-5x over-forecasting (spoilage) because stockouts trigger competitor orders.
**Evaluation metric:** Weighted Mean Absolute Percentage Error (WMAPE) with asymmetric penalty — 3x weight on under-forecast errors. Target: WMAPE under 15% for top-20 SKU-groups by volume.
**Scope:** 2-person team, 12-16 weeks. Feature engineering for perishable demand is the hard part — protein prices move daily and create substitution cascades (expensive salmon → cheaper halibut) that the model must capture. Gradient boosting with lag features and external regressors outperforms classical ARIMA approaches in this domain. Needs retraining monthly as seasonal patterns shift.
**Data availability:** Order history is available in ERP. USDA market reports and commodity prices are publicly available. Local event data can be scraped or purchased (PredictHQ). Menu change data is the scarcest signal — available only for accounts using digital ordering portals (~30% penetration).

---

## 4. Delivery Route Optimization with Time Window Constraints
#reinforcement-learning #regression #tabular-ml #automation

**Problem statement:** Optimize daily delivery routes across 40-80 stops per truck, respecting restaurant-specific delivery windows (most restaurants require delivery before 10 AM prep start or during a 2-hour afternoon window) and truck capacity constraints for mixed loads (frozen, refrigerated, dry).

**ML task:** Vehicle Routing Problem with Time Windows (VRPTW) — a combinatorial optimization problem enhanced with ML for travel time prediction and delivery duration estimation.
**Input data:** Daily stop list with GPS coordinates, delivery time windows per account, order weight/volume by temperature zone (frozen, cooler, dry), historical delivery completion times, real-time traffic data (Google Maps API), truck capacity specs, driver shift constraints (DOT hours of service).
**Target:** Optimal route sequence per truck minimizing total drive time while satisfying all time window constraints. Secondary objective: minimize the number of trucks required.
**Evaluation metric:** Total route-hours per day (primary), percentage of on-time deliveries (constraint — must exceed 95%), driver overtime hours (minimize). Compare against current dispatcher-planned routes as baseline.
**Scope:** 3-person team (ML engineer, backend engineer, mobile developer for driver app), 16-20 weeks. The VRPTW solver itself can use OR-Tools or a commercial engine (Routific, OptimoRoute); the ML layer predicts travel times and service durations more accurately than static estimates. Reinforcement learning can optimize over the dispatcher's daily adjustments. Integration with driver mobile app and dispatch system is the primary engineering challenge.
**Data availability:** GPS tracking data from delivery trucks (most distributors have basic telematics). Historical delivery timestamps from driver check-in apps or proof-of-delivery systems. Account time windows are known but often stored informally in dispatcher notes — digitization effort required.
