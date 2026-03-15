# Machine Learning Opportunities — Solar Installers

**Industry:** [[solar-installers|Solar Installers]]
**Derived from:** [[problems/solar-installers/high-impact|High Impact]], [[problems/solar-installers/low-impact-1|Low Impact 1]], [[problems/solar-installers/low-impact-2|Low Impact 2]], [[problems/solar-installers/worker-life-1|Worker Life 1]], [[problems/solar-installers/worker-life-2|Worker Life 2]]

---

## 1. System Layout Optimization from Aerial Imagery and Shade Analysis
#cnn #regression #computer-vision #tabular-ml #revenue-impact

**Problem statement:** Solar system design requires optimizing panel placement to maximize annual energy production given roof geometry, shade conditions, and structural/setback constraints. Automate the layout optimization that currently requires 45-90 minutes of experienced designer time per site.

**ML task:** Layout optimization — given roof geometry, LIDAR shade model, and production simulation, return optimal panel placement and stringing configuration that maximizes annual kWh production
**Input data:** Aurora Solar design records with panel placement configurations and associated production simulations. Actual production data from SolarEdge/Enphase monitoring for completed systems provides ground truth on simulated vs. actual production.
**Target:** Optimal panel layout (positions, string configuration); production estimate with confidence interval; flagged tradeoffs (adding 2 more panels adds 8% production but increases shade mismatch by 3%)
**Evaluation metric:** Simulated annual production of model-generated layout vs. experienced-designer layout on the same roof; actual-to-simulated production ratio for systems using auto-generated vs. manually designed layouts
**Scope:** Aurora Solar data partnership is the primary path — their platform has both the training data and the deployment channel. Optimization approach (genetic algorithm or reinforcement learning with production simulation as the reward function) may outperform discriminative ML for this combinatorial layout problem. 12-18 month development.
**Data availability:** Aurora Solar has the design data. Inverter monitoring platforms (SolarEdge, Enphase) have the actual production data. The combination — design parameters + actual production — provides the training signal for production prediction accuracy.

---

## 2. System Performance Anomaly Detection
#isolation-forest #anomaly-detection #time-series-forecasting #signal-processing #quick-win

**Problem statement:** Detect when an installed system's production is below weather-adjusted expectations, indicating hardware faults or degradation — before the customer notices.

**ML task:** Anomaly detection on time-series production data; expected production modeling (weather-adjusted baseline); binary classification (anomalous vs. normal for a given production period)
**Input data:** Monthly/weekly production from SolarEdge or Enphase monitoring per system; weather data from NREL NSRDB by system location; original Aurora Solar production estimate for each system
**Target:** System anomaly flag when production deviates > threshold from weather-adjusted baseline; anomaly type classification (string-level, inverter-level, full-system communication failure vs. performance degradation)
**Evaluation metric:** Recall on systems that subsequently required service calls (did we flag them before the customer called?); false positive rate (alert triggered but no issue found); lead time between first anomaly flag and confirmed hardware issue
**Scope:** Quick win — the data infrastructure (monitoring platform + weather data) exists. An ARIMA or Prophet baseline model for weather-adjusted production, combined with a statistical anomaly threshold, can be built in 4-6 weeks. The integration with SolarEdge/Enphase APIs is the primary technical work.
**Data availability:** SolarEdge and Enphase provide monitoring APIs. NREL NSRDB provides historical irradiance data by location. Original system production estimates from Aurora Solar project files.

---

## 3. Lead Qualification Scoring
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Score solar leads by close probability using property-specific features (roof orientation, electricity usage, utility rate, shade estimate) to focus sales team effort on highest-probability leads.

**ML task:** Binary classification (lead closes: yes/no) from property and engagement features
**Input data:** Lead records with property address (→ join to aerial imagery shade estimate, assessor data for roof area and age), electricity bill amount, utility territory, engagement signals (website form vs. referral source, response speed), outcome (closed vs. lost and reason)
**Target:** Lead score (0-100 close probability); priority tier (hot/warm/cold); specific friction factors (e.g., "roof orientation is east-facing — lower production than standard")
**Evaluation metric:** AUC-ROC for close prediction; revenue per sales hour for reps using scored list vs. unranked list; recall on deals above $20,000 system value
**Scope:** Any solar company with 500+ historical leads and close outcome tracking has training data. Gradient boosting on ~10 property and engagement features: 3-4 week project. CRM integration (HubSpot, Salesforce) is the deployment path.
**Data availability:** Property data from Google Project Sunroof API and county assessor. Utility rate from NREL utility rate database. Lead engagement data from CRM. Close outcome from CRM. All accessible.

---

## 4. Interconnection Timeline Prediction
#gradient-boosting #regression #tabular-ml

**Problem statement:** Predict interconnection approval timeline for a specific utility territory and project size from the solar company's historical submission records and public utility queue data.

**ML task:** Regression — expected timeline in days from submission to approval, by utility and project type
**Input data:** Historical interconnection submissions with utility territory, project size (kW), submission date, approval date, application type (simplified vs. standard review). Public FERC queue data for the utility.
**Target:** Timeline estimate with confidence interval; probability of exceeding 90/120/180 day threshold
**Evaluation metric:** MAE between predicted and actual timeline on held-out submissions; frequency of actual timeline within predicted confidence interval; improvement in customer timeline promise accuracy vs. manual estimates
**Scope:** Solar companies with 100+ historical interconnection submissions in a specific utility territory have the training data. Gradient boosting regression: 2-3 week project. High value for companies expanding into new utility territories where they lack historical experience.
**Data availability:** The solar company's own project records (submission and approval dates per utility). FERC queue data for public utilities. PUC filings for regulated utilities. State interconnection databases.

---

## 5. Roof Structural Suitability Screening from Aerial Imagery
#cnn #binary-classification #computer-vision #tabular-ml

**Problem statement:** Pre-screen leads for structural suitability before committing to a site survey — identifying roofs with obvious disqualifying characteristics (severe deterioration, insufficient south-facing area, complex geometry with excessive penetrations) that would produce unfavorable installation economics.

**ML task:** Binary classification (structurally suitable for solar installation: yes/no) from aerial imagery + property data; flagging of specific disqualifying features (extensive tree shade, roof age/condition concerns, insufficient area)
**Input data:** Aerial imagery (Google Maps, EagleView) matched to installation records — systems that proceeded to installation vs. leads that were lost after site survey due to structural disqualification
**Target:** Suitability score (0-100); specific disqualifying factor if below threshold; recommended next step (proceed to site survey / conditional proceed with noted concerns / do not proceed)
**Evaluation metric:** Recall on disqualified leads (did we flag the sites that were ultimately disqualified after survey?); precision on proceed recommendations (of auto-qualified sites, what fraction proceeded to installation?); reduction in wasted site survey cost
**Scope:** Aerial imagery + installation outcome data from a solar company's project records. 5,000-15,000 labeled addresses (qualified/disqualified by site survey outcome): 2-3 month data assembly + 8-10 week modeling. Reduces wasted site survey cost ($200-$400 per survey) on structurally unsuitable sites.
**Data availability:** Google Maps API provides aerial imagery by address. EagleView provides higher-resolution rooftop imagery. Site survey outcomes are in the solar company's project management system. The label (proceeded vs. disqualified after survey) is available in any firm with structured project tracking.
