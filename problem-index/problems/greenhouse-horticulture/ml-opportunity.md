# Machine Learning Opportunities — Greenhouse Horticulture

**Industry:** [[greenhouse-horticulture|Greenhouse Horticulture]]
**Derived from:** [[problems/greenhouse-horticulture/high-impact|High Impact]], [[problems/greenhouse-horticulture/low-impact-1|Low Impact 1]], [[problems/greenhouse-horticulture/low-impact-2|Low Impact 2]], [[problems/greenhouse-horticulture/worker-life-1|Worker Life 1]], [[problems/greenhouse-horticulture/worker-life-2|Worker Life 2]]

---

## 1. Pest and Disease Early Detection from Plant Images
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced IPM scouts visually identify pest damage, insect presence, and disease symptoms on greenhouse crops from subtle cues (leaf stippling, webbing, discoloration patterns, fungal sporulation) that take 2-3 years to learn. A CNN-based classifier can capture this tacit visual expertise and make it available to every worker holding a phone.

**ML task:** Multiclass image classification with localization (pest/disease type + severity grade)
**Input data:** RGB images of plant canopies, leaf surfaces (top and bottom), growing tips, and root zones. Captured via smartphone (scout-level) or fixed overhead cameras (zone-level). Minimum resolution 1280x960 for leaf-level detail. Supplementary metadata: crop type, zone ID, date, recent climate conditions.
**Target:** Multi-label classification across 15-25 pest/disease categories (thrips, whitefly, spider mites, fungus gnats, aphids, botrytis, powdery mildew, downy mildew, pythium, fusarium, bacterial leaf spot, edema, nutrient deficiency subcategories) plus a severity score (0-3 scale: absent, early, moderate, severe). Bounding box or heatmap localization for the affected area.
**Evaluation metric:** Macro F1-score across all categories, with recall weighted 2x for high-consequence pests (thrips, botrytis) where early detection prevents exponential spread. Target: >0.80 macro F1 for the top 10 most common categories.
**Scope:** 6-9 month build for a production-grade mobile classifier. Requires partnership with 5-10 commercial greenhouses for image collection across seasons and crop types. Transfer learning from PlantVillage or iNaturalist pretrained models provides a strong starting point but greenhouse conditions (controlled lighting, dense canopy, specific cultivars) differ enough from field crops that substantial fine-tuning is needed. Team: 2 ML engineers, 1 mobile developer, 1 domain expert (experienced IPM consultant). The hardest part is label quality — experienced scouts disagree on severity grades 20-30% of the time, requiring a consensus labeling protocol.
**Data availability:** Moderate. No large public dataset exists for greenhouse-specific pests at the cultivar level. PlantVillage covers field crop diseases. Individual greenhouses have scouting logs (text records of pest locations and severity) but no systematic image archives. Data collection must be designed into the product — the scouting app captures images that become training data. Expect 10,000-30,000 labeled images needed for the initial model, growing with use.

---

## 2. Climate Control Setpoint Optimization
#reinforcement-learning #regression #tabular-ml #revenue-impact

**Problem statement:** Greenhouse climate control involves continuous tradeoffs between energy cost, crop growth rate, crop quality, and disease pressure. Current rule-based controllers leave significant optimization headroom that an RL agent can capture by learning crop-specific response functions from sensor data and growth outcomes.

