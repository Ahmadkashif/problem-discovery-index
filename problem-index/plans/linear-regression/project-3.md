# Project 3: Crop Yield Prediction from Weather and Satellite Data

**Difficulty:** Advanced
**Domain:** Agriculture / Global Food Security
**Source Problem:** Farmers, commodity traders, and governments need to know how much food will be harvested before the combine hits the field. A good yield forecast months before harvest affects food prices, trade policy, and famine prevention globally. Your model predicts corn yield per county from weather patterns and vegetation signals.

---

## The Problem

The USDA publishes county-level crop yield data for every major US crop going back decades. Weather data (temperature, rainfall, drought indices) is freely available from NOAA. Satellite-derived vegetation indices (NDVI — how green and healthy the crop is) are free from Sentinel-2 and MODIS.

The advanced challenge: you need to **integrate multiple data sources** (USDA yields + NOAA weather + satellite vegetation), **engineer domain-specific features** (growing degree days, cumulative precipitation during critical growth stages), and discover that **feature engineering matters more than model complexity** — linear regression with smart features captures 60-75% of yield variance.

---

## Datasets

### Source 1: USDA NASS Crop Yields
- **URL:** https://quickstats.nass.usda.gov/
- **API:** https://quickstats.nass.usda.gov/api/
- **What:** County-level annual yields for corn, soybeans, wheat, and other crops
- **Key fields:** Year, State, County, Commodity, Yield (bushels/acre)
- **Size:** For corn: ~2,500-3,000 counties reporting annually, 20+ years = 50,000-75,000 county-year observations
- **Format:** CSV via Quick Stats download tool. Filter: Commodity = CORN, Data Item = YIELD (BU/ACRE), Geographic Level = COUNTY

### Source 2: NOAA County-Level Climate
- **URL:** https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping
- **What:** Monthly average temperature and precipitation by county
- **Also:** nClimDiv dataset for county-level monthly climate going back to 1895
- **Key features to derive:**
  - **Growing Degree Days (GDD):** `GDD = max(0, (T_max + T_min)/2 - 10°C)` accumulated over the growing season (April-September for corn). This is the #1 feature for crop yield prediction.
  - **Cumulative precipitation** during critical months (June-August for corn)
  - **Drought index:** Palmer Drought Severity Index (PDSI) — available from NOAA
  - **Heat stress days:** Count of days with max temperature > 35°C during silking (July)

