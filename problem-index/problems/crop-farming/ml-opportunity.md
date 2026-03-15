# Machine Learning Opportunities — Crop Farming

**Industry:** [[crop-farming|Crop Farming]]
**Derived from:** [[problems/crop-farming/high-impact|High Impact]], [[problems/crop-farming/low-impact-1|Low Impact 1]], [[problems/crop-farming/low-impact-2|Low Impact 2]], [[problems/crop-farming/worker-life-1|Worker Life 1]], [[problems/crop-farming/worker-life-2|Worker Life 2]]

---

## 1. Crop Stress Detection from Multispectral Imagery
#cnn #semantic-segmentation #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced agronomists diagnose crop stress from visual cues that take years to develop — reading the specific yellow-green of nitrogen deficiency versus the blue-green of water stress, distinguishing soilborne disease patterns from foliar infections, identifying pest damage versus environmental stress. A CNN-based system operating on drone or satellite multispectral imagery can perform zone-level diagnosis across entire operations, scaling the agronomist's diagnostic expertise to thousands of acres with daily revisit frequency.

**ML task:** Semantic segmentation (field zones classified by stress type) + multiclass classification (stress categories: nitrogen deficiency, water stress, fungal disease — subdivided by specific disease where possible, insect damage, herbicide injury, healthy)
**Input data:** Multispectral imagery (RGB + NIR + Red Edge bands) from drone (10-30cm resolution) or satellite (Planet 3m, Sentinel-2 10m); crop type and growth stage (from planting records); weather history (temperature, precipitation, humidity from field-level or county-level stations); input application history (what was applied to this field and when); soil type and drainage characteristics
**Target:** Per-zone stress classification with confidence score; for disease classifications, specific pathogen identification where imagery supports it; recommended action (specific input, rate, timing) per diagnosed stress type
**Evaluation metric:** Classification accuracy vs. ground-truth diagnosis from agronomist field confirmation and tissue/soil tests; detection lead time (days before symptoms are visible to untrained observer); false positive rate per stress category (false nitrogen-deficiency calls trigger unnecessary fertilizer application)
**Scope:** Crop-specific models (corn, soybeans, wheat as initial targets — each has different visual signatures). Requires 2-3 growing seasons of labeled imagery correlated with ground-truth diagnosis. 12-16 week initial model development; ongoing refinement with each season's data. Team: 1 ML engineer, 1 remote sensing specialist, agronomist advisors for labeling. Integration with drone platforms (DJI, senseFly) or satellite providers (Planet API).
**Data availability:** Multispectral imagery is commercially available (Planet, $5-$10/acre/year). The bottleneck is labeled ground-truth data — agronomist-annotated field zones correlated with confirmed diagnosis. University extension networks (land-grant universities) and crop consulting companies are the most efficient labeling partners. Public datasets (USDA CropScape, Sentinel-2 archives) provide supplementary unlabeled data for pre-training.

---

## 2. In-Season Yield Prediction from Field and Weather Data
#gradient-boosting #regression #tabular-ml

**Problem statement:** Predicting field-level crop yield before harvest — from planting parameters, weather accumulation, satellite vegetation indices, and soil characteristics — enables proactive marketing decisions (forward-contracting expected production), insurance planning, and input adjustment (reducing late-season input investment on fields with poor yield trajectory).

**ML task:** Regression (predicted yield in bushels/acre at field level, updated weekly throughout the growing season)
**Input data:** Planting parameters (date, population, variety, row spacing); soil characteristics (type, organic matter, drainage class, CEC); weather accumulation (GDD, precipitation, stress degree days); satellite vegetation indices (NDVI, EVI) at weekly intervals; input application records (fertilizer rates, chemical applications); historical yield data for the field (yield monitor data from previous 3-5 years)
**Target:** Predicted yield per field with confidence interval; yield trajectory (is yield potential increasing, stable, or declining week-over-week?)
**Evaluation metric:** MAE and MAPE on yield prediction vs. actual harvested yield; prediction accuracy improvement over growing season (model should converge as season progresses); comparison to USDA county-level yield forecasts (model should beat county average by leveraging field-specific data)
**Scope:** County-or-region-specific models (weather and soil patterns are geographically localized). Requires 3-5 years of field-level yield data correlated with weather and satellite data. 8-10 week project. Data joining (yield monitor data from farm management platform + weather + satellite) is the primary engineering task.
**Data availability:** Yield monitor data exists on most precision ag-equipped farms (60%+ of US corn/soybean acres). Weather data is publicly available (NOAA, PRISM). Satellite NDVI is free (Sentinel-2) or inexpensive (Planet). The challenge is aggregating these data sources at field level with consistent spatial alignment.

---

## 3. Variable-Rate Input Prescription Maps from Zone Analysis
#gradient-boosting #regression #tabular-ml

