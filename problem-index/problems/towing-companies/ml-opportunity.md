# Machine Learning Opportunities — Towing Companies

**Industry:** [[towing-companies|Towing Companies]]
**Derived from:** [[problems/towing-companies/high-impact|High Impact]], [[problems/towing-companies/low-impact-1|Low Impact 1]], [[problems/towing-companies/low-impact-2|Low Impact 2]], [[problems/towing-companies/worker-life-1|Worker Life 1]], [[problems/towing-companies/worker-life-2|Worker Life 2]]

---

## 1. Job Complexity and Duration Prediction from Call Description
#gradient-boosting #bert #regression #text-classification #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced dispatchers read a caller's description — often vague, inaccurate, or incomplete — and intuitively estimate the truck type needed, job duration, and whether the stated location is reliable. This tacit judgment, built over thousands of dispatched calls, is never recorded and cannot be transferred to new dispatchers. The goal is to capture this decision-making pattern and surface it as real-time recommendations during call intake.

**ML task:** Multi-output prediction — text classification (truck type: wheel-lift / flatbed / medium-duty / heavy-duty) + regression (predicted job duration in minutes) + binary classification (location accuracy: reliable / needs verification)
**Input data:** Call transcripts or dispatcher notes (free text), vehicle year/make/model (from plate lookup or caller report), GPS coordinates, time of day, day of week, weather conditions, caller source (motor club / police / direct), historical zone-level job data. Text features processed through a fine-tuned BERT encoder; structured features fed into a gradient-boosted ensemble.
**Target:** Truck type (4-class), job duration (continuous, minutes), location reliability flag (binary). Ground truth derived from completed job records: actual truck used, actual on-scene time, whether driver reported location discrepancy.
**Evaluation metric:** Truck type — weighted F1 (misclassifying heavy-duty need as wheel-lift is costlier than the reverse). Duration — MAE in minutes (target < 8 min error). Location reliability — recall prioritized over precision (better to flag a good location than miss a bad one).
**Scope:** Requires 6–12 months of historical dispatch records with completed job outcomes from 3–5 towing companies to build initial training set. Text encoder fine-tuning needs ~10,000 annotated call descriptions. A 2-person ML team (NLP + tabular) can build an MVP in 4–5 months. Deployment as a Towbook plugin or standalone dispatch overlay. The hardest part is data collection: most companies do not systematically record the dispatcher's initial assessment alongside the actual outcome.
**Data availability:** Dispatch records exist in Towbook, TOPS, or paper logs but vary wildly in completeness. Call descriptions range from structured (motor club digital dispatches with VIN and location) to unstructured (handwritten notes: "blue truck in ditch, caller says near Walmart"). Partnering with 3–5 mid-size operators (15+ trucks) who use Towbook provides the cleanest starting dataset. Expert dispatcher annotation sessions (having dispatchers label historical calls with what they would have decided) can bootstrap the tacit knowledge labels.

---

## 2. Demand Forecasting by Zone and Hour
#gradient-boosting #time-series-forecasting #tabular-ml

**Problem statement:** Towing demand is highly spatio-temporal — accident clusters correlate with rush hours, weather events, road construction, and local events, but companies position trucks reactively rather than predictively, leaving drivers idle in low-demand zones while calls queue in high-demand areas.

**ML task:** Time-series regression — predict call volume per geographic zone per hour for the next 24–72 hours.
**Input data:** Historical call logs with timestamps and GPS coordinates, weather forecasts (precipitation, temperature, visibility), day-of-week and holiday calendars, local event schedules (concerts, sports), road construction/closure feeds, traffic density data from public DOT APIs.
**Target:** Call count per zone per hour (continuous). Zones defined as 2–5 mile grid cells or municipal boundaries depending on market density.
**Evaluation metric:** MAPE at the zone-hour level; weighted by zone revenue value. Under-prediction is costlier than over-prediction (missed calls vs. idle time), so asymmetric loss weighting in training.
**Scope:** Requires 12–24 months of historical call data with GPS coordinates. Gradient-boosted trees (LightGBM) with lag features, calendar features, and weather features. Single ML engineer, 2–3 month build. The spatial granularity challenge is key — too coarse and predictions are useless, too fine and data is too sparse.
**Data availability:** Call logs with timestamps are universally available; GPS coordinates are available from companies using Towbook or GPS-tracked fleets. Weather and event data are freely available via APIs. The main gap is that many small operators lack sufficient historical volume per zone to train zone-level models — aggregation across multiple operators in a metro area solves this.

---

## 3. Optimal Truck Positioning and Pre-staging
#reinforcement-learning #regression #tabular-ml #revenue-impact

**Problem statement:** Between calls, tow trucks either return to the yard or idle at the last job location. Neither strategy minimizes response time for the next call. Optimal pre-staging — positioning trucks at locations that minimize expected response time given demand predictions — is a dynamic optimization problem that changes hourly.

**ML task:** Sequential decision-making — given current truck positions, active job queue, and demand forecast, recommend repositioning moves that minimize expected response time for the next N calls.
**Input data:** Real-time truck GPS positions, active job queue with estimated completion times, demand forecast from model #2, road network travel time estimates (Google Maps or OSRM), truck type availability.
**Target:** Repositioning recommendations (truck ID, suggested staging location) that minimize average response time across the next shift window. Evaluated via simulation against historical call sequences.
**Evaluation metric:** Average response time (minutes) vs. baseline (return-to-yard policy). Secondary metric: percentage of calls meeting motor club SLA window.
**Scope:** Depends on demand forecasting model (#2) as a prerequisite. Reinforcement learning approach requires a simulation environment built from historical data. More practically, a heuristic optimization (facility location problem) using demand forecasts can deliver 80% of the value with 20% of the complexity. Single ML engineer + ops research background, 3–4 months after demand model is validated. Requires buy-in from drivers, who may resist being told where to wait.
**Data availability:** Requires GPS tracking of fleet (increasingly common) plus historical call data. The simulation environment can be built from 6–12 months of timestamped call + truck position data from a single operator.

---

## 4. Motor Club Rotation Performance Scoring
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Motor clubs evaluate towing companies on response time, customer satisfaction, and claim accuracy to determine rotation ranking. Companies do not know which factors most influence their ranking or which calls are most likely to trigger a negative review that drops their position. A predictive model of rotation risk per call would let companies allocate their best drivers and fastest trucks to the calls that matter most.

**ML task:** Binary classification — predict whether a given motor club call will result in a negative performance mark (late arrival, customer complaint, documentation dispute).
**Input data:** Historical motor club call records with outcome data (on-time/late, customer rating, billing dispute flag), call characteristics (distance, vehicle type, time of day, weather), assigned driver profile (experience, historical performance), truck type match (was the right equipment sent?).
**Target:** Binary — negative performance mark (yes/no). Secondary regression target: predicted arrival time vs. SLA window (minutes of buffer or overage).
**Evaluation metric:** Recall at 80%+ precision — the cost of missing a high-risk call (and losing rotation position) far exceeds the cost of over-allocating resources to a call that would have been fine.
**Scope:** Requires motor club performance data, which companies receive monthly or quarterly as scorecards. Tabular gradient-boosted model, straightforward feature engineering. Single ML engineer, 6–8 weeks to MVP. The political challenge is that motor clubs do not publish their exact ranking algorithms, so the model learns from observed outcomes rather than stated rules.
**Data availability:** Motor club scorecards are available to participating companies but are not standardized across clubs. Historical call-level outcome data exists in dispatch records. Linking the two requires manual matching for the initial training set; once linked, ongoing data collection is automated.
