# Machine Learning Opportunities — Charter Bus Operators

**Industry:** [[charter-bus-operators|Charter Bus Operators]]
**Derived from:** [[problems/charter-bus-operators/high-impact|High Impact]], [[problems/charter-bus-operators/low-impact-1|Low Impact 1]], [[problems/charter-bus-operators/low-impact-2|Low Impact 2]], [[problems/charter-bus-operators/worker-life-1|Worker Life 1]], [[problems/charter-bus-operators/worker-life-2|Worker Life 2]]

---

## 1. Dispatcher Trip-Assignment Intelligence (Tacit Knowledge Capture)
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #optimization-fundamentals #tacit-knowledge-ml

**Problem statement:** Experienced charter dispatchers read a trip request — "55 seniors, 3-day wine country tour, pickup Napa, stops in Sonoma and Healdsburg, return via SF" — and immediately know which driver and which bus to assign. They factor in the driver's patience with elderly groups, the bus's suspension quality for winding roads, the driver's familiarity with Napa Valley parking restrictions, and whether the 2012 MCI has the luggage bay capacity for walkers and wheelchairs. This matching decision is made in seconds by a veteran dispatcher but takes a new dispatcher hours of trial-and-error and phone calls. The goal is to capture this tacit assignment logic in a model that recommends driver-bus-trip combinations ranked by predicted trip satisfaction and operational efficiency.

**ML task:** Multi-output regression — predict trip satisfaction score (1-10, based on post-trip client feedback and driver self-report) and operational efficiency score (deadhead ratio, on-time performance, fuel efficiency vs. baseline) for each candidate driver-bus-trip combination.
**Input data:** Trip parameters (origin, destination, stops, duration, group size, group type [wedding/corporate/school/senior/sports], amenity requirements, time of year), driver features (years of experience, endorsements, historical satisfaction scores by group type, route familiarity index, HOS remaining hours, fatigue accumulation score), bus features (capacity, amenities, age, maintenance state, fuel efficiency by route type, accessibility equipment, luggage capacity).
**Target:** Composite score combining predicted client satisfaction (70% weight) and operational efficiency (30% weight). Secondary target: probability of trip incident (late arrival, breakdown, complaint).
**Evaluation metric:** RMSE on satisfaction score with a secondary constraint on incident probability calibration (Brier score < 0.1). The model must outperform random assignment by >1.5 points on satisfaction and >10% on deadhead ratio.
**Scope:** This is a 6-9 month build for a 2-person ML team. The first 3 months focus on data collection infrastructure: instrumenting trip outcomes (satisfaction surveys, driver reports, telematics summaries) and building the historical feature store from existing records. Months 4-6 train the model on 500+ completed trips with outcome labels. Months 7-9 deploy as a recommendation layer in the dispatch workflow with A/B testing against dispatcher-only assignments.
**Data availability:** The hardest part is labeling. Most charter operators do not systematically collect post-trip satisfaction data — the first step is implementing a simple SMS-based feedback loop for group coordinators and a driver trip report form. Historical data (2-5 years of trip records) exists in spreadsheets and email but requires significant cleaning. Driver-specific features require dispatcher interviews to seed the initial feature values ("Which drivers are best with seniors? Which know the Napa routes?"). This tacit knowledge seeding is a one-time effort per fleet but is the critical bottleneck — dispatchers must be willing to externalize their judgment, and they may resist if they perceive the system as replacing them rather than augmenting them.

---

## 2. Predictive Maintenance from Telematics & Inspection Data
#random-forests #decision-trees #feature-engineering #cross-validation #evaluation-metrics #logistic-regression #conditional-probability-and-bayes-theorem #bias-variance-tradeoff #automation

**Problem statement:** Charter buses operate on irregular schedules with high mileage variance — a motorcoach might sit idle for 5 days then run 2,000 miles in 3 days. Standard mileage-based maintenance intervals miss the stress patterns unique to charter operations (mountain passes, frequent stops, extended idling at venues). The goal is to predict component failure risk windows so maintenance can be scheduled during idle periods rather than discovered during pre-trip inspections or, worse, on the road.