**Problem statement:** Variable-rate technology (VRT) allows seed, fertilizer, and chemical to be applied at different rates across different zones within a field, matching input rates to each zone's yield potential and nutrient needs. But generating the prescription map — deciding what rate to apply in each zone — requires agronomic expertise that most farmers don't have, and the prescription generation process is manual and time-consuming.

**ML task:** Regression (optimal input rate per management zone given soil characteristics, yield history, and current crop condition)
**Input data:** Soil test results by zone (pH, P, K, organic matter, CEC); historical yield by zone (from yield monitor data); satellite vegetation indices by zone; soil type and topographic position; current crop condition from imagery; input response trial data (where available — how yield responded to different rates in different zones)
**Target:** Recommended input rate (seed population, nitrogen rate, phosphorus rate, potassium rate, lime rate) per management zone; predicted yield response to recommended rate vs. uniform rate; economic return analysis (input cost vs. expected yield gain per zone)
**Evaluation metric:** Yield improvement vs. uniform-rate application on split-field trials; input cost reduction on zones where model recommends lower rates; ROI per acre from variable-rate adoption
**Scope:** Requires 3-5 years of zone-level yield data with soil test data and input records. 8-12 week project. The management zone definition (how to divide a field into meaningful zones) is a modeling decision that affects all downstream predictions — current practice uses soil maps and yield stability zones.
**Data availability:** Soil test data exists at most farms but is updated infrequently (every 3-4 years). Yield data from monitors is annual. The data exists in scattered formats — the integration task is the primary barrier to model training.

---

## 4. Harvest Timing Optimization
#lstm #time-series-forecasting #tabular-ml

**Problem statement:** The optimal harvest date balances grain moisture (lower moisture means less drying cost but higher field loss risk from weather), grain quality (protein content, test weight affected by late-season weather), weather risk (each day in the field increases exposure to storms), and market price (basis patterns shift through harvest season). Experienced farmers develop an intuitive sense of when to start and stop harvest on each field — a model can formalize this multi-objective optimization.

**ML task:** Time-series forecasting (grain moisture trajectory) + multi-objective optimization (minimize drying cost + field loss risk + weather damage probability)
**Input data:** Grain moisture trajectory from combine yield monitor (historical seasons); weather forecast (temperature, precipitation, humidity — 10-day forecast); crop maturity indicators (GDD accumulation, satellite NDVI trajectory); grain market data (local basis, futures price); drying cost parameters (energy price, dryer capacity)
**Target:** Recommended harvest start date per field; daily harvest priority ranking across fields (which field to harvest today given moisture, weather risk, and logistics); estimated drying cost per day of delay
**Evaluation metric:** Total drying cost reduction vs. farmer's actual harvest timing decisions; field loss avoidance (avoided exposure to storm damage events); grain quality preservation
**Scope:** Region-specific models (harvest timing is driven by local weather patterns). Requires 3-5 seasons of harvest data with daily moisture measurements. 6-8 week project. Most valuable for operations with more acres than harvest capacity — where the sequencing decision across fields determines total harvest cost.
**Data availability:** Combine yield monitors log moisture by field and by pass. Weather forecast data is commercially available. Grain market data is public. The data exists; the challenge is linking multi-season harvest data with weather outcomes to train the risk model.

---

## 5. Weed Species Identification for Targeted Spraying
#cnn #multiclass-classification #object-detection #computer-vision

**Problem statement:** Herbicide application is the largest chemical input cost for row crop farms ($30-$60/acre), and herbicide-resistant weed populations (waterhemp, Palmer amaranth, marestail) require species-specific treatment — a broad-spectrum application that worked 10 years ago is now ineffective on resistant populations. Identifying weed species at the field level enables targeted, species-specific herbicide application rather than blanket spraying.

**ML task:** Object detection (locate individual weed plants in imagery) + multiclass classification (weed species identification)
**Input data:** Ground-level RGB images from sprayer-mounted cameras or drone imagery at sufficient resolution to distinguish weed species (leaf shape, growth habit); crop type and growth stage (to distinguish crop from weed); regional weed species prevalence data
**Target:** Weed species identification per detected plant; weed density map per field zone; recommended herbicide program per zone based on identified species and resistance profile
**Evaluation metric:** Species classification accuracy (precision and recall per species); spot-spray savings vs. blanket application (herbicide volume reduction); weed control efficacy (post-treatment weed density)
**Scope:** Requires training data for the 10-15 most common weed species in the target geography. Public datasets exist (DeepWeeds, PlantVillage) but may not cover regional species. 8-12 week project. Hardware integration with spot-spray systems (See & Spray by John Deere, Bilberry) is the deployment path.
**Data availability:** Public weed image datasets provide a starting point. Regional calibration requires field-collected images labeled by agronomists — 500-1,000 images per species for fine-tuning. University weed science programs are natural data partners.
