# Machine Learning Opportunities — Food Trucks

**Industry:** [[food-trucks|Food Trucks]]
**Derived from:** [[problems/food-trucks/high-impact|High Impact]], [[problems/food-trucks/low-impact-1|Low Impact 1]], [[problems/food-trucks/low-impact-2|Low Impact 2]], [[problems/food-trucks/worker-life-1|Worker Life 1]], [[problems/food-trucks/worker-life-2|Worker Life 2]]

---

## 1. Location-Day Revenue Prediction (Tacit Knowledge Capture)
#gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #tacit-knowledge-ml #revenue-impact

**Problem statement:** Experienced food truck operators integrate weather, local events, day-of-week, competitor positions, and neighborhood foot-traffic patterns into a single daily location decision — but this intuition takes 2-3 years to develop and cannot be articulated as explicit rules. The goal is to capture this tacit decision process as a predictive model that any operator can use from day one.

**ML task:** Regression (predict daily gross revenue per candidate location)
**Input data:** Historical POS transaction logs with GPS coordinates and timestamps; weather forecast APIs (temperature, precipitation probability, wind); local event calendar data (concerts, sports, farmers markets, office-building occupancy proxies); day-of-week and month; competitor location pings from social media or shared scheduling platforms; Google Popular Times or SafeGraph foot-traffic estimates for candidate zones.
**Target:** Daily gross revenue in dollars for a specific truck at a specific location on a specific date.
**Evaluation metric:** Mean Absolute Error (MAE) in dollars, with a secondary metric of "top-3 accuracy" — how often the model's top-3 recommended locations include the actual best location. MAE matters more than RMSE because large outlier events (festivals) are genuinely different regimes and should be modeled separately.
**Scope:** Requires 6-12 months of geotagged POS data per truck for cold-start; a cooperative network of 20-50 trucks in a metro area accelerates training dramatically. A 2-person ML team can build an MVP in 3-4 months using XGBoost. City-specific models are necessary initially — transfer learning across cities is a later-stage problem. The hardest engineering challenge is feature integration: stitching together 5-6 real-time APIs into a daily feature vector reliably.
**Data availability:** POS data is available via Square/Clover APIs with operator consent. Weather and event data are publicly available. Foot-traffic data requires a SafeGraph or similar subscription ($500-$2,000/month). Competitor location data is the scarcest signal — requires either a cooperative network or social-media scraping. Labeling is straightforward (revenue is the label), but the tacit-knowledge challenge is that operators who already "know" the best spots may never generate negative examples at bad locations, creating selection bias in training data.

---

## 2. Daily Prep Quantity Optimization
#gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #quick-win

**Problem statement:** Food trucks must prep ingredients 4-8 hours before service with no ability to restock mid-shift. Over-prep wastes $50-$150/day in perishable ingredients; under-prep loses $200-$500 in turned-away customers. The optimal prep quantity depends on location, weather, day-of-week, menu mix, and whether there is a nearby event — the same features that drive revenue, but mapped to per-item demand.

**ML task:** Regression (predict units sold per menu item per shift)
**Input data:** Historical POS item-level sales with location and date; weather forecasts; event indicators; menu composition (which items are offered that day); price points.
**Target:** Units sold per menu item for the upcoming shift.
**Evaluation metric:** Weighted MAE, where the weight is ingredient cost per unit — penalizing over-prediction of expensive items (lobster rolls) more than cheap items (rice). A secondary metric is sell-out rate: the model should target <5% of shifts ending in complete sell-out (which indicates under-prep).
**Scope:** Simpler than location prediction because the operator controls the input (menu, location already decided). A single data scientist can build this in 6-8 weeks with 3+ months of item-level POS data. The main challenge is menu variability — many trucks rotate specials, which creates sparse data for non-core items. Start with core menu items only (top 5-8 items representing 80% of revenue).
**Data availability:** Item-level POS data is readily available from Square/Clover. The only labeling needed is matching item sales to contextual features (weather, location), which can be automated. Operators with 6+ months of consistent POS usage have sufficient data for a cold-start model.

---

## 3. Menu Item Demand by Location Type
#random-forests #decision-trees #k-means-clustering #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff

**Problem statement:** Different locations attract different customer demographics with different taste preferences — a tech-campus lunch crowd skews toward bowls and healthy options, while a late-night bar district wants loaded fries and tacos. Operators currently guess which menu items to emphasize at each location type, leading to mismatched inventory and missed upsell opportunities.

**ML task:** Multiclass classification (predict top-selling menu category per location type) combined with ranking (order menu items by predicted demand within a location context)
**Input data:** POS item-level sales tagged with location metadata (neighborhood type: office district, university, bar district, residential, event venue); time-of-day; demographic proxies from census tract data; historical item mix percentages per location.
**Target:** Ranked list of menu items by predicted share of sales for a given location-time context.
**Evaluation metric:** NDCG@5 (Normalized Discounted Cumulative Gain for the top 5 items) — measures whether the model's ranking of items matches actual sales ranking. Secondary metric: inventory waste reduction in dollars.
**Scope:** Requires clustering locations into types first (a k-means preprocessing step on location features), then training a classifier per truck's menu. A solo data scientist can prototype in 4-6 weeks. The model improves as the truck visits more location types, but cold-start for a new location type requires borrowing data from similar trucks — this is where a multi-truck cooperative network adds value.
**Data availability:** Same POS + location data as opportunities #1 and #2. Census-tract demographic data is freely available from the US Census Bureau API. The main gap is that most trucks visit the same 5-10 locations repeatedly, creating limited location-type diversity in any single truck's dataset.

---

## 4. Social Media Post Timing & Content Optimization
#gradient-boosting #linear-regression #decision-trees #feature-engineering #causal-inference #evaluation-metrics #hypothesis-testing #quick-win

**Problem statement:** Food trucks rely on Instagram, Twitter/X, and TikTok to announce daily locations and drive foot traffic, but operators post at random times with inconsistent content quality. The engagement-to-foot-traffic conversion is unmeasured: operators do not know whether a post at 9 AM or 10:30 AM generates more actual customers, or whether a photo of the truck at the location outperforms a menu close-up.

**ML task:** Regression (predict engagement rate and attributed foot traffic lift per post)
**Input data:** Historical social media posts with timestamps, content type (photo category, text length, hashtag count), platform; POS sales data for the corresponding shift (as a proxy for foot-traffic response); follower count at time of posting; day-of-week; whether the post included location pin.
**Target:** Two targets: (1) engagement rate (likes + comments + shares / impressions), (2) incremental revenue attributable to the post (estimated by comparing sales on days with vs. without morning posts, controlling for location and weather).
**Evaluation metric:** MAE on engagement rate; for the revenue-attribution target, a paired difference test (post vs. no-post days at the same location) with confidence intervals. The practical metric is "did posting at the recommended time increase same-day revenue by a statistically significant amount?"
**Scope:** This is a lighter-weight model that can be prototyped in 2-3 weeks by a single analyst. The causal inference challenge (did the post cause the traffic, or did the operator post more on days they expected to be busy?) requires careful experimental design — ideally A/B testing post timing on matched location-days. Most trucks have 6-12 months of social media history accessible via platform APIs.
**Data availability:** Social media data is accessible via Instagram Graph API, Twitter API (paid tier), and TikTok Creator API. POS data provides the revenue signal. The challenge is attribution: isolating the post's effect from confounders (weather, event, location) requires at least 50-100 matched pairs, which takes 3-4 months of deliberate experimentation to accumulate.