**ML task:** Binary classification — predict whether a specific component (brakes, transmission, HVAC, tires, engine) will require unscheduled maintenance within the next 14-day window.
**Input data:** Telematics streams (engine hours, coolant temp, oil pressure, transmission temp, brake pad wear sensors, tire pressure, DTC codes), historical maintenance records (component, date, mileage, cost, whether scheduled or unscheduled), trip profiles for the past 30 days (total miles, mountain miles, idle hours, stop frequency, passenger load), ambient weather data (temperature extremes stress HVAC and tires), bus age and model.
**Target:** Binary label per component per 14-day window: 1 = unscheduled maintenance event occurred, 0 = no event.
**Evaluation metric:** Recall at 80%+ (cannot miss failures that would strand passengers) with precision >50% (too many false alarms erode mechanic trust). F2 score as the primary optimization metric.
**Scope:** 4-6 month build for a 2-person team. Requires integration with telematics provider APIs (Samsara, Geotab) and maintenance record digitization. A fleet of 15+ buses generates enough data for training within 6 months of instrumented operation. The model improves significantly with fleet pooling across multiple operators.
**Data availability:** Telematics data is abundant for operators using ELD-compliant devices (federally mandated since 2019). Maintenance records are the bottleneck — most are in paper logbooks or unstructured notes in fleet management tools. A 3-month data entry sprint to digitize 2-3 years of maintenance history is the prerequisite.

---

## 3. Seasonal Demand Forecasting for Fleet & Staffing Planning
#gradient-boosting #decision-trees #feature-engineering #time-series-forecasting #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #revenue-impact

**Problem statement:** Charter bus demand is highly seasonal and event-driven — wedding season (May-October), school field trips (March-June, September-November), holiday travel (November-December), and sports seasons create overlapping demand waves. Operators make fleet acquisition and driver hiring decisions 3-6 months in advance but lack the forecasting tools to predict demand beyond gut feel and last year's calendar. Overcommitting leads to idle assets; undercommitting leads to turned-away bookings worth $3,000-$15,000 each.

**ML task:** Time-series regression — predict weekly booking volume and revenue by trip type (wedding, corporate, school, airport, tour) for a 12-week rolling horizon.
**Input data:** Historical booking data (date, trip type, group size, revenue, lead time from inquiry to departure), local event calendars (concerts, sports, conventions), school district calendars, wedding season indices by region, macroeconomic indicators (corporate travel budgets correlate with booking volume), weather forecasts (severe weather suppresses bookings), competitor pricing signals (where available from marketplace platforms).
**Target:** Weekly booking count and total revenue by trip type, with prediction intervals.
**Evaluation metric:** MAPE < 20% at 4-week horizon, < 30% at 12-week horizon. Calibration of prediction intervals (90% coverage).
**Scope:** 3-4 month build for 1-2 ML engineers. The model is relatively straightforward gradient-boosted regression with time features, but data aggregation across operators is needed for robust training. A single 15-bus operator has ~800-1,200 trips/year — enough for basic patterns but insufficient for rare event types. A cooperative data model across 10+ operators would dramatically improve accuracy.
**Data availability:** Booking data exists in operator CRMs, spreadsheets, and email inboxes. The cleaning and standardization effort is moderate. External features (event calendars, school schedules) are publicly available via APIs. The main challenge is convincing operators to share anonymized booking data for a pooled model.

---

## 4. Driver-Trip Compatibility Matching
#gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #optimization-fundamentals #bias-variance-tradeoff #worker-facing

**Problem statement:** Not all drivers perform equally well on all trip types. A driver who excels at corporate airport shuttles (punctual, professional, minimal interaction) may struggle with a 3-day senior tour (patience, flexibility, social engagement, luggage assistance). Currently, dispatchers make these matches based on personal knowledge of each driver — when the dispatcher is unavailable or leaves, the matching quality drops immediately and customer complaints spike.

**ML task:** Learning-to-rank — given a trip and a set of available drivers, rank drivers by predicted trip outcome quality.
**Input data:** Driver features (experience years, endorsements, trip history by type, historical satisfaction scores segmented by group type, reliability metrics [on-time rate, complaint rate], route familiarity scores), trip features (type, duration, group demographics, route complexity, amenity requirements, time sensitivity).
**Target:** Ranked list of available drivers per trip, trained on historical trip outcome scores (client satisfaction + operational metrics).
**Evaluation metric:** NDCG@3 (the top 3 recommended drivers should include the optimal match). Secondary: reduction in post-trip complaints vs. random/sequential assignment baseline.
**Scope:** 3-5 month build, tightly coupled with Opportunity #1 (shares the same feature store and outcome labels). Can be built as a lighter-weight extension once the trip-assignment model is operational. Requires the same satisfaction data collection infrastructure.
**Data availability:** Same constraints as Opportunity #1. The key additional requirement is sufficient trip volume per driver to learn driver-specific preferences — a fleet needs at least 6 months of outcome-labeled trips with 10+ trips per driver to begin learning meaningful patterns. Cold-start for new drivers uses demographic and endorsement features only, with rapid updating as trip outcomes accumulate.
