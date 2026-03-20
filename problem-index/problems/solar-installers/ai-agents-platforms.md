# AI Agents and Platforms — Solar Installers

**Industry:** [[solar-installers|Solar Installers]]
**Tags:** #ai-agent #ai-platform #cnns #gradient-boosting #time-series-forecasting #transfer-learning #feature-engineering #evaluation-metrics #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### Aurora Solar
The leading solar design platform. Contains system design data, shade analysis, and production simulations for thousands of installers. Aurora has a developer API. This is the primary integration point for design automation and the best training data source for layout optimization ML.

### SolarEdge / Enphase Enlighten
Inverter monitoring platforms with production APIs. SolarEdge's monitoring dashboard and Enphase's Enlighten platform provide per-system production time series. Both have developer APIs for data access. These are the data sources for anomaly detection.

### NREL (National Renewable Energy Laboratory)
Publishes the NSRDB (National Solar Radiation Database) — weather and irradiance data by location. Also maintains the SAM (System Advisor Model) for solar production simulation. NREL data is publicly available and is the weather normalization foundation for production anomaly detection.

---

## AI Agent Opportunities

### 1. New Lead Pre-Qualification Agent
**Trigger:** New lead submitted via web form or added to CRM.
**Action sequence:**
1. Pull address → aerial imagery shade estimate (Google Project Sunroof API) and roof area
2. Determine utility territory → pull net metering policy and current retail rate
3. Join to property assessor data (home age, structure type, ownership status)
4. Score the lead on close probability
5. Return score to CRM with supporting rationale and any disqualifying flags (rental property, heavily shaded roof)
**Value:** Sales rep sees a pre-scored lead within minutes of submission. Prioritizes outreach to high-probability leads before competitors contact them.

### 2. Post-Installation Monitoring Agent
**Trigger:** Monthly scheduled run for all active monitored systems.
**Action sequence:**
1. Pull monthly production from SolarEdge/Enphase API for each system
2. Pull weather data (actual irradiance) from NRDB for the system's location
3. Compute weather-adjusted production vs. original Aurora estimate
4. Flag systems with > 10% deviation for two consecutive months
5. Generate proactive customer message for flagged systems: friendly, non-alarming, offers a free check
6. Route to service team with flagged system details and production history
**Value:** Converts reactive complaint handling into proactive customer service. Identifies warranty-claimable hardware issues during the warranty period.

### 3. Site Survey Report Generation Agent
**Trigger:** Surveyor marks site survey complete in mobile app.
**Action sequence:**
1. Run OCR on electrical panel photos to extract main breaker size, bus bar rating, manufacturer
2. Pull aerial roof geometry from Aurora Solar API for the address
3. Combine with surveyor's checklist responses
4. Generate complete site survey report with extracted panel specs, roof dimensions, photos organized by category, and any access notes
5. Deliver to design team queue in Aurora Solar or project management system
**Value:** Eliminates 30-45 minutes of post-survey report writing. Panel spec extraction by OCR is more accurate than manual transcription from memory.

### 4. Pipeline Stall Detection Agent
**Trigger:** Daily run on active sales pipeline in CRM.
**Action sequence:**
1. Identify leads that have been in the same pipeline stage for > 2× the median time for that stage
2. Generate a recommended follow-up action for each stalled lead based on the reason for delay (awaiting utility decision, customer undecided, financing pending)
3. Draft personalized re-engagement message for customer-undecided stalls
4. Flag time-sensitive items (interconnection queue deadline, incentive expiration date approaching)
5. Present prioritized action list to sales rep
**Value:** Reduces pipeline leakage from neglected leads. Solar sales cycles are long and complex — systematic stall detection prevents the silent losses that account for 20-30% of qualified leads that go cold.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| System layout optimization | Build | Aurora Solar API | Optimization model is custom; Aurora platform is the deployment environment |
| Performance anomaly detection | Build | SolarEdge/Enphase API | Anomaly model is custom; monitoring data is buy |
| Lead qualification scoring | Build | Property data APIs | Scoring model is custom; property data is buy |
| Site survey OCR (panel specs) | Buy/extend | Google Vision / AWS Textract | OCR engine is commodity; panel label field extraction is custom |
| Interconnection timeline prediction | Build | FERC queue data (public) | Regression model; utility history is proprietary data advantage |
| Roof suitability screening | Build | Google Project Sunroof API | Suitability model is custom; imagery is buy |
