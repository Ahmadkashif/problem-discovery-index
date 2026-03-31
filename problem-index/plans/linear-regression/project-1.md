# Project 1: Building Energy Consumption Prediction

**Difficulty:** Beginner
**Domain:** Energy / Climate Policy
**Source Problem:** Buildings account for 40% of US energy consumption. NYC Local Law 97 now imposes carbon caps on large buildings. Your model identifies which buildings are the worst offenders and what drives their energy waste.

---

## The Problem

Every building in New York City over 25,000 sqft must report its annual energy consumption under Local Law 84. The data is public. Your job: predict a building's **Energy Use Intensity (EUI)** — kBTU per square foot per year — from its physical characteristics. A high EUI means the building is an energy hog. A low EUI means it's efficient.

Why this matters: if you can predict EUI from building type, age, and size alone, you can flag buildings that use *more* energy than similar buildings — those are the ones where retrofits will have the highest impact.

---

## Dataset

**Primary:** NYC LL84 Energy and Water Data Disclosure
- **URL:** https://data.cityofnewyork.us — search "Energy and Water Data Disclosure for Local Law 84"
- **Size:** ~35,000 properties per year
- **Format:** CSV, single download
- **Key columns:** Property Type (Office, Multifamily, Retail, Hotel, Hospital, etc.), Gross Floor Area (sqft), Year Built, Number of Buildings, Site EUI (kBTU/sqft — your target), Source EUI, Electricity Use (kWh), Natural Gas Use (therms), ENERGY STAR Score, GHG Emissions (metric tons CO2e), Weather Normalized EUI

**Starter alternative (ultra-clean, for first day):** UCI Energy Efficiency Dataset
- **URL:** https://archive.ics.uci.edu/dataset/242/energy+efficiency
- **Size:** 768 samples, 8 features
- **Features:** Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, Glazing Area Distribution
- **Targets:** Heating Load, Cooling Load

**Stretch (multi-city):** Chicago Energy Benchmarking (https://data.cityofchicago.org), Seattle Building Energy (https://data.seattle.gov), San Francisco (https://datasf.org)

---

## ML Task

**Regression:** Predict Site EUI (kBTU/sqft/year) from building characteristics.

**Input features:**
- Property type (categorical: Office, Multifamily Housing, Hotel, etc.)
- Gross floor area (continuous, sqft)
- Year built (continuous → can derive building age)
- Number of buildings on the property (integer)
- Borough (categorical: Manhattan, Brooklyn, etc.)

**Target:** Site EUI (kBTU/sqft/year) — continuous

---

## Evaluation Criteria

| Level | R² | RMSE (kBTU/sqft) | What it means |
|-------|-----|-------------------|--------------|
| Beginner | > 0.30 | < 120 | Your model beats guessing the average |
| Good | > 0.50 | < 90 | You capture the main drivers (building type, size) |
| Excellent | > 0.65 | < 70 | Strong feature engineering, regularization working |

**Primary metric:** R² (how much variance explained)
**Secondary:** RMSE (in same units as target — directly interpretable)

---

## Implementation — 4 Phases

### Phase 1: Exploration (Day 1)

1. Download NYC LL84 data (most recent year)
2. Load with pandas. Check shape, dtypes, missing values
3. Look at the target distribution: `df['Site EUI (kBtu/ft²)'].hist()` — is it skewed? (Yes — log-transform will help)
4. Check correlations: `df[numeric_cols].corr()` — which features correlate with EUI?
5. Visualize: scatter plots of EUI vs sqft, EUI vs year_built. Box plots of EUI by property_type.
6. Key questions to answer:
   - How many property types are there? Which have the highest/lowest median EUI?
   - Is there a relationship between building age and energy use?
   - Are there obvious outliers? (A building with EUI of 5,000 is probably a data entry error)

### Phase 2: Baseline (Day 2)

1. **Clean:** Remove rows with missing EUI. Drop obvious outliers (EUI > 1000 or < 1). Handle missing features.
2. **Encode:** One-hot encode Property Type. Keep sqft and year_built as-is.
3. **Split:** 80/20 train/test split
4. **Train a plain linear regression:**
   ```python
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_squared_error, r2_score

   model = LinearRegression()
   model.fit(X_train, y_train)
   y_pred = model.predict(X_test)

   print(f"R²: {r2_score(y_test, y_pred):.3f}")
   print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.1f}")
   ```
5. **Interpret coefficients:** `pd.Series(model.coef_, index=feature_names).sort_values()` — which features have the largest positive/negative weights?
6. Record your baseline R² and RMSE. This is what you'll improve on.

### Phase 3: Primary Model (Days 3-4)

1. **Feature engineering:**
   - Building age: `current_year - year_built`
   - Log-transform the target: `np.log1p(eui)` — this often improves R² significantly for skewed targets
   - Interaction: `sqft × num_buildings` (campus-style properties behave differently)
   - Borough as a feature (location affects energy use — Manhattan buildings differ from outer boroughs)
2. **Try Ridge and Lasso:**
   ```python
   from sklearn.linear_model import Ridge, Lasso
   from sklearn.model_selection import cross_val_score

   for alpha in [0.01, 0.1, 1.0, 10.0, 100.0]:
       ridge = Ridge(alpha=alpha)
       scores = cross_val_score(ridge, X_train, y_train, cv=5, scoring='r2')
       print(f"Ridge alpha={alpha}: R² = {scores.mean():.3f} ± {scores.std():.3f}")
   ```
3. **Lasso for feature selection:** Check which features Lasso zeros out. These are noise.
4. **Compare:** Plain LR vs Ridge vs Lasso. Which gives best test R²?

### Phase 4: Iteration (Day 5)

1. **Residual analysis:** Plot `y_test - y_pred` vs `y_pred`. Is there a pattern? (Curved residuals = non-linear relationship you're missing)
2. **Residuals by property type:** Which building types does the model get wrong most? Maybe hospitals need a separate model.
3. **Add polynomial features:** `sqft²`, `age²` — does this improve R²?
4. **Try multi-city:** Download Chicago or Seattle benchmarking data. Does a model trained on NYC generalize to Chicago? (Probably not perfectly — climate differences. This teaches domain shift.)
5. **Final report:** Your best model, its R², its top-5 most important features, and what they mean for energy policy.

---

## What You Learn from This Project

| Concept | How it shows up |
|---------|----------------|
| Features & target | Building characteristics → energy use |
| Train/test split | 80/20 split, evaluate on unseen buildings |
| Loss function (MSE) | What the model minimizes |
| R² interpretation | "My model explains X% of energy use variation" |
| Coefficient interpretation | "Hospitals use Y more kBTU/sqft than offices, all else equal" |
| Log transform | Handling skewed EUI distribution |
| One-hot encoding | Converting building type categories to numbers |
| Regularization | Ridge/Lasso to prevent overfitting with many building types |
| Feature engineering | Building age, interactions, polynomials |
| Residual analysis | Finding where the model fails and why |