### Source 3: Satellite Vegetation Index (Stretch Goal)
- **URL:** Google Earth Engine (https://earthengine.google.com/) — free account
- **What:** MODIS NDVI at 250m resolution, 16-day composites (product MOD13Q1)
- **Why:** NDVI (Normalized Difference Vegetation Index) measures crop greenness/health from space. High NDVI during July-August = healthy crop = high yield.
- **How to get it for beginners:** Skip raw satellite processing. Use the Rangeland Analysis Platform or pre-computed county-level NDVI from published datasets.
- **Alternative:** Several Kaggle datasets pre-combine yield + weather features — search "crop yield prediction"

---

## ML Task

**Regression:** Predict corn yield (bushels/acre) for a given county in a given year from weather features measured during the growing season.

**Input features (build progressively):**

*Level 1 (weather only):*
- Cumulative GDD April-September
- Total precipitation June-August (mm)
- Average temperature June-August (°C)
- PDSI drought index (July)
- County state (categorical — Midwestern states yield more than southern)
- Year (captures long-term yield trend from improving seed genetics)

*Level 2 (add temporal):*
- Previous year's yield for same county (autoregressive feature)
- 5-year moving average yield (captures long-term county productivity)
- GDD × precipitation interaction (hot + dry is catastrophically worse than either alone)
- Heat stress days in July (count of days > 35°C)

*Level 3 (add satellite — stretch):*
- Peak NDVI during July-August (county average)
- NDVI anomaly (current year NDVI minus 5-year average NDVI for same county)

**Target:** Corn yield in bushels/acre (continuous). Typical range: 100-250 bu/acre.

---

## Evaluation Criteria

| Level | R² | RMSE (bu/acre) | MAPE | What it means |
|-------|-----|----------------|------|--------------|
| Beginner | > 0.40 | < 35 | < 18% | Year + state explain the broad pattern |
| Good | > 0.60 | < 25 | < 12% | GDD and precipitation captured |
| Excellent | > 0.75 | < 18 | < 8% | Domain features (heat stress, interactions) + satellite |

**Primary metric:** R² and RMSE
**Secondary:** MAPE (% error — useful for comparing across regions with different baseline yields)
**Benchmark:** USDA's own forecasts achieve ~5-10% MAPE at national level. County-level is harder.

---

## Implementation — 4 Phases

### Phase 1: Exploration (Days 1-3)

1. **Download USDA yield data:**
   - Go to https://quickstats.nass.usda.gov/
   - Filters: Program = SURVEY, Sector = CROPS, Group = FIELD CROPS, Commodity = CORN, Data Item = CORN, GRAIN - YIELD, MEASURED IN BU / ACRE, Geographic Level = COUNTY
   - Download CSV for 2000-2023
2. **Download NOAA weather data:**
   - Go to https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping
   - Download monthly average temperature and precipitation for the same counties and years
   - Join on FIPS code + year + month
3. **Explore the yield data:**
   - Distribution of yields by state — which states produce the most corn?
   - Yield trend over time — yields have been steadily increasing due to better seed genetics (~2 bu/acre/year). This trend must be a feature.
   - Year-to-year variance — some years (2012 drought) show dramatic drops. These are what weather features explain.
4. **Explore weather-yield relationships:**
   - Scatter: July temperature vs yield. You should see a non-linear pattern — moderate heat is good, extreme heat is catastrophic.
   - Scatter: June-August precipitation vs yield. Too little = drought. Too much = flooding. There's a sweet spot.
   - This non-linearity is important — it's why feature engineering (heat stress days, interactions) matters.

### Phase 2: Baseline (Days 4-5)

1. **Compute GDD:** For each county-year, sum daily GDD over April-September. If you only have monthly averages, approximate: `monthly_GDD ≈ max(0, avg_temp - 10) × days_in_month`
2. **Build a simple feature matrix:** Year, State (one-hot), cumulative GDD, total summer precipitation
3. **Split:** Leave-one-year-out cross-validation is ideal for time-series — train on all years except 2020, predict 2020, repeat for each year. Alternatively, train on 2000-2018, test on 2019-2023.
4. **Train plain linear regression.** Report R² and RMSE.
5. **Examine coefficients:** GDD coefficient should be positive (more heat units = more growth). Precipitation should be positive. State dummies capture baseline productivity differences.
6. **Check the year coefficient:** If it's ~2 bu/acre/year, that matches the known genetic improvement trend. Your model learned something real.

### Phase 3: Primary Model (Days 6-8)

1. **Domain feature engineering (this is where you shine or stall):**
   - **Heat stress days:** Count of days in July with max temp > 35°C (corn silking is extremely heat-sensitive). If you only have monthly data, use: `heat_stress_proxy = max(0, july_avg_temp - 30)`. This single feature can improve R² by 5-10%.
   - **GDD × Precipitation interaction:** `gdd * summer_precip` — captures "hot and dry" vs "hot and wet" difference
   - **Precipitation squared:** Too much rain is also bad (flooding, disease). Adding a quadratic captures the diminishing/reversing returns.
   - **Previous year yield:** `yield_lag1` — accounts for soil condition and management continuity
   - **5-year rolling average:** captures long-term county productivity
2. **Ridge regression:** With many engineered features, regularization prevents overfitting
3. **Compare:** Baseline (3 features) vs full model (10+ features). How much did feature engineering buy you?

### Phase 4: Iteration (Days 9-10)

1. **Residual analysis by year:** Which years does the model miss badly? (2012 drought year will likely have large residuals — extreme events are hard to predict from monthly averages)
2. **Residual analysis by state:** Does the model work better in Iowa than Georgia? (Probably — Iowa has more consistent corn production)
3. **Add satellite NDVI (stretch):**
   - If you have Google Earth Engine access: compute county-level mean NDVI for July-August from MODIS
   - NDVI should be the strongest single predictor. A late-July NDVI measurement is essentially a "photo of the crop" — it directly reflects plant health.
   - Compare: weather-only model vs weather+NDVI model. NDVI should improve R² by 10-15%.
4. **The punchline:** Build the same model with gradient boosting (XGBoost). Compare R² to your best linear regression. The improvement is real but modest (5-15%) — because **you already captured the signal through feature engineering.** This is the lesson: with domain knowledge, a simple model goes very far.
5. **Final report:** Your best R², which features matter most (ranked by standardized coefficients), and what this means for yield forecasting.

---

## What You Learn from This Project

| Concept | How it shows up |
|---------|----------------|
| Multi-source data integration | Joining USDA yields + NOAA weather + satellite by FIPS + year |
| Domain-driven feature engineering | GDD, heat stress, interactions — domain knowledge creates features |
| Features > algorithms | Linear regression with smart features ≈ gradient boosting with raw features |
| Non-linear relationships | Temperature-yield curve is non-linear → polynomial/interaction features |
| Leave-one-year-out CV | Time-aware cross-validation for temporal data |
| Interaction terms | temp × precipitation captures "hot and dry" catastrophe |
| Quadratic features | precipitation² captures "too much rain is bad too" |
| Lagged features | Last year's yield as a predictor |
| Real-world benchmarking | Comparing against USDA's own forecast accuracy |
| Data pipeline skills | Downloading, cleaning, joining data from government sources |
