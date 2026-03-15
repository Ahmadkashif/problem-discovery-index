# Machine Learning Opportunities — Food Distributors

**Industry:** [[food-distributors|Food Distributors]]
**Derived from:** [[problems/food-distributors/high-impact|High Impact]], [[problems/food-distributors/low-impact-1|Low Impact 1]], [[problems/food-distributors/low-impact-2|Low Impact 2]], [[problems/food-distributors/worker-life-1|Worker Life 1]], [[problems/food-distributors/worker-life-2|Worker Life 2]]

---

## 1. Perishable Demand Forecasting with Censored Demand Correction
#gradient-boosting #lstm #time-series-forecasting #tabular-ml #revenue-impact

**Problem statement:** Predict daily demand at the SKU-customer-segment level for 2,000-10,000 perishable products with 3-14 day shelf lives, accounting for weather, events, promotions, and substitution effects — while correcting for censored demand during historical stockout periods.

**ML task:** Time-series forecasting with probabilistic output (quantile regression) + censored demand imputation
**Input data:** 3+ years of daily order history by SKU and customer, weather forecasts (temperature, precipitation from NOAA API), local event calendars, supplier promotional calendars, inventory position snapshots, historical stockout flags, SKU substitution mappings
**Target:** Probability distribution of daily demand per SKU per customer segment for days t+1 through t+7, expressed as 10th/50th/90th percentile quantities
**Evaluation metric:** Weighted Pinball Loss (asymmetric — underforecasting perishables is costlier than overforecasting for high-margin items, reversed for low-margin commodities). Secondary metric: spoilage rate and stockout rate on a rolling 30-day basis.
**Scope:** 6-9 month build for a team of 2 ML engineers and 1 data engineer. The hardest part is censored demand correction — requires building a stockout detection model first (did this SKU actually stock out, or did demand genuinely drop to zero?) before training the demand model. Feature engineering for substitution effects is also non-trivial: when SKU A stocks out, what fraction of its demand transfers to SKU B vs. is lost entirely?
**Data availability:** Order history is in every distributor's ERP (Produce Pro, Edible Software, SAP). Weather and event data are publicly available via APIs. The gap is stockout labeling — most ERP systems do not explicitly flag stockout events, so these must be inferred from inventory position time series and order rejection logs.

---

## 2. Product Quality and Remaining Shelf Life Estimation at Receiving
#cnn #random-forest #multiclass-classification #computer-vision #tabular-ml

**Problem statement:** At the receiving dock, estimate the remaining usable shelf life of incoming perishable products using visual inspection (photos) combined with sensor data (temperature logger readings from transit), so buyers can make immediate replenishment and pricing decisions.

**ML task:** Multiclass classification (shelf life bucket: 1-2 days, 3-5 days, 6-9 days, 10+ days) combining image and tabular features
**Input data:** Photographs of incoming product cases (taken by receiving staff on handheld devices), temperature logger time series from transit (min/max/mean/time-above-threshold), supplier identity, product category, transit duration, season, and historical shelf life actuals for the same supplier-product pair
**Target:** Predicted remaining shelf life bucket and a confidence score; secondary output is a binary flag for "reject at receiving" when predicted shelf life < minimum acceptable (typically 3 days for produce, 5 days for dairy)
**Evaluation metric:** Macro F1 across shelf life buckets, with heavy penalty for overestimating shelf life (a product predicted as "6-9 days" that actually lasts 2 days causes spoilage). Asymmetric cost matrix: false optimism is 3x worse than false pessimism.
**Scope:** 9-12 month build for 2 ML engineers, 1 CV specialist, and 1 domain expert (produce buyer). The image model requires collecting and labeling 50,000+ product photos across categories with ground-truth shelf life outcomes — a 3-4 month data collection effort before model training begins. Temperature logger integration varies by supplier (some use Sensitech, others Emerson, some use no loggers at all).
**Data availability:** Historical shelf life data exists in spoilage logs and QA records but is rarely structured. Photo data must be collected prospectively. Temperature logger data is available for 40-60% of shipments from major suppliers.

---

## 3. Dynamic Pricing for Short-Dated Inventory
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** Set optimal markdown prices for perishable inventory approaching its sell-by date, maximizing recovery revenue while ensuring product moves before it becomes waste — balancing price against demand elasticity, customer willingness to buy short-dated product, and cannibalization of full-price sales.

**ML task:** Regression (optimal price point) + binary classification (will this customer buy short-dated product at price X?)
**Input data:** Current inventory position and days-to-expiry by SKU, historical markdown transactions (price offered, quantity sold, customer, product), customer purchase history and price sensitivity profiles, competitor pricing signals (where available), day-of-week, and current full-price demand forecast for the same SKU
**Target:** Recommended markdown price per SKU that maximizes expected revenue = P(sale at price X) * price X, subject to the constraint that markdown price must be below a cannibalization threshold (typically 70% of full price to avoid training customers to wait for markdowns)
**Evaluation metric:** Revenue recovery rate = (markdown revenue collected) / (full-price value of items that would have been written off). Target: increase recovery from the current 10-20% to 40-60%.
**Scope:** 4-6 month build for 1-2 ML engineers. Relatively straightforward regression problem, but the cannibalization constraint requires careful A/B testing to calibrate. The model must be retrained weekly as seasonal elasticities shift. Integration with the order management system is needed so sales reps see markdown offers in real time.
**Data availability:** Markdown transaction history exists but is often informal — a sales rep calls a customer and offers a deal, logged as a note in CRM rather than structured data. Building the training set requires 3-6 months of structured markdown experiments.

---

## 4. Customer Churn Prediction from Order Pattern Changes
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Detect early signals that a food distribution customer is beginning to shift volume to a competitor, based on changes in order frequency, SKU breadth, order size, and complaint/credit patterns — giving sales reps 4-6 weeks of warning to intervene before the customer fully defects.

**ML task:** Binary classification (will this customer reduce spend by >30% in the next 60 days?) with feature importance explanations for sales rep action
**Input data:** Weekly order history per customer (total spend, number of line items, SKU diversity, order frequency), credit/return history, delivery performance metrics (on-time rate, substitution rate, stockout rate experienced by this customer), sales rep interaction logs, customer tenure, contract terms, and industry segment (restaurant, hospital, school, etc.)
**Target:** Binary label: churn (>30% spend reduction in next 60 days) vs. stable. Secondary output: ranked list of contributing factors (e.g., "stockout rate on their top 5 SKUs increased from 3% to 12% over past 4 weeks")
**Evaluation metric:** Recall at 80% precision — missing a churning customer is far more costly ($50K-$500K in annual revenue per customer) than a false alarm (a sales rep makes an unnecessary check-in call). AUC-PR as the primary ranking metric.
**Scope:** 3-4 month build for 1 ML engineer and 1 data analyst. The model itself is a standard tabular classification problem; the challenge is defining the churn label accurately (seasonal volume drops are not churn, but competitive switching is) and building the feature engineering pipeline from ERP order data. Requires 2+ years of customer order history with known churn examples.
**Data availability:** Order data is abundant in every ERP. The labeling challenge is retrospectively identifying customers who churned vs. those who had seasonal volume changes. Sales teams can label a subset of historical churners for initial training, with the model improving as new labels accumulate.
