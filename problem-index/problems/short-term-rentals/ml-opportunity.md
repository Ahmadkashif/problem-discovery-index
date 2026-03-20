# Machine Learning Opportunities — Short-Term Rentals

**Industry:** [[short-term-rentals|Short-Term Rentals]]
**Derived from:** [[problems/short-term-rentals/high-impact|High Impact]], [[problems/short-term-rentals/low-impact-1|Low Impact 1]], [[problems/short-term-rentals/low-impact-2|Low Impact 2]], [[problems/short-term-rentals/worker-life-1|Worker Life 1]], [[problems/short-term-rentals/worker-life-2|Worker Life 2]]

---

## 1. Per-Property Reinforcement Learning Pricing Agent
#markov-decision-processes #policy-gradient-methods #temporal-difference-learning #time-series-forecasting #gradient-boosting #feature-engineering #optimization-fundamentals #expectation-variance-covariance #revenue-impact

**Problem statement:** Learn the optimal pricing policy for a specific STR property from its own booking conversion history and local demand signals, outperforming generalized rule-based dynamic pricing tools that don't personalize to per-property booking behavior.

**ML task:** Contextual bandit / model-based RL — nightly rate recommendation given booking pace, available nights, and demand context
**Input data:** Per-property booking records: price quoted for each available night, whether it booked (and at what lead time), local demand signals (event calendar, competitor rates via scraping, weather). Property features: type, capacity, location, amenity set.
**Target:** Recommended nightly rate for next 90 days, updated daily; expected occupancy and revenue at the recommended rate vs. current pricing
**Evaluation metric:** Revenue per available night (RevPAN) for properties using RL pricing vs. matched control properties using PriceLabs/Beyond; improvement in RevPAN over 90-day test periods
**Scope:** PriceLabs has the booking data from their operator base — a natural dataset for training per-property models. A contextual bandit (simpler than full RL) can be deployed per-property with moderate data requirements (100+ historical nights per property). 6-9 month development for a production pricing agent. Reinforcement learning is appropriate because the pricing problem is sequential with delayed feedback (a booking tonight depends on prices set over the past week).
**Data availability:** PriceLabs, Beyond Pricing, and Wheelhouse have aggregate booking data. Guesty and Hostaway have per-property booking histories for their operators. The conversion signal (price → booked/not booked per available night) is the training signal — present in any property management system that logs price at booking time.

---

## 2. Problem Booking Classification from Booking Signals
#gradient-boosting #logistic-regression #word-embeddings #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff

**Problem statement:** Classify incoming bookings by risk of property damage or rule violation from booking pattern features and initial guest message content.

**ML task:** Binary classification (problem stay: yes/no) from booking features and NLP on inquiry text
**Input data:** Booking records with outcome labels (normal stay vs. party/damage event). Features: booking lead time, day of week, group size, guest review history, number of prior reviews, inquiry text, property type, local event calendar overlap.
**Target:** Problem probability score per booking; risk tier (auto-approve / review required / auto-decline); specific risk flags driving the score
**Evaluation metric:** Recall on bookings that resulted in damage/party events; precision at medium-risk tier (false positive rate for blocked legitimate bookings); net impact on damage costs and booking revenue for hosts using the model
**Scope:** Requires labeled outcome data: bookings where a damage event occurred vs. normal stays. Autohost and Superhog have damage claim records that can serve as supervision. NLP on inquiry text is off-the-shelf LLM capability. Gradient boosting on booking features + NLP embedding: 4-6 week project with sufficient labeled damage events.
**Data availability:** Damage incident records exist at insurance and deposit platforms (Superhog, Safely, Airbnb damage program). Booking feature data is in the PMS. The challenge is linking damage records to specific bookings at scale across multiple operators.

---

## 3. Guest Review Score Prediction from Listing and Property Features
#gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #descriptive-statistics #quick-win

