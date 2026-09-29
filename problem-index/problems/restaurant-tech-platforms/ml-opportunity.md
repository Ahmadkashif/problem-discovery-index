# Machine Learning Opportunities — Restaurant Tech Platforms

**Industry:** [[restaurant-tech-platforms|Restaurant Tech Platforms]]
**Derived from:** [[problems/restaurant-tech-platforms/high-impact|High Impact]], [[problems/restaurant-tech-platforms/low-impact-1|Low Impact 1]], [[problems/restaurant-tech-platforms/low-impact-2|Low Impact 2]], [[problems/restaurant-tech-platforms/worker-life-1|Worker Life 1]], [[problems/restaurant-tech-platforms/worker-life-2|Worker Life 2]]

---

## 1. Hierarchical Demand Forecasting Across the Location Base
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #exponential-smoothing #feature-engineering #cross-validation #evaluation-metrics #confidence-intervals #revenue-impact

**Problem statement:** Labour and prep are both committed in advance against a forecast, together representing about two thirds of a restaurant's cost structure. A single location has too little history to learn the effect of the events that matter — a home game, a festival, the first warm Saturday — which is why operator intuition beats the naive per-location forecasts every vendor ships, and why nobody trusts the feature.

**ML task:** Hierarchical multi-horizon probabilistic forecasting of covers and item-level demand by daypart, pooling across locations with location-specific effects
**Input data:** Transaction history at item and minute granularity per location; daypart and day-of-week structure; menu and price changes; promotions; weather observations and forecasts at location coordinates; local event calendars; school calendars; holidays; location attributes (service style, cuisine, format, seating, neighbourhood type, market).
**Target:** Covers and item quantities per daypart at horizons of one to fourteen days, as a distribution rather than a point.
**Evaluation metric:** Pinball loss across quantiles is the correct primary metric because the decision is asymmetric — under-prepping and over-staffing cost differently. Report calibration of prediction intervals and, separately, performance on the atypical days (extreme weather, event days, holidays), since average accuracy is dominated by ordinary Tuesdays and the value is entirely in the exceptions.
**Scope:** The modelling core is learning location archetypes so that driver effects can vary — a brunch café and a suburban steakhouse respond to rain in opposite directions and a naive pooled model averages them into nothing. Global models with location embeddings handle this well. 3-4 ML engineers plus an operations advisor, 6-9 months. The forecast must attach to the schedule and prep sheet, not to a dashboard.
**Data availability:** Outstanding — this is one of the densest consumer demand datasets in existence and it is almost entirely unmodelled. The complications are the pandemic discontinuity in historical series, menu changes that break item continuity, and location churn as restaurants open and close.

---

## 2. Cross-Channel Menu Structure Mapping
#bert #word-embeddings #large-language-models #k-nearest-neighbors #transfer-learning #evaluation-metrics #data-integration

**Problem statement:** A restaurant's menu must exist consistently across the POS, its own ordering channels and several delivery marketplaces, each of which models modifiers with different structures and constraints. Middleware moves menus; a human decides how to express a POS modifier group in a target schema, once per restaurant per channel, and then the mapping is frozen and drifts.

**ML task:** Structured schema mapping — proposing a target-channel menu representation given a source POS menu — plus drift detection as a comparison task across live channels
**Input data:** Historical menu builds across thousands of restaurants: source POS item and modifier structures paired with the published representation a specialist created in each target channel. Cuisine and service style. Target channel schema constraints. Live published menus per channel for drift monitoring.
**Target:** The confirmed published structure per channel — item names, prices, modifier groups with cardinality, availability windows.
**Evaluation metric:** Proportion of proposed mappings published without specialist edit, measured per channel and per cuisine. For drift, precision and recall on genuine divergences against a manually audited sample, with false positives weighted heavily because a noisy drift alert is ignored.
**Scope:** The repetition across restaurants is what makes this tractable — the same modifier patterns recur constantly within a cuisine. Retrieval of similar prior builds plus a structured generation step outperforms attempting the mapping from schema rules alone. Drift detection needs no learning at all and should ship first. 2 ML engineers, 4 months.
**Data availability:** Very strong and unassembled. Menu build history exists in onboarding systems as operational records rather than as a dataset. Marketplace schemas change without notice, which means the mapping model needs a maintenance path, not just a training run.

---

## 3. Distributor Invoice Line Resolution to Canonical Ingredients
#bert #word-embeddings #k-nearest-neighbors #dbscan #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** Food costing depends on matching every distributor invoice line to the ingredient it represents, across several distributors with incompatible item codes, inconsistent descriptions, varying pack sizes and substitutions. Invoice capture is solved; the matching is manual at every restaurant and re-done whenever a distributor changes a code.

**ML task:** Entity resolution over a large, drifting item catalogue — clustering invoice line descriptions into canonical ingredients, then normalising to cost per usable unit
**Input data:** Millions of invoice lines across the customer base with description, distributor item code, pack size, unit, quantity and price; confirmed restaurant-level mappings as labels; recipe ingredient definitions; published yield and conversion references.
**Target:** A canonical ingredient identifier per invoice line, with pack normalisation and a usable-unit conversion factor.
**Evaluation metric:** Cluster purity against confirmed mappings and top-1 assignment accuracy on held-out restaurants — generalisation to a restaurant and distributor combination never seen is the metric that matters, since that is every new customer. Track separately the rate of silent errors, where a line is confidently mapped to the wrong ingredient, because those corrupt costing invisibly.
**Scope:** Character and subword embeddings over abbreviated foodservice descriptions do most of the work; the harder parts are pack-size parsing from free text and yield normalisation, which is domain knowledge rather than modelling. Building the canonical ingredient catalogue is a prerequisite and should be induced from clustering rather than authored. 2-3 ML engineers plus a culinary operations expert, 5-6 months.
**Data availability:** Large volume and weak labels — restaurant-level mappings exist but are inconsistent between restaurants, which means the same line is labelled differently in different accounts and the label set itself needs reconciliation before training.

---

## 4. Device Degradation Detection Ahead of Service
#change-point-detection #time-series-forecasting #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #automation

**Problem statement:** Restaurant technology fails during service, when the system is loaded and the cost of failure is highest. The failures are almost always preceded by days of degrading telemetry — printer job failures, card reader retries, terminal errors, tablet connectivity drops — which the platform receives and treats as logs.

**ML task:** Per-device anomaly and change point detection over telemetry, with a survival component estimating time to hard failure
**Input data:** Device telemetry per location (terminal error rates and types, print job success, card reader retry and decline patterns, network latency and packet loss, tablet connectivity, application crash reports, battery health), device model and age, location network topology, and historical hard failure events with their support tickets.
**Target:** A hard failure or service-disrupting incident within a defined horizon, per device.
**Evaluation metric:** Precision at the alerting threshold is the constraint — a proactive contact that turns out to be nothing costs the restaurant's patience, which is the vendor's scarcest asset. Report precision@k for a daily alert budget, plus lead time distribution on true positives. A pre-service readiness check has different economics and can run at much higher recall.
**Scope:** Per-device baselining matters more than cross-fleet modelling, because a location's network conditions are idiosyncratic and a globally-tuned threshold produces constant noise in some sites and silence in others. The pre-service readiness check requires no modelling and should ship immediately. 2 ML engineers plus a hardware support lead, 4 months.
**Data availability:** Telemetry is abundant and retained inconsistently, often at short windows sized for debugging rather than for modelling. Hard failure labels come from support tickets and are noisy about timing — the ticket records when someone called, not when the device failed.
