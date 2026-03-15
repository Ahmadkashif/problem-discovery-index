# Machine Learning Opportunities — Specialty Food Retail

**Industry:** [[specialty-food-retail|Specialty Food Retail]]
**Derived from:** [[problems/specialty-food-retail/high-impact|High Impact]], [[problems/specialty-food-retail/low-impact-1|Low Impact 1]], [[problems/specialty-food-retail/low-impact-2|Low Impact 2]], [[problems/specialty-food-retail/worker-life-1|Worker Life 1]], [[problems/specialty-food-retail/worker-life-2|Worker Life 2]]

---

## 1. SKU-Level Demand Forecasting for Perishables
#gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact

**Problem statement:** Predict daily unit demand per SKU at an individual specialty food store, accounting for day-of-week seasonality, holidays, weather, and shelf-life constraints, to generate optimal reorder quantities that minimize both spoilage and stockouts.

**ML task:** Time-series regression (point forecast + prediction interval per SKU per day)
**Input data:** POS transaction history (item, quantity, timestamp, price), SKU metadata (shelf life, category, vendor lead time, unit cost), calendar features (day of week, holidays, local events), weather data (temperature, precipitation — relevant for foot traffic), current on-hand inventory with expiration dates.
**Target:** Daily unit sales per SKU for a 1–14 day forecast horizon, converted into a suggested order quantity per vendor order window.
**Evaluation metric:** Weighted mean absolute error (WMAE) where weights reflect item margin and shelf life — a miss on a $40/lb high-margin cheese with 5-day shelf life costs more than a miss on a $4 bag of chips with 90-day shelf life. Secondary metric: spoilage rate reduction (% of revenue discarded).
**Scope:** Cold-start is the main challenge — individual stores have sparse sales histories (some SKUs sell 2–5 units per week), requiring hierarchical models that pool information across product categories and similar stores. A team of 2 ML engineers + 1 data engineer can build an MVP in 3–4 months using gradient-boosted trees (LightGBM) with store-level fine-tuning. Production deployment is a daily batch job generating order suggestions pushed to a mobile app.
**Data availability:** POS transaction data is available via API from Square, Clover, Lightspeed, and Revel. Shelf-life metadata must be manually entered or scraped from distributor catalogs. Weather and calendar data are freely available. The main gap is expiration-date tracking at receiving, which requires a new workflow (barcode scan + best-by entry).

---

## 2. Dynamic Markdown Pricing for Approaching-Date Inventory
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** Determine the optimal markdown price and timing for perishable items approaching their sell-by date, maximizing recovery value while clearing inventory before spoilage.

**ML task:** Regression (optimal discount percentage as a function of remaining shelf life, historical price elasticity, and current inventory level)
**Input data:** Historical transaction data with price paid and quantity sold, item shelf life and current days-to-expiration, time-of-day and day-of-week, item category and substitutability (e.g., multiple brie options), store traffic patterns (transactions per hour as a proxy).
**Target:** Discount percentage that maximizes expected revenue recovery — specifically, P(sale at discount) * (price - discount) integrated over the remaining shelf window.
**Evaluation metric:** Revenue recovery rate: total revenue captured from items entering the markdown window, divided by full-price revenue if all had sold at list price. Target is 60–70% recovery versus the current ~30–40% achieved by ad hoc "manager's special" stickers.
**Scope:** Requires 6–12 months of markdown experiment data to train, which means an initial rule-based system (e.g., 25% off at 2 days remaining, 50% off at 1 day) must run first to generate labeled data. A single ML engineer can build this as an extension of the demand forecasting model. Deployment is a daily or twice-daily batch job that prints markdown labels.
**Data availability:** Markdown transaction data is available from POS but most stores do not systematically track which items were marked down versus discarded. The initial deployment phase must instrument this tracking. Price elasticity data is sparse at the SKU level and requires category-level pooling.

---

## 3. Customer Basket Analysis and Product Affinity
#k-means #recommendation #tabular-ml #revenue-impact

**Problem statement:** Identify product co-purchase patterns and customer segments in specialty food retail to inform cross-merchandising, staff pairing recommendations, and targeted promotions.

**ML task:** Association rule mining (frequent itemsets) + customer clustering (unsupervised segmentation)
**Input data:** POS transaction baskets (items purchased together in a single transaction), customer loyalty data where available (repeat purchase history), product category and price tier metadata, time-of-purchase (morning coffee-and-pastry shoppers vs. weekend dinner-party shoppers).
**Target:** For association rules: item pairs and triplets with high lift and support (e.g., "customers who buy aged gouda also buy membrillo paste 40% of the time"). For clustering: 4–8 customer segments defined by purchase frequency, basket composition, and average spend, actionable for different merchandising strategies.
**Evaluation metric:** For association rules: lift > 2.0 and support > 1% of transactions as minimum thresholds for actionable rules. For clustering: silhouette score for segment separability, validated by store owner review ("yes, that's my Saturday dinner-party crowd vs. my Tuesday lunch regulars").
**Scope:** Straightforward analytics project buildable in 4–6 weeks by a single data scientist. The Apriori or FP-Growth algorithm handles association rules; k-means or DBSCAN handles customer segmentation. The value is in the presentation layer — translating statistical patterns into merchandising actions the owner can implement (move the membrillo paste next to the gouda, train staff to suggest it).
**Data availability:** POS transaction data is readily available. Customer-level linkage depends on whether the store uses a loyalty program or can match transactions by payment card. Stores without loyalty programs will only have basket-level data (no repeat-customer tracking), which limits the clustering component.

---

## 4. Seasonal Assortment Planning and SKU Rationalization
#random-forest #multiclass-classification #tabular-ml #data-integration

**Problem statement:** Recommend which SKUs to add, drop, or adjust quantities for in upcoming seasonal rotations, based on historical performance, category balance, and margin contribution.

**ML task:** Multiclass classification (retain / drop / add-trial / increase-depth / decrease-depth per SKU per season) plus ranking of candidate new SKUs from distributor catalogs.
**Input data:** 2+ years of SKU-level sales data with seasonal indicators, SKU margin data (cost, retail price, markdown frequency), category-level performance metrics (cheese category growing 5% YoY while crackers flat), distributor catalog data for candidate new items (description, price, category, producer region), competitive landscape signals (what similar stores in the region carry, where available via distributor data or web scraping).
**Target:** Per-SKU seasonal action recommendation with confidence score plus a ranked list of 10–20 candidate new SKUs per seasonal rotation.
**Evaluation metric:** Precision on "drop" recommendations (avoiding the removal of items that would have sold well) and recall on "add-trial" recommendations (surfacing items that would succeed). Validated retrospectively: for stores that adopted recommendations, did seasonal margins improve versus stores that did not?
**Scope:** Requires multi-store data to train effectively — a single store's history is too sparse for seasonal pattern detection at the SKU level. A cooperative data-sharing model (anonymized, aggregated) across 50+ stores would be ideal. Build effort: 2 ML engineers, 4–6 months including data pipeline from multiple POS systems. The hardest part is normalizing SKU catalogs across stores that use different naming conventions for the same products.
**Data availability:** Individual store POS data is available but siloed. Building a cross-store training dataset requires a platform play where stores opt in to anonymized data sharing in exchange for better recommendations. Distributor catalog data (UNFI, specialty importers) is available via API or bulk export but varies in structure and completeness.