**Problem statement:** Predict a property's expected review score distribution (cleanliness, location, value, check-in, accuracy) from listing and property features, enabling targeted investments in the categories most likely to improve the overall rating.

**ML task:** Regression (expected category review score) from property and listing feature inputs
**Input data:** Property listings with their review scores by category. Features: amenity set, listing photo quality score, property age, price tier vs. market, host response rate, location characteristics.
**Target:** Predicted score per review category; sensitivity analysis (which property or listing change has the highest expected score improvement?); comparison to comparable properties with higher scores
**Evaluation metric:** MAE between predicted and actual review scores on held-out listings; improvement in target review categories for properties that made model-recommended changes vs. control
**Scope:** Quick win — Airbnb review data by category is public (visible on listings). Feature extraction from listings is automatable. Any STR analytics platform with 10,000+ listings in their dataset can build this. Gradient boosting regression: 3-4 week modeling project with scraped Airbnb listing data.
**Data availability:** Airbnb review scores by category are publicly visible on listing pages. Scraped Airbnb data provides training signal. Listing features (amenity list, photo count) are also publicly visible.

---

## 4. Turnover Scheduling Optimization
#gradient-boosting #feature-engineering #optimization-fundamentals #combinatorics-and-counting #evaluation-metrics #workflow-orchestration #quick-win

**Problem statement:** Optimize cleaner assignment and scheduling for daily STR turnovers given cleaner availability, property-cleaner familiarity, time windows between checkout and check-in, and travel time between properties.

**ML task:** Constraint satisfaction + optimization — cleaner assignment per turnover given availability, familiarity, and travel time constraints; scheduling order for cleaners with multiple same-day assignments
**Input data:** Historical cleaner assignment records with outcome (turnover completed on time: yes/no), cleaner performance ratings, property-cleaner familiarity, geographic locations.
**Target:** Daily cleaner assignment schedule; ETA alerts when a turnover is at risk of missing the check-in window; re-assignment recommendations when a cleaner cancels
**Evaluation metric:** Turnover-on-time rate with model scheduling vs. manual; cleaner cancellation recovery time; property manager coordination time per day
**Scope:** Quick win — the scheduling optimization is a well-structured combinatorial problem. A constraint programming approach (not complex ML) handles the assignment. The ML component is predicting turnover risk (which assignments are likely to run long). Breezeway or Properly has the historical data. 3-4 week project.
**Data availability:** Breezeway and Properly log turnover assignments and completion times. Booking calendar provides the constraint window. Cleaner performance history is in the platform.

---

## 5. Listing Copy and Photo Optimization
#large-language-models #linear-regression #gradient-boosting #transfer-learning #feature-engineering #evaluation-metrics #word-embeddings

**Problem statement:** Identify specific listing improvements (photo reordering, headline rewrite, amenity completeness gaps) that are predicted to improve search ranking and booking conversion for a specific property.

**ML task:** Regression — predicted booking conversion rate change from specific listing modifications; NLP for listing quality scoring vs. high-performing comparables
**Input data:** STR listings with booking conversion rates and review scores. High-performing listings (top-quartile conversion) in each market and property type as positive examples.
**Target:** Ranked list of recommended listing changes with predicted conversion impact; generated headline alternatives; amenity list completeness gap vs. comparable high-performers
**Evaluation metric:** Conversion rate improvement for listings that implement model recommendations vs. control; click-through rate from Airbnb search results for optimized vs. unoptimized listings
**Scope:** LLM-based listing analysis is commercially available (Hospitable, Lodgify have early versions). The differentiator is the conversion impact regression — linking specific listing attributes to measured booking conversion. Scraped Airbnb data provides the training signal. 4-6 week project with sufficient scraped listing + conversion data.
**Data availability:** Listing text and photos are publicly available on Airbnb/Vrbo. Conversion rate data requires platform partnership or host-provided data (bookings/views ratio visible in host dashboard).