**ML task:** Model-based reinforcement learning for sequential decision-making (setpoint adjustment every 15-60 minutes) with a multi-objective reward: minimize energy cost, maximize crop growth rate, maintain quality thresholds.
**Input data:** Time-series sensor data from climate computers (inside temperature, humidity, CO2 concentration, PAR light, pipe temperature, vent position, shade curtain position — typically logged every 60 seconds). External weather data (temperature, solar radiation, wind speed, cloud cover forecast). Energy price signals (natural gas spot price, electricity TOU rates). Crop growth measurements (weekly: stem length, leaf count, flower stage, fresh weight samples).
**Target:** Optimal setpoint vector every 15-60 minutes: heating pipe temperature, ventilation temperature, CO2 injection rate, shade curtain position, supplemental light on/off. Constrained to grower-defined safety bounds.
**Evaluation metric:** Composite reward: energy cost reduction ($/sq ft/week) + crop quality score (grower-rated 1-5) + growth rate deviation from target schedule. Primary business metric: $/sq ft/year total margin improvement. Target: 15-25% energy cost reduction with no quality degradation.
**Scope:** 12-18 month build. The RL agent must be trained in simulation first (crop growth models from Wageningen literature provide reasonable dynamics), then fine-tuned with real greenhouse data via constrained exploration. Requires API integration with at least one major climate computer platform (Priva's API is the most accessible). Team: 2 ML engineers (RL experience), 1 controls engineer, 1 crop science advisor. The key risk is sim-to-real transfer — greenhouse dynamics vary significantly by structure, location, and crop.
**Data availability:** Good for climate sensor data — every commercial greenhouse with a Priva, Ridder, or Argus controller has years of minute-level logs. Poor for crop response data — growth measurements are manual, inconsistent, and rarely linked to climate records. The data pipeline (connecting climate logs to crop outcomes) is the primary data engineering challenge.

---

## 3. Crop Growth Rate Prediction
#gradient-boosting #regression #tabular-ml

**Problem statement:** Greenhouse crop scheduling depends on accurate finish-date predictions, but actual crop duration varies by 1-3 weeks from catalog estimates due to accumulated light, temperature, and cultivar-specific responses. A regression model that predicts days-to-finish from current growth stage and climate trajectory would transform scheduling accuracy.

**ML task:** Regression — predict days remaining to shipping readiness from current crop state and forecasted growing conditions.
**Input data:** Crop lot records (cultivar, planting date, pot size, current growth stage scored on a standardized scale), accumulated growing degree days (GDD) and daily light integral (DLI) since planting, 10-day weather/climate forecast, zone assignment and substrate type. Historical lot-level data: planting date, weekly growth stage scores, actual ship date.
**Target:** Continuous value: predicted days to ship-readiness, plus a prediction interval (e.g., 80% confidence the crop ships between day X and day Y).
**Evaluation metric:** Mean absolute error (MAE) in days, targeting MAE < 3 days for crops with 8-16 week production cycles. Also track calibration of prediction intervals (80% of actual outcomes should fall within the 80% interval).
**Scope:** 4-6 month build. Gradient-boosting (XGBoost/LightGBM) on tabular features is the natural starting point. Requires historical lot data from 3-5 greenhouses across at least 2 growing seasons. Team: 1 ML engineer, 1 data engineer, 1 domain consultant. The main challenge is standardizing growth stage scoring across growers — each operation uses slightly different scales.
**Data availability:** Moderate. Large ornamental operations (Metrolina, Costa Farms, Color Point) track lot-level planting and ship dates in their ERP systems, but growth-stage measurements are inconsistent. Climate data is abundant from climate computers. The gap is linking lot records to climate zone history — most ERPs don't record which zone a lot was in.

---

## 4. Irrigation Scheduling from Substrate Sensor Data
#lstm #anomaly-detection #signal-processing

**Problem statement:** Greenhouse irrigation management requires interpreting substrate moisture, EC, and temperature signals to determine when and how much to water — a skill that experienced irrigation technicians develop through years of observing plant response. An LSTM-based model can learn normal irrigation-response patterns per zone and crop type, then flag anomalies and recommend adjustments.

**ML task:** Time-series anomaly detection + regression (predict next irrigation event timing and volume).
**Input data:** Substrate sensor time series (moisture content, EC, temperature — sampled every 5-15 minutes per zone), irrigation event logs (valve open/close times, flow meter readings), climate data (inside temperature, humidity, solar radiation), crop type and growth stage per zone.
**Target:** Dual output: (1) anomaly flags with severity and probable cause (clogged emitter, valve leak, salt buildup, sensor drift), (2) recommended next irrigation time and volume per zone.
**Evaluation metric:** For anomaly detection: precision@90% recall for critical anomalies (clogged emitters, valve failures). For irrigation recommendation: MAE of predicted optimal irrigation volume vs. expert-adjusted volume (calibrated against experienced grower decisions over a validation period).
**Scope:** 6-8 month build. Requires sensor infrastructure investment — most greenhouses have climate sensors but not per-zone substrate sensors. Grodan GroSens and Meter TEROS provide commercial options at $200-500 per sensor point, needing 2-4 sensors per irrigation zone. Team: 1 ML engineer (time-series experience), 1 data engineer, 1 irrigation consultant. Training requires 6-12 months of sensor data with annotated irrigation decisions from an experienced technician.
**Data availability:** Low to moderate. Few greenhouses have dense substrate sensor networks today. Grodan has a cloud platform (e-Gro) with data from Dutch vegetable greenhouses, but US ornamental data is scarce. This is a "build the data pipeline to enable the ML" problem — the sensor deployment is the prerequisite.

---

## 5. Bloom Timing Prediction for Ornamental Crops
#gradient-boosting #time-series-forecasting #tabular-ml

**Problem statement:** Ornamental growers selling flowering plants (poinsettias, chrysanthemums, Easter lilies, spring bulbs) must deliver product in bloom for specific retail windows. Bloom timing depends on photoperiod manipulation, temperature, cultivar genetics, and accumulated growing conditions. Mis-timed crops lose 30-60% of their value.

**ML task:** Time-series forecasting — predict bloom date (and bloom window duration) for each crop lot.
**Input data:** Cultivar identity, photoperiod treatment start date and protocol (short-day initiation, lighting schedule), accumulated temperature and DLI since treatment start, historical lot data (treatment start → actual first-color date → actual full-bloom date → actual market-window end date). External data: cultivar response curves from breeder trial data (Syngenta, Dümmen Orange, Selecta One publish these).
**Target:** Three date predictions per lot: first color, full bloom (peak marketability), and end of market window. Each with confidence intervals.
**Evaluation metric:** MAE in days for full-bloom date prediction. Target: MAE < 2 days for major cultivar groups (poinsettia, chrysanthemum). Business metric: percentage of lots that hit their target ship week.
**Scope:** 4-6 month build. This is a high-value, narrow-domain problem well-suited to gradient boosting on tabular features. The breeder trial data provides strong priors. Requires partnership with 3-5 flowering plant producers who track photoperiod treatment dates and actual bloom dates at the lot level. Team: 1 ML engineer, 1 domain expert. Key risk: cultivar turnover — breeders release new varieties annually, requiring continuous model updates with limited data per new cultivar.
**Data availability:** Moderate to good. Large flowering plant producers (Ecke/Syngenta for poinsettias, Yoder/Dümmen Orange for mums) track treatment and bloom dates meticulously because mis-timing is so costly. Breeder trial reports are semi-public. The challenge is getting growers to share proprietary lot-level data — a cooperative data model or anonymized benchmarking service could unlock this.
